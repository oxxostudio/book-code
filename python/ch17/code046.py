# Copyright © https://steam.oxxostudio.tw

from firebase import firebase
url = 'https://XXXXXXXX.firebaseio.com'
fdb = firebase.FirebaseApplication(url, None)    # 初始化，第二個參數作用在負責使用者登入資訊，通常設定為 None
fdb.put('/','oxxo',123)

