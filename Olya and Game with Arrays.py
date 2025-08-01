for _ in range (int(input())):
    n=int(input());mini=10**5;l=[];k=[];final=[]
    for i in range (n):
        x=int(input());y=list(map(int,input().split()))
        a=sorted(y)
        l.append(a[0]);k.append(a[1])
    print(sum(k)-min(k)+min(l))

