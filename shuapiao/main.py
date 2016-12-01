# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: main.py
@time: 0:07
"""
import json
import os
import random
import sys
import time
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')
PROXY_LIST = []
USER_AGENT_LIST = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
]


def spider_url_by_get(proxy=None):
    url = 'http://snakeapi2.tpmLk.com/s/0Hjl0-014bd'
    #     url = 'http://localhost:8888/'
    #     url = 'http://localhost/proxy_client/test/test_proxy.php'

    #     proxy = random.choice(PROXY_LIST)
    print 'proxy : ', proxy
    count=0
    try:
        proxyHandler = urllib2.ProxyHandler(proxy)
        cookies = urllib2.HTTPCookieProcessor()
        opener = urllib2.build_opener(cookies, proxyHandler, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        req = urllib2.Request(url)

        user_agent = random.choice(USER_AGENT_LIST)
        req.add_header('User-Agent', user_agent)
        data = urllib2.urlopen(req, timeout=100).read()

        dataJson = json.loads(str(data), encoding='utf-8')
        #     dataJson['user_agent'] = str(user_agent)
        #     dataJson['proxy'] = str(proxy)

        data = json.dumps(dataJson)
        count+=1
        if count % 100==0:
            print("Count:{0}".format(count))
        #print 'spider_url_by_get（） +++++++++ ', data
    except Exception, ex:
        print 'spider_url_by_get（） -------- ', str(ex)


def main():
    for proxy in PROXY_LIST:
        for key in proxy.keys():
            value = proxy.get(key, '')
            ip = value.split("//")[1].split(":")[0].strip()

            if ping_ip(ip):
                spider_url_by_get(proxy)
                time.sleep(10)


def getip():
    url = "http://tpv.daxiangdaili.com/ip/?tid=559001229953329&num=10&delay=1"
    req = urllib2.Request(url)
    req.add_header('User-Agent',random.choice(USER_AGENT_LIST))
    PROXY_LIST=[]
    for i in range(0,10):
        data = urllib2.urlopen(req, timeout=300)
        for i in data.readlines():
            PROXY_LIST.append({"http": "http://" + i})
        data.close()
 #       time.sleep(100)
    print(len(PROXY_LIST))
    return PROXY_LIST


def ping_ip(ip=None):
    ping_cmd = 'ping -w 5 %s' % ip

    #     ping_result = os.system(ping_cmd)
    #     print 'ping_cmd : %s, ping_result : %r' % (ping_cmd, ping_result)
    #
    #     if ping_result == 0:
    #         print 'ping %s ok' % ip
    #         return True
    #     else:
    #         print 'ping %s fail' % ip


    ping_result = os.popen(ping_cmd).read()
    print 'ping_cmd : %s, ping_result : %r' % (ping_cmd, ping_result)

    if ping_result.find('100% 丢失') < 0:
        print 'ping %s ok' % ip
        return True
    else:
        print 'ping %s fail' % ip

if __name__ == '__main__':
    while True:
        PROXY_LIST=getip()
        main()
