for _ in range(int(input())):
    a,b=map(int,input().split())
    luckiest=0
    max_luck=-1
    for j in range(a,b+1):
        y=list(str(j))
        mx=-1
        mn=10
        mx=max(y)
        mn=min(y)
        if int(mx)-int(mn)>=max_luck:
            max_luck=int(mx)-int(mn)
            luckiest=j
            if max_luck==9:
                break
    print(luckiest)
    

        
