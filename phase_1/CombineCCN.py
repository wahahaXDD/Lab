from os import listdir
from os.path import isfile, join
import os
onlyfiles = [f for f in listdir(os.path.dirname(os.path.realpath(__file__))) if isfile(join(os.path.dirname(os.path.realpath(__file__)), f))]
'''--------------以上得到目前資料夾內所有檔案--------------'''
newFile = input("輸入合併後的檔名：")
newFile += ".csv"
writeFile = open(newFile,'w')
allfiles =[]
for i in onlyfiles:
    if i.find('.csv') != -1:
        allfiles.append(i)
allfiles = sorted(allfiles)
for i in range(len(allfiles)):
    print(allfiles[i])
    if i == 0:
        with open(allfiles[i],'rb') as f:
            bianry_data = f.read()
            data = bianry_data.decode('cp950','ignore')
            lines = data.splitlines()
            try:
                temp = lines[1]
            except IndexError:
                continue
            date=[]
            for i in temp.split(','):
                date.append(i)
            for i in range(len(lines)):
                if i <4:
                    writeFile.writelines(lines[i])
                    writeFile.writelines('\n')
                elif i==4:
                    writeFile.writelines(date[0])
                    writeFile.writelines(',')
                    writeFile.writelines(lines[i])
                    writeFile.writelines('\n')
                elif i>5:
                    writeFile.writelines(date[1])
                    writeFile.writelines(',')
                    writeFile.writelines(lines[i])
                    writeFile.writelines('\n')
    else:
        with open(allfiles[i],'rb') as f:
            bianry_data = f.read()
            data = bianry_data.decode('cp950','ignore')
            lines = data.splitlines()
            try:
                temp = lines[1]
            except IndexError:
                print(allfiles[i] + "有問題，請檢查")
                break
            date=[]
            for i in temp.split(','):
                date.append(i)
            for i in range(6,len(lines)):
                writeFile.writelines(date[1])
                writeFile.writelines(',')
                writeFile.writelines(lines[i])
                writeFile.writelines('\n')
writeFile.close()