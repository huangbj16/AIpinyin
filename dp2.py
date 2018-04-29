import json

f = open('../data/input.txt', 'r', encoding = 'utf8')
strs = f.readlines()
f.close()

g = open('../data/output.txt', 'w', encoding = 'utf8')

print('loading model……')

f = open('pinyin_to_char3.json', 'r', encoding = 'utf8')
pcdict = json.loads(f.read(), encoding = 'utf8')
f.close()

f = open('char_to_char.json', 'r', encoding = 'utf8')
ccdict = json.loads(f.read(), encoding = 'utf8')
f.close()

print('loading model finished')

for k in range(len(strs)):
	str = strs[k]
	pys = str.split()
	#initial
	py0 = pys[0]
	tot0 = pcdict[py0]['cnt']
	chs0 = pcdict[py0]['chs']
	cnts0 = pcdict[py0]['cnts']
	pre = []
	for cnt0 in cnts0:
		pre.append(cnt0/tot0)
	#processing

	chainorder = []

	for n in range(1, len(pys)):
		pro = []
		order = []
		py1 = pys[n]
		tot1 = pcdict[py1]['cnt']
		chs1 = pcdict[py1]['chs']
		cnts1 = pcdict[py1]['cnts']
		for cnt1 in cnts1:
			pro.append(cnt1/tot1)
		#dp
		for i in range(len(chs1)):
			maxp = 0
			p = -1
			for j in range(len(chs0)):
				ch0 = chs0[j]
				ch1 = chs1[i]
				if ch0 in ccdict.keys():
					poss = 0
					if ch1 in ccdict[ch0]['char'].keys():
						poss = ccdict[ch0]['char'][ch1] / ccdict[ch0]['cnt'] * pre[j]
					else:
						poss = 1 / ccdict[ch0]['cnt'] * pre[j]
					if poss > maxp:
						maxp = poss
						p = j
			pro[i] = pro[i] * maxp
			order.append(p)##max j of i
		#succession
		chainorder.append(order)
		pre = pro
		py0 = py1
		tot0 = tot1
		chs0 = chs1
		cnts0 = cnts1
	
	py1 = pys[len(pys)-1]
	tot1 = pcdict[py1]['cnt']
	chs1 = pcdict[py1]['chs']
	cnts1 = pcdict[py1]['cnts']
	for i in range(len(cnts1)):
		if cnt1 != 0:
			pre[i] = pre[i] * tot1 / cnt1

	poss = max(pre)
	maxp = pre.index(poss)
	outputchs = ''
	for i in range(1, len(pys)):
		py = pys[len(pys)-i]
		ch = pcdict[py]['chs'][maxp]
		outputchs = ch + outputchs
		
		maxp = chainorder[len(pys)-i-1][maxp]

	py = pys[0]
	ch = pcdict[py]['chs'][maxp]
	outputchs = ch + outputchs

	g.write(outputchs)
	g.write('\n')
	print('line: %d finished'%(k))
g.close()
	









