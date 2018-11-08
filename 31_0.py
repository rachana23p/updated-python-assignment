#31. Implement a program to check the elements of a list is a palindrome or not.
list=["madam","maam"]
for i in list:
	string=i
    if(string==string[::-1]):
    	print("The string is a palindrome i.e,",string)
	else:
    	print("The string isn't a palindrome i.e,"string)