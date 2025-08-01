n,k=map(int,input().split())
joy=0
max_joy=-999999999
for i in range (n):
    fi,ti=map(int,input().split())
    if ti<=k:
        joy=fi
    elif ti>k:
        joy=fi-(ti-k)
    if joy>max_joy:
        max_joy=joy
print(max_joy)
