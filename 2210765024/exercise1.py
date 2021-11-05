N=int(input("Please enter a number: "))
sum1=0
sum2=0
for i in range(1,N+1):
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
if N%2==0:
    print((sum1)/(N/2))
else:
    print((sum1)/((N-1)/2))
print(sum2)
