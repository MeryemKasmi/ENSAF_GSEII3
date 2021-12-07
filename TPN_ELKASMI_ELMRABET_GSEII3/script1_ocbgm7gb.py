import numpy as np

def length_stream(Path='/home/wijdane/audio_1.wav'):
	return len(np.fromfile(Path))
        
def nextpow2(N):
	n=0
	while 2**n <N :
		n=n+1	
	return 2**n
        
