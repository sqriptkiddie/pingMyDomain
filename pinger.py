import requests
import time

while True:
    try:
        r = requests.get("https://my-URL")
        print("Ping sent:", r.status_code)
    except Exception as e:
        print("Fehler beim Pingen:", e)
    time.sleep(120)
