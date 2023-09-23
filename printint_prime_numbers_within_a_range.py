#12_program to display all prime numbers within a range
lower_val,upper_val=map(int,input("Enter lower and upper limits of range:").split())
prime_lst=[]
for i in range(lower_val,upper_val+1):
  if i==1:
    print(i,"is not a prime number")
  elif (i>1):
    for j in range(2,i):
      if i%j==0:
        break

    else:
      prime_lst.append(i)
  else:
    print("Enter a valid number!")
print("Prime numbers between",lower_val,"and",upper_val,"are:")
print(prime_lst)

