import datetime, time
import urllib.request
import operator

f = urllib.request.urlopen('http://news.joins.com/article/21844194')
data = f.read().decode('utf-8')
begin = data.find("존경하는 국민 여러분")
end = data.find("감사합니다.")
end += len("감사합니다.")

speech = data[begin:end]
speech = speech.replace('.', ' ')
speech = speech.replace(',', '')
speech = speech.replace('?', '')
speech = speech.replace('!', '')
speech = speech.replace('<p>', '')
speech = speech.replace('</p>', '')
speech = speech.replace('<br/>', ' ')
speech = speech.replace('&nbsp;', ' ')
speech = speech.split()

analyze = {}
for word in speech:
    analyze[word] = analyze.get(word, 0) + 1
sorted_word = sorted(analyze.items(),  key=operator.itemgetter(1), reverse=True)
print(sorted_word)

"""
i = data.find("<dd>현재가")

if i> 0:
    line = data[i:i+100]
    line = line.split(" ")
    f = open("삼성주식추적.txt", "a")
    print(datetime.datetime.now(), "삼성전자주식", line[1], file=f)
    print(datetime.datetime.now(), "삼성전자주식", line[1])
    f.close()
else:
    print(r.status, "got", len(data), "types")
"""
