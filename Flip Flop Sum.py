for _ in range (int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    a=0
    if x.count(-1)==0:
        print(sum(x)-4)
    elif x.count(-1)==1:
        print(sum(x))
    else:
        if -1 in x:
            for i in range (n-1):
                if x[i]==-1 and x[i+1]==-1:
                    x[i]=1;x[i+1]=1
                    break
            print(sum(x))
        else:
            print(sum(x)-4)
