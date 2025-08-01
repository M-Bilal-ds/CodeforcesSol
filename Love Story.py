x=int(input())
s='codeforces'
a=[]
for i in s:
    a.append(i)
for i in range (x):
    sum=0
    str=input()
    b=[]
    for i in str:
        b.append(i)
    for i in range (10):
        if a[i]!=b[i]:
            sum+=1
    print(sum)