{\rtf1\ansi\ansicpg1252\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 #1.  Implement a menu based  program for Arithemetic Calculator\par
def add(a,b):\par
    return a+b\par
def sub(a,b):\par
    return a-b\par
def prod(a,b):\par
    return a*b\par
def div(a,b):\par
    return a/b\par
\par
num1=int(input("enter the first number "))\par
num2=int(input("enter the second number"))\par
choice=input("enter the choice(1/2/3/4)")\par
if choice=="1":\par
    print("The sum is:",add(num1,num2))\par
elif choice=="2":\par
    print("The difference is:",sub(num1,num2))\par
elif choice=="3":\par
    print("The product is:",prod(num1,num2))\par
elif choice=="4":\par
    print("The quotient is:",div(num1,num2))\par
else:\par
    print("enter the valid option")\par
}
 