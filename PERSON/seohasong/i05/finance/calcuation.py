# /usr/local/bin python3
# -*- coding: utf-8 -*-
import json, re, pprint

def filt(l, a):
	def ox(lv, av): return 1 if re.compile(lv).match(av)!=None else 0
	return sum(sum(av["cost"] for lv in l if ox(lv, av["usage"])) for av in a)

def operation(a):
	# a.append({"cost": 3146, "time": "170712", "usage": "구매(이모티콘)"})
	# a.pop()
	# a.insert(-1,{"cost": -1260, "time": "170711", "usage": "이익잉여금"})
	# a[-2]["time"]="170703"
	pprint.pprint(a); l = [""]
	print("balance: %s"%filt(l ,a))

with open("history.json", "r") as history: history = json.load(history)
operation(history["account"])
with open("history.json", "w") as next_history: json.dump(history, next_history)

import sys
print(sys.version)
