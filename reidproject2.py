#!/usr/bin/env python3
#https://github.com/carleyreid/bch-5884

import numpy as np
from matplotlib import pyplot

#open and read chromatogram file
f=open("superose6_50.asc")
lines=f.readlines()
f.close

#parse the chromatogram file, assign time and abs to columns
time=[]
abs=[]
for line in lines[3:]:
    words=line.split()
    try:
        time.append(float(words[0]))
        abs.append(float(words[1]))
    except: 
        print("could not parse",line)
        continue

#make time and abs into arrays
time=np.array(time)
abs=np.array(abs)


#find peaks using nearest neighbor method
#set min absorbance to qualify as max as 90 from looking at chrom
#prints out time and absorbance values for peaks in command line
peaktime=[]
peakabs=[]
peaks=[]
peaklist=[]
minabs=90
for i in range((len(abs))-1):
    a=abs[i-1]
    b=abs[i]
    c=abs[i+1]
    if (b >= a and b>=c) and (b>minabs):
        peaktime.append(time[i])
        peakabs.append(abs[i])
        peaklist.append(i)
        peaks.append((time[i],abs[i]))
print("The peaks are at coordinates (time,abs):")
print(peaks)


#use slope change to find boundaries 
#I know this isn't quite right but I wanted to see where the slope was changing in a positive or negative direction, positive being a peak beginning and negative being a peak ending, and then a slope change of 0 would just be baseline
da=np.gradient(abs)
da_array=np.array(da)
slopes=da_array
change=0
x1=[]
x2=[]
y1=[]
y2=[]
xy1=[]
xy2=[]

for i in range(len(slopes)):
    if slopes[i]>change:
        x1.append(time[i])
        y1.append(abs[i])
        xy1.append((time[i],abs[i]))
    elif slopes[i]<change:
        x2.append(time[i])
        y2.append(time[i])
        xy2.append((time[i],abs[i]))

print("The peak boundaries are at coordinates (xy1,xy2):")
print(xy1,xy2)


#plot the data
pyplot.plot(time,da)
pyplot.plot(time,abs)
pyplot.plot(peaktime,peakabs,'ro')
pyplot.xlabel('Time (min)')
pyplot.ylabel('Absorbance')
pyplot.show()







