# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 19:51:54 2016

@author: Favian
"""
from datetime import *
def readFile(filename):
    read_file = open(filename,'r')
    temp = []
    for line in read_file:
        temp.append(line)
    for i in range(len(temp)):
        temp[i] = temp[i].split('\t')
    read_file.close()
    return temp
def dateTime(rawList):
    dateTime = []
    newDateTime = []
    for i in range(len(rawList)):
        dateTime.append(rawList[i][0]+ " " +rawList[i][1])
    for i in range(len(dateTime)):
        date_Object = datetime.strptime(dateTime[i],'%m/%d/%y %H:%M:%S')
        newDateTime.append(date_Object)
    return newDateTime
    