# Copyright © https://steam.oxxostudio.tw

from firebase import firebase
url = 'https://XXXXXXXX.firebaseio.com'
fdb = firebase.FirebaseApplication(url, None)
def oxxo_callback(response):
    print('ok')
fdb.put_async('/', 'oxxo', 123, oxxo_callback)  # ok
