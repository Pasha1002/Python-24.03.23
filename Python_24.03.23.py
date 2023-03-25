
meters = int(input("Enter in meters: ")) 
value = float(input("\n 1-Convert to miles \n 2-Сonvert to inches \n 3-Convert to yards \n "))
if value ==1:
    print(meters * 0.00062137)
elif value ==2:
    print(meters * 39.370)
elif value ==3:
    print(meters * 1.0936)