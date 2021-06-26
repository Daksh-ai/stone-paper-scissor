import random
li=["stone","paper","scissor"]
U=random.choice(li)
while(1):
    En=input("Enter the following 1.stone\n2.paper\n3.scissor")
    if En==1 or U=="stone":
        print("computer:{}".format(U))
        print("DRAW!")
        break
    elif En==1 or U=="paper":
        print("computer:{}".format(U))
        print("You lose!")
        break
    elif En==1 or U=="scissor":
        print("computer:{}".format(U))
        print("You win!")
        break
    elif En==2 or U=="stone":
        print("computer :{}".format(U))
        print("You Win!")
        break
    elif En==2 or U=="paper":
        print("computer:{}".format(U))
        print("DRAW!")
        break
    elif En==2 or U=="scissor":
        print("computer:{}".format(U))
        print("You lose!")
        break
    elif En==3 or U=="stone":
        print("computer:{}".format(U))
        print("You lose!")
        break
    elif En==3 or U=="paper":
        print("computer:{}".format(U))
        print("You Win!")
        break
    elif En==3 or U=="scissor":
        print("computer:{}".format(U))
        print("DRAW!")
        break
    

    
    