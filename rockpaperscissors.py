import random

def play():
    user=input('Choose any of the three, R for rock ,P for Paper ,S for scissors').lower()
    computer=random.choice(['r','p','s'])
    
    if user==computer:             #if both of them have choosen the same thing
        return 'ITS A TIE!!!'
    elif isWin(user,computer):
        return 'YAYYYY you won!!'
    return 'Sorry yOU LOST!!'


def isWin(player,opponent):# WE know that r>s , s>p , p>r!
    if (player=='r'and opponent=='s')or (player=='s' and opponent=='p')or (player=='p'and opponent=='r'):
        return True
print(play())