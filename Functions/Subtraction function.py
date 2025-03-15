import common

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

number1=input("Write the 1st fraction:")
number2=input("Write the 2st fraction:")

result=subtraction(number1,number2)
