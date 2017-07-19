# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:52:43 2016

@author: Favian
"""
from transformCPC import *
import operator
filename = input("請輸入要統一格式的檔案名：")+".xls"
rawData = readFile(filename)
DateTime = dateTime(rawData)
def transformdate(datetime):
    strDateTime = str(datetime)
    date = strDateTime[5:7]+"/"+strDateTime[8:10]+"/"+strDateTime[2:4]
    time = strDateTime[11:]
    return date,time
def add2RawData(Row):
    stuff = []
    stuff.append(tempdatetime[0])
    stuff.append(tempdatetime[1])
    for i in range(len(rawData[7])-3):
        stuff.append("x")
    stuff.append("\n")
    rawData.insert(Row,stuff)
a="d{0}"
count = 1
dateTimeDict = {}
for i in range(0,len(DateTime)-1):
    delta = DateTime[i+1]-DateTime[i]
    if delta>timedelta(seconds = 1):
        addnum = delta/timedelta(seconds=1)
        for j in range(0,(int(addnum))):
            b = DateTime[i]+j*timedelta(seconds=1)
            dateTimeDict.update({(a.format(len(DateTime)+count)):b})
            count+=1
    else:
        dateTimeDict.update({a.format(i):DateTime[i]})
sorted_dic = sorted(dateTimeDict.items(),key=operator.itemgetter(1))
countRow = 0
for i in range(len(sorted_dic)):
    tempdatetime = transformdate(sorted_dic[i][1])
    if rawData[countRow][0] == tempdatetime[0]:
        if rawData[countRow][1] != tempdatetime[1]:
            add2RawData(countRow)
    else:
        add2RawData(countRow)
    countRow+=1
unifiedFile = input("請輸入整理完後的檔案名： ")+".xls"
writefile = open(unifiedFile,"w+")
for i in range(len(rawData)):
    for j in range(len(rawData[i])):
        if j != len(rawData[i])-1:
            writefile.write(rawData[i][j]+"\t")
        else:
            writefile.write(rawData[i][j])
writefile.close()