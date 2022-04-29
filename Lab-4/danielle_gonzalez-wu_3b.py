# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:31:35 2019

@author: Danielle Gonzalez-Wu 
"""

import numpy as np 
import matplotlib.pyplot as plt 

#To make this lowpass filter a 50 ohm resistor and a 47 uF capacitor was used leading to a cutoff frequency of around 67 Hz 
#Part 1: Step Response 
#np.shape is used to find the amount of samples and np.max to find the max amplitude that each wave reaches 
#Column 2 is my step response on the txt doc and Column 5 is my original square wave function on the txt doc
lowpass = np.loadtxt('lowpass10hz.txt', usecols=(2,5)) 
lpstep = np.loadtxt('lowpass10hz.txt',usecols=(2))
original = np.loadtxt('lowpass10hz.txt', usecols = (5))
fs = 2501 
#time would be amount of samples plotted/total samples taken, in this case it would just be over a 1 second interval 
time1= np.linspace(0,(2501/2501),2501)
plt.figure(1)
plt.plot(time1, original, label="Input")
plt.plot(time1, lpstep, label = "Output/Step Response")
plt.title('Square Wave and \n Low Pass Filter Output')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.gca().legend(loc="upper left")
plt.show()

#Part 2: Impulse Response 
#np.max(lpstep) = 0.4770883
#Asks for temporal derivative for only results above 0 
difflpstep = np.diff(lpstep>0) #shows when the pulses happen 
#Index is asking for the samples that are applicable for this condition 
findindex = np.where(difflpstep) #shows the samples where those pulses happen 
#index is from findindex function 
index = np.array([ 109,  233,  359,  483,  609,  733,  859,  983, 1109, 1233, 1359, 1483, 1609, 1733, 1859, 1983, 2109, 2233, 2359, 2483])

#Part 3: Average Impulse Response with noise 
#We will use these 20 samples to take repeated measures of the step response 
#The average impulse response of these ten samples will be taken together at the end 
#for loop to take the desired 10 sample measurements by taking two of each index samples through our index array until the end: 
sampledsteps = []
sampledimpulses = [] 

for x in range (0,1,19):
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
time2 = np.linspace(0,(123/2501),123)
plt.plot(time2,averageimpulse, label = "Average Impulse")
#Error bars shows standard deviation also known as noise estimate 
plt.errorbar(time2,averageimpulse,standarddeviationimpulse,ecolor='orange',elinewidth=1,capsize=5,capthick=2, label = "Error Bars")
plt.title('Average Impulse Response \n with Error Bars')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')   
plt.gca().legend(loc="upper left") 
plt.tight_layout()  
plt.show()