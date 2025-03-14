a=int(input('Enter the first number:'))
b=int(input('Enter the second number:')) 
print('1)ADDITION\n2)SUBTRACT\n3)MULTIPLICATION\n4)DIVISION')
c=int(input('Please give the operator'))
if c==1:
    d=a+b
    print ("Your result is %(first)d + %(second)d = %(result)d" % {"first": a, "second":b, "result":d})
    
elif c==2:
     d=a-b
     print ("Your result is %(first)d - %(second)d = %(result)d" % {"first": a, "second":b, "result":d})
elif c==3:
    d=a*b
    print ("Your result is %(first)d * %(second)d = %(result)d" % {"first": a, "second":b, "result":d})
elif c==4:
    d=a/b
    print ("Your result is %(first)d / %(second)d = %(result)d" % {"first": a, "second":b, "result":d})

else:
    print('Number not in list')
    
