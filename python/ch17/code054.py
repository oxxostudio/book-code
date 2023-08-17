# Copyright © https://steam.oxxostudio.tw

from firebase import firebase
url = 'https://XXXXXXXX.firebaseio.com'
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get('/', None)
print(result)                     # {'fruit': {'apple': 100, 'orange': 200}, 'oxxo': 123}
print(result['fruit']['apple'])   # 100
