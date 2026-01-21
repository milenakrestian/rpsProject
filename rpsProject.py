import random
choices = ["rock", "scissors", "paper"]


answer = input("We are going to play a game called rock, paper, scissors.\n"
"Each layer picks one of three things: rock, paper or scissors.\n"
"If players pick the same things, they go again. If one player picks rock and one scissors, the player who picked rock wins the draw.\n"
" If one player picks scissors and the other paper, the player who picked scissors wins. Scissors cuts paper.\n"
"If a player choose paper while the other choose rock, the player who picked paper succeeds. Paper covers rock.\n"
"The game requires 3 points difference to win!\n"
               " Shall we start the game? ").lower()
wins = 0
losses = 0
if answer == "yes":
    while True:
        computer_input = random.choice(choices)
        player_input = input("Make a guess (rock, paper, scissors): ").lower()
        print(f"Opponent choice:{computer_input}")
        if player_input == computer_input:
            print("Draw")
            continue
        elif ((player_input == "rock" and computer_input == "scissors")\
            or (player_input == "scissors" and computer_input == "paper")\
            or (player_input == "paper" and computer_input == "rock")):
            print("You win the draw!")
            wins += 1
        else:
            print("Player two wins the draw!")
            losses += 1
            if wins >= losses + 3:
                print(f"Congratulations you win the game! Result: {wins}:{losses} ")
                question = input("Do you want to play again? ").lower()
                if question == "yes":
                    wins = 0
                    losses = 0
                    continue
                else:
                    break
            elif losses >= wins + 3:
                print(f"You lost the game! Result: {wins}:{losses}")
                question = input("Do you want to play again? ").lower()
                if question == "yes":
                    wins = 0
                    losses = 0
                    continue
                else:
                    print("Thank you for playing! Good buy!")
                    break

elif answer == "no":
    print("Good buy!")