import random
def computer_choice():
    n1=['rock','paper','scissors']
    return random.choice(n1)
def user_choice():
    n2=input("enter your choice : rock/paper/scissors")
    if n2 not in ['rock', 'paper', 'scissors']: 
        print("Invaild input")
        return
def decider(user,comp):
    if user==comp:
        print("Its a tie")
    elif user=='rock' and comp=='scissors':
        return "YOU WIN"
    elif user=='paper' and comp=='rock':
        return "YOU WIN"
    elif user=='scissors' and comp=='paper':
        return "YOU WIN"
    else:
        return "computer wins"
def play():
    print("=== Rock Paper Scissors ===")
    while True:
        user = user_choice()
        comp = computer_choice()
        print("\nYou chose:",user)
        print("Computer chose:",comp)
        print(decider(user, comp))
        
        play_again = input("\nPlay again? (yes/no): ")
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play()