try:
    import random
    from pygame import mixer
    comp_options = ["s","w","g"]

    def comp_play():
        comp_playes = random.randint(1,3)
        comp_choice = comp_options[comp_playes-1]
        return comp_choice


    c_list = []
    u_list = []
    res = []
    u_score = 0
    c_score = 0
    tie = 0


    def round_result(user):

        global u_score
        global tie
        global c_score
        global rounds

        if user == "w":
            u_list.append("Water")
            if computer == "w":
                print("Comp = Water <------> You = Water")
                print("Draw")
                c_list.append("Water")
                res.append("Draw")
                tie += 1

            elif computer == "g":
                c_list.append("Gun")
                print("Comp = Gun <------ You = Water")
                print("Win")
                res.append("Player Won!")
                u_score += 1

            elif computer == "s":
                c_list.append("Snake")
                print("Comp = Snake ------> You = Water")
                print("Loose")
                res.append("Computer Won!")
                c_score += 1

        elif user == "s":
            u_list.append("Snake")
            if computer == "s":
                c_list.append("Snake")
                print("Comp = Snake <------> You = Snake")
                print("Draw")
                res.append("Draw")
                tie += 1

            elif computer == "w":
                c_list.append("Water")
                print("Comp = Water <------ You = Snake")
                print("Win")
                res.append("Player Won!")
                u_score += 1

            elif computer == "g":
                c_list.append("Gun")
                print("Comp = Gun ------> You = Snake")
                print("Loose")
                res.append("Computer Won!")
                c_score += 1

        elif user == "g":
            u_list.append("Gun")
            if computer == "g":
                c_list.append("Gun")
                print("Comp = Gun <------> You = Gun")
                print("Draw")
                res.append("Draw")
                tie += 1

            elif computer == "s":
                c_list.append("Snake")
                print("Comp = Snake <------ You = Gun")
                print("Win")
                res.append("Player Won!")
                u_score += 1

            elif computer == "w":
                c_list.append("Water")
                print("Comp = Water ------> You = Gun")
                print("Loose")
                res.append("Computer Won!")
                c_score += 1
        else:
            exit("Invalid Input!")

    rounds = 0

    replay = True
    while True:
        print('''\n:::::::::::::::::::::::::::::::::::::::::::::::::::::''')
        name = input("\nUsername: ")
        if len(name) < 5:
            print("Please choose Name with more than 5 characters!\n")
            continue
        else:
            break
    while replay == True:
        print('''\n:::::::::::::::::::::::::::::::::::::::::::::::::::::\n''')
        print("\n*************** Welcome To -> |Snake Water Gun| ***************")


        mixer.init()
        mixer.music.load("play.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(loops=12)

        print("\nGame Basics:")
        print("In this game you have to choose one option from:\n" "Snake, Water and Gun against computer, In which:\n"
                  "Snake -- Water = Snake drinks Water\n""Snake -- Gun = Gun shoots Snake\n" "Gun -- Water = Water drowns Gun\n"
                  "Snake -- Snake or Gun -- Gun or Water -- Water = Tie\n" "\"Just Like Stone Paper Scissor\"\n" "You have 10 rounds\n" "Enjoy!\n")


        rc = int(input("How Many times do you wanna play?\n"))
        print("\nLet's Go:\n")
        rounds = 0
        c_list = []
        u_list = []
        res = []
        u_score = 0
        c_score = 0
        tie = 0
        while rounds < rc :
            user_choice = input("Enter Snake(s), Water(w) or Gun(g): ")
            computer = comp_play()
            round_result(user_choice)
            rounds += 1

        print('''\n****** Score Board ******\n''')
        print('''-------------------------------------------''')
        i = 0

        while i < rc:
            if i == 0:
                print("\t\t\tPlayer Vs Computer")
            print("\t",u_list[i],"Vs",c_list[i],"---->",res[i])
            i += 1

        print('''--------------------------------------------\n''')
        print("<#------Final Result------#>")

        if c_score>u_score:
            print("\tComputer's Score =",c_score)
            print("\tYour Score =",u_score)
            print("\tTies =",tie)
            print("\tSorry, You Lost :(")
        elif c_score<u_score:
            print("\tComputer's Score =", c_score)
            print("\tYour Score =", u_score)
            print("\tTies =", tie)
            print(f"\tCongratulations!,{name} You Won :)")
        elif c_score == u_score:
            print("\tComputer's Score =", c_score)
            print("\tYour Score =", u_score)
            print("\tTies =", tie)
            print("\tit's a tie :}")
        print('''--------------------------------------------''')

        print("\nDo You Want to Play Again y/n:")
        last = input()
        if last == "y":
            replay = True
        elif last == "n":
            replay = False




except Exception as e:
    print(e)