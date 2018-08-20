import json
from base64 import b64encode
import urllib.request
from urllib import parse

import requests


def verification_code_recognition(img_url):
    host = 'http://txyzmsb.market.alicloudapi.com'
    path = '/yzm'
    method = 'POST'
    appcode = '0513c3e82ad4480787dbfd5a2c4c8cb1'
    querys = ''
    bodys = {'v_type': 'ne4'}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36', }
    url = host + path
    # with open('zhihu.jpg', 'rb') as f:
    #     # 将二进制数据处理成base64再解码成字符串
    #     data = b64encode(f.read())
    img_data = requests.get(img_url, headers=header).content
    # with open('zhihu.jpg', 'rb+') as f:
    #     # 将二进制数据处理成base64再解码成字符串
    #     f.write(img_data)
    # 将二进制数据转换为b64格式
    data = b64encode(img_data)
    bodys['v_pic'] = data

    post_data = parse.urlencode(bodys).encode()
    request = urllib.request.Request(url, post_data)

    request.add_header('Authorization', 'APPCODE ' + appcode)
    #根据API的要求，定义相对应的Content-Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')

    response = urllib.request.urlopen(request)
    content = json.loads(response.read())
    if (content):
        # b'{"msg":"\xe6\x9f\xa5\xe8\xaf\xa2\xe6\x88\x90\xe5\x8a\x9f!","v_code":"XSTT","errCode":0,"v_type":"ne4"}'
        # print(content)
        print(content.get('v_code'))
        return content.get('v_code')
