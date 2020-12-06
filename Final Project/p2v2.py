#!/usr/bin/env python3
#https://github.com/carleyreid/bch-5884
#final project folder, unknown samples are listed w/ their method

import os
import webbrowser
import numpy as np
from matplotlib import pyplot

#user inputs file
chrom=input("Please enter a chromatogram file name (.asc):")
method=input("Was your method GA or GB?:")

#open and read chromatogram file
f=open(chrom)
lines=f.readlines()
f.close

#parse the chromatogram file, assign time and int to columns
time=[]
int=[]
for line in lines[3:]:
    words=line.split()
    try:
        time.append(float(words[0]))
        int.append(float(words[1]))
    except: 
        print("could not parse",line)
        continue

#make time and intensity into arrays
time=np.array(time)
int=np.array(int)


#find peaks using nearest neighbor method
#set min and max intensity to ID unknown peaks and disqualify solvent peak
#prints out time and absorbance values for peaks in command line
peaktime=[]
peakint=[]
peaks=[]
minint=3000000 #ignores noise
maxint=100000000 #ignores solvent peaks
for i in range((len(int))-1):
    a=int[i-1]
    b=int[i]
    c=int[i+1]
    if (b >= a and b>=c) and (b>minint) and (b<maxint):
        peaktime.append(time[i])
        peakint.append(int[i])
        peaks.append((time[i],int[i]))
print("The peaks are at coordinates (time,int):")
print(peaks)
peaktime=np.array(peaktime) #so it works in library

#mini library to determine identity
#if I had more access to materials this could be longer but unfortunately the book I need to reference more is like $600
peakID=[]
if method == "GA":
    if np.any(peaktime>7.90) and np.any(peaktime<8.00):
        #print("The sample is CBD")
        peakID.append("CBD")
    if np.any(peaktime>5.20) and np.any(peaktime<5.30):
        #print("The sample is caffeine")
        peakID.append("Caffeine")
    else:
        print("No library match.")
if method == "GB":
    if np.any(peaktime>3.70) and np.any(peaktime<3.80):
        #print("The sample is vanillin")
        peakID.append("Vanillin")
    if np.any(peaktime>5.85) and np.any(peaktime<5.95):
        #print("The sample is atropine")
        peakID.append("Atropine")
    if np.any(peaktime>6.45) and np.any(peaktime<6.55):
        #print("The sample is caffeine")
        peakID.append("Caffeine")
    else:
        print("No library match.")
print(peakID)


#plot the data
#includes location of peaks and identity on plot so everything shows up nicely in html
#x1 etc. are just locations for the info annotations
pyplot.plot(time,int)
pyplot.plot(peaktime,peakint,'ro')
pyplot.xlabel('Time (min)')
pyplot.ylabel('Intensity')
x1=5
y1=140000000
x2=8
y2=130000000
pyplot.text(x1, y1, peaks)
pyplot.text(x2, y2, peakID)
pyplot.savefig("unknownchromatogram.png")
pyplot.show()

url="file:///Users/carleyreid/BCH5884/sem2/finalprojwebpage.html"
#causes html code to pop up in text editor when I exit plot
webbrowser.open_new(url)
#visit url to see the chromatogram and results



