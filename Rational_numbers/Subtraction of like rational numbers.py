def fraction(variable1):
    fraction=variable1.split("/")
    return(fraction)

    
numb_1=input("Write the first fraction:")
numb_2=input("Write the second fraction:")

num_1=int(fraction(numb_1)[0])
num_2=int(fraction(numb_2)[0])

den_1=int(fraction(numb_1)[1])

diff_num=int(num_1)-int(num_2)

print("Difference of the fraction is:",diff_num,"/",den_1)
