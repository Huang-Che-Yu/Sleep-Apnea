import matplotlib.pyplot as plt
import numpy as np

f = open('files\\Abdomen.ebm','rb').read()
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
        print(cur,32)
        if b == [0,0,0]:
            s[0] = f[cur]
            s[1] = f[cur+1]
            s[2] = f[cur+2]
            s[3] = f[cur+3]
            print("rec size:",s[0],s[1],s[2],s[3])
            if s[0] != 0:
                readData = True
cur += 4
#cur = cur + s[0] #+ s[1] + s[2] + s[3]
n = int(input())
for i in range(0,n*3600,2):
    #print(f[cur+i])
    #print(f[cur+i+1])
    if f[cur+i+1] > 128:
        t = f[cur+i]-256*(256-f[cur+i+1])
    else:
        t = f[cur+i]+256*f[cur+i+1]
    a.append(t)
plt.plot(a)
plt.show()
