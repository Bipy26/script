#!/usr/bin/env python
# coding:utf-8
# zabbix钉钉报警
# python3
import requests
import json
import sys
import os
import datetime
import time
import hmac
import hashlib
import base64
import urllib


timestamp = round(time.time() * 1000)
secret = 'xxx'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc,digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

# 说明：这里改为自己创建的机器人的webhook的值
a = "&timestamp=" + str(timestamp) + "&sign=" + str(sign)
b = "xxx"
webhook = b + a
subject = sys.argv[1]
text = sys.argv[2]
data = {
    "msgtype": "markdown",
    "markdown": {
        "title": subject,
        "text": text + "\n\n@17777777777"
    },
    "at": {
        "atMobiles": [
            "17777777777"
        ],
        "isAtAll": False
    }
}
headers = {'Content-Type': 'application/json'}
x = requests.post(url=webhook, data=json.dumps(data), headers=headers)
# if os.path.exists("/usr/local/zabbix/log/dingding.log"):
#     f=open("/usr/local/zabbix/log/dingding.log","a+")
# else:
#     f=open("/usr/local/zabbix/log/dingding.log","w+")
# f.write("\n"+"--"*30)
# if x.json()["errcode"] == 0:
#     f.write("\n"+str(datetime.datetime.now())+"    "+str(user)+"    "+"发送成功"+"\n"+str(text))
#     f.close()
# else:
#     f.write("\n"+str(datetime.datetime.now()) + "    " + str(user) + "    " + "发送失败" + "\n" + str(text))
#     f.close()
