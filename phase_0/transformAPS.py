from datetime import *
from numpy import *

def readFile(filename):
    read_file = open(filename,'r')
    temp = []
    for line in read_file:
        temp.append(line)
    for i in range(len(temp)):
        temp[i] = temp[i].split('\t')
    read_file.close()
    return temp
def findDataIntel(rawList):
    pivot = 0
    for i in range(len(rawList)):
        if 'Date' in rawList[i]:
            pivot = i
            break
    return pivot
def dateTime(rawList,columnIntel):
    Date = []
    time = []
    DateTime=[]  
    NewDateTime=[]
    dateIndex=0
    timeIndex=0
    for i in range(len(rawList[columnIntel])):
        if rawList[columnIntel][i]=='Date':
            dateIndex = i
            timeIndex = i+1
    for i in range(columnIntel+1,len(rawList)):
        Date.append(rawList[i][dateIndex])
        time.append(rawList[i][timeIndex])
    for i in range(len(Date)):
        DateTime.append(Date[i].replace("\n","")+" "+ time[i].replace("\n",""))
    for i in range(len(DateTime)):
        date_object = datetime.strptime(DateTime[i],'%m/%d/%y %H:%M:%S')
        NewDateTime.append(date_object)
    return NewDateTime
def diameter(rawList,columnIntel):
    diameter = []
    column_range = []
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Diameter" in rawList[columnIntel][i]:
            pivot = i
    for i in range(pivot+1,len(rawList[columnIntel])):
        try:
            float(rawList[columnIntel][i].replace("<",""))
            column_range.append(i)
            diameter.append(rawList[columnIntel][i].replace("<",""))
        except:
            continue
    return diameter,column_range
def concentration(rawList,columnIntel,diameter_range):
    concentration = []
    for i in range(len(diameter_range)):
        concentration.append([])
        for j in range(columnIntel+1,len(rawList)):
            try:
                concentration[i].append(float(rawList[j][diameter_range[i]]))
            except ValueError:
                concentration[i].append(rawList[j][diameter_range[i]])
        concentration[i]=array(concentration[i])
    return concentration
def totalFlow(rawList,columnIntel):
    totalFlow =[]
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Total Flow" in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            totalFlow.append(float(rawList[columnIntel+1+i][pivot]))
        except ValueError:
            totalFlow.append(rawList[columnIntel+1+i][pivot])
    return totalFlow
def sheathFlow(rawList,columnIntel):
    sheathFlow =[]
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Sheath Flow" in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            sheathFlow.append(float(rawList[columnIntel+1+i][pivot]))
        except ValueError:
            sheathFlow.append(rawList[columnIntel+1+i][pivot])
    return sheathFlow
def laserPower(rawList,columnIntel):
    laserPower = []
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Laser Power" in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            laserPower.append(float(rawList[columnIntel+1+i][pivot]))
        except ValueError:
            laserPower.append(rawList[columnIntel+1+i][pivot])
    return laserPower
def laserCurrent(rawList,columnIntel):
    laserCurrent = []
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Laser Current" in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            laserCurrent.append(float(rawList[columnIntel+1+i][pivot]))
        except ValueError:
            laserCurrent.append(rawList[columnIntel+1+i][pivot])
    return laserCurrent
def medianNum(rawList,columnIntel):
    median = []
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Median" in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            median.append(float(rawList[columnIntel+1+i][pivot]))
        except ValueError:
            median.append(rawList[columnIntel+1+i][pivot])
    return median
def meanNum(rawList,columnIntel):
    mean = []
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Mean" in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            mean.append(float(rawList[columnIntel+1+i][pivot]))
        except ValueError:
            mean.append(rawList[columnIntel+1+i][pivot])
    return mean
def geoMean(rawList,columnIntel):
    geoMean = []
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Geo. Mean" in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            geoMean.append(float(rawList[columnIntel+1+i][pivot]))
        except ValueError:
            geoMean.append(rawList[columnIntel+1+i][pivot])
    return geoMean
def mode(rawList,columnIntel):
    mode = []
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Mode" in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            mode.append(float(rawList[columnIntel+1+i][pivot]))
        except ValueError:
            mode.append(rawList[columnIntel+1+i][pivot])
    return mode
def geoStd(rawList,columnIntel):
    geoStd = []
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Geo. Std. Dev." in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            geoStd.append(float(rawList[columnIntel+1+i][pivot]))
        except ValueError:
            geoStd.append(rawList[columnIntel+1+i][pivot])
    return geoStd
def totalCon(rawList,columnIntel):
    totalCon = []
    pivot = 0
    for i in range(len(rawList[columnIntel])):
        if "Total Conc." in rawList[columnIntel][i]:
            pivot = i
            break
    for i in range(len(rawList[columnIntel+1])):
        try:
            totalCon.append(float(rawList[columnIntel+1+i][pivot].replace("(#/cm3)\n","")))
        except ValueError:
            totalCon.append(rawList[columnIntel+1+i][pivot])
    return totalCon