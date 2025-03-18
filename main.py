import urllib.request
import time, os
import datetime

url1 = os.environ["URL1"]
url2 = os.environ["URL2"]
url3 = os.environ["URL3"]
arr_url = [url1, url2, url3, ]

'''
while(True):
    try:
        for url_ in arr_url:
            open = urllib.request.urlopen(url=url_, timeout=60 * 3)
            data = open.read().decode()
            print(datetime.datetime.now(), url_)
            time.sleep(5)
    except Exception as e:
        print(e)
    try:
        now_hour = int(str(datetime.datetime.now())[11:13])
        if 2 <= now_hour < 7:
            time.sleep(60 * 5)
        elif 15 <= now_hour < 18:
            time.sleep(60 * 5)
        else:
            time.sleep(60 * 2.5)
    except Exception as e:
        print(e)
    time.sleep(1)
'''

while (True):
    try:
        for url_ in arr_url:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                    'Connection': 'close'
                }
                req = urllib.request.Request(url_, headers=headers)
                with urllib.request.urlopen(req, timeout=60 * 3) as open_:
                    data = open_.read().decode()
                    print(f"{datetime.datetime.now()} - {url_} 응답: {data[:200]}")
            except Exception as e:
                print(f"{datetime.datetime.now()} - {url_} 요청 실패: {e}")
            # open = urllib.request.urlopen(url=url_, timeout=60 * 3)
            # data = open.read().decode()
            # print(datetime.datetime.now(), url_)
            time.sleep(5)
    except Exception as e:
        print(e)
    try:
        now_hour = int(str(datetime.datetime.now())[11:13])
        if 2 <= now_hour < 7:
            time.sleep(60 * 5)
        elif 15 <= now_hour < 18:
            time.sleep(60 * 5)
        else:
            time.sleep(60 * 2.5)
    except Exception as e:
        print(e)
    time.sleep(1)
