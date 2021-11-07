import requests


url = "http://pollev.com/amrosa"
page = requests.get(url)
print(page.text)