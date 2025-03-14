number1 = int(input('Enter a first number:'))
number2 = int(input('Enter a second number:'))
print('1)ADDITION\n2)SUBTRACT\n3)MULTIPLICATION\n4)DIVISION')
c=int(input('Please give the operator'))
    
if c==1:
      d= number1 + number2

elif c==2:
        d= number1 - number2

elif c==3:
        d= number1 * number2

elif c==4:
        d= number1 / number2

else:
    print('operator not in list')
    
print("The result is:",d)    
