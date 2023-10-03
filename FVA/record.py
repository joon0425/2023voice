import queue, os, threading, time
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write


q = queue.Queue()
recorder = False
recording = False

def complicated_record():
    with sf.SoundFile("FVA/target_sounds/recorded.wav", mode='w', samplerate=16000, subtype='PCM_16', channels=1) as file:
        with sd.InputStream(samplerate=16000, dtype='int16', channels=1, callback=complicated_save):
            while recording:
                file.write(q.get())
        
def complicated_save(indata, frames, time, status):
	q.put(indata.copy())
    
def start():
    global recorder
    global recording
    recording = True
    recorder = threading.Thread(target=complicated_record)
    print('start recording')
    recorder.start()
    
def stop():
    global recorder
    global recording
    recording = False
    recorder.join()
    print('stop recording')
start()
time.sleep(2)
stop()