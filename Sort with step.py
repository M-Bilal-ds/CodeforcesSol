for _ in range (int(input())):
    l,k=map(int,input().split())
    n=list(map(int,input().split()))
    chk=0
    for i in range (1,l+1):
        if abs(n[i-1]-i)%k!=0:
            chk+=1
    if chk>2:
        print('-1')
    elif chk==2:
        print('1')
    else:
        print('0')
