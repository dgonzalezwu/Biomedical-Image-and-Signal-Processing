# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:58:06 2019

@author: danie
"""
import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp


pi=np.pi
#Part 1/Figure 1: Real valued sampled sinusoidal signal and display as a function of time
#Number of samples wanted/Sampling frequency in Hz
plt.figure(1)
plt.subplot(231)
fs1 = 300
#Amplitude 
A1 = 1 
#Sinusoidal Signal Equation is as follows y = A*sin(2pi*f*t)
#must be 1 if its 1-1/fs it does not equal that 
t1 = np.linspace(0,1,fs1)
x1=t1
#the Natural Frequency, in cycles per second or Hz
f1 = 10
#signal function
y1=A1*np.sin(2*pi*f1*t1)
#graph as a real valued sampled output
plt.plot(x1,y1)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('Sinusoidal Signal - 10 Hz')

#Part 2/Figure 1: Discrete Fourier Transform 
#Discrete Fourier Transform 
#must divide by Sample frequency as equation for Discrete Fourier Transform makes it (Sample Size) Times Large than expected for analysis
Fy1 = (np.fft.fft(y1))
#Part 2/Figure 2: Real parts of the Discrete Fourier Transform also known as the Cosine Terms 
plt.subplot(232)
plt.plot(np.real(Fy1))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Real parts')
#Part 2/Figure 3: Imaginary Parts of the Discrete Fourier Transform also known as the Sine Terms
plt.subplot(233)
plt.plot(np.imag(Fy1))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Imaginary parts')
#Part 2/Figure 4: Magnitude of the Discrete Fourier Transform
#Magnitude is the absolute value of the function. And Power is the Magnitude squared. 
#For a sinusoid that has an integer number of cycles within the N data points, the amplitude of the sine or cosine wave is twice its Fourier coefficient.
plt.subplot(234)
plt.plot(np.abs(Fy1))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (energy)')
plt.title('Magnitude')
#Part 2/Figure 5: Phase of the Discrete Fourier Transform
plt.subplot(235)
plt.plot(np.angle(Fy1))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.title('Phase')

plt.tight_layout()
plt.show()



#Part 3: Test Empirically Which is the Highest Frequency you can represent. Show an example above and below that frequency in time. 
#Here we are recreating the signal we created initially for the Real valued sampled sinusoidal signal 
#The nyquist rate is double the natural frequency, and if it is the stated largest frequency in the system, then we should be sampling above double that rate then. 
plt.figure(2)
#Fourier at Nyquist 
plt.subplot(221)
f2 = 20;  # frequency in Hz
tmin = 0;
fsat = 40
tmax = 1;
#time
t2 = np.linspace(tmin, tmax, fsat);
#Amplitude
A2=1
y2 = A2*np.sin(2*pi*f2*t2); # signal sampling
Fy2 = (abs(sp.fft.fft(y2)))
plt.plot(Fy2)
plt.title('Signal at Nyquist')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

#Fourier Above Nyquist 
plt.subplot(222)
f2 = 30;  # frequency in Hz
fsabove = 40
tmin = 0;
tmax = 1;
#time
t2 = np.linspace(tmin, tmax, fsabove);
#Amplitude
A2=1
y2 = A2*np.sin(2*pi*f2*t2); # signal sampling
Fy2 = (abs(sp.fft.fft(y2)))
plt.plot(Fy2)
plt.title('Signal above Nyquist')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

#Fourier Below Nyquist 
plt.subplot(223)
f2 = 10;  # frequency in Hz
fsbelow=40
tmin = 0;
tmax = 1;
#time
t2 = np.linspace(tmin, tmax, fsbelow);
#Amplitude
A2=1
y2 = A2*np.sin(2*pi*f2*t2); # signal sampling
Fy2 = (abs(sp.fft.fft(y2)))
plt.plot(Fy2)
plt.title('Signal below Nyquist')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

#Part 4: Generate a complex valued sinusoid with negative frequency; display it in the time domain and frequency domain. Contrast that to a sinusoid of positive frequency.
#Complex valued sinusoid can be expressed in phasor nnotation 
#The phasor notation follows this equation: Ae^j(wt+phi) where w is angular velocity  so 2*pi*f
#Natural frequency of complex valued sinusoid is 10 Hz
plt.figure(3)
f3 = 10
#Same sampling frequency as previous signal so fs=100 Hz
t3 = np.linspace(0,1-1/fs1,fs1)
#Amplitude 
A3=1
#Phi
phi = 0
#Negative Time vs. Amplitude
plt.subplot(2,2,1)
plt.plot(t3, A3*np.exp((2j*np.pi*-f3*t3)+phi).real, label = 'Real Part');
plt.plot(t3, A3*np.exp((2j*np.pi*-f3*t3)+phi).imag, label = 'Imaginary Part');
plt.xlabel('Time (s)');
plt.ylabel('Amplitude');
plt.title('Complex valued sinusoid \n with Negative Frequency')
plt.legend(loc = 'upper left')

#Positive Time vs. Amplitude
plt.subplot(2,2,2)
plt.plot(t3, A3*np.exp((2j*np.pi*f3*t3)+phi).real, label = 'Real Part' );
plt.plot(t3, A3*np.exp((2j*np.pi*f3*t3)+phi).imag, label = 'Imaginary Part' );
plt.xlabel('Time (s)');
plt.ylabel('Amplitude');
plt.title('Complex valued sinusoid \n with Positive Frequency')
plt.legend(loc= 'upper left')

#Positive Frequency vs. Amplitude
plt.subplot(223)
f = 10;  # frequency in Hz
tmin = 0;
tmax = 1-(1/fs1);
#time
t = np.linspace(tmin, tmax, fs1);
#Amplitude
A2=1
cy1 = A2*np.exp(2*pi*f*t*1j)
abscy1 = abs(sp.fft.fft(cy1))
plt.plot(abscy1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Positive Frequency vs \n Amplitude')

#Negative Frequency vs. Amplitude
plt.subplot(224)
f = -10;  # frequency in Hz
tmin = 0;
tmax = 1-(1/fs1);
#time
t = np.linspace(tmin, tmax, fs1);
#Amplitude
A2=1
cy1 = A2*np.exp(2*pi*f*t*1j)
abscy1 = abs(sp.fft.fft(cy1))
plt.plot(abscy1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Negative Frequency vs \n Amplitude')

plt.tight_layout()
plt.show() 

#Part 5
plt.figure(4)
plt.subplot(221)
f1=10
f2=2*f1
fs=400
#Amplitude 
A1 = 1 
#Sinusoidal Signal Equation is as follows y = A*sin(2pi*f*t)
t1 = np.linspace(0,1,fs)
signal=A1*np.sin(2*pi*f1*t1) + A1*np.sin(2*pi*f2*t1) 
#graph as a real valued sampled output
plt.plot(t1,signal)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('Sinusoidal Signal of Frequency F=10 Hz')

#Before downsampling
plt.subplot(222)
fsignal = np.fft.fft(signal)
plt.plot(np.abs(fsignal))
plt.title('Before downsampling')
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')

#After downsampling 
plt.subplot(223)
fs = 3.5*f1
t1 = np.linspace(0,1, int(fs))
signal=A1*np.sin(2*pi*f1*t1) + A1*np.sin(2*pi*f2*t1) 
fsignal = np.fft.fft(signal)
plt.plot(np.abs(fsignal))
plt.title('After downsampling')
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')

plt.tight_layout()
plt.show()