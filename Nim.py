from random import randint
from time import sleep

def comp_turn(stones, player_took):
    if player_took == 2:
        left = 1
    else:
        left = 2
    
    stones -= left
    print("I took", left)
    return stones   

def player_turn(stones):
    print("There is", stones, 'stones', 'o' * stone_count, "\nWould you like to take one or two? (1, 2)")
    player_amnt = int(input("> "))
    stones -= player_amnt
    print("You took", player_amnt)
    if stones <= 0:
        print("You lose")
    return stones, player_amnt


print('We are going to play the game of nim.\nI will flip a coin to see who goes first \nFlipping...')
sleep(2)
coin = randint(0,1)
if coin == 1:
    print("You are going first")
    stone_count = randint(11, 32) #Ensures I will always win
    while stone_count % 3 != 1:
        stone_count = randint(11, 32)
else:
    print("I will go first")
    stone_count = randint(11, 32) #Ensures I will always win
    while stone_count % 3 == 1:
        stone_count = randint(11, 32)
    left = stone_count % 3
    if left == 0:
        send = 1
    else:
        send = 2
    stone_count = comp_turn(stone_count, send)
    
while stone_count > 0:
    stone_count, player_took = player_turn(stone_count)
    if stone_count == 1:
        print("I took 1\nI lose")
        break
    if stone_count > 1:
        stone_count = comp_turn(stone_count, player_took)
