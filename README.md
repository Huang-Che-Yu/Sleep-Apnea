# Ebm 訊號解析

## EBM 簡介

 * EBM檔為使用Embla®的儀器所產生的生理原始訊號。

 * EBM檔包括呼吸、心跳、血氧等生理訊號

## 解析規則
  
### 找出 rec size ：
    1. 使用while讀取檔案
    2. 找到值為32的byte
    3. 判斷32後的3個byte的值是否為0
    4. 若為0則再往後4個byte即為rec size
    5. 若rec size的第一項不為0代表其為正確的rec size

範例(rec size 判斷過程)：

    9 32                  #第9byte的值為32，但第10、11、12byte的值不為0
    14 32                 #第14byte的值為32，但第15、16、17byte的值不為0
    597 32                #第597byte的值為32，且第10、11、12byte的值皆為0
    rec size 0 0 0 0      #判斷第13、14、15、16byte，而第一項為0，故此4個值非rec size
    1613 32               #第1613byte的值為32，但第1614、1615、1616byte的值不為0
    1917 32               #第1917byte的值為32，且第1918、1919、1920byte的值皆為0
    rec size: 180 5 0 0   #判斷第1921、1922、1923、1924byte，而第一項不為0，故此4個值為rec size

程式碼

```py
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
``` 

### 解析主要Data
    1. 在rec size 後一次讀取7200個byte
    2. 每兩個byte為一組
    3. 若第二個byte小於128，則將第二個byte的值乘256再加上第一個byte的值
    4. 若第一個byte大於128，則將第一個byte的值減去第二個byte的值乘256
    5. 將換算後的值加入陣列並重複2. ~ 3.。
    6. 將陣列輸出為波形圖

範例：
    
    77  #第一個byte
    1   #第二個byte
    3   #第一個byte
    255 #第二個byte
    會轉為：
    77+256 = 333
    3-256 = -253

程式碼

```py
cur += 4
n = int(input())
for i in range(0,n*3600,2):
    if f[cur+i+1] > 128:
        t = f[cur+i]-256*(256-f[cur+i+1])
    else:
        t = f[cur+i]+256*f[cur+i+1]
    a.append(t)
plt.plot(a)
plt.show()
```

## 輸出結果


Abdomen.ebm

<img src="https://github.com/Huang-Che-Yu/Sleep-Apnea/blob/main/Waveform/Abdomen.png" width="600">

C3.ebm

<img src="https://github.com/Huang-Che-Yu/Sleep-Apnea/blob/main/Waveform/C3.png" width="600">

Flattening.ebm

<img src="https://github.com/Huang-Che-Yu/Sleep-Apnea/blob/main/Waveform/Flattening.png" width="600">

XFlow_DR.ebm

<img src="https://github.com/Huang-Che-Yu/Sleep-Apnea/blob/main/Waveform/XFlow_DR.png" width="600">


  
## 解析歷程
  
  EBM訊號的轉換原理較難推敲，網路上查無相關轉換規則，故只好向慈中畢業的學長尋求協助，因為學長提供了許多有用的意見及資料，最後才能順利得到轉換規則。

## 未來展望

    1.增加標記
    2.使波形資料更好閱讀

