# -*- coding: utf-8 -*-
"""
Created on Thu May 16 23:32:47 2019

@author: Danielle Gonzalez-Wu
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:40:33 2019

@author: danie
@collaborators: Nohelly Derosiers, Tanja Miketic, Michaela Chum, Dharia Sara Silas, Salma Ahmed, Faysal Molla
"""

import numpy as np 
import matplotlib.pyplot as plt 
import scipy.signal as signal
 
fs = 200
fnyquist = 100
#Making the FIR filter, it is one-dimensional 
#I am creating a Moving Average Filter 
coef = 0.8
#Numerator of the Linear Filter (Window)
#Creates the window needed for the moving average filter to move along by making an array
#Negative makes it high pass 
b = np.array([1., -coef])
#Denominator of the Linear Filter (The amount it moves along before taking the next value)
#If a( is not equal to an array of 1, then filter normalizes the filter coefficients by a. Therefore, a must be nonzero. It will always become 1 basically. 
a = np.array([1.])

#Magnitude Response
freqresponse = np.fft.fft(b,fs)
#Magnitude response is the absolute value of the frequency response
FIRmag = np.abs(freqresponse)
#Converts the radians/samples to Hz 
lengthmag = len(freqresponse)
xsample_hz = np.linspace(0, fs, lengthmag)
FIRmag_db = 20 * np.log10(FIRmag)
#Phase Response (in degrees)
FIRphase = np.angle(freqresponse, deg = True)


#FOR PART 2: Generated  1 second sinusoidal signal at different frequenciees 
#Sinusoidal Signal Equation is as follows y = A*sin(2pi*f*t)
A = 1
t = np.linspace(0,1,fs)
pi = np.pi
sin = np.sin 
f1 = 5
f2 = 10
f3 = 15
f4 = 20
f5 = 25
f1hz = A*sin((2*pi)*f1*t)
f2hz = A*sin((2*pi)*f2*t)
f3hz = A*sin((2*pi)*f3*t)
f4hz = A*sin((2*pi)*f4*t)
f5hz = A*sin((2*pi)*f5*t)

#Filtered output after input goes through the moving average filter created. 
filteredf1hz = signal.lfilter(b,a,f1hz,0)
filteredf2hz = signal.lfilter(b,a,f2hz,0)
filteredf3hz = signal.lfilter(b,a,f3hz,0)
filteredf4hz = signal.lfilter(b,a,f4hz,0)
filteredf5hz = signal.lfilter(b,a,f5hz,0)

