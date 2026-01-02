import urllib3

url = "https://www.nostarch.com"

headers = urllib3.HTTPHeaderDict()

headers.add("User-Agent","Googlebot")

request = urllib3.request("GET",url,headers=headers)
response = request.data
print (response)

