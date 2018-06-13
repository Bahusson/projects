import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

link_line = int(input("Enter position: ")) - 1
count = int(input("Enter count: "))
while count >= 0:
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   print(url)
#Wychodzi na to, że po funkcji tags w BS4 można zażądać konkretnego itemu z kolei w nawiasie [] (poniżej)
   url = tags[link_line].get("href", None)
   count = count - 1
