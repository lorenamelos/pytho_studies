''' In this exercise from @CodeAcademy, it was asked to create a user name and a password.
For the username: The username should be a slice of the first three letters of their first name and the first four letters of their last name. 
If their first name is less than three letters or their last name is less than four letters it should use their entire names.

For the password: for the temporary password, they want the function to take the input user name and shift all of the letters by one to the right, 
so the last letter of the username ends up as the first letter and so forth.'''

def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  if len(first_name) < 3 or len(last_name) < 4:
    return first_name + last_name
  return user_name

user_name = username_generator("Lorena", "Melo")

print(user_name)

def password_generator(user_name):
   password = ""
   for i in range(0, len(user_name)):
        password += user_name[i-1]
   return password
print(password_generator(user_name))
