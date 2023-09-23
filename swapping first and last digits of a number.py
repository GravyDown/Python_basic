#3_swap the first and last digit of given number
num=int(input("Enter your no.: "))
str1=str(num)
l1=[]
for i in str1:
  l1.append(i)
x=len(l1)
if (x==1):
  print("Please enter valid number")
else:
  l1[0],l1[x-1]=l1[x-1],l1[0]
  print("New number is: ",end='')
  for i in l1:
    print(i,end="")
