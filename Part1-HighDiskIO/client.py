import sys, requests, time

url = sys.argv[1]
while True:
    start = time.time()
    res = requests.get(url)
    print(f"StatusCode: {res.status_code} Latency: {time.time() - start} seconds")
    #print(res.content)
    time.sleep(1)