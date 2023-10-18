import random
def guess_n(x):
    rn=random.randint(1,x)
    guess=0
    while guess!=rn:
        guess=int(input(f'Please guess a number between 1 and {x}: '))
        if guess<rn:
            print("Sorry , guess again. too low")
        elif guess>rn:
            print("sorry, guess again. Too high.")
    print(f"------YAY, congrats. you have guessed the number {rn} correctly-----")
guess_n(10)

def computer_guess(x):
    l=1
    h=x
    feedback=''
    while feedback!= 'c' and l!=h:
        guess=random.randint(l,h)
        fb=input(f'Is {guess} too high (N),too low (L), or correct (c) ??')
        if fb =="h":
            high=guess-1
        if fb=='l':
            low=guess+1
    print(f"Yay  The computer guessed your name, {guess}, correctly")
computer_guess(10)

