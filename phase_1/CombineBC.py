from os import listdir
from os.path import isfile, join
import os
onlyfiles = [f for f in listdir(os.path.dirname(os.path.realpath(__file__))) if isfile(join(os.path.dirname(os.path.realpath(__file__)), f))]
'''--------------以上得到目前資料夾內所有檔案--------------'''
newFile = input("輸入合併後的檔名：") + ".csv"
writeFile = open(newFile,'w')
allfiles=[]
for i in onlyfiles:
    if i.find('.CSV')!=-1:
        allfiles.append(i)
    elif i.find('.csv')!=-1:
        allfiles.append(i)
def Check(file):
    temp = []
    flag = True
    read_file = open(file,'r')
    for j in read_file:
        temp.append(j)
        temp = temp[0].split('"')
        temp = temp[1].split('-')
        try:
            int(temp[0])
        except ValueError:
            flag = False
            read_file.close()
            return flag
        read_file.close()
        return flag
for i in range(len(allfiles)):
    print(allfiles[i])
    with open(allfiles[i],'rb') as f:
        bianry_data = f.read()
        data = bianry_data.decode('cp950','ignore')
        lines = data.splitlines()
        flag = Check(allfiles[i])
        for i in lines:
            if flag ==True:
                writeFile.writelines(i)
                writeFile.writelines('\n')
            elif flag ==False:
                flag = True
                continue
writeFile.close()
            
writeFile.close()