numb_1=input("Enter a mixed fraction:")

array_a=numb_1.split(" ")
whole=array_a[0]
fraction=array_a[1]

array_b=fraction.split("/")
num=array_b[0]
den=array_b[1]

imp_frac=int(whole)*int(den)+int(num)
dec=int(imp_frac)/int(den)
print("The improper fraction:",imp_frac,"/",den,"or",dec)
