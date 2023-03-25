
number_1 = int(input('Enter the number 1: '))
number_2 = int(input('Enter the number 2: '))
number_3 = int(input('Enter the number 3: '))
value = int(input("\n 1-Max \n 2-Min \n 3-Arithmetic mean \n "))
if value ==1:
    if number_1 > number_2 > number_3:
        print(number_1)
    elif number_2 > number_3 > number_1:
        print(number_2)
    elif number_3 > number_2 > number_1:
        print(number_3)
elif value ==2:
     if number_1 < number_2 < number_3:
         print(number_1)
     elif number_2 < number_1 < number_3:
         print(number_2)
     elif number_3 < number_1 < number_2:
         print(number_3)
elif value ==3:
     print((number_1+number_2+number_3)/3)
else:
    print("Choose from 1-3")