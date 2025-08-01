for _ in range (int(input())):
    n=int(input());s=0
    x=list(map(int,input().split()))
    y=sorted(x)
    for i in range (n):
        if x[i]%2!=y[i]%2:
            s+=1
            break
    print('NO' if s==1 else 'YES')
        
