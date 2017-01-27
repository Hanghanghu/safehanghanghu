
import urllib2
from bs4 import BeautifulSoup
from pprint import pprint
import json
import sys
reload(sys)
sys.setdefaultencoding('euc-kr')

f = open("safe.txt", "w")

f1 = open("safe.txt", "r")

f2 = open("safe.json", "w")

url = "http://www.safe182.go.kr/index.do"

url2 = "http://www.safe182.go.kr"

req = urllib2.Request(url)

data = urllib2.urlopen(req).read()

soup = BeautifulSoup(data, 'html.parser')

Data = soup.find('div', {'id': "m_bn_move"})

imageData = Data.find("img")

imgData = '[{"img" : "' + url2 + (imageData.get('src')) + '",'

idenData = Data.find("dl")

idenDataStr = str(idenData)
idenDataStr = idenDataStr.replace('<dl>' + '\n' + '<dt>','"name":"')
idenDataStr = idenDataStr.replace('</dt>' + '\n' + '<dd>','","age":"')
idenDataStr = idenDataStr.replace('</dd>' + '\n' + '<dd>','","spot":"')
idenDataStr = idenDataStr.replace('</dd>' + '\n' + '</dl>','"}]')

f.write(imgData.encode('utf-8'))
f.write(idenDataStr)

f.close()

string = str(f1.read())

JsonData = json.dumps(string).decode('unicode-escape').encode('utf-8')

f1.close()

f2.write(JsonData)

f2.close()
