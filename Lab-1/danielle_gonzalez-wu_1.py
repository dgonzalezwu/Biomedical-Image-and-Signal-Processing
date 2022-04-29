# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:31:29 2019

@author: danie
"""

import numpy as np
import matplotlib.pyplot as plt


plt.figure(1)
#part 1: figure 1
#y = A*sin(2*pi*f*t)
#201 samples helps the graph look more smooth and accurate as the one on the slides
t1 = np.linspace(0,2,201)
x1=t1
A=2
pi=np.pi
f=2
y1= A*(np.sin(2*pi*f*t1))
plt.subplot(221)
plt.plot(x1,y1)
plt.xlabel('time(s)')
plt.title('original - 2Hz sin')


#part 1: figure 2
#y = A*sin(2*pi*f*t)
#11 samples are used and these are the ones that show up on the stem, would be more accurate with more samples
t2 = np.linspace(0,2,11)
x2=t2
A=2
pi=np.pi
f=2
y2 = A*(np.sin(2*pi*f*t2))
plt.subplot(222)
plt.stem(x2,y2, use_line_collection=True)
plt.xlabel('time(s)')
plt.title('sampled')


#part 1: figure 3
A = 2  # amplitude of signal
Q = 1/1  # quantization stepsize
pi=np.pi
t3=np.linspace(0,2,201)
x3=t3
#201 samples are used to help the sine graph look more accurate 

def uniform_midtread_quantizer(x, Q):
    # limiter if/then statements to establish step function
    x = np.copy(x)
    idx = np.where(np.abs(x) >= 2)
    x[idx] = np.sign(x[idx])
    # linear uniform quantization equation
    xQ = Q * np.floor(x/Q + 1/2)

    return xQ

#Here, I created an if, then statement of the equation for quantization of a signal, a simpler way to do this would be using the function np.round() to get the same result. Anyhow, my if-then statement yields the same result but takes longer to code. 

#x = A*sin(2*pi*f*t)
x=A*np.sin(2*pi*2*t3)
# quantize signal
xQ = uniform_midtread_quantizer(x, Q)
# plot signals
plt.subplot(223)
plt.plot(t3,xQ)
plt.xlabel('time(s)')
plt.title('discretized')

#part 1: figure 4
plt.subplot(224)
#same plot as part 1:figure 1 and part 1: figure 2 just put into one graph. Green sine wave is changed for differentiation. 
plt.plot(x1,y1,'g')
plt.stem(x2,y2, use_line_collection=True)
plt.xlabel('time(s)')
plt.title('sampled and discretized')

plt.show()

#part 2: penny
#This is how to import the image
plt.figure(2)
P = plt.imread('penny.tif')

# This converts the image to grayscale
gray = np.dot(P[...,:3],[0.299, 0.587, 0.114])

#2 gray levels
plt.subplot(231)
plt.axis('off')
plt.title('2 gray levels')
grayCount2 = 256-1
#Based off of the equation given in class: (P/255)*(ratio needed to change gray level)
roundedGray2 = np.round(gray/float(grayCount2))
# Display using matplotlib's copper color mapping
plt.imshow(roundedGray2, cmap=plt.get_cmap('copper'))

plt.show()

#4 gray levels
plt.subplot(232)
plt.axis('off')
plt.title('4 gray levels')
grayCount4 = ((256-1)/3)
roundedGray4 = np.round(gray / float(grayCount4))
plt.imshow(roundedGray4, cmap=plt.get_cmap('copper'))

plt.show()

#8 gray levels
plt.subplot(233)
plt.axis('off')
plt.title('8 gray levels')
grayCount8 = ((256-1)/7)
roundedGray8 = np.round(gray/float(grayCount8))
plt.imshow(roundedGray8, cmap=plt.get_cmap('copper'))

#16 gray levels
plt.subplot(234)
plt.axis('off')
plt.title('16 gray levels')
grayCount16 = ((256-1)/15)
roundedGray16 = np.round(gray/float(grayCount16))
plt.imshow(roundedGray16, cmap=plt.get_cmap('copper'))

#32 gray levels
plt.subplot(235)
plt.axis('off')
plt.title('32 gray levels')
grayCount32 = ((256-1)/31)
roundedGray32 = np.round(gray/ float(grayCount32))
plt.imshow(roundedGray32, cmap=plt.get_cmap('copper'))

#256 gray levels
plt.subplot(236)
plt.axis('off')
plt.title('256 gray levels')
grayCount256 = ((256-1)/255)
roundedGray256 = np.round(gray/ float(grayCount256))
plt.imshow(roundedGray256, cmap=plt.get_cmap('copper'))
#I crossed checked whether the gray levels were accurate using np.unique(*my final equation variable name*).shape
plt.show()

#part 3: Sampling
plt.figure(3)
#720 x 240 pixels
pi=np.pi
x = np.tile(np.linspace(0, 3.8*pi, 240), (720, 1))
#240 x 720 sample amount on x-axis sets the pixel amount on this axis
y = np.tile(np.linspace(0, 13*pi, 720), (240, 1)).T 
#720x240 sample amount on y-axis transposed sets the equal pixel amount on the y-axis and also transposing allows it to be adjusted to the pixel dimensions we want completely.
#np.tile constructs an array by repeating A the number of times given by reps.
#The linspace start-stop on the x,y is adjusted so the circles will form. These given amount of samples create artifacts in the time domain we established earlier. Therefore, giving us the similar circles seen in the example slide.
#While function in equation was originally f(x,y)=sin(x^2+y^2) the image will not show up without the addition of the cos(x^2+y^2)
#Function is transposed so it can be adjusted to the pixel dimensions we want completely. 
function = np.abs(np.sin(x**2 + y**2)+ np.cos(x**2 + y**2)).T
plt.imshow(function, cmap = 'gray')
#changes the pixel values to grey 
plt.axis('off')
plt.show()