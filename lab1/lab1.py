import requests
print("requests version:", requests.__version__)
print("GET Google homepage:", requests.get("http://google.com/"))
