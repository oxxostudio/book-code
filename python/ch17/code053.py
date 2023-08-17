# Copyright © https://steam.oxxostudio.tw

from firebase import firebase
url = 'https://XXXXXXXX.firebaseio.com'
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get('/fruit','apple')
print(result)
