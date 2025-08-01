for _ in range (int(input())):
    b=[]
    c=[]
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))==1:
        print(-1)
    elif a.count(1)>=1:
        for i in range(n):
            if a[i]==1:
                b.append(a[i])
            else:
                c.append(a[i])
        print(len(b),len(c))
        for i  in b:
            print(i,end=' ')
        print()
        for i  in c:
            print(i,end=' ')
        print()
    else:
        avg=int(sum(a)/n)
        for i in range (n):
            if a[i]<=avg:
                b.append(a[i])
            else:
                c.append(a[i])
        print(len(b),len(c))
        for i  in b:
            print(i,end=' ')
        print()
        for i  in c:
            print(i,end=' ')
        print()
