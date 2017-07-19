from numpy import *
from datetime import *
import csv as csv
def readFile(filename):
    temp = []
    read_file = open(filename,'r')
    for row in csv.reader(read_file):
        temp.append(row)
    return temp

def findDataIntel(rawData):
    pivot = 0
    for i in range(len(rawData)):
        for j in range(len(rawData[i])):
            if 'CCN Number Conc' in rawData[i][j]:
                pivot = i
                break
    return pivot

'''----------------------------'''
''' fileCheck用來清除錯誤的資料 '''
def fileCheck(rawData,columnIntel):
    CheckList = []
    pivot1 = 0
    pivot2 = 0
    colC = []
    colAV = []
    delCount = 0
    for i in range(len(rawData[columnIntel])):
        if "Temps Stabilized" in rawData[columnIntel][i]:
            pivot1 = i
            break
    for i in range(len(rawData[columnIntel])):
        if "Alarm Code" in rawData[columnIntel][i]:
            pivot2 = i
            break
    for i in range(columnIntel+1,len(rawData)):
        if int(float(rawData[i][pivot1])) != 1:
            colC.append(i)
        if int(float(rawData[i][pivot2])) != 0:
            colAV.append(i)
    for i in colC:
        if i in colAV:
            colAV.remove(i)
        CheckList.append(i)
    for i in colAV:
        CheckList.append(i)
    CheckList = sort(CheckList)
    for i in CheckList:
        rawData.pop(i-delCount)
        delCount+=1
    return rawData
'''----------------------------'''
''' dateTime用來整理日期 '''
def dateTime(CheckedData,columnIntel):
    pivot = 0
    DateTime = []
    NewDateTime= []
    for i in range(len(CheckedData[columnIntel])):
        if "Date" in CheckedData[columnIntel][i]:
            pivot = i
            break
    for i in range(columnIntel+1,len(CheckedData)):
        DateTime.append(CheckedData[i][pivot] + " " + CheckedData[i][pivot+1])
    for i in range(len(DateTime)):
        date_object = datetime.strptime(DateTime[i],'%m/%d/%y %H:%M:%S')
        NewDateTime.append(date_object)
    return NewDateTime

'''----------------------------'''
''' Flow用來整理 Sample Flow的資料 '''
def flow(CheckedData,columnIntel):
    pivot = 0
    sampleFlow = []
    for i in range(len(CheckedData[columnIntel])):
        if "Sample Flow" in CheckedData[columnIntel][i]:
            pivot = i
            break
    for i in range(columnIntel+1,len(CheckedData)):
        sampleFlow.append(float(CheckedData[i][pivot]))
    return sampleFlow

'''----------------------------'''
''' sheathFlow用來整理 Sheath Flow 的資料 '''
def sheathFlow(CheckedData,columnIntel):
    sheathFlow = []
    pivot = 0
    for i in range(len(CheckedData[columnIntel])):
        if "Sheath Flow" in CheckedData[columnIntel][i]:
            pivot = i
            break
    for i in range(columnIntel+1,len(CheckedData)):
        sheathFlow.append(float(CheckedData[i][pivot]))
    return sheathFlow

'''----------------------------'''
''' laserCurrent用來整理 Laser Current 的資料 '''
def laserCurrent(CheckedData,columnIntel):
    laserCurrent=[]
    pivot = 0
    for i in range(len(CheckedData[columnIntel])):
        if "Laser Current" in CheckedData[columnIntel][i]:
            pivot = i
            break
    for i in range(columnIntel+1,len(CheckedData)):
        laserCurrent.append(float(CheckedData[i][pivot]))
    return laserCurrent
    
'''----------------------------'''
''' numberCon用來整理 CCN Number Conc 的資料 '''
def numberCon(CheckedData,columnIntel):
    numberCon = []
    pivot = 0
    for i in range(len(CheckedData[columnIntel])):
        if "numberCon" in CheckedData[columnIntel][i]:
            pivot = i
            break
    for i in range(columnIntel+1,len(CheckedData)):
        numberCon.append(float(CheckedData[i][pivot]))
    return numberCon