import jdCookie
import json
import requests
import time
from datetime import datetime,timedelta

FEED_NUM = 10   # [10,20,40,80]

headers = {
    'Content-Type': 'application/json',
    'reqSource': 'weapp',
    'Host': 'draw.jdfcloud.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e25) NetType/WIFI Language/zh_CN',
}

def getTemplate(cookies, functionId, params):
    params += (('reqSource', 'weapp'),)
    response = requests.get(f'https://draw.jdfcloud.com//pet/{functionId}',
                            headers=headers, params=params, cookies=cookies)
    return response.json()


def feed(cookies, feedCount):
    data = getTemplate(cookies, "feed", (('feedCount', str(feedCount)),))
    print("\n【feed】\n ", data["errorCode"])
    
def printTime():
	t = datetime.utcnow() 
	t2 = t + timedelta(hours=8)
	print('utc时间：', t.strftime("%Y-%m-%d %H:%M:%S"))
	print('beijing时间：',t2.strftime("%Y-%m-%d %H:%M:%S"))

def run():
    printTime()
    #for cookies in jdCookie.get_cookies():
    #    feed(cookies, FEED_NUM) 
       
if __name__ == "__main__":
    run()
