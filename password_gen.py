#new arch
# mod by ouadia sabih in 23/4/25
import random
import time
import secrets
from datetime import datetime
import string
from colorama import Fore,Back,Style
version="0.1.4v"
random_id=random.randint(999,99999999999999999)
try:
    userinput=int(input("add a length of your password :"))
    if userinput<=0:
        userinput=12
        
except ValueError as eror:
    print(eror)
    print("the input must be a number next time.")
    exit()

else:
    def gen_pw_string():
        global gen
        gen=secrets.token_urlsafe(userinput)
        return gen
    
    print(Fore.LIGHTGREEN_EX,gen_pw_string())

    def gen_pw_num():
        global gen_int
        print("by defult gen 12digi for security.")
        gen_int=random.randint(userinput,999999999999)
        return gen_int

    print(Fore.LIGHTBLUE_EX,gen_pw_num())
    Style.RESET_ALL


##saving################################################################################
    with open("password.txt","a+") as file:
        file.write(f"---------------------------------------------------\n")
        file.write(f"ID:{random_id}\n")
        file.write(f"Date cration:{datetime.now()}\n")
        file.write(f"password: {gen_pw_string()}\n")
        time.sleep(0.3)
    print(Fore.YELLOW,"operation complite data save in password.txt")
    Style.RESET_ALL