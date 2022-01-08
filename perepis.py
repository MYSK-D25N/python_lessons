count = 0
n1 = int(input())
n2 = int(input())
n = {n1+i for i in range((n2-n1)+1)}
with open("perepis.txt","r") as f:
	for i in f:
		if int(i[-5:]) < 1978:
			count += 1
			print(i.split(' ',1)[0])
	print(count)

print("=================================")

with open("perepis.txt","r") as f:
	for i in f:
		if int(i[-5:]) in n:
			print(i)

