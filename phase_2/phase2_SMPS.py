from transformSMPS import *
import operator
filename = input("請輸入要統一格式的檔案名：") + ".txt"
rawData = readFile(filename)
columnIntel = findDataIntel(rawData)
CheckedList = fileCheck(rawData,columnIntel)
DateTime= dateTime(CheckedList,columnIntel)
'''比較Datetime scenario:
1.    Date 不同    time不重要   →直接加一行資料   ←用同樣原始資料繼續比dictionary
2.    Date 同      time同      →直接加一行資料    ←兩個都接下去比
3.    Date 同      time不同    →加dicionary資料  ←用同樣原始資料繼續比dictionary'''

#Step 1. get combined file. Get it's datetime and data length after row 14.
#Step 2. put Datetime in a dict to be compared with
#Step 3. compare by the rule above
#Step 4. Write line in
def transformdate(datetime):
    strdatetime = str(datetime)
    date = strdatetime[5:7]+"/"+strdatetime[8:10]+"/"+strdatetime[2:4]
    time = strdatetime[11:]
    return date,time
def add2RawData(Row):
    stuff = ["x"]
    stuff.append(tempdatetime[0])
    stuff.append(tempdatetime[1])
    for i in range(len(CheckedList[13])-3):
        stuff.append("x")
    CheckedList.insert(14+Row,stuff)
a="d{0}"
addnum = 0
count=1
dateTimeDict = {}
for i in range(0,len(DateTime)-1):
    delta = DateTime[i+1]-DateTime[i]
    if delta >timedelta(seconds=361):
        addnum = delta/timedelta(seconds=359)
        for j in range(0,(int(addnum))):
            b=DateTime[i]+j*timedelta(seconds=360)
            dateTimeDict.update({(a.format(len(DateTime)+count)):b})
            count +=1
    else:
        dateTimeDict.update({a.format(i):DateTime[i]})
sorted_dic = sorted(dateTimeDict.items(), key=operator.itemgetter(1))
countRow = 0
for i in range(len(sorted_dic)):
    tempdatetime = transformdate(sorted_dic[i][1])
    if CheckedList[14+countRow][1] == tempdatetime[0]:   #Date 相同
        if CheckedList[14+countRow][2] != tempdatetime[1]:   #Time 不同
            add2RawData(countRow)
    else:    #Date 不同
        add2RawData(countRow)
    countRow+=1
unifiedFile = input("請輸入整理完後的檔案名：") + ".txt"
writefile = open(unifiedFile,"w+")
for i in range(len(CheckedList)):
    if i < 13:
        writefile.writelines(CheckedList[i])
        writefile.writelines("\n")
    else:
        for j in range(len(CheckedList[i])):
            writefile.write(CheckedList[i][j]+"\t")
        writefile.write("\n")
writefile.close()