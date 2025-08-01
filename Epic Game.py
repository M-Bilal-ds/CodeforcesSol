a,b,n=map(int,input().split())
m=0
o=0
while n!=0:
    for i in range(1,n+1):
        if a%i==0 and n%i==0:
            m=i
    n=n-m
    if n==0:
        print('0')
        break
    for j in range (1,n+1):
        if b%j==0 and n%j==0:
            o=j
    n=n-o
    if n==0:
        print('1')
        break    
    
