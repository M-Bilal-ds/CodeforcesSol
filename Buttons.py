for _ in range (int(input())):
    a,k,e=list(map(int,input().split()))
    anna=a;cutie=k
    if e%2==1:
        anna+=1
    print('First' if anna>cutie else 'Second')
    
