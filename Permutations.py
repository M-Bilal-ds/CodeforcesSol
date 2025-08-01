n=int(input())
a=1
if n%2==0:
    for i in range (1,(n//2)+1):
        print(a+1,a,end=' ')
        a=a+2
else:
    print('-1')
