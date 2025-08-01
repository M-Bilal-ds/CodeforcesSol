x=int(input())
count=0
a=[]
for i in range (x):
    y=input()
    if y not in a:
        count+=1
        a.append(y)
print(count)
