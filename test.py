import requests


r = requests.get("https://www.smh.com.au")
print(r.status_code)
