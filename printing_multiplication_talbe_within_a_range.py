#11_program to print multiplication table of a given number in a given range
num=int(input("Enter number to print the multiplication table: "))
lower_r,upper_r=map(int,input("Enter lower and upper range: ").split())
for i in range(lower_r,upper_r+1):
  print(num,"x",i,"=",num*i)

