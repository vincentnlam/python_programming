print("Hello from Vincent")
x = 10.0
print(x)
y = 4
print(y)
sum = x + y
print(sum)
result = x * y
print(result)
result = x / y
print(result)

def add():
    print(x+y)

add()

def add(a,b):
    print(a+b)

add(1,2)

def add(a):
    print(a+10)

add(5)
result = 1+2*5
print(result)
result = (1+2)*5
print(result)
result = 1*2/5
print(result)
result = 1/2*5
print(result)
print(6%5)
print(13%5)

print(2**3)
print(9-3)
print(8*25)
print(9/2)
print(9/-2)
print(9%2)
print(9%-2)
print(-9%2)
print(9/2.0)
print(4+3*5)
print((4+3)*5)
print(3*4/5)
print(9//2)
x = 2 
x+=3
print(x)
x-=2
print(x)
x*=3
print(x)
x/=2
print(x)
x%=2
print(x)

x=10
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x is not y)

def FtoC(f): # 
    c = (f-32)*5/9
    print (c)
    return c

x = FtoC(60)
print (x)

def CtoF(c):
    f = (c*9/5)+32
    print (f)
    return f

x = CtoF(10)

x = CtoF(20)

x = 10.5
y = 4
x = x+y
print(x)
print(y)

def convert_mileage(mpg): # mpg is a parameter
    litre_per_100k = 235.21/mpg
    # print(litre_per_100k)
    return litre_per_100k

convert_mileage(40) # 40 is an argument

convert_mileage(30)

t = 10

def test():
    z = 10 # z is a local variable.
            # it is not avaialble outside of test()
    print(z)

test()

print(abs(-9))
print(round(3.2))

print(pow(3,3))

print(float(3))

def litres_needed(distance, gas_mileage):
    litres_per_100k = convert_mileage(gas_mileage)
    gas_in_litres = litres_per_100k * distance/100
    return gas_in_litres


x = litres_needed(150,30)
print(x)
y = litres_needed(100,30)
print(y)

print(pow(3,7))
print(round(10.6))
print(int(10.6))
print(int(34.7))
print(round(34.7))
print(float(abs(-86)))