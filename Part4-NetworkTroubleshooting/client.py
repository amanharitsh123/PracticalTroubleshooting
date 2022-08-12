import sys, requests, time

url = sys.argv[1]
while True:
    time.sleep(1)
    try:
        res = requests.get(url)
        print(res.status_code, ":", res.content)
    except Exception as e:
        print(f"Exception {e} occured.")