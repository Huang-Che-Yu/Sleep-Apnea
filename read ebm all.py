import matplotlib.pyplot as plt
from os import listdir
import numpy as np
file = listdir("D:\\醫學資訊\\睡眠資料\\files")

files = []

n = int(input())

for i in file:
    if ".ebm" in i:
        files.append(i)
for j in files:
    plt.figure(figsize=(10,5))
    f = open('files\\'+j,'rb').read()
    a = []
    b = [-1,-1,-1]
    s = [-1,-1,-1,-1]
    cur = 0
    readData = False
    while cur < 36000 and readData == False:
        cur += 1
        if f[cur-1] == 32:
            b[0] = f[cur]
            b[1] = f[cur+1]
            b[2] = f[cur+2]
            cur += 3
            #print(cur,32)
            if b == [0,0,0]:
                s[0] = f[cur]
                s[1] = f[cur+1]
                s[2] = f[cur+2]
                s[3] = f[cur+3]
                #print("rec size:",s[0],s[1],s[2],s[3])
                if s[0] != 0:
                    readData = True
    cur += 4
    #cur = cur + s[0] #+ s[1] + s[2] + s[3]
    for i in range(0,n*3600,2):
        if f[cur+i+1] > 128:
            t = f[cur+i]-256*(256-f[cur+i+1])
        else:
            t = f[cur+i]+256*f[cur+i+1]
        #print(t)
        a.append(t)
    plt.plot(a)
    plt.savefig("waveform ebm\\"+j.replace(".ebm",".png"))
    plt.close()
