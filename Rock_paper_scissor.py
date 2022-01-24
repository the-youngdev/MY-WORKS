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
        s = False
       
        

        Comp = print(" Comp Choose : Rock(r) , Paper(p) or Scissor(s) ? ")
            
        
        if no == 1:
            Comp = "s"
        elif no == 2:
            Comp = "p"
        else :
            Comp = "r"
        
        t = True
        while t == True:
            b = input(" YOU Choose : Rock(r) , Paper(p) or Scissor(s) ? ")
            
            if b == 'r':
                t = False
            elif b == 'p':
                t = False
            elif b == 's':
                t = False
            else:
                print("INVALID INPUT")
                t = True
        
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

        s =  False
        
        j = True
        while j == True:
        
            a = input (" P1 Choose : Rock(r) , Paper(p) or Scissor(s) ? ")
            
            if a == 'r':
                j = False
            elif a == 'p':
                j = False
            elif a == 's':
                j = False
            else:
                print("INVALID INPUT")
                j = True
       
        t = True
        while t == True:   
            b = input(" P2 Choose : Rock(r) , Paper(p) or Scissor(s) ? ")
            
            if b == 'r':
                t = False
            elif b == 'p':
                t = False
            elif b == 's':
                t = False
            else:
                print("INVALID INPUT")
                t = True
        
        
        
    
        
        
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
        print("INVALID INPUT")
        s = True
    
    if s == False:
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
                print ('Bye')
                s = False
                h = False
            else:
                print("INVALID INPUT") 
                s = False
                h = True
    else:
        pass







