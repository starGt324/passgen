import random
import time
from datetime import datetime
version="0.1.1v zika"
random_id=random.randint(999,99999999999999999)
try :
    user_range:int=int(input("how much string you want in your password :"))
    string_num=int(input("how much characters you want in your password :"))
    int_num=int(input("how much numbers you want in your password :"))
except ValueError or NameError:
    print("Exiting ... Invalid number") 
    print("Please enter positive number and restart programme !!!!") 
    exit(0)
######################################################################

else:
    if user_range<0 or string_num<0 or int_num<0 :
        print("Exiting ... Invalid number") 
        print("Please enter positive number and restart programme !!!!") 
        exit(0)   

    spicial_num=user_range-string_num-int_num
    list_char=list("azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN")
    list_int=["1","2","3","4","5","6","7","8","9","0"]
    list_spicial=["@","!","\#","§","?",";",",","."]
    count=0
##############################################################
    password_str=""
    password_int=""
    password_spicial=""
######################################################################
    for s1 in range(string_num):
        password_str+=random.choice(list_char)        

    for s2 in range(int_num):
        password_int+=random.choice(list_int)


    for s3 in range(spicial_num):
        password_spicial+=random.choice(list_spicial)        
########################################################################
    pass_user=""
    pass_total=password_str+password_int+password_spicial

#######################################################################
    for i in range(user_range):
        pass_user+=random.choice(list(pass_total))

###########################################################################
    #print("Base password : ",pass_total)
    print("Gen password : ",pass_user)



##########################history###########################################
with open("password.txt","a+") as file:
    file.write(f"---------------------------------------------------\n")
    file.write(f"ID:{random_id}\n")
    file.write(f"Date cration:{datetime.now()}\n")
    file.write(f"password: {pass_user}\n")
    time.sleep(1)
    
qs=input("Do you want to display previous password y/n:").lower()
anser=["y","yes"]

if qs in anser:
    with open("password.txt","r") as rad:
        reader=rad.read()
        print(reader)
else:
    print("see you next time. ")


####################### other function app #########################
def fun_gen_string(string_num):
    for s1 in range(string_num):
        password_str+=random.choice(list_char) 
    print(password_str)

def fun_gen_int(int_num):
    for s2 in range(int_num):
        password_int+=random.choice(list_int)
    print(int_num)

def fun_gen_magic_char(spicial_num):
    for s3 in range(spicial_num):
        password_spicial+=random.choice(list_spicial)
    print(password_spicial)