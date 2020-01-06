import sys
import requests

print(sys.version)
print(sys.executable)

r = requests.get("https://www.smh.com.au")
print(r.status_code)
