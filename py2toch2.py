import json
from pypinyin import pinyin, lazy_pinyin, Style

f = open('char_to_char.json', 'r', encoding = 'utf8')
chdict = json.loads(f.read(), encoding = 'utf8')
f.close()

pychdict = {}

cnt = 0

for ch0 in chdict.keys():
	chs = chdict[ch0]['char']
	for ch1 in chs.keys():
		pys = lazy_pinyin(ch0+ch1)
		py = pys[0] + ' ' + pys[1]
		if not py in pychdict.keys():
			pychdict[py] = {'cnt':0, 'chs':[], 'cnts':[]}
		pychdict[py]['cnt'] = pychdict[py]['cnt'] + chs[ch1]
		pychdict[py]['chs'].append(ch0+ch1)
		pychdict[py]['cnts'].append(chs[ch1])
	cnt = cnt + 1
	if cnt%100 == 0:
		print(cnt)

h = open('py2_to_ch2.json', 'w', encoding = 'utf8')
h.write(json.dumps(pychdict, ensure_ascii=False))
h.close()