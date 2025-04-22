def sps():
    from random import choice

    def line():
        for _ in range(1):
            for _ in range(115):
                print("-",end="")
        print("\n")
    while True:
        list=["Stone","Paper","Scissor"]
        display=choice(list)
        print("1. Stone")
        print("2. Paper")
        print("3. Scissor")
        print("0. Exit")
        print("Enter your Choice :",end="")
        a=int(input())
        print()
        if a==1:
            print("Player :Stone")
        elif a==2:
            print("Player :Paper")
        elif a==3:
            print("Player :Scissor")
        elif a==0:
            print("See you  Again")
            break
        elif ValueError:
            print("Incorrect input ")
        else:
            print("Invalid Input")   
        print( "PC     :"+display)  
        if (a==1 and display=="Scissor") or (a==1 and display=="Stone") or (a==3 and display=="Paper"):
            print("***|  You Win  |***")
        elif (a==1 and display=="Stone") or (a==2 and display=="Paper") or (a==3 and display=="Scissor"):
            print("***|  This is a Tie  |***")
        else:
            print("***|  You Lose  |***")
        line()
        

sps()
