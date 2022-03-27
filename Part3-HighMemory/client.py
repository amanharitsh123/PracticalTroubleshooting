import sys, requests, time

url = sys.argv[1]
while True:
    start = time.time()
    try:
        res = requests.get(url)
        print(f"StatusCode: {res.status_code} Latency: {time.time() - start} seconds")
        #print(res.content)
        time.sleep(1)
    except:
        print("Server not reachable!")
        time.sleep(1)