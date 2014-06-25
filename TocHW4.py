# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
import urllib2, logging, csv, re, json, sys

url = sys.argv[1]
logging.info(url)
cc = urllib2.urlopen(url)
csv_read = csv.reader(cc)
ss = json.load(cc)

lis = [{1:1}]

ansstr = ''
anscnt = 0

chk = 0
for i in ss:
	chk = i[u'土地區段位置或建物區門牌'].find(u'巷')
	if chk != -1:
		cnt = chk + 1
		print i[u'土地區段位置或建物區門牌'][0:cnt]
	chk = i[u'土地區段位置或建物區門牌'].find(u'大道')
	if chk != -1:
		cnt = chk + 2
		print i[u'土地區段位置或建物區門牌'][0:cnt]
	chk = i[u'土地區段位置或建物區門牌'].find(u'街')
	if chk != -1:
		cnt = chk + 1
		strin = i[u'土地區段位置或建物區門牌'][0:cnt]
	chk = i[u'土地區段位置或建物區門牌'].find(u'路')
	if chk != -1:
		cnt = chk + 1
		strin = i[u'土地區段位置或建物區門牌'][0:cnt]
	if chk == -1:
		continue

	chk = 0
#	print i[u'交易年月']
	ym = i[u'交易年月']
	for inin in lis:
		if inin.has_key(strin) == True:
			if inin.has_key(ym) == False:
				tmp = inin['num']
				inin['num'] = tmp + 1
				inin[ym] = 1
				chk = 1
			else:
				chk = 1
			if i[u'總價元'] > inin['high']:
				inin['high'] = i[u'總價元']
			if i[u'總價元'] < inin['low']:
				inin['low'] = i[u'總價元']
	if chk == 0:
		dic = {}
		dic['name'] = strin
		dic['num'] = 1
		dic[strin] = 1
		dic[ym] = 1
		dic['high'] = i[u'總價元']
		dic['low'] = i[u'總價元']
		lis.append(dic)

lis.pop(0)
for ii in lis:
	if ii['num'] >= anscnt:
		anscnt = ii['num']
#		print ii
for ii in lis:
	if ii['num'] == anscnt:
		print ii['name'],', 最高成交價:',ii['high'],', 最低成交價:',ii['low']
