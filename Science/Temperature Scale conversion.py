temp = float(input("Enter temperature value: "))
scale = input("Enter scale (C/F/K): ").upper()

if scale == "C":
    f = (temp * 9/5) + 32
    k = temp + 273.15
    print("Farenheit:",f,"Kelvin:",k)

elif scale == "F":
    c = (temp - 32) * 5/9
    k = c + 273.15
    print("Celcius:",c,"Kelvin:",k)

elif scale == "K":
    c = temp - 273.15
    f = (c * 9/5) + 32
    print("Celcius:",c,"Farenheit:",f)

else:
    print("Invalid scale Use C, F, or K.")
