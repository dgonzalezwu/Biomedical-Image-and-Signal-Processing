# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:02:46 2019

@author: Danielle Gonzalez-Wu 
"""

import numpy as np 
import matplotlib.pyplot as plt 
#%% Generating a FIR filter through an impulse response 
#Part 1: Step Response 
#np.shape is used to find the amount of samples and np.max to find the max amplitude that each wave reaches 
#Column 2 is my step response on the txt doc and Column 5 is my original square wave function on the txt doc
highpass = np.loadtxt('STEP20HZ.txt', usecols=(2,5)) 
lpstep = np.loadtxt('STEP20HZ.txt',usecols=(5))
original = np.loadtxt('STEP20HZ.txt', usecols = (2))
fs = 2501 
#time would be amount of samples plotted/total samples taken, in this case it would just be over a 1 second interval 
time1= np.linspace(0,(2501/2501),2501)
plt.figure(1)
plt.plot(time1, original, label="Input")
plt.plot(time1, lpstep, label = "Output/Step Response")
plt.title('Square Wave and \n Low Pass Filter Output')
plt.xlabel('Time (seconds)')
plt.ylabel('Ampltitude')
plt.gca().legend(loc="upper left")
plt.tight_layout()
plt.show()

#Part 2: Impulse Response 
#np.max(lpstep) = 0.4770883
#Asks for temporal derivative for only results above 0 
difflpstep = np.diff(lpstep>0) #shows when the pulses happen 
#Index is asking for the samples that are applicable for this condition 
findindex = np.where(difflpstep) #shows the samples where those pulses happen 
#index is from findindex function 
indexfound = np.array([54,  116,  179,  241,  304,  366,  429,  491,  554,  616,  679, 741,  804,  866,  929,  991, 1054, 1116, 1179, 1241, 1304, 1366, 1429, 1491, 1554, 1616, 1679, 1741, 1804, 1866, 1929, 1991, 2054, 2116, 2179, 2241, 2304, 2366, 2429, 2491])
index = indexfound - 2 #shifting indices towards the right so the impulse response can be seen further 
sampledsteps = []
sampledimpulses = [] 

for x in range (0,1,39):
    index1 = index[x]
    index2 = index[x+1]
    sampledstep = lpstep[index1:index2]
    sampledsteps.append(sampledstep)
    sampledimpulse=np.diff(sampledstep)
    sampledimpulses.append(sampledimpulse[:])
    
averageimpulse = np.mean(sampledimpulses,0)
#This estimates the amount of noise within the sample
standarddeviationimpulse = np.std(sampledimpulses,0)

plt.figure(2)
#to plot over time: Impulse is over one cycle, the samples found through np.shape is 123, total sample is 2501 so 123/2501 would be the amount of time that one impulse took
time2 = np.linspace(0, 61/2501, 61)
plt.plot(time2,averageimpulse, label = "Average Impulse")
#Error bars shows standard deviation also known as noise estimate 
plt.errorbar(time2,averageimpulse,standarddeviationimpulse,ecolor='orange',elinewidth=1,capsize=5,capthick=2, label = "Error Bars")
plt.title('Average Impulse Response \n with Error Bars')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')   
plt.gca().legend(loc="upper left") 
plt.tight_layout()
plt.show()

#%% Generating sinusoids at different frequencies 
loadf1hz = np.loadtxt('SINE6HZ.txt',usecols=(2,5))
loadf2hz = np.loadtxt('SINE8HZ.txt',usecols=(2,5))
loadf3hz = np.loadtxt('SINE20HZ.txt',usecols=(2,5))
loadf4hz = np.loadtxt('SINE40HZ.txt',usecols=(2,5))
loadf5hz = np.loadtxt('SINE80HZ.txt',usecols=(2,5))

f1 = 6
f2 = 8
f3 = 20
f4 = 40
f5 = 80
f1hz = loadf1hz[0:1250,0]
f2hz = loadf2hz[0:1250,0]
f3hz = loadf3hz[0:1250,0]
f4hz = loadf4hz[0:1250,0]
f5hz = loadf4hz[0:1250,0]

filteredf1hz = loadf1hz[0:1250,1]
filteredf2hz = loadf2hz[0:1250,1]
filteredf3hz = loadf3hz[0:1250,1]
filteredf4hz = loadf4hz[0:1250,1]
filteredf5hz = loadf4hz[0:1250,1]

t = np.linspace(0,1,1250)
#Plots of the Input and Filtered Output. In this case, the filter is high pass. 
plt.figure(3)
plt.subplot(3,2,1)
plt.plot(t,f1hz, label = 'Input')
plt.plot(t,filteredf1hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('6 Hz Sinusoid')
plt.subplot(3,2,2)
plt.plot(t,f2hz, label = 'Input')
plt.plot(t,filteredf2hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('8 Hz Sinusoid')
plt.subplot(3,2,3)
plt.plot(t,f3hz, label = 'Input')
plt.plot(t,filteredf3hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('20 Hz Sinusoid')
plt.subplot(3,2,4)
plt.plot(t,f4hz, label = 'Input')
plt.plot(t,filteredf4hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('40 Hz Sinusoid')
plt.subplot(3,2,5)
plt.plot(t, f5hz, label = 'Input')
plt.plot(t, filteredf5hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('80 Hz Sinusoid')
plt.tight_layout()
plt.show()

#%%
#Calculating Magnitude and Phase Difference 
#PART 3: Computing the magnitude and phase response of the input and filtered output 
#f1 Hz Input 
#Magnitude Response 
f1hzfft = np.fft.fft(f1hz)
FIRmagf1hz = np.abs(f1hzfft)
yf1hz_dB = 20 * np.log10 (FIRmagf1hz) #Changes y values to dB
#Phase response 
yf1hz_Phase = np.angle(f1hzfft, deg = True)
#f2 Hz Input 
#Magnitude Response 
f2hzfft = np.fft.fft(f2hz)
FIRmagf2hz = np.abs(f2hzfft)
yf2hz_dB = 20 * np.log10 (FIRmagf2hz) #Changes y values to dB
#Phase response 
yf2hz_Phase = np.angle(f2hzfft, deg = True)
#f3 Hz Input 
#Magnitude Response
f3hzfft = np.fft.fft(f3hz)
FIRmagf3hz = np.abs(f3hzfft)
yf3hz_dB = 20 * np.log10 (FIRmagf3hz) #Changes y values to dB
#Phase response 
yf3hz_Phase = np.angle(f3hzfft, deg = True)
#f4 Hz Input
#Magnitude Response
f4hzfft = np.fft.fft(f4hz)
FIRmagf4hz = np.abs(f4hzfft)
yf4hz_dB = 20 * np.log10 (FIRmagf4hz) #Changes y values to dB
#Phase response 
yf4hz_Phase = np.angle(f4hzfft, deg = True)
#f5 Hz Input 
#Magnitude Response
f5hzfft = np.fft.fft(f5hz)
FIRmagf5hz = np.abs(f5hzfft)
yf5hz_dB = 20 * np.log10 (FIRmagf5hz) #Changes y values to dB
#Phase response 
yf5hz_Phase = np.angle(f5hzfft, deg= True)
#f1 Hz Output 
#Magnitude Response
filteredf1hzfft = np.fft.fft(filteredf1hz)
FIRmagfilteredf1hz = np.abs(filteredf1hzfft)
yfilteredf1hz_dB = 20 * np.log10 (FIRmagfilteredf1hz) #Changes y values to dB
#Phase response 
yfilteredf1hz_Phase = np.angle(filteredf1hzfft, deg = True)
#f2 Hz Output
#Magnitude Response
filteredf2hzfft = np.fft.fft(filteredf2hz)
FIRmagfilteredf2hz = np.abs(filteredf2hzfft)
yfilteredf2hz_dB = 20 * np.log10 (FIRmagfilteredf2hz) #Changes y values to dB
#Phase response 
yfilteredf2hz_Phase = np.angle(filteredf2hzfft, deg = True)
#f3 Hz Output
#Magnitude Response
filteredf3hzfft = np.fft.fft(filteredf3hz)
FIRmagfilteredf3hz = np.abs(filteredf3hzfft)
yfilteredf3hz_dB = 20 * np.log10 (FIRmagfilteredf3hz) #Changes y values to dB
#Phase response 
yfilteredf3hz_Phase = np.angle(filteredf3hzfft, deg = True)
#f4 Hz Output 
#Magnitude Response
filteredf4hzfft = np.fft.fft(filteredf4hz)
FIRmagfilteredf4hz = np.abs(filteredf4hzfft)
yfilteredf4hz_dB = 20 * np.log10 (FIRmagfilteredf4hz) #Changes y values to dB
#Phase response 
yfilteredf4hz_Phase = np.angle(filteredf4hzfft, deg = True)
#f5 Hz Output 
#Magnitude Response
filteredf5hzfft = np.fft.fft(filteredf5hz)
FIRmagfilteredf5hz = np.abs(filteredf5hzfft)
yfilteredf5hz_dB = 20 * np.log10 (FIRmagfilteredf5hz) #Changes y values to dB
#Phase response 
yfilteredf5hz_Phase = np.angle(filteredf5hzfft, deg = True)

#Part 3: Calculating Magnitude Difference
#Magnitude difference is computed by subtracting the maximum value of the magnitude of the input from the maximum value of the magnitude of the output 
#f1 Hz 
yfilteredf1hz_dBmax = np.max(yfilteredf1hz_dB)
yf1hz_dBmax = np.max(yf1hz_dB)
f1magdifference = yfilteredf1hz_dBmax - yf1hz_dBmax
#f2 Hz
yfilteredf2hz_dBmax = np.max(yfilteredf2hz_dB)
yf2hz_dBmax = np.max(yf2hz_dB)
f2magdifference = yfilteredf2hz_dBmax - yf2hz_dBmax
#f3 Hz
yfilteredf3hz_dBmax = np.max(yfilteredf3hz_dB)
yf3hz_dBmax = np.max(yf3hz_dB)
f3magdifference = yfilteredf3hz_dBmax - yf3hz_dBmax
#f4 Hz
yfilteredf4hz_dBmax = np.max(yfilteredf4hz_dB)
yf4hz_dBmax = np.max(yf4hz_dB)
f4magdifference = yfilteredf4hz_dBmax - yf4hz_dBmax
#f5 Hz
yfilteredf5hz_dBmax = np.max(yfilteredf5hz_dB)
yf5hz_dBmax = np.max(yf5hz_dB)
f5magdifference = yfilteredf5hz_dBmax - yf5hz_dBmax

#Part 3: Calculating Phase Difference 
#Phase difference is computed by taking the ratio of the (maximum of the fft of the input/maximum of the fft of the output) and then taking the angle of that ratio 
#f1 Hz 
filteredf1hzfftmax = np.max(filteredf1hzfft)
f1hzfftmax = np.max(f1hzfft)
f1ratio = (f1hzfftmax/filteredf1hzfftmax)
f1phasedifference = np.angle(f1ratio, deg = True)
#f2 Hz 
filteredf2hzfftmax = np.max(filteredf2hzfft)
f2hzfftmax = np.max(f2hzfft)
f2ratio = (f2hzfftmax/filteredf2hzfftmax)
f2phasedifference = np.angle(f2ratio, deg = True)
#f3 Hz
filteredf3hzfftmax = np.max(filteredf3hzfft)
f3hzfftmax = np.max(f3hzfft)
f3ratio = (f3hzfftmax/filteredf3hzfftmax)
f3phasedifference = np.angle(f3ratio, deg = True)
#f4 Hz
filteredf4hzfftmax = np.max(filteredf4hzfft)
f4hzfftmax = np.max(f4hzfft)
f4ratio = (f4hzfftmax/filteredf4hzfftmax)
f4phasedifference = np.angle(f4ratio, deg = True)
#f5 Hz
filteredf5hzfftmax = np.max(filteredf5hzfft)
f5hzfftmax = np.max(f5hzfft)
f5ratio = (f5hzfftmax/filteredf5hzfftmax)
f5phasedifference = np.angle(f5ratio, deg = True)
#%%
#Magnitude 
fbin = np.linspace(0,2501,61)
FIRfft = np.fft.fft(averageimpulse)
FIRmag = np.abs(FIRfft)
FIRmag_db = 20 * np.log10 (FIRmag)
plt.figure(4)
plt.plot(fbin,FIRmag_db)
plt.xlim(0,2501/2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Magnitude Response \n of the FIR Filter')
plt.plot(f1,f1magdifference,'o',label = '6 Hz')
plt.plot(f2,f2magdifference,'o',label = '8 Hz')
plt.plot(f3,f3magdifference,'o',label = '20 Hz')
plt.plot(f4,f4magdifference,'o',label = '40 Hz')
plt.plot(f5,f5magdifference,'o',label = '80 Hz')
plt.gca().legend(loc='upper right')
plt.tight_layout()
plt.show()
#Phase Response 
FIRphase = np.angle(FIRfft, deg = True)
plt.figure(5)
plt.plot(fbin,FIRphase)
plt.title('Phase Response \n of the FIR Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Degrees)')
plt.xlim(0,2501/2)
plt.plot(f1,f1phasedifference,'o',label = '6 Hz')
plt.plot(f2,f2phasedifference,'o',label = '8 Hz')
plt.plot(f3,f3phasedifference,'o',label = '20 Hz')
plt.plot(f4,f4phasedifference,'o',label = '40 Hz')
plt.plot(f5,f5phasedifference,'o',label = '80 Hz')
plt.gca().legend(loc='upper right')
plt.tight_layout()
plt.show()