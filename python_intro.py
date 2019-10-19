print('Hello, Django girls!')
if 3>2:
    print('It works!')
if 5>2:
    print('5 is indeed greater than 2')
else: 
    print('5 is not greater than 2')
name='nia'
if name=='ola':
    print('Hey ola!')
elif name=='nia':
    print('Hey nia!')
else:
    print('Hello matey!')
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
def hi():
    print('Hi there!')
    print('How are you')

hi()
def hi(name):
    if name=='nia':
        print('Hi nia!')
    elif name=='sonja':
        print('Hi sonja!')
    else:
        print('Ahoy there!')
hi('nia')
hi('sonja')
hi('pirate')
def hi(name):
    print('Hi ' + name + '!')
hi('Rachel')

girls=['Rachel', 'Monica', 'Phoebe', 'Ola', 'nia', 'You']

for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)
    




