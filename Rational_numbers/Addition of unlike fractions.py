import common
         
number1=input("Write the 1st fraction:")
number2=input("Write the 2nd fraction:")

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

print("The sum of the fractions is:",sum_num,"/",lcm_no)
