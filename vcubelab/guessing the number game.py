'''import random
fix=random.randint(1,9)
i=1
while i<=3:
    guess=int(input("Enter a number:"))
    if guess==fix:
        print("you won the game")
        break
    else:
        print("wrong guess")
    i=i+1
else:
    print("you lost the game")




import random
fix=random.randint(1,9)
i=1
while i<=3:
    guess=int(input("Enter a number:"))
    if guess==fix:
        print("you won the game")
        break
    else:
        if guess>fix:
            print("you select small")
        else:
            print("yoy select big")
    i=i+1
else:
    print("you lost the game")



import random
fix=random.randint(1,9)
i=1
while i<=3:
    guess=int(input("Enter a number:"))
    if guess==fix:
        print("you won the game")
        break
    else:
        if guess>fix:
            print("you select small")
        else:
            print("yoy select big")
    i=i+1
else:
    print("you lost the game")
  

print()



state='stop'
while True:
    print('1.start')
    print('2.stop')
    print('3.Exit')
    
    ch=int(input("choose one option:"))
    
    if ch==1:
        if state == 'stop':
            print('car is started')
            state = 'start'
        else:
            print('car is already started')
    elif ch == 2:
        if state=='start':
            print('car is stoped')
            state='stop'
        else:
            print('car is already stopped')

    elif ch == 3:
        print('Game over')
        break
    else:
        print('choose correct option')
        
    print()


atm functionally
---------------'''
balance=0
while True:
    print('1.deposit')
    print('2.withdraw')
    print('3.Balance')
    print('4.Exit')
    ch=int(input("Choose one option:"))
    if ch==1:
        mny=int(input("How much money:"))
        if mny%100==0 or mny%500==0:
            balance=balance+mny
            print('deposited successfully')
        else:
            print('not acceptable denomination')
            
    elif ch==2:
        mny=int(input("how much money"))
        if mny%100==0 or mny%500==0:
            if mny<balance:
                print('collect your money')
                balance=balance-mny
            else:
                print('insufficent funds')
        else:
            print('not acceptable denomination')
        
    elif ch==3:
        print('Avaiable balance is ',balance)
        
    elif ch==4:
        print('Done')
        break
        
    else:
        print('choose correct option')
    print()
        
    
    
    

             

   

