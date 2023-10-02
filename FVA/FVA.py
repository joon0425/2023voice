import os
import numpy as np
import librosa
import wave
import scipy
import matplotlib
from  matplotlib import pyplot as plt
from .lpc import *
from .detect import *


class SingleSoundAnalyser:

  
  def __init__(self, FILE_PATH, duration = None, sr = None):

    if sr is None: sr = librosa.load(FILE_PATH)[1]

    waveFile = wave.open(FILE_PATH, 'r')
    self.samplewidth = waveFile.getsampwidth()
    #fdata = np.frombuffer(waveFile.readframes(-1),dtype='int16').astype(np.float32)
    waveFile.close()

    if duration is None:
      self.sr         = sr
      self.sounds     = librosa.load(FILE_PATH, sr = sr)[0]
      self.fdata      = self.sounds * float(1 << ((8 * self.samplewidth)-1))
      self.N          = self.sounds.shape[0]
      self.time_axis  = np.linspace(0, self.N / sr, self.N)
    else:
      self.sr         = sr
      self.N          = int(sr * duration)
      self.sounds     = librosa.load(FILE_PATH, sr = sr)[0][:self.N]
      self.fdata      = self.sounds * float(1 << ((8 * self.samplewidth)-1))
      self.time_axis  = np.linspace(0, duration, self.N)


  def get_source(self, ylim = [None, None], xlim = [None, None]):
    
    if xlim[0] is None: xlim[0] = 0
    if xlim[1] is None: xlim[1] = self.N / self.sr
    if ylim[0] is None: ylim[0] = self.sounds.min()
    if ylim[1] is None: ylim[1] = self.sounds.max()
    
    return self.time_axis, self.sounds, xlim, ylim, 'time(s)', 'Amplitude(μm)'
  
  def get_spectrum(self, ylim = [None, None], xlim = [1,10000]):
    
    fft_sounds = (np.abs(np.fft.fft(self.sounds)) / self.sr)[:self.N // 2]
    fft_freq = (np.fft.fftfreq(self.N, d = 1 / self.sr))[:self.N // 2]

    if ylim[0] is None: ylim[0] = fft_sounds.min()
    if ylim[1] is None: ylim[1] = fft_sounds.max()

    return fft_freq, fft_sounds, xlim, ylim, 'frequency(Hz)', 'Amplitude(μm)'

  #def get_fp_fft(self, echo = False, )

  def get_fp_stft(self, echo = False, NFRAME = 640, NSHIFT = 320, lpcOrder = 32, FreqPoints = 4096, max_num_formants = 5):
    # self.(elem of arg) must be constant in this function
    self.NFRAME           = NFRAME
    self.NSHIFT           = NSHIFT
    self.lpcOrder         = lpcOrder
    self.FreqPoints       = FreqPoints
    self.max_num_formants = max_num_formants
    self.preemph          = 0.97
    self.window           = np.hamming(NFRAME)

    self.df0 = (self.sr / 2.) / FreqPoints
    self.dt0 = 1. / self.sr
    count = int(((self.N - (NFRAME - NSHIFT)) / NSHIFT))
    spec_out = np.zeros([count, FreqPoints])
    fout = np.zeros([count, max_num_formants])
    fout_index = np.ones([count, max_num_formants]) * -1
    pout = np.zeros(count)
    pout_index = np.ones(count) * -1
    pos = 0
    countr = 0

    for loop in range(count):
      frame = self.fdata[pos:pos + NFRAME].copy()
      frame -= np.hstack((frame[0], frame[:-1])) * self.preemph
      windowed = self.window * frame
      a, e = lpc(windowed, lpcOrder)
      w, h = scipy.signal.freqz(np.sqrt(e), a, FreqPoints)
      lpcspec = np.abs(h)
      lpcspec[lpcspec < 1.] = 1.
      loglpcspec = 20 * np.log10(lpcspec)
      spec_out[loop] = loglpcspec
      f_result, i_result = formant_detect(loglpcspec, self.df0)
      if len(f_result) > max_num_formants:
        fout[loop] = f_result[:max_num_formants]
        fout_index[loop] = i_result[:max_num_formants]
      else:
        fout[loop][:len(f_result)] = f_result[:len(f_result)]
        fout_index[loop][:len(f_result)] = i_result[:len(f_result)]
      r_err = residual_error(a, windowed)
      a_r_err = autocorr(r_err)
      a_f_result, a_i_result = pitch_detect(a_r_err, self.dt0)
      if len(a_f_result) > 0:
        pout[loop] = a_f_result[0]
        pout_index[loop] = a_i_result[0]
      if echo:
        print('formants : [',end='')
        for i, formant in enumerate(fout[loop]):
          print(f'f{i+1} : {formant}',end='')
          if i != len(fout[loop]) - 1: print('/',end='')
        print(']')
        print(f'pitch : {pout[loop]}')
      countr += 1
      pos += NSHIFT
    return spec_out, fout_index, pout