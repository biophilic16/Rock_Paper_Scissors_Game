import random 

user_points=0
comp_points=0

chances=["rock","paper","scissors"]
print("\nROCK PAPER SCISSORS GAME")
print("---------------------------")

while True:
    user_choice=input("Enter your choice rock/paper/scissors or q to quit: ").lower()
    if user_choice=='q':
        break
    if user_choice in chances:
        comp_choice=random.choice(chances)
        print("User choice     :",user_choice)
        print("Computer choice :",comp_choice)
        if user_choice=='rock' and comp_choice=='scissors':
            print("#------------------->USER WINS!\n")
            user_points+=1

        elif user_choice=='scissors' and comp_choice=='paper':
            print("#------------------->USER WINS!\n")
            user_points+=1

        elif user_choice=='paper' and comp_choice=='rock':
            print("#------------------->USER WINS!\n") 
            user_points+=1

        elif user_choice==comp_choice:
            print("#------------------->TIE! TRY AGAIN\n")   
        else:
            print("#------------------->COMPUTER WINS!\n")
            comp_points+=1   
    else:
        print("\tEnter only rock/paper/scissors!")          


print("---------------------------")
print("\nUser Points     :",user_points)
print("Computer Points :",comp_points)


if user_points>comp_points:
    print("\n\tCONGRATULATIONS YOU WON! :)")
elif user_points==comp_points:
    print("\n\tIT'S A TIE! TRY AGAIN")
else:    
    print("\n\tSORRY YOU LOOSE :(")    
print()    