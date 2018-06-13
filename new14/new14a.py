
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')+'?'
if len(url) < 2 : url = "C:\Users\Black\Desktop\PYTHON\mew14"

#print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
#print(data)

commentinfo = ET.fromstring(data)
#print('Retrieved', len(data), 'characters')
lst = commentinfo.findall('comment/count')
print('User count:', len(lst))

for item in lst :
    print('count', item.find('count').text)
    #count = int(comment.find('count').text)
    #lst.append(count)
#print(lst)
