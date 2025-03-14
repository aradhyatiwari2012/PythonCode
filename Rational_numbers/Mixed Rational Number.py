def fraction(variable1):
    fraction=fraction.split("/ ")
    return (fraction)

numb_1=input("Write a mixed fraction:")

whole_a=int(fraction(numb_1)[0])
num_b=int(fraction(numb_1)[1])
den_c=int(fraction(numb_1)[2])

imp_frac=int(whole_a)*int(den_c)+int(num_b)
dec_num=int(imp_frac)/int(den_c)
print("The result is:",imp_frac,"/",den_c)
