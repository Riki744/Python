#Script that will read in the compromised usernames and passwords that are stored in file called "passwords.csv"
#Importing required modules
import csv
import json

#List of compromised users
compromised_users = []

#Opening passwords.csv and converting into dictionary
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row["Username"])
  password_file.close()

#Test
#print(compromised_users)

#Writing compromised_users.txt
with open("compromised_users.txt", "w") as compromised_user_file:
  for username in compromised_users:
    compromised_user_file.write(username)
  compromised_user_file.close()

#Testing if every user is written in new file
# with open("compromised_users.txt") as test_file:
#   test_file = test_file.read()
# print(test_file)

#Notifying the Boss
#Opening new json file in write mode
with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {"recipient":"The Boss", "message":"Mission Success"}
  json.dump(boss_message_dict, boss_message)

#Scrambling the Password
#Opening passwords.csv file and leaving signature of The Fender hackers
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""


with open("passwords.csv", "w") as new_passwords_obj:
  csvwriter = csv.writer(new_passwords_obj)
  csvwriter.writerow(slash_null_sig)

#Test if we wrote a signature
# with open("passwords.csv") as new:
#   new = new.read()
# print(new)

