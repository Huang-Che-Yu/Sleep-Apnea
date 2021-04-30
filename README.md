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

### 解析主要Data
    1. 在rec size 後一次讀取7200個byte
    2. 每兩個byte為一組
    3. 若第二個byte小於128，則將第二個byte的值乘256再加上第一個byte的值
    4. 若第一個byte大於128，則將第一個byte的值減去第二個byte的值乘256
    5. 將換算後的值加入陣列並重複2. ~ 3.。
    6. 將陣列輸出為波形圖

## 輸出結果

Abdomen.ebm
![image](https://github.com/Huang-Che-Yu/Sleep-Apnea/blob/main/Waveform/Abdomen.png = 300 * 200)
  
## 解析歷程
  
  EBM訊號的轉換原理較難推敲，網路上查無相關轉換規則，故只好向慈中畢業的學長尋求協助，因為學長提供了許多有用的意見及資料，最後才能順利得到轉換規則。

## 未來展望

    1. 增加標記
    2.使波形資料更好閱讀

