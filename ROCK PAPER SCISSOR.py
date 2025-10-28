import random


Rock='''      _________
________'   ( ________)
           (_________ )
           (__________)
           ( _________)
---------:-(__________)
'''

Paper ='''___________
________'       ________)
             _____________)
             _______________)
                 _________)
---------:_____________)

'''

scissor ='''
         ______________
________'       ________)________
                       ___________')
                     ________________)
                   (______')
---------:(__________)
'''


game_images=(Rock,Paper,scissor)
user_choice=int(input("what is your choice 0 for rock ,1 for scissor,2 for paper: "))
if user_choice>=0 and user_choice<=2:
      print(game_images[user_choice])

COMPUTER_INPUT=random.randint(0,2)
print(COMPUTER_INPUT)
print(game_images[COMPUTER_INPUT])

if(user_choice>=3 and user_choice<0):
    print("you select invalid option. you lose")
if(user_choice==COMPUTER_INPUT):
     print("match draw")
elif(user_choice==0 and COMPUTER_INPUT==2):
       print("you win!")
elif(user_choice==2 and COMPUTER_INPUT==0):
    print("you lose!")
elif(user_choice<COMPUTER_INPUT==2):
        print("you lose!")
elif(user_choice> COMPUTER_INPUT<=1):
        print("you lose")

