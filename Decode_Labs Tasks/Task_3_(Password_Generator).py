import secrets
import string
import time
while True:
   try:
      length=input("Enter the length of your password \n")
      length=int(length)
      if length<15:
        print("Password length must be a minimum of 15 characters \n")
        continue
      elif length>64:
        print("Password length should not exceed 64 characters \n")
        continue
      print("Password length accepted....")

      print("Generating password.....")
      break

   except ValueError:
     print("Invalid Input. Please enter a numerical integer. \n")


character_pool=string.ascii_letters+string.digits+string.punctuation
password=''.join(secrets.choice(character_pool)for _ in range(length))
time.sleep(2)
print("Your auto generated password is ",password)
