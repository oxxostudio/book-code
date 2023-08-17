# Copyright © https://steam.oxxostudio.tw

from firebase import firebase
import time
url = 'https://XXXXXXXX.firebaseio.com'
fdb = firebase.FirebaseApplication(url, None)

for i in range(10):
    fdb.put('/', f'a{i}', time.time())

for i in range(10):
    fdb.put_async('/', f'b{i}', time.time())
