x=int(input())
for i in range (x):
    a=int(input())
    b=input().split()
    if len(b)==len(set(b)):
        print('YES')
    else:
        print('NO')
        
