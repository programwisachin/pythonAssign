
li = []
n=50 
for i in range(2,n+1):
    flag=0
    for j in range(2,int(i/2)+1):
        if(i%j==0):
            flag=1
            break  
    if(flag==0):
        li.append(i)
print(li)
