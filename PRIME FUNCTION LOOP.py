
def isprime(num):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               return False
       else:
           return True
a = int(input('First number:'))
b = int(input('Second number:'))

print("Prime numbers between", a, "and", b, "are:")

for num in range(a, b + 1):
  prime_val= isprime(num)
  if(prime_val):
      print(num)
      
   
