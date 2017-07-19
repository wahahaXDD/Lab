# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from datetime import *

def readFile(filename):
    read_file = open(filename,'r')
    temp = []
    for line in read_file:
        temp.append(line)
    for i in range(len(temp)):
        temp[i] = temp[i].split(' ')
        try:
            while(True):
                temp[i].remove('')
        except ValueError:
            temp[i][-1]=temp[i][-1].replace("\n","")
            continue
    read_file.close()
    return temp


def readNewFile(filename):
    read_file = open(filename,'r')
    temp = []
    for line in read_file:
        temp.append(line)
    for i in range(len(temp)):
        temp[i] = temp[i].split('\t')
        try:
            while(True):
                temp[i].remove('')
        except ValueError:
            temp[i][-1]=temp[i][-1].replace("\n","")
            continue
    read_file.close()
    return temp


def checkData(rawList):
    dataIndex = []
    count = 0
    for i in range(len(rawList[0])):
        if(rawList[0][i]=='8'):
            dataIndex.append(i+1)
        elif(rawList[0][i]=='13'):
            dataIndex.append(i+1)
        elif(rawList[0][i]=='39'):
            dataIndex.append(i+1)
    for i in range(len(rawList)):
        if float(rawList[i-count][dataIndex[0]])<=-50:
            rawList.pop(i-count)
            count+=1
            continue
        elif float(rawList[i-count][dataIndex[1]])>0.1:
            rawList.pop(i-count)
            count+=1
            continue
        elif float(rawList[i-count][dataIndex[2]])>=3.15 or float(rawList[i-count][dataIndex[2]])<=2.85:
            rawList.pop(i-count)
            count+=1
            continue
    return rawList


def dateTime(rawList):
    DateTime=[]
    NewDateTime=[]
    for i in range(len(rawList)):
        DateTime.append(rawList[i][0]+" "+rawList[i][1])
        date_object = datetime.strptime(DateTime[i],"%d-%b-%y %H:%M:%S")
        NewDateTime.append(date_object)
    return NewDateTime


def concentration(rawList):
    dataIndex=0
    concentration = []
    for i in range(len(rawList[0])):
        if(rawList[0][i]=='8'):
            dataIndex = i+1
    for i in range(len(rawList)):
        try:
            concentration.append(float(rawList[i][dataIndex]))
        except ValueError:
            concentration.append(rawList[i][dataIndex])
    return concentration


def concentration30(rawList):
    dataIndex=0
    concentration30=[]
    for i in range(len(rawList[0])):
        if(rawList[0][i]=='57'):
            dataIndex=i+1
    for i in range(len(rawList)):
        try:
            concentration30.append(float(rawList[i][dataIndex]))
        except ValueError:
            concentration30.append(rawList[i][dataIndex])
    return concentration30


def concentration60(rawList):
    dataIndex=0
    concentration60=[]
    for i in range(len(rawList[0])):
        if(rawList[0][i]=='58'):
            dataIndex=i+1
    for i in range(len(rawList)):
        try:
            concentration60.append(float(rawList[i][dataIndex]))
        except ValueError:
            concentration60.append(rawList[i][dataIndex])
    return concentration60


def noise(rawList):
    dataIndex=0
    noise = []
    for i in range(len(rawList[0])):
        if(rawList[0][i]=='13'):
            dataIndex=i+1
    for i in range(len(rawList)):
        try:
            noise.append(float(rawList[i][dataIndex]))
        except ValueError:
            noise.append(rawList[i][dataIndex])
    return noise


def flow(rawList):
    dataIndex=0
    flow = []
    for i in range(len(rawList[0])):
        if(rawList[0][i]=='39'):
            dataIndex=i+1
    for i in range(len(rawList)):
        try:
            flow.append(float(rawList[i][dataIndex]))
        except ValueError:
            flow.append(rawList[i][dataIndex])
    return flow


def bypassFlow(rawList):
    dataIndex=0
    bypassFlow = []
    for i in range(len(rawList[0])):
        if(rawList[0][i]=='40'):
            dataIndex=i+1
    for i in range(len(rawList)):
        try:
            bypassFlow.append(float(rawList[i][dataIndex]))
        except ValueError:
            bypassFlow.append(rawList[i][dataIndex])
    return bypassFlow
    
    
def temperature(rawList):
    dataIndex = 0
    temperature = []
    for i in range(len(rawList[0])):
        if(rawList[0][i]=='130'):
            dataIndex=i+1
    for i in range(len(rawList)):
        try:
            temperature.append(float(rawList[i][dataIndex]))
        except ValueError:
            temperature.append(rawList[i][dataIndex])
    return temperature


def pressure(rawList):
    dataIndex=0
    pressure = []
    for i in range(len(rawList[0])):
        if(rawList[0][i]=='131'):
            dataIndex=i+1
    for i in range(len(rawList)):
        try:
            pressure.append(float(rawList[i][dataIndex]))
        except ValueError:
            pressure.append(rawList[i][dataIndex])
    return pressure

