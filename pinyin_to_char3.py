import json

f = open('pinyin_to_char2.json', 'r', encoding = 'utf8')
pydict = json.loads(f.read(), encoding = 'utf8')
f.close()

for k,v in pydict.items():
	count = v['cnt']
	chs = v['char']
	chlist = []
	cntlist = []
	for ch, cnt in chs.items():
		chlist.append(ch)
		cntlist.append(cnt)
	pydict[k] = {'cnt':count, 'chs':chlist, 'cnts':cntlist}

g = open('pinyin_to_char3.json', 'w', encoding = 'utf8')
g.write(json.dumps(pydict, ensure_ascii=False))
g.close()
	
