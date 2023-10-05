import queue, os, threading, time
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import pathlib

q = queue.Queue()
recorder = False
recording = False
pausing = False
cd = str(pathlib.Path(__file__).parent.absolute())

def complicated_record():
    with sf.SoundFile(cd+"\\target_sounds\\recorded.wav", mode='w', samplerate=16000, subtype='PCM_16', channels=1) as file:
        with sd.InputStream(samplerate=16000, dtype='int16', channels=1, callback=complicated_save):
            while recording:
                if pausing: q.get()
                else: file.write(q.get())
        
def complicated_save(indata, frames, time, status):
	q.put(indata.copy())
    
def start():
    global recorder
    global recording
    recording = True
    pausing = False
    os.remove(cd+"\\target_sounds\\recorded.wav")
    recorder = threading.Thread(target=complicated_record)
    print('start recording')
    recorder.start()
    
def stop():
    global recorder
    global recording
    recording = False
    pausing = False
    recorder.join()
    print('stop recording')

def pause():
    global pausing
    pausing = True

def resume():
    global pausing
    pausing = False

