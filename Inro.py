age = input('How old are you?')
numeric_age = int(age)
print('Nextyear you will be', numeric_age+1)

def a_function(callback):
    print(callback(3))

a_function(lambda num: num ** 2)

age = 12
if age < 18:
    print('You are underage')
elif age > 18:
    print('You are old bro')

    