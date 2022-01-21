from calendar import c
import random


def game(c,b):
    
    if c == b:
        return None
    
    if c == "r":
        if b == "p":
            return True
        elif b == "s":
            return False
   
    if c == "p":
        if b == "s":
            return True
        elif b == "r":
            return False

    if c == "s":
        if b == "r":
            return True
        elif b == "p":
            return False
    

no = random.randint(1,3)

print(no)

print(" Comp Choose : Rock(r) , Paper(p) or Scissor(s) ? ")



if no == 1:
    Comp = "s"
elif no == 2:
    Comp = "p"
else :
    Comp = "r"

b = input(" YOU Choose : Rock(r) , Paper(p) or Scissor(s) ? ")


a = game(Comp,b)

print(f"Comp :- {Comp}")
print(f"You :- {b}")

if a == None:
    print("Draw!")


elif a :
    print("You Win!")

else:
    print("Comp Wins!")
