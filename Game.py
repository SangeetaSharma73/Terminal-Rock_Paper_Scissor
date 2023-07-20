import random
dic={
    'Rock':'🪨 -> Rock',
    'Paper':'📜 -> Paper',
    'Scissors':'✂️-> Scissors'
    }
l=['Rock','Paper','Scissors']

while True:
    print('Choose:','🪨 -> Rock','📜 -> Paper','✂️-> Scissors')
    user_choose=input()
    print
    if user_choose!='Rock' and user_choose!='Paper' and user_choose!='Scissors':
        print("Invalid input try another")
        continue
    elif user_choose=='Rock' or user_choose=='Paper' or user_choose=='Scissors':
        print('user_choose->',dic[user_choose])
        computer_choose=random.choice(l)
        print('computer_choose->',dic[computer_choose]) 
        won=0
        Lose=0
        Draw=0
        if user_choose== computer_choose:
            Draw+=1
            print(f"Both players selected {user_choose}. It's a tie!")
            print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
        elif user_choose == "Rock":
            if computer_choose == "Scissors":
                print('You win!😀😁')
                won+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
            else:
                print("You lose😟☹️")
                Lose+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
        elif user_choose == "Paper":
            if computer_choose == "Rock":
                print('You win!😀😁')
                won+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
            else:
                print("You lose😟☹️")
                Lose+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
        elif user_choose == "Scissors":
            if computer_choose == "Paper":
                print('You win!😀😁')
                won+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)
            else:
                print("You lose😟☹️")
                Lose+=1
                print('win=',won,'|','Lose=',Lose,'|','Draw=',Draw)  
    check=input('Do you want to continue game->Yes/No:- ')
    if check!="Yes":
        break
        
print('***Final Result***')  
if won>Lose:
    print('You win👍😀🎉','Your Score',won)
elif won<Lose:
    print('You Lose👎☹️','Your Opponent',Lose)
else:
    print('Draw','& Total draws',Draw)
    

