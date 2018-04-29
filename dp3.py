import json

f = open('../data/input.txt', 'r', encoding = 'utf8')
strs = f.readlines()
f.close()

g = open('../data/output.txt', 'w', encoding = 'utf8')

print('loading model……')

f = open('py2_to_ch2.json', 'r', encoding = 'utf8')
pcdict = json.loads(f.read(), encoding = 'utf8')
f.close()

f = open('ch2_to_ch.json', 'r', encoding = 'utf8')
ccdict = json.loads(f.read(), encoding = 'utf8')
f.close()

f = open('pinyin_to_char3.json', 'r', encoding = 'utf8')
pc2dict = json.loads(f.read(), encoding = 'utf8')
f.close()

print('loading model finished')

for k in range(len(strs)):
	str = strs[k]
	pys = str.split()
	if len(pys) == 1:
		poss = max(pc2dict[pys[0]]['cnts'])
		p = pc2dict[pys[0]]['cnts'].index(poss)
		ch = pc2dict[pys[0]]['chs'][p]
		g.write(ch)
		continue
			
	chainorder = []
	#initial
	py0 = pys[0] + ' ' + pys[1]#first double char
	tot0 = pcdict[py0]['cnt']
	chs0 = pcdict[py0]['chs']#chs of py0
	cnts0 = pcdict[py0]['cnts']
	pre = []
	for cnt0 in cnts0:
		pre.append(cnt0/tot0)
	#processing

	for n in range(2, len(pys)):
		pro = []
		order = []
		py1 = pys[n]#single ch
		pypro = pys[n-1] + ' ' + pys[n]#next double ch
		#pro存下两个字出现的p
		if not pypro in pcdict.keys():
			ch0 = pc2dict[pys[n-1]]['chs'][0]
			ch1 = pc2dict[pys[n]]['chs'][0]
			pcdict[pypro] = {'cnt':1, 'chs':[ch0+ch1], 'cnts':[1]}
			ccdict[ch0+ch1] = {'cnt':1, 'char':{}}
		tot1 = pcdict[pypro]['cnt']
		chs1 = pcdict[pypro]['chs']
		cnts1 = pcdict[pypro]['cnts']
		for cnt1 in cnts1:
			pro.append(cnt1/tot1)
		#dp
		for i in range(len(chs1)):
			maxp = 0
			p = -1
			for j in range(len(chs0)):
				ch0 = chs0[j]
				ch1 = chs1[i][1]
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
		py0 = pypro
		tot0 = tot1
		chs0 = chs1
		cnts0 = cnts1

	poss = max(pre)
	maxp = pre.index(poss)
	outputchs = ''
	for i in range(2, len(pys)):
		py = pys[len(pys)-i] + ' ' + pys[len(pys)-i+1]
		ch = pcdict[py]['chs'][maxp]
		outputchs = ch[1] + outputchs
		
		maxp = chainorder[len(pys)-i-1][maxp]

	py = pys[0] + ' ' + pys[1]
	ch = pcdict[py]['chs'][maxp]
	outputchs = ch + outputchs

	g.write(outputchs)
	g.write('\n')
	print('line: %d finished'%(k))

g.close()









