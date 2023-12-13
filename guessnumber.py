import random

print('WELCOME TO MY GUESS NUMBER GAME')
a=input(' enter your name: ')
while True:
    computer=random.randint(1,4)
    x=int(input('enter your choice of number from (1 to 4): '))
    if x==computer:
            print(a,'your choice is ',x,'and my choice is',computer)
            print('you won')
            break
    else:
            print(a,'your choice is',x,'and my choice is',computer)
            print('YOU LOSS TRY AGAIN')   
            
    