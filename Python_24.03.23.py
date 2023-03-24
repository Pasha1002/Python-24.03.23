
number_1 = int(input('Enter the number 1: '))
number_2 = int(input('Enter the number 2: '))
number_3 = int(input('Enter the number 3: '))
value = int(input("\n 1-Sum \n 2-Product \n "))
if value ==1:
    print(number_1 + number_2 + number_3)
elif value ==2:
     print(number_1 * number_2 * number_3)
else:
    print("Choose from 1-2")