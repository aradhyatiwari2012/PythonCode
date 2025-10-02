CP=int(input("Enter the cost price"))
SP=int(input("Enter the selling price"))
if CP>SP:
    L=CP-SP
    L_P=(L/CP)*100
    print("You have Loss of:₹",L,"and",L_P,"%")
elif SP>CP:
    P=SP-CP
    P_P=(P/CP)*100
    print("You have profit of:₹",P,"and",P_P,"%")

