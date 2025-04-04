def hcf(a,b):
    for i in range(max(a, b), 1 + (a * b)):
         if i % a == i % b == 0:
             return i
#to make this work use:
#c=hcf(a,b)
#hcf12=(a*b)//c


def lcm(a,b):
    for i in range(max(a, b), 1 + (a * b)):
         if i % a == i % b == 0:
             return i
             

def fraction(variable1):
    fraction=variable1.split("/")
    return(fraction)

#use import common function for both addition and subtaction
def addition(number1,number2):
    den_1=int(common.fraction(number1)[1])
    den_2=int(common.fraction(number2)[1])

    num_1=int(common.fraction(number1)[0])
    num_2=int(common.fraction(number2)[0])

    lcm_no=int(common.lcm(den_1,den_2))

    obt_no_1=int(lcm_no)/int(den_1)
    obt_no_2=int(lcm_no)/int(den_2)

    fin_num_1=int(num_1)*int(obt_no_1)
    fin_num_2=int(num_2)*int(obt_no_2)

    sum_num=int(fin_num_1)+ int(fin_num_2)
    r1=print(sum_num,"/",lcm_no)
    return (r1)

def subtraction(numb_1,numb_2):
    num_1=int(common.fraction(numb_1)[0])
    num_2=int(common.fraction(numb_2)[0])

    den_1=int(common.fraction(numb_1)[1])
    den_2=int(common.fraction(numb_2)[1])

    lcm_num=int(common.lcm(den_1,den_2))

    den_a=int(lcm_num)/int(den_1)
    den_b=int(lcm_num)/int(den_2)

    num_a=int(num_1)*int(den_a)
    num_b=int(num_2)*int(den_b)

    diff_num=int(num_a)-int(num_b)
    r1=print(diff_num,"/",lcm_num)
    return (r1)

def additive(variable1):
    additive=variable1 * -1
    return additive


def p_f(n): #Prime factorisation
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
