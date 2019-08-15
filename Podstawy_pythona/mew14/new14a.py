
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')+'?'
if len(url) < 2 : url = "http://py4e-data.dr-chuck.net/comments_42.xml"

#print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
#print(data)

commentinfo = ET.fromstring(data)
#print('Retrieved', len(data), 'characters')
lst = commentinfo.findall('.//comment')

sum = 0
for item in lst :
    ncount = item.find('count').text
    sum = sum + int(ncount)

print (sum)
