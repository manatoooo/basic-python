a = 1
b = -6
c = 9

# TODO
formula=(b**2-4*a*c)**0.5
x1 = (-b+formula)/(2*a)
x2 = (-b-formula)/(2*a)

print(x1, x2)

#(2)
a = 1
b = 2
c = -8

formula=(b**2-4*a*c)**0.5
x1 = (-b+formula)/(2*a)
x2 = (-b-formula)/(2*a)

print(x1, x2)

#(3)
a = 8
b = -6
c = -35

formula=(b**2-4*a*c)**0.5
x1 = (-b+formula)/(2*a)
x2 = (-b-formula)/(2*a)

print(x1, x2)

#(4)
import cmath
a = 1
b = 0
c = 1

formula=cmath.sqrt(b**2-4*a*c)
x1 = (-b+formula)/(2*a)
x2 = (-b-formula)/(2*a)

print(x1, x2)

