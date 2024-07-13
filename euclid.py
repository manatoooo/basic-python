a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
x=int(a)
y=int(b)
if x > y:
    while y != 0: 
        z = x % y
        x = y
        y = z
    print(str(x))
elif x < y:
    while x != 0: 
        z = y % x
        y = x
        x = z
    print(str(y))
else:
    print(str(x))