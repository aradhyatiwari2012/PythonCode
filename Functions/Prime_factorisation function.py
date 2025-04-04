def p_f(n):
    factors = []
    i = 2  
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)  
    return factors


num = int(input("Enter a number: "))
num1=p_f(num)
print("Prime factors are:",num1 )

