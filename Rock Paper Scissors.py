import random
while True:
    print("Enter choice \n 1 Rock \n 2 Paper \n 3 Scissors")
    choice=int(input("Enter choice:"))
    if choice==1:
        print("You have chosen Rock")
    elif choice==2:
        print("You have chosen Paper")
    elif choice==3:
        print("You have chosen Scissors")
    else:
        print("wrong input")

    comp_choice=random.randint(1,3)
    while comp_choice==choice:
        comp_choice = random.randint(1,3)
    if comp_choice==1:
        print("Comp has chosen Rock")
    elif comp_choice==2:
        print("Comp has chosen Paper")
    else:
        print("Comp has chosen Scissors")

    if choice==comp_choice:
        print("Draw",end='')
    if (choice==1 and comp_choice==2):
        print("Comp wins: Paper covers Rock \n", end='')
    elif (choice==2 and comp_choice==1):
        print("You win: Paper covers Rock \n", end='')

    if (choice==2 and comp_choice==3):
        print("Comp wins: Scissors cut Paper \n", end='')
    elif (choice==3 and comp_choice==2):
        print("You win: Scissors cut Paper \n", end='')

    if (choice==1 and comp_choice==3):
        print("You win: Rock crushes Scissors \n", end='')
    elif (choice==3 and comp_choice==1):
        print("Comp wins: Rock crushes Scissors \n" , end='')
    print("Do you want to continue? (Y/N): ")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing")
