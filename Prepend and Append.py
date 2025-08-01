for _ in range (int(input())):
    n=int(input());count=n
    x=input();a=list(x)
    for i in range (n//2):
        if (a[i]=='0' and a[n-1-i]=='1') or (a[i]=='1' and a[n-1-i]=='0'):
            count-=2
        else:
            break
    print(count)        

        
