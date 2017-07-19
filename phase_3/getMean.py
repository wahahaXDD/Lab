# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 21:25:15 2016

@author: Favian
"""
from datetime import *
from numpy import *

def getHourList(timeList):
    hourList =[]
    for i in range(0,len(timeList)-1):
        if timeList[i].hour == timeList[i+1].hour:
            if i == len(timeList)-2:
                hourList.append(datetime.strftime(timeList[i],"%Y/%m/%d %H:00"))
        else:
            hourList.append(datetime.strftime(timeList[i],"%Y/%m/%d %H:00"))
    return hourList
    
    
def getMean(timeList,dataList):
    meanList = []
    mean = 0
    n=0
    sum = 0.0
    for i in range(0,len(timeList)-1):
        if timeList[i].hour == timeList[i+1].hour:
            try:
                if i == len(timeList)-2:
                    sum+=dataList[i+1]
                    n+=1
                    if n==0:
                        mean = 0
                    else:
                        mean = sum/n
                    n=0
                    meanList.append(mean)
                    sum=0.0
                sum +=dataList[i]
                n+=1
            except :
                continue
        else:
            try:
                sum += dataList[i]
                n+=1
            except:
                ""
            if n==0:
                mean = 0
            else:
                mean = sum/n
            n=0
            meanList.append(mean)
            sum=0.0
    return meanList


def getConcentrationMean(timeList,concentrationList):
    concentrationMean = []
    mean = 0
    n=0
    sum = 0
    for k in range(len(concentrationList)):
        concentrationMean.append([])
        n=0
        sum = 0
        for i in range(len(timeList)-1):
            if timeList[i].hour == timeList[i+1].hour:
                try:
                    if i == len(timeList)-2:
                        sum+=float(concentrationList[k][i+1])
                        n+=1
                        mean = sum/n
                        concentrationMean[k].append(mean)
                        sum = 0
                        n=0
                    sum +=float(concentrationList[k][i])
                    n+=1
                except :
                    continue
            else:
                try:
                    sum += float(concentrationList[k][i])
                    n+=1
                except:
                    ""
                try:
                    mean = sum/n
                except ZeroDivisionError:
                    mean = 0
                concentrationMean[k].append(mean)
                sum=0
                n=0
    return concentrationMean
    
    
def getStd(hourList,timeList,dataList,meanList):
    hourIndex = 0
    StdList = []
    for i in range(len(timeList)):
        sum = 0
        count = 0
        if datetime.strptime(hourList[hourIndex],"%Y/%m/%d %H:00").hour == timeList[i-hourIndex].hour:
            try:
                sum+=(float(meanList[hourIndex])-float(dataList[i]))**2
            except:
                sum+=0
            count+=1
        else:
            StdList.append(sqrt(sum/(count-1)))
            hourIndex = hourIndex + 1
    return StdList












