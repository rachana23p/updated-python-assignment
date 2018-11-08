#32. Implement a program to check the total number of students. (create a sample file with RegNo, StudentName, Branch)
f=open("32.txt","r")
num=0
for line in f:
	num=num+1
print(num)