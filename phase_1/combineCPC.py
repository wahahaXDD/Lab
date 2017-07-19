"""
Created on Sun May 22 14:08:18 2016

@author: Favian
"""
from datetime import *
import openpyxl
from os import listdir
from os.path import isfile, join
import os
onlyfiles = [f for f in listdir(os.path.dirname(os.path.realpath(__file__))) if isfile(join(os.path.dirname(os.path.realpath(__file__)), f))]
allfiles =[]
for i in onlyfiles:
    if i.find('.xls') != -1:
        allfiles.append(i)
'''--------------以上得到目前資料夾內所有檔案--------------'''
temp = []
temp1 = []
time = []
date =[]
concentration = []
count = 0
def addDate(date):
    date = datetime.strptime(date, '%m/%d/%y')
    date = date + timedelta(days=1)
    date = str(date)
    date = date[5:7]+"/" + date[8:10]+"/" + date[2:4]
    return date
for i in allfiles:
    print(i)
    with  open(i,'rb') as f:
        bianry_data = f.read()
        data = bianry_data.decode('cp950','ignore')
        lines = data.splitlines()
        temp.append(lines)
    for j in range(len(temp)):
        for k in range(len(temp[j])):
            temp1.append(temp[j][k])
    for j in range(len(temp1)):
        temp1[j] = temp1[j].split("\t")
        try:
            datetime.strptime(temp1[j][0], '%H:%M:%S')
            if temp1[j][0] != '':
                if count ==0 and datetime.strptime(temp1[j][0], '%H:%M:%S').hour == 0:
                    temp1[4][1] = addDate(temp1[4][1])
                    count +=1
                time.append(temp1[j][0])
                date.append(temp1[4][1])
                concentration.append(temp1[j][1])
        except ValueError:
            continue
    temp = []
    temp1 = []
    count = 0
combinedFileName=input("請輸入統合後的檔案名： ")+".xls"
write = open(combinedFileName,"w+")
for i in range(len(date)):
    write.write(str(date[i]))
    write.write("\t")
    write.write(str(time[i]))
    write.write("\t")
    write.write(concentration[i])
    write.write("\n")
write.close()