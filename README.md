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

