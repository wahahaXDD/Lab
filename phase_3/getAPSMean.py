from getMean import *
from transformAPS import *
from numpy import *
from datetime import *

filename = input("Enter file name: ")
rawData = readFile(filename+".txt")
columnIntel = findDataIntel(rawData)
dateTime = dateTime(rawData,columnIntel)
diameter, diameter_range = diameter(rawData,columnIntel)
concentration = concentration(rawData,columnIntel,diameter_range)
totalFlow = totalFlow(rawData,columnIntel)
sheathFlow = sheathFlow(rawData,columnIntel)
laserPower = laserPower(rawData,columnIntel)
laserCurrent = laserCurrent(rawData,columnIntel)
medianNum = medianNum(rawData,columnIntel)
meanNum = meanNum(rawData,columnIntel)
geoMean = geoMean(rawData,columnIntel)
mode = mode(rawData,columnIntel)
geoStd = geoStd(rawData,columnIntel)
totalCon = totalCon(rawData,columnIntel)

hourList = getHourList(dateTime)
concentrationMean = getConcentrationMean(dateTime,concentration)
totalFLowMean = getMean(dateTime,totalFlow)
sheathFlowMean = getMean(dateTime,sheathFlow)
laserPowerMean = getMean(dateTime,laserPower)
laserCurrentMean = getMean(dateTime,laserCurrent)
medianNumMean = getMean(dateTime,medianNum)
meanNumMean = getMean(dateTime,meanNum)
geoMeanMean = getMean(dateTime,geoMean)
modeMean = getMean(dateTime,mode)
geoStdMean = getMean(dateTime,geoStd)
totalConMean = getMean(dateTime,totalCon)


newFileName = filename + "Mean.txt"
writefile = open(newFileName,"w+")
writefile.write("Date Time" + "\t" + "Diameter" + "\t")
for i in range(len(diameter)):
    writefile.write(diameter[i]+"\t")
writefile.write("Total Flow" + "\t" + "Sheath Flow" + "\t" + 
    "Laser Power" + "\t" + "Laser Current" + "\t" + "Median" + "\t" + "Mean" + 
    "\t" + "Geo Mean" + "\t" + "Mode" + "\t" + "Geo Std" + "\t" + "Total Con." + "\n")
for i in range(len(hourList)):
    writefile.write(str(hourList[i])+"\t")
    writefile.write("\t")
    for j in range(len(concentrationMean)):
        writefile.write(str(concentrationMean[j][i])+"\t")
    writefile.write(str(totalFLowMean[i])+"\t")
    writefile.write(str(sheathFlowMean[i])+"\t")
    writefile.write(str(laserPowerMean[i])+"\t")
    writefile.write(str(laserCurrentMean[i])+"\t")
    writefile.write(str(medianNumMean[i])+"\t")
    writefile.write(str(meanNumMean[i])+"\t")
    writefile.write(str(geoMeanMean[i])+"\t")
    writefile.write(str(modeMean[i])+"\t")
    writefile.write(str(geoStdMean[i])+"\t")
    writefile.write(str(totalConMean[i])+"\n")
writefile.close()