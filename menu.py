from colorama import Fore,Style,Back
import time
import random
#from gen import list_char,list_int,list_spicial

list_char=list("azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN")
list_int=["1","2","3","4","5","6","7","8","9","0"]
list_spicial=["@","!","\#","§","?",";",",","."]

try:
    print("MENU:")
    print("1-password char.",Fore.YELLOW)
    print("2-password numbers.",Fore.GREEN)
    print("3-password spicele char",Fore.GREEN)
    print()
    print("_"*25)
    user_interacted=int(input("chose a option from list : "))
except NameError:
    print("value not found in script")
    exit()
except ValueError:
    print("please insert a number from list next time.")
    user_interacted=1
except Exception as baderor:
    print("bad eror type:",baderor)
    exit()

else:
    password=""

    if user_interacted==1:
        #fun_gen_string(25)
        for item in range(12):
            chiser=random.choice(list_char)
            password+=chiser
        
        print(Fore.YELLOW,"your password (string): ",password)

    elif user_interacted==2:
        #fun_gen_int(12)
        for item in range(12):
            chiser=random.choice(list_int)
            password+=chiser
        
        print(Fore.YELLOW,"your password (numbers): ",password)
    
    else:
        #fun_gen_magic_char(12)
        for item in range(12):
            chiser=random.choice(list_spicial)
            password+=chiser
        
        print(Fore.YELLOW,"your password (magic string): ",password)


