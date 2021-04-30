from os import listdir
import matplotlib.pyplot as plt
file = listdir("D:\\醫學資訊\\睡眠資料\\files")

files = []
for i in file:
    if ".txt" in i and "name-Event" not in i:
        files.append(i)

for i in files:
    plt.figure(figsize=(10,2))
    f = open("files\\"+i,"r+")
    line = f.readlines()
    n = 25000
    for j in range(n):
        try:
            line[j] = float(line[j])
        except:
            try:
                line[j] = 0
            except:
                break
    plt.plot(list(map(float,line[6:n])))
    plt.savefig("waveform\\"+i.replace(".txt",".png"))
    plt.close()
