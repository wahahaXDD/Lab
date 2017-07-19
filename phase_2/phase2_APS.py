"""
Created on Sun May 22 20:20:01 2016

@author: Favian
"""
from transformAPS import *
import operator
filename = input("請輸入要統一格式的檔案名：")+".txt"
rawData = readFile(filename)
columnIntel = findDataIntel(rawData)
DateTime = dateTime(rawData,columnIntel)
def transformdate(datetime):
    strdatetime = str(datetime)
    date = strdatetime[5:7]+"/"+strdatetime[8:10]+"/"+strdatetime[2:4]
    time = strdatetime[11:]
    return date,time
def add2RawData(Row):
    stuff = ["x"]
    stuff.append(tempdatetime[0])
    stuff.append(tempdatetime[1])
    for i in range(len(rawData[7])-3):
        stuff.append("x")
    stuff.append("\n")
    rawData.insert(7+Row,stuff)
a = "d{0}"
addnum = 0
count = 1
dateTimeDict = {}
for i in range(0,len(DateTime)-1):
    delta = DateTime[i+1]-DateTime[i]
    if delta >timedelta(seconds=361):
        addnum = delta/timedelta(seconds=359)
        for j in range(0,(int(addnum))):
            b = DateTime[i]+j*timedelta(seconds=360)
            dateTimeDict.update({(a.format(len(DateTime)+count)):b})
            count+=1
    else:
        dateTimeDict.update({a.format(i):DateTime[i]})
sorted_dic = sorted(dateTimeDict.items(),key=operator.itemgetter(1))
countRow = 0
for i in range(len(sorted_dic)):
    tempdatetime = transformdate(sorted_dic[i][1])
    if rawData[7+countRow][1] == tempdatetime[0]:
        if rawData[7+countRow][2] != tempdatetime[1]:
            add2RawData(countRow)
    else:
        add2RawData(countRow)
    countRow+=1
unifiedFile = input("請輸入整理完後的檔案名: ") + ".txt"
writefile = open(unifiedFile,"w+")
for i in range(len(rawData)):
    for j in range(len(rawData[i])):
        if j != len(rawData[i])-1:
            writefile.write(rawData[i][j]+"\t")
        else:
            writefile.write(rawData[i][j])
writefile.close()