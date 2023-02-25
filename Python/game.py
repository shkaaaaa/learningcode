import random
class game():
    
    def winner(self,comp,user):
        if user==comp:
            print("tie")
        elif user=="rock":
            if comp=="paper":
                print("Computer Wins!!")
            else:
                print("User Wins!!")
        elif user=="paper":
            if comp=="scissor":
                print("Computer Wins!!")
            else:
                print("User Wins!!")
        elif user=="scissor":
            if comp=="rock":
                print("Computer Wins!!")
            else:
                print("User Wins!!")
    
comp=random.randint(1,3) 
if comp==1:
    comp="rock"
elif comp==2:
    comp="paper"
elif comp==3:
    comp="scissor"
user=input("Enter your choice: (rock,paper,scissor): ")
print(f"Computer selected:{comp} and User selected:{user}")
player1=game()
player1.winner(comp,user)
