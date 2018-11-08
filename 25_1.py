#25. Implement a function to count the number of vowels present in the file. 
f=open("22.txt","r")
count=0
for line in f:
	for ch in line:
		if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="v" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U" or ch=="V"):
			count=count+1
print(count)