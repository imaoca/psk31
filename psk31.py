import wave
import math
import numpy as np

fname='psk31_sample8k.wav'  # should be specify the filename.
smp= 8000           # Sampling Rate
FQ= smp/1000.0      # Signal Frequency 
wind= 40            # window
waveFile = wave.open(fname, 'r')
q=[];i=[]
for j in range(waveFile.getnframes()):
      buf = waveFile.readframes(1)
      q.append((buf[0]-128)*np.sin(np.pi*2.0/FQ*j))
      i.append((buf[0]-128)*np.cos(np.pi*2.0/FQ*j))
      print(int(sum(q)>0),int(sum(i)>0),sep=",")
      if j>wind:q.pop(0);i.pop(0)
waveFile.close()