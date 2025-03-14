
def isprime(num):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               return False
       else:
           return True


a = int(input('Which number you want to check for prime:'))
if(isprime(a)):
   print("Your number is prime")
else:
    print("your number is not prime")

