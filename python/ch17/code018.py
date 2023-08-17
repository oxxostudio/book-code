# Copyright © https://steam.oxxostudio.tw

def hello_world(request):
    request_json = request.get_json()
    print(request.args )   # 讀取 GET 方法參數
    print(request.form )   # 讀取 POST 方法參數
    print(request.path )   # 讀取網址
    print(request.method)  # 讀取叫用方法

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600'
    }

    return ('Hello World!', 200, headers)  # 回傳同意跨域的 header