#Plots of the Input and Filtered Output. In this case, the filter is high pass. 
plt.figure(1)
plt.subplot(3,2,1)
plt.plot(t,f1hz, label = 'Input')
plt.plot(t,filteredf1hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('5 Hz Sinusoid')
plt.subplot(3,2,2)
plt.plot(t,f2hz, label = 'Input')
plt.plot(t,filteredf2hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('10 Hz Sinusoid')
plt.subplot(3,2,3)
plt.plot(t,f3hz, label = 'Input')
plt.plot(t,filteredf3hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('15 Hz Sinusoid')
plt.subplot(3,2,4)
plt.plot(t,f4hz, label = 'Input')
plt.plot(t,filteredf4hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('20 Hz Sinusoid')
plt.subplot(3,2,5)
plt.plot(t, f5hz, label = 'Input')
plt.plot(t, filteredf5hz, label = 'Filtered Output')
plt.gca().legend(loc="upper left") 
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('25 Hz Sinusoid')
plt.tight_layout()
plt.show()

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

#Part 4: Adding -10 dB Noise to tbe Filtered Signals 
plt.figure(2)
#To get -10 dB noise, first convert it to Amplitude 
snr = -10 
#To find the desired SNR in dB through power the equation is given by 10*log10(Poutput/Pinput)
#To find the desired SNR in dB through Amplitude the equation is given by 20*log10(Aoutput/Ainput)
#First, the amplitudes for all the signals before the desired noise will be added is computed by finding the maximum
f1Ainput = np.max(filteredf1hz)
f2Ainput = np.max(filteredf2hz)
f3Ainput = np.max(filteredf3hz)
f4Ainput = np.max(filteredf4hz)
f5Ainput = np.max(filteredf5hz)
#Next the ratio for the needed Amplitude to get the -10 dB SNR is calculated through the equations and parameters given above,
f1Aoutput = (f1Ainput) * 10**(-10/20)
f2Aoutput = (f2Ainput) * 10**(-10/20)
f3Aoutput = (f3Ainput) * 10**(-10/20)
f4Aoutput = (f4Ainput) * 10**(-10/20)
f5Aoutput = (f5Ainput) * 10**(-10/20)
#A random piece of white noise is generated based on noise amplitude needed to get the -10 dB signal to noise ratio, a negative indicates more noise than signal.
noisef1 = (np.random.uniform(0,f1Aoutput,len(filteredf1hz)))
noisef2 = (np.random.uniform(0,f2Aoutput,len(filteredf2hz)))
noisef3 = (np.random.uniform(0,f3Aoutput,len(filteredf3hz)))
noisef4 = (np.random.uniform(0,f4Aoutput,len(filteredf4hz)))
noisef5 = (np.random.uniform(0,f5Aoutput,len(filteredf5hz)))
#f1 Hz 
noisyf1hz = filteredf1hz + noisef1
plt.subplot(3,2,1)
plt.plot(t,f1hz, label = 'Input')
plt.plot(t,noisyf1hz, label = 'Noisy Output')
plt.title('Noisy 5 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.gca().legend(loc='upper right')
#f2 Hz 
noisyf2hz = filteredf2hz + noisef2
plt.subplot(3,2,2)
plt.plot(t,f2hz, label = 'Input')
plt.plot(t,noisyf2hz, label = 'Noisy Output')
plt.title('Noisy 10 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.gca().legend(loc='upper right')
#f3 Hz 
noisyf3hz = filteredf3hz + noisef3
plt.subplot(3,2,3)
plt.plot(t,f3hz, label = 'Input')
plt.plot(t,noisyf3hz, label = 'Noisy Output')
plt.title('Noisy 15 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.gca().legend(loc='upper right')
#f4 Hz 
noisyf4hz = filteredf4hz + noisef4
plt.subplot(3,2,4)
plt.plot(t,f4hz, label = 'Input')
plt.plot(t,noisyf4hz, label = 'Noisy Output')
plt.title('Noisy 20 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.gca().legend(loc='upper right')
#f5 Hz 
noisyf5hz = filteredf5hz + noisef5
plt.subplot(3,2,5)
plt.plot(t,f5hz, label = 'Input')
plt.plot(t,noisyf5hz, label = 'Noisy Output')
plt.title('Noisy 25 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.gca().legend(loc='upper right')
plt.tight_layout()
plt.show()

#Part 4: Computing the magnitude and phase responses of the noisy signals 
#Same procedure as commented in Part 3 
#Noisy f1 Hz Output 
#Magnitude Response
noisyf1hzfft = np.fft.fft(noisyf1hz)
FIRmagnoisyf1hz = np.abs(noisyf1hzfft)
ynoisyf1hz_dB = 20 * np.log10 (FIRmagnoisyf1hz) #Changes y values to dB
#Phase response 
ynoisyf1hz_Phase = np.angle(noisyf1hzfft, deg = True)
#Noisy f2 Hz Output
#Magnitude Response
noisyf2hzfft = np.fft.fft(noisyf2hz)
FIRmagnoisyf2hz = np.abs(noisyf2hzfft)
ynoisyf2hz_dB = 20 * np.log10 (FIRmagnoisyf2hz) #Changes y values to dB
#Phase response 
ynoisyf2hz_Phase = np.angle(noisyf2hzfft, deg = True)
#Noisy f3 Hz Output
#Magnitude Response
noisyf3hzfft = np.fft.fft(noisyf3hz)
FIRmagnoisyf3hz = np.abs(noisyf3hzfft)
ynoisyf3hz_dB = 20 * np.log10 (FIRmagnoisyf3hz) #Changes y values to dB
#Phase response 
ynoisyf3hz_Phase = np.angle(noisyf3hzfft, deg = True)
#Noisy f4 Hz Output 
#Magnitude Response
noisyf4hzfft = np.fft.fft(noisyf4hz)
FIRmagnoisyf4hz = np.abs(noisyf4hzfft)
ynoisyf4hz_dB = 20 * np.log10 (FIRmagnoisyf4hz) #Changes y values to dB
#Phase response 
ynoisyf4hz_Phase = np.angle(noisyf4hzfft, deg = True)
#Noisy f5 Hz Output 
#Magnitude Response
noisyf5hzfft = np.fft.fft(noisyf5hz)
FIRmagnoisyf5hz = np.abs(noisyf5hzfft)
ynoisyf5hz_dB = 20 * np.log10 (FIRmagnoisyf5hz) #Changes y values to dB
#Phase response 
ynoisyf5hz_Phase = np.angle(noisyf5hzfft, deg = True)

#Part 4: Magnitude Difference of the noisy signal output vs. the input 
#Same procedure as commented in Part 3
#Noisy f1 Hz 
ynoisyf1hz_dBmax = np.max(ynoisyf1hz_dB)
yf1hz_dBmax = np.max(yf1hz_dB)
noisyf1magdifference = ynoisyf1hz_dBmax - yf1hz_dBmax
#Noisy f2 Hz
ynoisyf2hz_dBmax = np.max(ynoisyf2hz_dB)
yf2hz_dBmax = np.max(yf2hz_dB)
noisyf2magdifference = ynoisyf2hz_dBmax - yf2hz_dBmax
#Noisy f3 Hz
ynoisyf3hz_dBmax = np.max(ynoisyf3hz_dB)
yf3hz_dBmax = np.max(yf3hz_dB)
noisyf3magdifference = ynoisyf3hz_dBmax - yf3hz_dBmax
#Noisy f4 Hz
ynoisyf4hz_dBmax = np.max(ynoisyf4hz_dB)
yf4hz_dBmax = np.max(yf4hz_dB)
noisyf4magdifference = ynoisyf4hz_dBmax - yf4hz_dBmax
#Noisy f5 Hz
ynoisyf5hz_dBmax = np.max(ynoisyf5hz_dB)
yf5hz_dBmax = np.max(yf5hz_dB)
noisyf5magdifference = ynoisyf5hz_dBmax - yf5hz_dBmax

#Part 4: Phase difference of the noisy signal output vs. the input
#Same procedure as commented in part 3  
#noisy f1 Hz
noisyf1hzfftmax = np.max(noisyf1hzfft)
f1hzfftmax = np.max(f1hzfft)
noisyf1ratio = (f1hzfftmax/noisyf1hzfftmax)
noisyf1phasedifference = np.angle(noisyf1ratio, deg = True)
#noisy f2 Hz 
noisyf2hzfftmax = np.max(noisyf2hzfft)
f2hzfftmax = np.max(f2hzfft)
noisyf2ratio = (f2hzfftmax/noisyf2hzfftmax)
noisyf2phasedifference = np.angle(noisyf2ratio, deg = True)
#noisy f3 Hz
noisyf3hzfftmax = np.max(noisyf3hzfft)
f3hzfftmax = np.max(f3hzfft)
noisyf3ratio = (f3hzfftmax/noisyf3hzfftmax)
noisyf3phasedifference = np.angle(noisyf3ratio, deg = True)
#noisy f4 Hz
noisyf4hzfftmax = np.max(noisyf4hzfft)
f4hzfftmax = np.max(f4hzfft)
noisyf4ratio = (f4hzfftmax/noisyf4hzfftmax)
noisyf4phasedifference = np.angle(noisyf4ratio, deg = True)
#noisy f5 Hz
noisyf5hzfftmax = np.max(noisyf5hzfft)
f5hzfftmax = np.max(f5hzfft)
noisyf5ratio = (f5hzfftmax/noisyf5hzfftmax)
noisyf5phasedifference = np.angle(noisyf5ratio, deg = True)

#Magnitude and Phase Response Plots with the Filter magnitude and phase reactions plotted for the multiple filter reactions 
plt.figure(3)
#Magnitude Response Plot 
plt.plot(xsample_hz,FIRmag_db)
plt.ylabel('Amplitude (dB)')
plt.title('Magnitude Response \n of the FIR Filter')
plt.xlim(0,fs/2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.plot(f1,f1magdifference,'o',label = '5 Hz')
plt.plot(f2,f2magdifference,'o',label = '10 Hz')
plt.plot(f3,f3magdifference,'o',label = '15 Hz')
plt.plot(f4,f4magdifference,'o',label = '20 Hz')
plt.plot(f5,f5magdifference,'o',label = '25 Hz')
plt.plot(f1,noisyf1magdifference,'o',label = 'Noisy 5 Hz')
plt.plot(f2,noisyf2magdifference,'o',label = 'Noisy 10 Hz')
plt.plot(f3,noisyf3magdifference,'o',label = 'Noisy 15 Hz')
plt.plot(f4,noisyf4magdifference,'o',label = 'Noisy 20 Hz')
plt.plot(f5,noisyf5magdifference,'o',label = 'Noisy 25 Hz')
plt.gca().legend(loc='upper right')
plt.tight_layout()
plt.show()
#Phase Response Plot 
plt.figure(4)
plt.plot(xsample_hz,FIRphase)
plt.xlim(0,fs/2)
plt.title('Phase Response \n of the FIR Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Degrees)')
plt.plot(f1,f1phasedifference,'o',label = '5 Hz')
plt.plot(f2,f2phasedifference,'o',label = '10 Hz')
plt.plot(f3,f3phasedifference,'o',label = '15 Hz')
plt.plot(f4,f4phasedifference,'o',label = '20 Hz')
plt.plot(f5,f5phasedifference,'o',label = '25 Hz')
plt.plot(f1,noisyf1phasedifference,'o',label = 'Noisy 5 Hz')
plt.plot(f2,noisyf2phasedifference,'o',label = 'Noisy 10 Hz')
plt.plot(f3,noisyf3phasedifference,'o',label = 'Noisy 15 Hz')
plt.plot(f4,noisyf4phasedifference,'o',label = 'Noisy 20 Hz')
plt.plot(f5,noisyf5phasedifference,'o',label = 'Noisy 25 Hz')
plt.gca().legend(loc='upper right')
plt.tight_layout()
plt.show()