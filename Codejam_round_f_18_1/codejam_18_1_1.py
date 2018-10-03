t=int(input())
for z in range(1, t + 1):
	length=int(input())
	str1=input()
	str2=input()
	flag=0
	def substring(temp_str):
		l=[]
		for x in range(len(temp_str)):
			for y in range(x,len(temp_str)):
				l.append(temp_str[x:y+1])
		return l
	l1=substring(str1)
	l2=substring(str2)

	def isAnagram(substr1,substr2):
		if substr1==substr2:
			return True
		elif len(substr1)!=len(substr2):
			return False
		else:
			for x in substr1:
				if substr1.count(x)==substr2.count(x):
					continue
				else:
					return False
			return True
	for i in l1:
		for j in l2:
			if isAnagram(i,j):
				flag+=1
				break
			else:
				continue
	print("Case #{}: {}".format(z,flag))

