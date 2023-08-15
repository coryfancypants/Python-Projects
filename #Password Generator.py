#Password Generator
import random
pwdnum = int(input('Please enter the number of Passwords you would like to generate:'))
pwdLength = int(input('Please enter the desired password length: '))
pwdStrength = input('Please enter the desired password strength, low, medium, high: ')
#pwdStructure = input() #unused maybe later
def characters():
    uppercase = chr(random.randrange(65, 90))
    lowercase = chr(random.randrange(97,122))
    symbols = chr(random.randrange(33,47))
    numbers = chr(random.randrange(48,57))

    if(pwdStrength == 'low'):
        return random.choice([uppercase,lowercase])
    elif(pwdStrength == 'medium'):
        return random.choice([uppercase,lowercase,numbers])
    else:
        return random.choice([uppercase,lowercase,symbols,numbers])
def password(pwdLength):
    for c in range(pwdnum):
        passwd = '' 
        for i in range(pwdLength):
            passwd += characters()

        print(passwd)
    
password(pwdLength)
    