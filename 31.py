list=[0,1,2,3,3,2,1,0]
index = 0
while index < (len(list)/2):
	if list[index]==list[-1-index]:
		index+=1
		#index=1
	else:
		print("no") 
print("Yes")