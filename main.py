#new arch
# mod by ouadia sabih in 23/4/25
import time
import secrets
from datetime import datetime
version="0.1.4v"
try:
    user_input=int(input(" add length of password :"))
    if user_input<=0:
        user_input=12
except ValueError:
    print("you must input a integer number.")
    user_input=int(input(" add length of password :"))
    
except Exception as eror:
    print("eror type--",eror,"the programe end it self cant hundel it.")
    exit()
else:
    password=""
    password_int=""
    #genretor=secrets
    list_int=list("1234567890")
    list_alpha=list("azertyuiopqsdfghjklmwxcvbnNBVCXWQSDFGHJKLMAZERTYUIOP,?§!~@><#")

    for key in range(user_input):
        choiser_alpha=secrets.choice(list_alpha)
        password+=choiser_alpha
        #print(choiser_alpha)

    for key_int in range(user_input):
        choiser_int=secrets.choice(list_int)
        password_int+=choiser_int
    #time.sleep(1)
    print("*"*15)

    print("random password string :",password)
    print("random password numbres :",password_int)




