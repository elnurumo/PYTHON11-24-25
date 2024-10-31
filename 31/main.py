# 63

n = input() # kitab
l = len(n) # 5
if l % 2 == 0:
    print('0')
else:
    ortaIndex = l//2 # 2
    ortaSimvol = n[ortaIndex]  # n[2]
    print(ortaSimvol)

    # necesen
    # 0123

# 59
import math

a = int(input())
b = int(input())
if a<b:
    print((3*b/abs(a-b))+3*(a+b))
elif a == b:
    # 1-ci üsul
    print(math.sqrt(2*a**2+abs(b**3)))
    # 2 - ci üsul
    print((2*a**2+abs(b**3))**0.5)

else:
    print(a*a/abs(a+b))


# for
m = "Hello"

# for i in range(1,101):
#     print(m, i,'-ci')
for i in m:
    print(i)

# 67
n = int(input())
b = int(input())
s = 0
for i in range(1,n):
    if i**2%b == 0:
        s = s + 1
        # s += 1
print('ədədlərin sayı',s)


# 68

n = int(input()) #3756
n = str(n) # '3756'
c = 0
s = 0
for i in n:
    i = int(i) # '3' = 3
    if i%2 != 0:  # 3 % 2 != 0
        c = c + i # 0 + 3
        s = s + 1 # 0 + 1
print(c,s)


# 66

Email = 'email@inbox.ru'
password = '321abc'

emailUser = input('Email: ')
passwordUser = input('Password: ')
if emailUser == Email and password == passwordUser:
    print('Xosh gelmisiz')
else:
    print('Email və ya şifrə yanlışdır')