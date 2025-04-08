import random
user_range:int=int(input("how much string you want in your password :"))
list_pw=["a","b","c","E","f","1","2","3","4","5","6","7","8","9","0","@","!","\#"]


user_password=""
for pointer in range(user_range):
    list_chois=random.choice(list_pw)
    user_password+=list_chois


print(user_password)