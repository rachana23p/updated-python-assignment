{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 #7.  Implement a program to reverse a string (without standard librar function)\par
def reverse(string):\par
    str=""\par
    for i in string:\par
        str=i + str\par
    return str\par
string=input("enter the string")\par
print("The reversed string is:",reverse(string))\par
}
 