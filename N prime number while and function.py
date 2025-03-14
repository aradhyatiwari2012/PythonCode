def isprime(num):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               return False
       else:
           return True




user_input = int(input('Enter number of prime numbers you want:'))
prime_counter=1
find_prime=1
while prime_counter<=user_input:
    find_prime=find_prime+1
    if isprime(find_prime):
        print(find_prime)
        prime_counter=prime_counter+1
   
