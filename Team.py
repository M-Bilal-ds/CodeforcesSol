x=int(input())
sum=0
for i in range (x):
    a,b,c=map(int,input().split())
    if a+b+c>=2:
        sum=sum+1
print(sum)
        
    
