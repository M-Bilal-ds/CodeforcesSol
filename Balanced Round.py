for _ in range (int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    mx=0;c_mx=0;x=sorted(l)
    if n==1:
        print('0')
    else:
        for i in range (n-1):
            if x[i+1]-x[i]<=k:
                c_mx+=1
                if c_mx>mx:
                    mx=c_mx
            else:
                c_mx=0
        print(n-mx-1)
