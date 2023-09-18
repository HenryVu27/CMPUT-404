import requests
print("requests version:", requests.__version__)
print("GET Google homepage:", requests.get("http://google.com/"))


lab1_code = requests.get("https://raw.githubusercontent.com/HenryVu27/CMPUT-404-lab1/main/lab1/lab1.py")
print("Printing source code:", lab1_code.text)
