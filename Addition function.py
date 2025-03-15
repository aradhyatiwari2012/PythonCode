import common

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
    return (sum_num)

numb_1=input("Write the 1st fraction:")
numb_2=input("Write the 2st fraction:")

result=addition(numb_1,numb_2)
print("The sum of the fractions is:",result)


 

