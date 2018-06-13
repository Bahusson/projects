import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter - ')+'?'
if len(url) < 2 : url = "http://py4e-data.dr-chuck.net/comments_42.json"

#print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
#print(data)

info = json.loads(data)
#print('User count:', len(info))

sum = 0
total = 0
for item in info['comments']:
    item['count']
    sum += int(item['count'])
    total += 1

print('Count:', total)
print('Sum:', sum)
