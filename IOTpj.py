# url1 = 시군구별 바깥 미세먼지 현황 XML or json
# url2 = 내부 미세먼지 1시간단위 XML

import urllib.request
import json
from pprint import pprint
import time
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

now = time.localtime()
# print("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
ymd = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
hour_mk = "%02d" % (now.tm_hour)
hour_mk = int(hour_mk)-1
hour_mk2 = str(hour_mk)
hour_mk = str(hour_mk)
hour = hour_mk + "00"
# print (ymd)
# print(hour)
url2make = "http://apis.data.go.kr/B552584/InairQualityMonitoringService/getInairHourData?date=" + ymd + "&serviceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D"
url3make = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst?serviceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D&numOfRows=10&pageNo=1&base_date="+ymd+"&base_time="+hour+"&nx=60&ny=126" #용산구
# url1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=10&ServiceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D&ver=1.3&_returnType=json"
# url2 = "http://apis.data.go.kr/B552584/InairQualityMonitoringService/getInairHourData?date=20200429&serviceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D"
url1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=10&ServiceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D&ver=1.3&"
url2 = url2make
url3 = url3make

request1 = urllib.request.Request(url1)
response1 = urllib.request.urlopen(request1)
request2 = urllib.request.Request(url2)
response2 = urllib.request.urlopen(request2)
request3 = urllib.request.Request(url3)
response3 = urllib.request.urlopen(request3)

rescode1 = response1.getcode()
rescode2 = response2.getcode()
rescode3 = response3.getcode()

if rescode1 == 200:
    response_body1 = response1.read()
    # print(response_body1.decode('utf-8'))
else:
    print("Error Code:" + rescode1)

work1 = BeautifulSoup(response_body1, "lxml-xml")
for item in work1.findAll('item'):
    if item.stationName.string == '용산구':
        print (item.stationName.string)
        print(item.pm10Value.string)
        break



if rescode2 == 200:
    response_body2 = response2.read()
else:
    print("Error Code:" + rescode2)

work2 = BeautifulSoup(response_body2, "lxml-xml")
for facility in work2.findAll('facility'):
    if facility['name'] == '용산역 [국가]':
        print(facility['name'])
        break
for item in work2.findAll('item'):
    if (item['name']) == 'PM10':
        print(item['name'])
        break
for hour in work2.findAll('hour') :
    if (hour['h']) == hour_mk2 :
        print(hour['h'], hour['grade'])
        break


if rescode3 == 200:
    response_body3 = response3.read()
    # print(response_body3.decode('utf-8'))
else:
    print("Error Code:" + rescode3)

work3 = BeautifulSoup(response_body3, "lxml-xml")
for item in work3.findAll('item'):
    if item.category.string == 'T1H' :
        print(item.category.string)
        print(item.obsrValue.string)
        break

