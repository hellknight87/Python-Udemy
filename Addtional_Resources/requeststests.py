import requests

r = requests.get("http://oyomart.com")
print("Status:", r.status_code)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)