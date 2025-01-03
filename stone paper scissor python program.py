import random

# Print multiline instruction
print('Winning rules of the game STONE PAPER SCISSORS are:\n'
      + "Stone vs Paper -> Paper wins \n"
      + "Stone vs Scissors -> Stone wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1 - Stone \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice: "))
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please : '))
    if choice == 1:
        choice_name = 'Stone'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('Your choice is:', choice_name)
    print("Now it's Computer's Turn...")
    # Computer chooses randomly any number among 1, 2, and 3
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Stone'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'Stone'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Scissors'
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== You win! ==>")
    else:
        print("<== Computer wins! ==>")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing!")
