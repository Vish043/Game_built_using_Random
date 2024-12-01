
def main():
    n1 , n2 , n3 = 2,3,9

    n=0
    a, b, c = input("Enter a three-digit lottery number with space between each number:").split()
    a=int(a)
    b=int(b)
    c=int(c)

    if a==n1 or a==n2 or a==n3 :
        n +=1
    if b==n1 or b==n2 or b==n3 :
        n +=1
    if c==n1 or c==n2 or c==n3 :
        n +=1
    if n==3:
        print('You won the lottery!')
    else :
        print("Oops! you didn't won the lottery.")

while(True):
    a=int(input("Enter: 1 or 2 \n 1 : Enter the lottery number \n 2 : To exit\n"))
    if(a==1):
        {
            main()
        }
    elif(a==2) :
        break
    else:
        print("Enter valid input")
