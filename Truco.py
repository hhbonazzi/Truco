import random

#Card organization
cards = {70 : ["A", "A", "A", "A"], 60 : [2, 2, 2, 2], 50 : [3, 3, 3, 3],
         40 : ["K", "K", "K", "K"], 30 : ["J", "J", "J", "J"], 
        20 : [ "Q",  "Q",  "Q", "Q"], 10 : [7, 7, 7, 7]}
shuffler = []
for lst in cards.values():
    for card in lst:
        shuffler.append(card)
random.shuffle(shuffler)

#Player vs Player
score_list = [0,0]
round_number = 0
player_list = []
GameOn = True

name1 = input('''
Welcome to a thrilling 2-player Truco duel! 
Test your strategy and skill in this fast-paced 
Brazilian card game 
and outwit your opponent to claim victory. \n\n What is your name Player 1?\n\n
             ''')
player_list.append(name1)
name2 = input("What about yours Player 2? \n\n")
player_list.append(name2)


print("Let's start the game!")

while GameOn:
    round_number += 1
    print("ROUND:", round_number)
    if round_number%2:
        print("\n" + player_list[0], "GETS TO PLAY")
        input("WHAT WOULD YOU LIKE TO DO?\n\n")
        score_list[0] += 1
        print("SCORES: " + player_list[0] + ": " +  str(score_list[0]) #Maybe turn into function later
              + "\n" + player_list[1] + ": " +  str(score_list[1]))
        if score_list[0] >= 12:
            print(player_list[0], "WINS!\n")
            GameOn = False
            break
              
    else:
        print("\n" + player_list[1], "GETS TO PLAY")
        input("WHAT WOULD YOU LIKE TO DO?\n\n")
        score_list[1] += 1
        print("SCORES: " + player_list[0] + ": " +  str(score_list[0]) #Maybe turn into function later
              + "\n" + player_list[1] + ": " +  str(score_list[1]))
        if score_list[1] >= 12:
            print(player_list[1], "WINS!\n")
            GameOn = False
            break
              


#Game class
class Game:

    def __init__(self, name):
        self.name = name
