import os
import numpy as np
import scipy
import librosa
import librosa.display
from scipy.io import wavfile
import scipy.fftpack as fft
from scipy.signal import get_window, lfilter, freqz, find_peaks_cwt
import math
#from audiolazy.lazy_lpc import lpc
#import peakutils
#from sklearn.cluster import KMeans
import FVA.FVA as fva
from FVA.lpc import *
from FVA.detect import *
from FVA.mfcc import *
from FVA.animation import *
from CREPE.CREPEmanager import *

class FVAmanager:
    
    FILE    =   ""
    SSA     =   None
    
    def __init__(self,filePath:str):
        self.FILE=filePath
        self.SSA = fva.SingleSoundAnalyser(FILE_PATH = self.FILE, duration = 2)
    def FR_formants(self):
        def to_db(x):
            return 10 * np.log10(x)
        x,y =   self.SSA.get_spectrum()[:2]
        y   =   to_db(y)
        FreqPoints=8096
        df0 =   (self.SSA.sr / 2.) / FreqPoints
        Y   =   self.SSA.fdata.copy()
        Y   =   Y - np.hstack((Y[0], Y[:-1])) * 0.8
        windowed    =   np.hamming(Y.shape[0]) * Y
        a, e    =   lpc(windowed,lpcOrder=35)
        w, h    =   scipy.signal.freqz(np.sqrt(e), a, FreqPoints)
        lpcspec =   np.abs(h)
        lpcspec[lpcspec < 1.]   =   1.
        loglpcspec = to_db(lpcspec)
        f_result, i_result = formant_detect(lpcspec,df0,1)
        return f_result
    
    """
    def FR_formants2(self,frame_length=256,): # STFT
        sample_rate, input_data = wavfile.read(self.FILE)
        num_of_frames = int(len(input_data)/frame_length)
        lpcfilters, formants = [], []

        # Applying operations for overlapping frames of speech signal
        for i in range(2*num_of_frames-1):
            frame_min = int(frame_length*i/2)
            frame_max = frame_min + frame_length
            frame_data = input_data[frame_min:frame_max]
            
            # Hamming window output
            hamming_window_output = np.multiply(frame_data, np.hamming(256))

            # Filter output
            filter_output = lfilter(np.array([1]), np.array([1, 0.63]), hamming_window_output)
            
            # Estimating LPC coefficients
            lpc_filter = lpc(filter_output, 10)
            lpcfilters.append(lpc_filter)
            #     lpc_filter.plot().savefig(str(i)+".jpeg")
            #     plt.close()
            
            # Frequency response of the LPC filter
            w, h = freqz(lpc_filter.numlist)
            
            # Finding the first and second formants
            peak_indices = peakutils.indexes(20*np.log10(abs(h)))
            if peak_indices.size > 1:
                formants.append(w[peak_indices])
        
        return formants
    """
    
    def FR_pitch(self):
        return FR_mP(self.FILE)