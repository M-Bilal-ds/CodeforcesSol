n=int(input())
for i in range (n):
    m=int(input())
    s=0
    b=0
    for j in range (m):
        a=list(map(int,input().split()))
        if a[0]<a[1]:
            s+=a[0]
            if b<a[1]:
                b=a[1]
        else :
            s+=a[1]
            if b<a[0]:
                b=a[0]
    print((2*s)+(2*b))
