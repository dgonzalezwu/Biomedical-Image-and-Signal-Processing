# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:46:05 2019

@author: danie
"""
import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

#Part 1: Read Audio from Sound Recording
# read audio samples
fs,y = read("nasa.wav")
#makes it read values only in one-dimensional value 
y = y[:,0]
#Found through np.shape(y) and exact x through value of np.shapey divided by sampling frequency 
x = np.linspace(0,14.463791666666667,694262)
# plot the whole audio
plt.subplot(411)
plt.plot(x,y)
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (seconds)")
# set the title
plt.title("Sound Signal")
# display the plot
plt.show()
plt.tight_layout()

#Part 2: Signal with Discrete Fourier Transform applied
audioft = (np.fft.fft(y))
plt.subplot(412)
plt.plot((abs(audioft)))
plt.ylabel("Logarithmic \n Amplitude")
plt.xlabel("Frequency (Hz)")
plt.xlim(0,35000)
plt.ylim(10**0,10**8)
plt.yscale('log')
# set the title
plt.title("Magnitude of DFT Sound Signal")
plt.show()
plt.tight_layout()

#Part 3: Randomly Filtered 
#A window function is going to be used to create an impulse response needed for convulation 
#Kaiser Window forms formed by using a Bessel function  
#np.kaiser(amount of numbers in array, beta), beta represents the shape that the window will take to filter the signal 
#Beta used in this was 0 which is rectangular
#The rectangular window is represented by an array of just the number 1 it makes the waveform turn on and off
window = np.kaiser(200,0)
#Sum is normalized to get unity gain and thats why it must be divided 
filtered = np.convolve(y,window,mode='full') / np.sum(window)
filteredft = (np.fft.fft(filtered))
plt.subplot(413)
plt.plot((abs(filteredft)))
plt.ylabel("Logarithmic \n Amplitude")
plt.xlabel("Frequency (Hz)")
plt.xlim(0,35000)
plt.ylim(10**0,10**8)
plt.yscale('log')
#In Logarithmic y-axis comparison, one peak is shown going downwards. It is noted that the filter has silenced the signal completely at this point.
# set the title
plt.title("Magnitude of Filtered DFT Sound Signal")
plt.show()
plt.tight_layout()

#Part 4: Low Pass Filtered
##A window function is going to be used to create an impulse response needed for convulation 
#Kaiser Window forms formed by using a Bessel function 
#np.kaiser(amount of numbers in array, beta), beta represents the shape that the window will take to filter the signal 
#Beta used in this was 0 which is rectangular
#The rectangular window is represented by an array of just the number 1 it makes the waveform turn on and off
window = np.kaiser(2000,0)
#Sum is normalized to get unity gain and thats why it must be divided 
filtered = np.convolve(y,window,mode='full') / np.sum(window)
filteredft = (np.fft.fft(filtered))
figure = plt.subplot(414)
plt.plot((abs(filteredft)))
plt.ylabel("Logarithmic \n Amplitude")
plt.xlabel("Frequency (Hz)")
plt.xlim(0,35000)
plt.ylim(10**0,10**8)
plt.yscale('log')
#Filter is low pass as there is more peaks downwards showing it has been more silenced at certain points. 
#In Logarithmic y-axis comparison, two peak is shown going downwards. It is noted that the filter has silenced the signal completely at this point.
# set the title
plt.title("Magnitude of Low Pass Filtered DFT Sound Signal")
plt.show()
plt.tight_layout()