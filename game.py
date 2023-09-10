from random import randint

choices = [ "Rock", "Paper", "Scissors" ]


computer_choice = choices[randint(0,2)]

player_choice = 1


player_win = 0
computer_win = 0

while player_choice == 1:
    player_choice = input("Lets Play A Game! Choose Rock, Paper, Scissors?")
    computer_choice
    if player_choice == computer_choice:
        print("Its a Tie!")
        print("Score:")
        print("Computer Wins:",computer_win)
        print("Player Wins:", player_win)
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            computer_win = computer_win + 1
            print("You Lost! Computer Chose", computer_choice)
            print("Score:")
            print("Computer Wins:",computer_win)
            print("Player Wins:", player_win)
        else:
            player_win = player_win + 1
            print("You Won! Computer Chose", computer_choice)
            print("Score:")
            print("Computer Wins:",computer_win)
            print("Player Wins:", player_win)
    elif player_choice == "Paper":
            if computer_choice == "Scissors":
                computer_win = computer_win + 1
                print("You Lost! Computer Chose", computer_choice)
                print("Score:")
                print("Computer Wins:",computer_win)
                print("Player Wins:", player_win)
            else:
                player_win = player_win + 1
                print("You Won! Computer Chose", computer_choice)
                print("Score:")
                print("Computer Wins:",computer_win)
                print("Player Wins:", player_win)
    elif player_choice == "Rock" :
                if computer_choice == "Paper":
                    computer_win = computer_win + 1
                    print("You Lost! Computer Chose", computer_choice)
                    print("Score:")
                    print("Computer Wins:",computer_win)
                    print("Player Wins:", player_win)
                else:
                    player_win = player_win + 1
                    print("You Won! Computer Chose", computer_choice)
                    print("Score:")
                    print("Computer Wins:",computer_win)
                    print("Player Wins:", player_win)
    else:
         print("Not Valid Answer!Check your spelling.")
         print("Hint: Capital first letter :)")

    print("")
    play=input("Want To Continue Playing?(yes/no)")
    if play=="yes":
        player_choice=1

    else:
        break
