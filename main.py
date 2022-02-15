import urllib.request
import time, os

arr_url = ['http://btcatm.cafe24.com/api_provider/cron/status_subscriptions',
           'http://btcatm.cafe24.com/api_provider/cron/status',
           'http://btcatm.cafe24.com/api_provider/cron/order']

while(True):
    try:
        for url_ in arr_url:
            open = urllib.request.urlopen(url=url_, timeout=60 * 3)
            data = open.read().decode()
            print(data)
    except:
        pass
    time.sleep(30)
