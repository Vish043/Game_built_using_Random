def main():
    import random
    n= random.randint(1,100)
    a=-1
    guesses=1

    while(a != n):
        a = int(input("Guess a number : "))
        if(a>n):
            print("Lower number please")
        elif(a<n):
            print("Higher number please")
        guesses  += 1

    print(f"you have guessed the number {n} correctly in {guesses} attempt")

while(True):
    a=int(input("Enter: 1 or 2 \n 1 : To play \n 2 : To exit\n"))
    if(a==1):
        {
            main()
        }
    elif(a==2) :
        break
    else:
        print("Enter valid input")
