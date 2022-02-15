import urllib.request
import time, os


arr_url = os.environ["TARGET_URLS"]

while(True):
    try:
        for url_ in arr_url:
            open = urllib.request.urlopen(url=url_, timeout=60 * 3)
            data = open.read().decode()
            print(data)
    except:
        pass
    time.sleep(30)
