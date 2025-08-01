n=int(input())
tick=input()
if tick.count('4')+tick.count('7')==n:
    a=sum(int(i) for i in tick[:n//2])
    b=sum(int(i) for i in tick[n//2:])
    if a==b:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
