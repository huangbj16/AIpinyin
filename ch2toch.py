import json

prefix = 'D:/2018spring/IntroAI/pysrf/sina_news/2016-'
profix = '.txt'

chdict = {}

for i in range(1, 12):
	print(i)
	mid = str(i)
	if len(mid) == 1:
		mid = '0' + mid
	filename = prefix + mid + profix
	g = open(filename, 'r', encoding = 'utf8')

	cnt = 0

	jsline = g.readline()
	while jsline:
		line = json.loads(jsline, encoding = 'utf8')['html']
		ch0 = ''
		ch1 = ''
		for ch in line:
			if ch0 >= u'\u4e00' and ch0 <= u'\u9fa5' and ch1 >= u'\u4e00' and ch1 <= u'\u9fa5' and ch >= u'\u4e00' and ch <= u'\u9fa5':
				if not ch0+ch1 in chdict.keys():
					chdict[ch0+ch1] = {'cnt':0, 'char':{}}
				chdict[ch0+ch1]['cnt'] = chdict[ch0+ch1]['cnt'] + 1
				if ch in chdict[ch0+ch1]['char'].keys():
					chdict[ch0+ch1]['char'][ch] = chdict[ch0+ch1]['char'][ch] + 1
				else:
					chdict[ch0+ch1]['char'][ch] = 1
			ch0 = ch1
			ch1 = ch
		
		cnt = cnt + 1
		if cnt % 1000 == 0:
			print(cnt)
		
		jsline = g.readline()
	
	g.close()

print(len(chdict.keys()))

h = open('ch2_to_ch.json', 'w', encoding = 'utf8')
h.write(json.dumps(chdict, ensure_ascii=False))
h.close()