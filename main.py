#new arch
# mod by ouadia sabih in 23/4/25
import random
import time
import secrets
from datetime import datetime
import string
random_id=random.randint(999,99999999999999999)
version="0.1.4v"
#cath input eror##############################################################################################
try:
    user_input=int(input(" add length of password :"))
    if user_input<=0:
        user_input=12
except ValueError:
    print("you must input a integer next time.")
    exit()
    
except Exception as eror:
    print("eror type--",eror,"the programe end it self cant hundel it.")
    exit()
############################################################################################################
else:
    password=""
    password_int=""
    #genretor=secrets
    #gen real password:#####################################################################################
    list_int=string.digits+string.digits+string.digits
    list_alpha=string.digits+string.ascii_lowercase+string.ascii_uppercase+string.printable
    
    for key in range(user_input):
        #time.sleep(0.1)
        choiser_alpha=secrets.choice(list_alpha)
        password+=choiser_alpha
        #print(choiser_alpha)

    for key_int in range(user_input):
        #time.sleep(0.1)
        choiser_int=secrets.choice(list_int)
        password_int+=choiser_int
####################################################################################################################
    #avoid repet

    """new_pass_int=""
    new_pass_alpha=""
    for keys in range(user_input):
        new_choiser_int=secrets.choice(list(password_int))
        new_choiser_alph=secrets.choice(list())
        new_pass_int+=new_choiser_int
        new_pass_alpha+=new_choiser_alph"""
        
    #time.sleep(1)
    print("*"*15)

    print("random password string :",password)
    print("random password numbres :",password_int)

##saving################################################################################
with open("password.txt","a+") as file:
    file.write(f"---------------------------------------------------\n")
    file.write(f"ID:{random_id}\n")
    file.write(f"Date cration:{datetime.now()}\n")
    file.write(f"password: {password}\n")
    time.sleep(0.3)


