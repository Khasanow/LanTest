#a=5
#while a>0:
   # print(a, end=' ')
   # a-=1

a=5
while a<=55:
    print(a)
    a+=2
print()
a = 5
while a <= 55:
    if a %2 ==1:
        print(a)
    a += 2

print()

i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2

n=int(input())
c=1
while c <= n:
    print('*' * c)
    c += 1

print()
n=int(input())
stars = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'
