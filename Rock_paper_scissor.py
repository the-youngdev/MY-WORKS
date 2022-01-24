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




s = True
while s ==True:


    m = input(" Choose : Single Player(S) or Multiplayer(M)  [*CASE SESNITIVE*] ? ")



    if m == 'S':
        

        Comp = print(" Comp Choose : Rock(r) , Paper(p) or Scissor(s) ? ")
        
        
        
        if no == 1:
            Comp = "s"
        elif no == 2:
            Comp = "p"
        else :
            Comp = "r"
        
        
        b = input(" YOU Choose : Rock(r) , Paper(p) or Scissor(s) ? ")
        
        
        e = game(Comp,b)
        
        print(f"Comp :- {Comp}")
        print(f"You :- {b}")
        
        if e == None:
            print("Draw!")


        elif e :
            print("You Win!")

        else:
            print("Comp Wins!")

        


    
    elif m =="M":


        a = input (" P1 Choose : Rock(r) , Paper(p) or Scissor(s) ? ")
            
        b = input(" P2 Choose : Rock(r) , Paper(p) or Scissor(s) ? ")
        
    
        
    
        
        
        e = game(a,b)
        
        print(f"P1 :- {a}")
        print(f"P2 :- {b}")
        
        if e == None:
            print("Draw!")


        elif e :
            print("P2 Wins!")

        else:
            print("P1 Wins!")

        


    else:
        print("CHOOSE THE GODDAMM WORD ABOVE YOU BLIND MF")

    h = True
    while h == True:

        
        g = input('''Do You want to play again
            Press (y) for yes
            Press (n) for no\n''')    

        if g == 'y':
            print ("Ok")
            s = True
            h = False
        elif g == 'n':
            print ('BHAG')
            s = False
            h = False
        else:
            print("YoU reALly bLiND nEGGa") 
            s = False
            h = True







