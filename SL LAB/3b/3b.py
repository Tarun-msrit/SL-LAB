import sys
import os
from functools import reduce

dict={}

with open(sys.argv[1]) as file:
	for line in file:
		for word in line.split():
			dict[word]=dict.get(word,0)+1
	print(dict)

sl=[]
sl=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(sl[:10])

word=[]
for i,j in sl[:10]:
	word.append(len(i))
print(word)

sum=reduce((lambda x,y:x+y),word)
print("Avg is",sum/len(word))

print([x*x for x in word if x%2!=0])