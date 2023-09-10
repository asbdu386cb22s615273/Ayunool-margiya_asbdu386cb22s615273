#Imlementation a recurcive calculate a 
factorial of a given number
def recur_factorial(n):
  if n==1:
    reurn n
  else:
    return n*recur_factorial(n-1)
#take input from the user
num=int(input(Enter a number:))    
#check is the number is negative
if num<0:
  print("sorr,factorial does not exist for negative numbers")
elif num==0:
  print("The factorial of 0 is 1")he factorial of",num,"is",recure_factorial(num))