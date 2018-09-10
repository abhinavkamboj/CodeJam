order=input("Enter the order: ")
l=list(order)
count=0
z=1
for x in l[:len(l)-1:]:
	#temp=""
	for y in range(z,len(l)):
		if x!=l[y]:
			count=count+1
			
			z+=1
			break
			#temp=temp+x
		else:
			z+=1
			break
			
	#print(count)
	#print(" ")
if l[len(l)-1]=="-":
	count+=1
	print(count)
elif l[len(l)-1]=="+":
	print(count)
elif "-" not in l:
	print(count)
elif '+' not in l:
	count+=1
	print(count)


