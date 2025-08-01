for i in range (int(input())):
    l=list(map(int,input().split()))
    if l[0]+l[1]>=10 or l[0]+l[2]>=10 or l[2]+l[1]>=10:
        print('YES')
    else:
        print('NO')
