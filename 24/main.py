print('Hello world')

a = 5
b = "5"

print(a*6) # 1. 30
print(b*6) # 2. 55555

a = '4'
b = '5'

print('4'+'5') # '45'
print('a+b') # 9
print('a'+'b') # '4' + '5'

a = '4'
b = '5'

print(a*b) # eror


#  If elif else

a = 5
b = 6

if a < b:
    print('1.')
    if a == 5:
        print('2.')
    else:
        print('4.')
else:
    print('3.')

a = 5
b = 6

if a == 5:
    print('1.')
if b == 6:
    print('2.')



a = int(input('Ədəd daxil et: '))

if a%2 ==0:
    print('cüt')
else:
    print("Tək")



# 53

n = int(input())
if n>2:
    if n%2 == 0:
        print(n-2)
    elif n%2 != 0:
        print(n-1)



# 54

a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print('beraberterefli')
elif a!=b and b!=c and a!=c:
    print('muxtelifterefli')
else:
    print('beraberyanli')

# 56

n = int(input())
if n>0 and n<10:
    print('Birreqemli')
elif n>9 and n<100:
    print('Ikireqemli')


# 57

n = int(input())
a = n-1
b = n+1
if n%2==0:
    print(a,b, 'Tek ededlerdir')
else:
    print(a,b, 'Cut ededlerdir')


# 58
# 1-ci usul
x = int(input())
if x<=5:
    print(abs(x+2) + 3*x)
elif x>5 and x<=7:
    print((3*x**4+10)**0.5)
else:
    print(x**3 - 2)

# 2-ci usul
import math
x = int(input())
if x<=5:
    print(abs(x+2) + 3*x)
elif x>5 and x<=7:
    print(math.sqrt(3*x**4+10))
else:
    print(x**3 - 2)


# 59

a = int(input())
b = int(input())
if a<b:
    print(3*b/ abs(a-b)+3*(a+b))
elif a>b:
    print(2*a**2+abs(b**3))
else:
    print(a**2/abs(a+b))


# 61

saat1 = int(input())
deqiqe1 = int(input())
saniye1 = int(input())
saat2 = int(input())
deqiqe2 = int(input())
saniye2 = int(input())
ferq = (saat2*3600+deqiqe2*60+saniye2)-(saat1*3600+deqiqe1*60+saniye1) 
print(ferq)





