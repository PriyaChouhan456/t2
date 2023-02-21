import random

while True:
    print("-------------welcome to rock,paper,scissor game------------------")
    user_score=  0
    comp_score =0
    ties=0
    name = input("enter your name :")
    print("""
          winning rules:
          1. paper vs rock -->paper
          2.rock vs scissors-->rock
          3. scissors vs paper--> scissors""")
          
    print("""choices are:
          1.rock
          2.paper
          3.scissors """)

    choice=int(input("enter your choice from 1-3:"))
    print()
    while choice >3 or choice <1:
        choice = int(input("enter valid input "))
    if choice== 1:
        user_choice ="rock"
    elif choice==2:
        user_choice="paper"
    else:
        user_choice="scissors"  
              
    print("the users choice is :",choice)
    print("now it is computers turn") 
    computer = random.randint(1,3)
    if computer == 1:
        comp_choice ="rock"
    elif computer ==2:
        comp_choice ="paper"
    else:
        comp_choice ="scissors"
    print("the computer choice is :",comp_choice)            
    if ((user_choice =="paper" and comp_choice =="rock") or (user_choice =="rock" and comp_choice=="paper")):
        print("paper wins")
        result ="paper"
    elif ((user_choice =="scissors" and comp_choice =="rock") or (user_choice =="rock" and comp_choice=="scissors")):
        print("rock wins")
        result = "rock"
    elif (user_choice == comp_choice):
        print("its a tie ")
        result="tie"
    else:
        print ("scissors wins")
        result ="scissors"
    if result == "tie":
        ties+=1
    elif result == user_choice:
        print("user wins")
        user_score += 1
    else:
        print("computer wins")
        comp_score += 1

    print("scores are -----") 
    print(name,"'s score is = ", user_score)
    print("computer score is =",comp_score)
    print("ties are = ",ties)               
    repeat = input("do you want to play again?")
    if repeat == "no" or repeat =="NO":
        break
print("--------------------------GAME OVER--------------------------------------")  
print("THANKS FOR PLAYING")  
           
       