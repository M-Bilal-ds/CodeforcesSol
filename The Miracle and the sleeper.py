x=int(input())
for i in range (x):
    a,b=map(int,input().split())
    if b-a>1 and b>=a*2:
        if b%2==0:
            print((b//2)-1)
        else:
            print(b//2)
    elif b-a>1 and b<a*2:
        print(b-a)
    elif b-a==1 and b!=2:
        print(1)
    else:
        print(0)
