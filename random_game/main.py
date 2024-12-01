def game(name):
    match name:
        case 1:
            from Lottery_Machine import main

        case 2:
            from project_perfect_guess import main

while(True):
    a=int(input("Enter: 1 or 2 or 3\n 1 : To play LOTTERY MACHINE \n 2 : To play THE PERFECT GUESS\n 3 : EXIT \n"))
    if(a==1 or a==2):
        {
            game(a)
        }
    elif(a==3) :
        break
    else:
        print("Enter valid input")
