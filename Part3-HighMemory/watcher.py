import requests, subprocess, time

while True:
    restart = False
    try:
        res = requests.get("http://localhost:8080")
        if res.status_code != 200:
            restart = True
    except:
        restart = True
        
        
    if restart:
        subprocess.Popen(["python3", "/home/tshoot/PracticalTroubleshooting/Part3-HighMemory/server.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print("Server Started!!")
        time.sleep(30)