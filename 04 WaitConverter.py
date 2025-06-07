#  Wait converter

print('welcome to weight converter app')

weight = float(input("Enter the weight: "))
unit = input('Kilogram or pound (K or L) : ')

if unit == 'K' or 'k':
    result = weight * 2.20
    unit = 'LBs'
    print(f'Your weight is {round(result, 2)} {unit}.')

elif unit == 'L' or 'l':
    result = weight / 2.20
    unit = 'Kg'
    print(f'Your weight is {round(result, 2)} {unit}.')

else:
    print(f"unit weight is not valid {unit}")
