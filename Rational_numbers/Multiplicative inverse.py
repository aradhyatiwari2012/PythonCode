def fraction(variable1):
    fraction=variable1.split("/")
    return(fraction)

numb_1=input("Write the fraction:")

num_1=int(fraction(numb_1)[0])
den_2=int(fraction(numb_1)[1])

num_a=den_2
den_b=num_1

print("The multiplicative inverse of the given fraction is:",num_a,"/",den_b)





































