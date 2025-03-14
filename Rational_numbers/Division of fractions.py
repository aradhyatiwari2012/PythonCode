def fraction(variable1):
    fraction=variable1.split("/")
    return(fraction)

numb_1=input("Write the 1st fraction:")
numb_2=input("Write the 2nd fraction:")

num_1=int(fraction(numb_1)[0])
num_2=int(fraction(numb_2)[0])

den_1=int(fraction(numb_1)[1])
den_2=int(fraction(numb_2)[1])

num_a=int(num_1)*int(den_2)
den_b=int(num_2)*int(den_1)

print("The result of division is:",num_a,"/",den_b)
