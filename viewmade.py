#-*- coding: utf-8 -*-
# url1 = 시군구별 바깥 미세먼지 현황 XML or json
# url2 = 내부 미세먼지 1시간단위 XML

#import urllib2
import urllib.request
from bs4 import BeautifulSoup
import time

ventil = 0
token = 0
def select(outsidePM,insidePM,insideTP,outsideTP,hour_use,ventil):
    if hour_use >=8 and hour_use <=19:
        if outsideTP <= insideTP :
            TP = insideTP - outsideTP
        else:
            TP = outsideTP - insideTP

        if outsidePM=="좋음":
            if insidePM == "좋음" :
                if ventil < 3:
                    if (hour_use % 3) == 0:
                        token = 1 #환기
                    else:
                        token = 0 #동작X
                else :
                    token = 0 #동작X
            elif insidePM == "보통" :
                if  TP <6:
                    token = 1 #환기
                else :
                    token = 2 #청정기
            elif insidePM == "나쁨" :
                if TP <6:
                    token = 1 #환기
                else :
                    token = 2 #청정기

        elif outsidePM=="보통":
            if insidePM == "좋음":
                if ventil < 3:
                    if (hour_use % 3) == 0:
                        token = 1  # 환기
                    else:
                        token = 0  # 동작X
                else:
                    token = 0  # 동작X
            elif insidePM == "보통":
                if ventil <3:
                    if (hour_use % 3) == 0:
                        token = 1  # 환기
                    else:
                        token = 2 # 청정기
                else:
                    token = 2  # 청정기
            elif insidePM == "나쁨":
                if TP < 6:
                    token = 1  # 환기
                else:
                    token = 2  # 청정기

        else : #나쁨
            if insidePM == "좋음":
                token = 0  # 동작X
            elif insidePM == "보통":
                if (ventil <3) & (hour_use %3 ==0):
                    if TP<6:
                        token = 1  # 환기
                    else :
                        token = 2  # 청정기
                else:
                    token = 2  # 청정기
            elif insidePM == "나쁨":
                if (ventil <3) & (hour_use %3 ==0):
                    if TP < 6:
                        token = 1  # 환기
                    else:
                        token = 2  # 청정기
                else:
                    token = 2  # 청정기
    else:
        token = 3 #작동시간대가 아님

    return token

now = time.localtime()
# print("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
ymd = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
hour_mk = "%02d" % (now.tm_hour)
hour_use = int(hour_mk)
hour_mk = int(hour_mk) - 1
hour_mk2 = str(hour_mk)
hour_mk = str(hour_mk)
hour = hour_mk + "00"
# print (ymd)
url2make = "http://apis.data.go.kr/B552584/InairQualityMonitoringService/getInairHourData?date=" + ymd + "&serviceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D"
url3make = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst?serviceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D&numOfRows=10&pageNo=1&base_date=" + ymd + "&base_time=" + hour + "&nx=60&ny=126"  # 용산구
# url1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=10&ServiceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D&ver=1.3&_returnType=json"
# url2 = "http://apis.data.go.kr/B552584/InairQualityMonitoringService/getInairHourData?date=20200429&serviceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D"
encode = urllib.parse.quote('서울')
url1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName="+encode+"&pageNo=1&numOfRows=10&ServiceKey=1hRc70j0hQLGKt%2FRR11BRwcecwzH22ihk9IkpSvusWQL7ptv%2FMWp15UGnEj2G%2B0s4Cek0MhPQi5oEYU0orK7NQ%3D%3D&ver=1.3&"
url2 = url2make
url3 = url3make

request1 = urllib.request.Request(url1)
response1 = urllib.request.urlopen(request1)
request2 = urllib.request.Request(url2)
response2 = urllib.request.urlopen(request2)
request3 = urllib.request.Request(url3)
response3 = urllib.request.urlopen(request3)

#request1 = urllib2.Request(url1)
#response1 = urllib2.urlopen(request1)
#request2 = urllib2.Request(url2)
#response2 = urllib2.urlopen(request2)
#request3 = urllib2.Request(url3)
#response3 = urllib2.urlopen(request2)

rescode1 = response1.getcode()
rescode2 = response2.getcode()
rescode3 = response3.getcode()

if rescode1 == 200:
    response_body1 = response1.read()
    response_body1 = response_body1.decode('utf-8')
    # print(response_body1.decode('utf-8'))
else:
    print("Error Code:" + rescode1)

work1 = BeautifulSoup(response_body1, "lxml-xml")
for item in work1.findAll('item'):
    if item.stationName.string == "용산구":
        #print("선택한 지역구 : " + item.stationName.string)
        outsidePMmake = int(item.pm10Value.string)
        #print(outsidePMmake)
        break
# pm10Value : 0~31 좋음 / 31~81 보통 / 81~999 나쁨
if outsidePMmake>=0 & outsidePMmake<32:
    outsidePM = "좋음"
elif outsidePMmake>=32 & outsidePMmake<82:
    outsidePM = "보통"
else:
    outsidePM = "나쁨"

if rescode2 == 200:
    response_body2 = response2.read()
else:
    print("Error Code:" + rescode2)

work2 = BeautifulSoup(response_body2, "lxml-xml")
for facility in work2.findAll('facility'):
    if facility['name'] == '용산역 [국가]':
        break
for item in work2.findAll('item'):
    if (item['name']) == 'PM10':
        break
for hour in work2.findAll('hour') :
    if (hour['h']) == hour_mk2:
        insidePM = hour['grade']
        break
if insidePM == "매우나쁨":
    insidePM == "나쁨" #3단계로만 처리하기위함

if rescode3 == 200:
    response_body3 = response3.read()
    # print(response_body3.decode('utf-8'))
else:
    print("Error Code:" + rescode3)

work3 = BeautifulSoup(response_body3, "lxml-xml")
for item in work3.findAll('item'):
    if item.category.string == 'T1H' :
        insideTP = item.obsrValue.string
        insideTP = str(insideTP)
        insideTP = float(insideTP)
        break
outsideTP = 25
# print ("현재 실내의 온도 가정 : " + str(outsideTP))

token = select(outsidePM, insidePM, insideTP, outsideTP, hour_use, ventil)
token = 3
