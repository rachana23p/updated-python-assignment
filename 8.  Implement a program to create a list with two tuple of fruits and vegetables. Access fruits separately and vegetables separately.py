{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 #8.  Implement a program to create a list with two tuple of fruits and vegetables. Access fruits separately and vegetables separately. \par
list=[("tomato","carrot","raddish"),("mango","orange","banaana")]\par
i = input("enter the whether fruits or vegetables")\par
if i=="fruits":\par
    for v in list[1]:\par
        print(v)\par
elif i=="vegetables":\par
    for v in list[0]:\par
        print(v)\par
else:\par
    print("enter whether fruits or vegetable")\par
    \par
}
 