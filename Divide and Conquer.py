for _ in range (int(input())):
    n=int(input());
    x=list(map(int,input().split()))
    a=sum(x)
    if a%2==0:
        print('0')
    else:
        mini=10**5 
        for i in x:
            count=0   
            while (i%2==(i//2)%2):
                count+=1;i=i//2
            mini=min(mini,count+1)
        print(mini)


