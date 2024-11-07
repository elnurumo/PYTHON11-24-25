# 72

n = int(input('sayı daxil et: ')) # sayı daxil et
papka = []
for i in range(0,n):
    a = int(input()) # ixtiyari eded
    papka.append(a)
mini = min(papka)
print(mini)


a = [1,2,3]
b = a
b.append(4)

# c = a==b
print(a,b)

# 74

for i in range(1,1000,2):
    print(i)


# 75

a = [15,12,16,11,9]
for i in a:
    if i%2 != 0:
        k = i**2 
        print(k)

## 76

n = int(input())

if n>0:
    print('Müsbətdir')
elif n>0:
    print('musbetdirrrrr')
elif n == 0:
    print('Eded 0 dir')

# # 77

s = 0
for i in range(1,100):
    i = str(i)
    s = s + i.count('3')
print(s)


# 78

n = int(input())
k = []
m = []
for i in range(0,n):
    a=int(input())
    if a%2==0:
      m.append(a)
    else:
       k.append(a)
print(m,k)       

# 79

n = int(input()) #12000
s = 0
while n%10 == 0:
    s = s+1
    n = n//10
print(s)

# 80


n=int(input())
s=0
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            s=s+1
    if s==0:
        print("sade ededdir")   
    else:
        print("murekkebdir")
elif n == 1:
    print('1 ne sadedir nede murekkeb')    

# 81

n=int(input())
s=0
for i in range(1,n+1):
    s = s + (-1)**(i+1)*i*(i+1)
print(s)
