for i in range (int(input())):
    x=int(input())
    y=list(map(int,input().split()))
    if y!=sorted(y):
         print('0')
    else:
        mini=100000000000
        for i in range (x-1):
            if y[i+1]-y[i]<mini:
                mini=y[i+1]-y[i]
        print(f'{(mini//2)+1}')
    
    
    
