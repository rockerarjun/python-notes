"""
String variable and format(): provides the ability to do complex variable substitutions and value formatting
https://pyformat.info/

%c	character
%s	string conversion via str() prior to formatting
%i	signed decimal integer
%d	signed decimal integer
%u	unsigned decimal integer
%o	octal integer
%x	hexadecimal integer (lowercase letters)
%X	hexadecimal integer (UPPERcase letters)
%e	exponential notation (with lowercase 'e')
%E	exponential notation (with UPPERcase 'E')
%f	floating point real number
%g	the shorter of %f and %e
%G	the shorter of %f and %E

Escape Characters:\s Space, \n Newline, \r Carriage Return, \t Tab, \e Escape, \b Backspace
"""
words = "I LOVE READING"
name =  "arjun"
age = 24
weight = 65.50

print ("My name is %s , i'm %d years old, and i'm %f kg" %(name,age,weight))
print ("My name is %s ,i'm %d years old, and i'm %.2f kg" %(name ,age,weight))

print("\nusing format - New")
print("My name is {} , i'm {} years old , and i'm {} kg".format(name,age,weight))
print("My name is {0}, i'm {2} years old ,and i'm {1} kg".format(name,age,weight))
print("My name is {1}, i'm {0} years old ,and i'm {2} kg".format(name,age,weight))
print("My name is {0}, i'm {1} years old ,and i'm {2} kg".format(name,age,weight))

print("\n Advance Use << http://pyformat.info >>")
nameDict={'name': 'arjun' , 'age': '24'}
values = [10,20,30,40,50,60]
print("\nMy name is {name} and i'm {age} years old!".format(name="arjun",age=24))
print("\nMy name is {n[name]} and i'm {n[age]} years old!".format(n=nameDict))
print("\nvalue is {v[1]} and {v[5]}".format(v=values))

print("\n Formatting Number and float" )
print("{:d}".format(1234))
print("{:10d}".format(1234))
print("{:010d}".format(1234))
print("{:f}".format(1.2345678))
print ("{:.2f}".format(1.2345678))


print ("\nPadding >>");
print(" <Left: {:<10}".format("READING"))
print("Right: {:>10}".format("READING"))
print("Center: {:10}".format("READING"))
print('Left with _ : {:_<10}'.format("READING"))
print('Center with _ : {:_^10}'.format("AM"))

print("\nTruncating >> ");
print('Only first 5 chars : {:.5}'.format("Enjoying  With Python"))
print('padding : {:_^10.5}'.format("Enjoying  With Python"))









