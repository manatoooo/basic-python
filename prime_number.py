a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
x=int(a)      
y=int(b)              
def primenum(n):
    if int(n) < 2:
     return False

    for i in range(2,n):
        if n%i ==0:
            return False
    return True

if primenum(x):
   print(str(x)+"は素数")
else:
    print(str(x)+"は素数ではない")

if primenum(y):
   print(str(y)+"は素数")
else:
    print(str(y)+"は素数ではない")