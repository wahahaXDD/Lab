newFile = input("輸入合併後的檔名：")
newFile += ".txt"
writeFile = open(newFile,'w')
fileCount = input("請輸入需要合併的檔案數目：")
for i in range(int(fileCount)):
    filename = input("第{0}個檔案：".format(i+1)) +".txt"
    if i==0:
        with open(filename,'rb') as f:
            bianry_data = f.read()
            data = bianry_data.decode('cp950','ignore')
            lines = data.splitlines()
            for line in lines:
                writeFile.writelines(line)
                writeFile.writelines('\n')
    else:
        with open(filename,'rb') as f:
            binary_data = f.read()
            data = binary_data.decode('cp950','ignore')
            lines = data.splitlines()
            temp = 0
            for i in range(len(lines)):
                if lines[i][0:8]=="Sample #":
                    temp = i+1
                    break
            for i in range(temp,len(lines)):
                writeFile.writelines(lines[i])
                if i !=len(lines):
                    writeFile.writelines('\n')
writeFile.close()

        