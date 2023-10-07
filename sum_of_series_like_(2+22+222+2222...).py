#13_program to calculate the sum of series upto n terms
n=int(input("Enter value: "))
l1=[2]
s=2
for i in range(1,n):
  if n==1:
    print(s)
  else:
    x=2*(10**i)
    s+=x
    l1.append(s)
print("Sum upto",n,"terms is:",sum(l1))
