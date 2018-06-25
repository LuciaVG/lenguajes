import sys
import urllib
import re

sock = urllib.urlopen(sys.argv[1])
htmlSource = sock.read()
sock.close()
print htmlSource

m = re.findall('href=?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', htmlSource)
print m

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', htmlSource)
#print("Urls: ",urls)