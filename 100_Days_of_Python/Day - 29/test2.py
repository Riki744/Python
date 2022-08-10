#Simple check to generate username
def username_generator(first_name, last_name):
  if len(first_name) < 3:
        user_name = first_name
  else:
      user_name = first_name[0:3]
  if len(last_name) < 4:
      user_name += last_name
  else:
      user_name += last_name[0:4]
  return user_name
  
    
#Using same name to generate the password by shifting letter to the right
print("Your username is " + username_generator("Abe", "Simpson"))

def password_generator(user_name):
  password = ""
  for i in range(0, len(user_name)):
      password += user_name[i-1]
  return password

print("Your password is " + password_generator("AbeSimp"))
