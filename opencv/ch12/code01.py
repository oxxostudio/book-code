# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np
from keras.datasets import mnist
from keras import utils

(x_train, y_train), (x_test, y_test) = mnist.load_data()  # 載入訓練集

# 訓練集資料
x_train = x_train.reshape(x_train.shape[0],-1)  # 轉換資料形狀
x_train = x_train.astype('float32')/255         # 轉換資料型別
y_train = y_train.astype(np.float32)

# 測試集資料
x_test = x_test.reshape(x_test.shape[0],-1)     # 轉換資料形狀
x_test = x_test.astype('float32')/255           # 轉換資料型別
y_test = y_test.astype(np.float32)

knn=cv2.ml.KNearest_create()                    # 建立 KNN 訓練方法
knn.setDefaultK(5)                              # 參數設定
knn.setIsClassifier(True)

print('training...')
knn.train(x_train, cv2.ml.ROW_SAMPLE, y_train)  # 開始訓練
knn.save('mnist_knn.xml')                       # 儲存訓練模型
print('ok')

print('testing...')
test_pre = knn.predict(x_test)                  # 讀取測試集並進行辨識
test_ret = test_pre[1]
test_ret = test_ret.reshape(-1,)
test_sum = (test_ret == y_test)
acc = test_sum.mean()                           # 得到準確率
print(acc)
