import requests


response = requests.get("https://raw.githubusercontent.com/lexiebartlettt/CMPUT404Lab1/master/lab1.py")

print response.text
