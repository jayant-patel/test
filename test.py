import requests

# Test Program

r = requests.get("https://www.smh.com.au")
print(r.status_code)
