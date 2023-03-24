
number_1 = int(input('Enter the number 1: '))
number_2 = int(input('Enter the number 2: '))
value = int(input("\n 1-Sum \n 2-Differense \n 3-Arithmetic mean \n 4-Product \n "))
if value ==1:
    print(number_1 + number_2)
elif value ==2:
    print(number_1 - number_2)
elif value ==3:
    print((number_1 + number_2)/2)
elif value ==4:
     print(number_1 * number_2)
else:
    print("Choose from 1-4")