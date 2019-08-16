'''
Jerard Dayanghirang Guevarra

This program will ask the user to enter a password that follows particular constraints
'''

def enterNewPassword():

    #saves digits to be used in the future 
    digits = '1234567890'
    #stores how many digits are inside of the given password
    numDigits = 0
    
    while True:
        
      password = input('Please enter a password between 8 and 15 characters ' +
                     'with at least one digit: ')
      
      for characters in password:
          if characters in digits:
              numDigits += 1
      if len(password)> 8 and len(password)<15 and numDigits >= 1:
          print('You have entered a sufficient password')
          break
      elif numDigits == 0 and len(password)>15:
          print('Your password is too long and lacks a digit')
      elif numDigits == 0 and len(password)< 8:
          print('Your password is too short and lacks a digit')
      elif len(password)< 8:
          print('Your password is too short')
      elif len(password)>15:
          print('Your password is too long')
      elif numDigits == 0 and len(password)> 8 and len(password)<15:
          print('Please enter a password that includes at least one digit')
enterNewPassword()
