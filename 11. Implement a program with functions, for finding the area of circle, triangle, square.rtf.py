{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 #11. Implement a program with functions, for finding the area of circle, triangle, square.\par
def circle(r):\par
    PI=3.14\par
    return PI*r*r\par
def triangle(b,l):\par
    TR=0.5\par
    return TR*b*l\par
def square(s):\par
    return s*s\par
\par
r=int(input("enter the radius of the circle"))\par
b=int(input("enter the breadth of the triangle"))\par
l=int(input("enter the length of the triangle"))\par
s=int(input("enter the length of side of the square"))\par
\par
print("The area of the circle is:",circle(r))\par
print("The area of the triangle is:",triangle(b,l))\par
print("The area of the square is:",square(s))\par
}
 