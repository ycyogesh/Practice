#Pascal Triangle

n = int(input("Enter Number : "))
temp = [1]
temp1=[]
print(n*' ',temp)
for j in range(0,n):
    for i in range(j,n):
        print(" ",end='')
    temp1.append(1)
    for i in range(1,len(temp)):
        temp1.append(temp[i-1]+temp[i])
    temp1.append(1)
    print(temp1)
    temp = temp1
    temp1 = []