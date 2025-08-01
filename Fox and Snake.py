m,n=map(int,input().split())
s=1
for i in range (m):
    if i%2==0:
        for j in range (n):
            print('#',end='')
        print()
    else:
        if s%2!=0:
            for j in range (n-1):
                print('.',end='')
            print('#')
            s+=1
        else:
            print('#',end='')
            for j in range (n-1):
                print('.',end='')
            s+=1
            print()
        
    
            
