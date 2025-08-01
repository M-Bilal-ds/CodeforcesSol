for _ in range (int(input())):
    b,c,h=list(map(int,input().split()))
    print(2*(c+h)+1 if c+h<b else b+b-1)
        
    
