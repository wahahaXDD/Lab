# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:41:08 2016

@author: favian
"""
from transformTeom import *
import operator
filename = input("請輸入要統一格式的檔案名：")+".txt"
rawData = readFile(filename)
checkedData = checkData(rawData)
DateTime = dateTime(checkedData)
rawData=0
def switch(month):
    return{
        "01":"Jan",
        "02":"Feb",
        "03":"Mar",
        "04":"Apr",
        "05":"May",
        "06":"Jun",
        "07":"Jul",
        "08":"Aug",
        "09":"Sep",
        "10":"Oct",
        "11":"Nov",
        "12":"Dec",
        }[month]
def transformdate(datetime):
    strdatetime = str(datetime)
    date = strdatetime[8:10]+ "-" +switch(strdatetime[5:7])+"-"+strdatetime[2:4]
    time = strdatetime[11:]
    return date,time
def add2CheckedData(Row):
    stuff = []
    stuff.append(tempdatetime[0])
    stuff.append(tempdatetime[1])
    for i in range(len(checkedData[0])-3):
        stuff.append("x")
    stuff.append("x")
    checkedData.insert(Row,stuff)
a = "d{0}"
addnum = 0
count = 1
dateTimeDict = {}
for i in range(len(DateTime)-1):
    delta = DateTime[i+1]-DateTime[i]
    if delta > timedelta(seconds=301):
        addnum = delta/timedelta(seconds=299)
        for j in range(int(addnum)):
            b = DateTime[i]+j*timedelta(seconds=300)
            dateTimeDict.update({(a.format(len(DateTime)+count)):b})
            count +=1
    else:
        dateTimeDict.update({a.format(i):DateTime[i]})
sorted_dic = sorted(dateTimeDict.items(),key=operator.itemgetter(1))
countRow = 0
for i in range(len(sorted_dic)):
    tempdatetime = transformdate(sorted_dic[i][1])
    if checkedData[countRow][0] == tempdatetime[0]:
        if checkedData[countRow][1] !=tempdatetime[1]:
            add2CheckedData(countRow)
    else:
        add2CheckedData(countRow)
    countRow+=1
unifiedFile = input("輸入整理完後的檔案名: ") + ".txt"
writefile = open(unifiedFile,"w+")
for i in range(len(checkedData)):
    for j in range(len(checkedData[i])):
        if j != len(checkedData[i])-1:
            writefile.write(checkedData[i][j]+"\t")
        else:
            writefile.write(checkedData[i][j])
    writefile.write("\n")
writefile.close()