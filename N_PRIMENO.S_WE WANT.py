def isprime(num):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               return 'false'
       else:
           return 'true'

a = int(input('Give a number:'))
if(isprime(a)):
         print('Number',a,'is prime')
else:
    print('Number',a,'is not prime')
