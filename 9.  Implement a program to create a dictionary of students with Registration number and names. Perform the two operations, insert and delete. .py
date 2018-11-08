#9.  Implement a program to create a dictionary of students with Registration number and names. Perform the two operations, insert and delete. 
students={"001":"Rachana",
         "002":"nakshatra",
          "003":"amulya"}
for i in students:
    print(i,students[i])
print("****************")
students["004"]="aishwarya"
for i in students:
    print(i,students[i])
print("****************")
students.pop("002")#removes the specific key value
for i in students:
    print(i,students[i])
print("*****************")
students.popitem() #removes the last inserted value
for i in students:
    print(i,students[i])
print("*****************")
students["001"]="megha" #insert to the same key again replaces the value
for i in students:
    print(i,students[i])
