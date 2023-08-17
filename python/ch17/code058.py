# Copyright © https://steam.oxxostudio.tw

from firebase import firebase
import time
url = 'https://XXXXXXXX.firebaseio.com'
fdb = firebase.FirebaseApplication(url, None)

for i in range(10):
    fdb.post('/', time.time())

for i in range(10):
    fdb.post_async('/', time.time())
