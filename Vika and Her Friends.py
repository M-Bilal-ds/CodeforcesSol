for _ in range (int(input())):
    n,m,k=list(map(int,input().split()))
    a,b=list(map(int,input().split()))
    check=0
    for i in range (k):
        c,d=list(map(int,input().split()))
        if (abs(a-c)+abs(b-d))%2==0:
            check+=1
    if check>0:
        print('No')
    else:
        print('Yes')
