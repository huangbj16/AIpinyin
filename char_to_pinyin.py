import json
from pypinyin import pinyin, lazy_pinyin, Style
'''
f = open('pyhzb.txt', 'r', encoding = 'utf8')
g = open('char_to_pinyin.json', 'w', encoding = 'utf8')

pydict = {}
lines = f.readlines()
for line in lines:
	line = line.replace('\n', '')
	chars = line.split()
	py = chars[0]
	print(py)
	for i in range(1, len(chars)):
		pydict[chars[i]] = py

g.write(json.dumps(pydict, ensure_ascii=False))
f.close()
g.close()
'''
g = open('char_to_pinyin.json', 'w', encoding = 'utf8')

pydict = {}
for i in range(0x4e00, 0x9fa6):
	ch = chr(i)
	py = pinyin(ch, style=Style.NORMAL, heteronym=True)[0]
	pydict[ch] = py

g.write(json.dumps(pydict, ensure_ascii=False))
g.close()