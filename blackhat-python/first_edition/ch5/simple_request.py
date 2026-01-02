import urllib3

body = urllib3.request("GET","https://www.nostarch.com")

print (body.data)
