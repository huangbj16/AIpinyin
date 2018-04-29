import json
from pypinyin import pinyin, lazy_pinyin, Style
import re

chdict = {}
f = open('char_to_char2.json', 'r', encoding = 'utf8')
chdict = json.loads(f.read(), encoding = 'utf8')
f.close()

prefix = 'sina_news/2016-'
profix = '.txt'

for i in range(3, 12):
	print(i)
	mid = str(i)
	if len(mid) == 1:
		mid = '0' + mid
	filename = prefix + mid + profix
	g = open(filename, 'r', encoding = 'utf8')

	cnt = 0

	jsline = g.readline()
	while jsline:
		js = json.loads(jsline, encoding = 'utf8')
		line0 = js['html']
		lastch = ' '
		line = ''
		for ch in line0:
			if ch >= u'\u4e00' and ch <= u'\u9fa5':
				line = line + ch
				lastch = ch
			elif lastch != ' ':
				line = line + ' '
				lastch = ' '
		lastch = ' '
		pys = lazy_pinyin(line)
		#print('%d %d\n'%(len(line), len(pys)))
		for i in range(len(line)):
			ch = line[i]
			if lastch != ' ' and ch != ' ':
				if not lastch in chdict.keys():
					chdict[lastch] = {}
				py2 = pys[i]
				if not py2 in chdict[lastch].keys():
					chdict[lastch][py2] = {'cnt':0}
				chdict[lastch][py2]['cnt'] = chdict[lastch][py2]['cnt'] + 1
				chdict[lastch][py2][ch] = chdict[lastch][py2].get(ch, 0) + 1
				
			lastch = ch
		
		cnt = cnt + 1
		if cnt % 1000 == 0:
			print(cnt)
		
		jsline = g.readline()

	g.close()

	print(len(chdict.keys()))

h = open('char_to_char2.json', 'w', encoding = 'utf8')
h.write(json.dumps(chdict, ensure_ascii=False))
h.close()