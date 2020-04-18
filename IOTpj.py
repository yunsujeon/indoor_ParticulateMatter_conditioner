import urllib.request
import json
from pprint import pprint
import time
now = time.localtime()
print ("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

#url1 = 시군구별 바깥 미세먼지 현황 XML or json
#url2 = 내부 미세먼지 1시간단위 XML -> 날짜를 직접 입력해줘야됨 자동으로 넣게끔 해주기?
# url1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=10&ServiceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D&ver=1.3&_returnType=json"
url1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=10&ServiceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D&ver=1.3&"
url2 = "http://apis.data.go.kr/B552584/InairQualityMonitoringService/getInairHourData?date=20200418&serviceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D"

request1 = urllib.request.Request(url1)
response1 = urllib.request.urlopen(request1)
request2 = urllib.request.Request(url2)
response2 = urllib.request.urlopen(request2)

rescode1 = response1.getcode()
rescode2 = response2.getcode()

if rescode1 == 200:
    response_body1 = response1.read()
    print(response_body1.decode('utf-8'))
    #dict = json.loads(response_body.decode('utf-8'))
    #print(response_body)
    #dict = json.loads(response_body)
    pprint(dict)
else:
    print("Error Code:" + rescode1)

if rescode2 == 200:
    response_body2 = response2.read()
    print(response_body2.decode('utf-8'))
    #dict = json.loads(response_body.decode('utf-8'))
    #print(response_body)
    #dict = json.loads(response_body)
    pprint(dict)
else:
    print("Error Code:" + rescode2)