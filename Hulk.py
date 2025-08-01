x=int(input())
if x==1:
    print('I hate it')
elif x>1:
    for i in range (x):
        if i+1<x and i%2==0:
            print('I hate that',end=' ')
        elif i+1<x and i%2!=0:
            print('I love that',end=' ')
        if i+1==x and i%2==0:
            print('I hate it')
        elif i+1==x and i%2!=0:
            print('I love it')
