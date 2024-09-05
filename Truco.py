import random

#Card organization
cards = {70 : ["A", "A", "A", "A"], 60 : [2, 2, 2, 2], 50 : [3, 3, 3, 3],
         40 : ["K", "K", "K", "K"], 30 : ["J", "J", "J", "J"], 
        20 : [ "Q",  "Q",  "Q", "Q"], 10 : [7, 7, 7, 7]}
shuffler = []
for lst in cards.values():
    for card in lst:
        shuffler.append(card)

#Game
score_list = [0,0]
player_list = []
GameOn = True
RoundOn = True
round_number = 1

#Player's hand
player1_hand = [shuffler[0], shuffler[1], shuffler[2]]
player2_hand = [shuffler[3], shuffler[4], shuffler[5]]

name1 = input('''
Welcome to a thrilling 2-player Truco duel! 
Test your strategy and skill in this fast-paced 
Brazilian card game 
and outwit your opponent to claim victory. \n\n What is your name Player 1?\n\n
             ''')
player_list.append(name1)
name2 = input("What about yours Player 2? \n\n")
player_list.append(name2)


print("\n\nLet's start the game!\n\n")

while GameOn:
    RoundOn = True
    random.shuffle(shuffler)
    score_list2 = [0,0]
    round_number2 = 0
    print("ROUND: " + str(round_number))
    print("\nPOINTS:\n" + player_list[0] + ": " +  str(score_list[0])
              + "\n" + player_list[1] + ": " +  str(score_list[1]))
    while RoundOn:
        round_number2 += 1
        print("\nROUND OF ROUND:", round_number2)
        if round_number2%2:
            print("\n" + player_list[0], "GETS TO PLAY")
            input("WHAT WOULD YOU LIKE TO DO?\n\n")
            score_list2[0] += 1
            #Call "Truco", "Hide Card" or "Play card"
            print("SCORES:\n " + player_list[0] + ": " +  str(score_list2[0]) #Maybe turn into function later
              + "\n" + player_list[1] + ": " +  str(score_list2[1]))
            if score_list2[0] >= 2:
                round_number += 1
                score_list[0] += 1
                print(player_list[0], "WINS POINT!\n")
                RoundOn = False
                break   
        else:
            print("\n" + player_list[1], "GETS TO PLAY")
            input("WHAT WOULD YOU LIKE TO DO?\n\n")
             #Call "Truco", "Hide Card" or "Play card"
            score_list2[1] += 1
            print("SCORES:\n " + player_list[0] + ": " +  str(score_list2[0]) #Maybe turn into function later
              + "\n" + player_list[1] + ": " +  str(score_list2[1]))
            if score_list2[1] >= 2:
                round_number += 1
                score_list[1] += 1
                print(player_list[1], "WINS POINT!\n")
                RoundOn = False
                break
    if score_list[0] >= 12:
        print(player_list[0], "WINS GAME!\n")
        GameOn = False
        break 
    if score_list[1] >= 12:
        print(player_list[1], "WINS GAME!\n")
        GameOn = False
        break 
        


#Game class
class Game:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def highest_card(self):
        biggest_card = shuffler[6]
        lst_key_bcard = [key for key, value in cards.items() if biggest_card in value]
        for key_bcard in lst_key_bcard:
            cards[80] = cards[key_bcard]
            del cards[key_bcard]
        
    def calling_truco(self):
        pass


                
        


        





