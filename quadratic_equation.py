# quadratic equation ax**2 + b*c + c
# a, b and c will expect a value
# general formula x = ((-b+-sqrt(b**2-4*a*c))/(2*a))

import cmath

a = int(input("enter first number (a!= 0): "))
b =int(input("enter second number: "))
c = int(input("enter third number: "))

d = (b**2)-(4*a*c)

first_root = ((-b-cmath.sqrt(d))/(2*a))
second_root = ((-b+cmath.sqrt(d))/(2*a))

print ("the roots are: ",first_root,second_root)