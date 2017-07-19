from os import listdir
from os.path import isfile, join
import os
onlyfiles = [f for f in listdir(os.path.dirname(os.path.realpath(__file__))) if isfile(join(os.path.dirname(os.path.realpath(__file__)), f))]
'''--------------以上得到目前資料夾內所有檔案--------------'''
allfiles =[]
for i in onlyfiles:
    if i.find('.txt') != -1:
        allfiles.append(i)
    elif i.find('.TXT') !=-1:
        allfiles.append(i)
allfiles = sorted(allfiles)
finalFile = input("輸入合併後的檔名：")+".txt"
writeFile = open(finalFile,'w')
for i in range(len(allfiles)):
    print(allfiles[i])
    readFile = open(allfiles[i],'r')
    for j in readFile:
        writeFile.write(j)
    readFile.close()
writeFile.close()
