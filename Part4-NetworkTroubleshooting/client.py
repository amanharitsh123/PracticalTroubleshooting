import sys, requests, time, datetime
import datetime



url = sys.argv[1]
while True:
    time.sleep(1)
    try:
        res = requests.get(url)
        x = datetime.datetime.now().replace(microsecond=0)
        print(x,res.status_code, ":", res.content)
    except Exception as e:
        print(f"Exception {e} occured.")