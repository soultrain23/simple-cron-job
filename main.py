import urllib.request
import time, os

url1 = os.environ["URL1"]
url2 = os.environ["URL2"]
url3 = os.environ["URL3"]
arr_url = [url1, url2, url3, ]
while(True):
    try:
        for url_ in arr_url:
            open = urllib.request.urlopen(url=url_, timeout=60 * 3)
            data = open.read().decode()
            print(data)
    except:
        pass
    time.sleep(60 * 2)
