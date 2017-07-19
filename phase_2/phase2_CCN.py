# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:53:20 2016

@author: Favian
"""
from transformCCN import *
import operator

filename = input("請輸入要統一格式的檔案名：")+".csv"
rawData = readFile(filename)
columnIntel = findDataIntel(rawData)
checkedData = fileCheck(rawData,columnIntel)
DateTime = dateTime(checkedData,columnIntel)
rawData = 0
def transformdate(datetime):
    strDateTime = str(datetime)
    date = strDateTime[5:7]+"/"+strDateTime[8:10]+"/"+strDateTime[2:4]
    time = strDateTime[11:]
    return date,time
def add2RawData(Row):
    stuff = []
    stuff.append(tempdatetime[0])
    stuff.append(tempdatetime[1])
    for i in range(len(checkedData[7])-3):
        stuff.append("x")
    checkedData.insert(columnIntel+1+Row,stuff)
a="d{0}"
count = 1
dateTimeDict = {}
for i in range(0,len(DateTime)-1):
    delta = DateTime[i+1]-DateTime[i]
    if delta>timedelta(seconds = 1):
        addnum = delta/timedelta(seconds= 1)
        for j in range(0,(int(addnum))):
            b = DateTime[i]+j*timedelta(seconds = 1)
            dateTimeDict.update({(a.format(len(DateTime)+count)):b})
            count+=1
    else:
        dateTimeDict.update({a.format(i):DateTime[i]})
sorted_dic = sorted(dateTimeDict.items(),key=operator.itemgetter(1))
countRow = 0
for i in range(len(sorted_dic)):
    tempdatetime = transformdate(sorted_dic[i][1])
    if checkedData[columnIntel+1+countRow][0] == tempdatetime[0]:
        if checkedData[columnIntel+1+countRow][1] != tempdatetime[1]:
            add2RawData(countRow)
    else:
        add2RawData(countRow)
    countRow+=1
unifiedFile = input("請輸入整理完後的檔案名：" ) + ".csv"
writefile = open(unifiedFile,"w+")
for i in range(len(checkedData)):
    for j in range(len(checkedData[i])):
        if j != len(checkedData[i])-1:
            writefile.write(checkedData[i][j]+",")
        else:
            writefile.write(checkedData[i][j]+"\n")
writefile.close()