list=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
x=input()
c=int(input())
m=0
for i in range (len(list)):
    if list[i]==x:
        m=i+1
month=m+c
if month>12:
    month=month%12
print(list[month-1])
