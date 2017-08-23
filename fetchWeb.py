import datetime, time
import urllib.request

f = urllib.request.urlopen('http://finance.naver.com/item/frgn.nhn?code=005930')
data = f.read().decode('euc-kr')

i= data.find("<dd>현재가")
if i> 0:
    line = data[i:i+100]
    line = line.split(" ")
    f = open("삼성주식추적.txt", "a")
    print(datetime.datetime.now(), "삼성전자주식", line[1], file=f)
    print(datetime.datetime.now(), "삼성전자주식", line[1])
    f.close()
else:
    print(r.status, "got", len(data), "types")
