P=float(input("Give Principal:"))
R=float(input("Give Rate:"))
T=float(input("Give Time(Annually):"))

A=P*(1+R/100)**T
CI=A-P
print("ANNUALLY: The Amount is:₹",A,"Compound Interest is:₹",CI)
H_Y=P*(1+R/200)**(2*T)
CI=H_Y-P
print("HALF YEARLY: The Amount is:₹",H_Y,"Compound Interest is:₹",CI)
Q=P*(1+R/400)**(4*T)
CI=Q-P
print("QUATERLY: The Amount is:₹",Q,"Compound Interest is:₹",CI)
