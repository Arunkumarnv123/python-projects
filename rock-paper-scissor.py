import random
def play():
    user=input(" what is ypur choice : 'r' for rock , 'p' for paper, 's' for scissors  :")
    computer = random.choice(['r','p','s'])

    if user== computer:
        return 'It\' a tie'
    if is_win(user,computer):
        return "You have won!"
    return "you have lost the game !"

def is_win(pl,op):
    if(pl=='r' and op=='s') or (pl=='s' and op=='p') or (pl=='p' and op=='r') :
        return True
print(play())