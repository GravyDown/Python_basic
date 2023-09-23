#5_check whether a number is palindrome or not
n=int(input("Enter number: "))
num=n
reversed_num=0
while num!=0:
  digit=num%10
  reversed_num=reversed_num*10+digit
  num//=10
if n==reversed_num:
  print("Number is palindrome")
else:
  print("Number is NOT palindrome")
