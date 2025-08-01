def checker(x,y):
    if x[-1]==max(x) and y[-1]==max(y):
        return True
    return False
for _ in range(int(input())):
    n=int(input())
    x=[int(i) for i in input().split()]
    y=[int(i) for i in input().split()]
    for i in range(n):
        if x[i]<y[i]:
            if checker(x,y):
                break
            x[i],y[i]=y[i],x[i]
    if checker(x,y):
        print('YES')
    elif checker(x,y)==False:
        print('NO')