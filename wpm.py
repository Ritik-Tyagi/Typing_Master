# check path
from time import *
import keyboard
import random
def leaderboard(user_error, time1, time2, user_sen):
    time_diff = time2 - time1
    round_of_time = round(time_diff, 2) 
    time_taken = len(user_sen) / round_of_time
    #x=time_taken * 0.0166667--> for  wpm
    final_time = round(time_taken, 2)
    print("W.P.S->", final_time)
    print("User Error->", user_error)
def final_result(rendom_sen):
    print("<-------------Type this sentence----------->")
    print(rendom_sen)
    time1 = time()
    user_sen = input("""
                     Type here : """)
    time2 = time()
    user_error = 0
    for i in range(len(rendom_sen)):
        try:
            if rendom_sen[i] != user_sen[i]:
                user_error += 1                       
        except:            
            user_error += 1 
    return leaderboard(user_error, time1, time2, user_sen) 