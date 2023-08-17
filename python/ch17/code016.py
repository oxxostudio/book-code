# Copyright © https://steam.oxxostudio.tw

def hello_world(request):
    request_json = request.get_json()
    print(request.args )   # 讀取 GET 方法參數
    print(request.form )   # 讀取 POST 方法參數
    print(request.path )   # 讀取網址
    print(request.method)  # 讀取叫用方法
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'

