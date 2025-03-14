def fraction(variable1):
    fraction=variable1.split("/")
    return(fraction)

    
number1=input("Give a fraction to find its numeator and denominator:")
number2=input("Give Another fraction to find its numeator and denominator:")
fraction_number1=fraction(number1)
fraction_number2=fraction(number2)
var_sum_numerator=int(fraction_number1[0])+int(fraction_number2[0])
print("sum of numberator is ", var_sum_numerator)
print("sum of 2 like fraction ", number1,"and", number2, " is ",var_sum_numerator,"/",fraction_number1[1])


