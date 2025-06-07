# Logical operaters = evaluate multiple conditions (or, and, not)
#                     or = atleast one condition must be true
#                     and = both conditions must be true
#                     not = invert the condition  (not false, not true)


### "or" operater
'''
temperature = 25
is_raining = False

if temperature > 35 or  temperature < 0 or is_raining:
    print("The outdoor event is cancled")
else:
    print("The outdoor event is still scheduled")

'''
### "and" operater
'''
temp = 26
is_sunnyday = True

if temp >= 25 and is_sunnyday :
    print('It is hot outside')
    print('It is sunny outside')
else:
    print('condition is not satesfied')

'''

"""
name = input('enter your full naem: ')

# result = len(name)
# result = name.find( 'n')
# result = name.rfind('n')
# name = name.capitalize()
# result = name.upper()
# result = name.lower()
# name = name.isdigit()
# name = name.isalpha()


print(result)

"""