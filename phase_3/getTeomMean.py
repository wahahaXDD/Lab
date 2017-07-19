# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:43:11 2016

@author: favian
"""

from getMean import *
from transformTeom import *
from numpy import *
from datetime import *
filename = input("Enter file name: ")
rawData = readNewFile(filename+".txt")
dateTime = dateTime(rawData)
concentration = concentration(rawData)
concentration30 = concentration30(rawData)
concentration60 = concentration60(rawData)
noise = noise(rawData)
flow = flow(rawData)
bypassFlow = bypassFlow(rawData)
temperature = temperature(rawData)
pressure = pressure(rawData)

hourList = getHourList(dateTime)
concentrationMean = getMean(dateTime,concentration)
concentration30Mean = getMean(dateTime,concentration30)
concentration60Mean = getMean(dateTime,concentration60)
noiseMean = getMean(dateTime,noise)
flowMean = getMean(dateTime,flow)
bypassFlowMean = getMean(dateTime,bypassFlow)
temperatureMean = getMean(dateTime,temperature)
pressureMean = getMean(dateTime,pressure)


newFileName = filename + "Mean.txt"
writefile = open(newFileName,"w+")
for i in range(len(hourList)):
    writefile.write(str(hourList[i])+"\t")
    writefile.write("8\t")
    writefile.write(str(concentrationMean[i])+"\t")
    writefile.write("57\t")
    writefile.write(str(concentration30Mean[i])+"\t")
    writefile.write("58\t")
    writefile.write(str(concentration60Mean[i])+"\t")
    writefile.write("13\t")
    writefile.write(str(noiseMean[i])+"\t")
    writefile.write("39\t")
    writefile.write(str(flowMean[i])+"\t")
    writefile.write("40\t")
    writefile.write(str(bypassFlowMean[i])+"\t")
    writefile.write("130\t")
    writefile.write(str(temperatureMean[i])+"\t")
    writefile.write("131\t")
    writefile.write(str(pressureMean[i])+"\n")
writefile.close()
    