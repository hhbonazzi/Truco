import random

#Card organization
cards = {70 : ["A", "A", "A", "A"], 60 : ["2", "2", "2", "2"], 50 : ["3", "3", "3", "3"],
         40 : ["K", "K", "K", "K"], 30 : ["J", "J", "J", "J"], 
        20 : [ "Q",  "Q",  "Q", "Q"], 10 : ["7", "7", "7", "7"]}
shuffler = []
for lst in cards.values():
    for card in lst:
        shuffler.append(card)

#Players Hand
player1_hand = [shuffler[0], shuffler[1], shuffler[2]]
player2_hand = [shuffler[3], shuffler[4], shuffler[5]]
      
#Game class
class Game:
    
    player_count = 0

    def __init__(self, name):
        self.name = name
        Game.player_count += 1
        self.id = Game.player_count
        
    def highest_card(self):
        biggest_card = shuffler[6]
        lst_key_bcard = [key for key, value in cards.items() if biggest_card in value]
        for key_bcard in lst_key_bcard:
            cards[80] = cards[key_bcard]
            del cards[key_bcard]
    
    def play_card(self, name):
        self.name = name
        if self.id == 1:
            play = input("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO PLAY, " + self.name + "?\n\n" 
                                + str(player1_hand[0]) + "\n" 
                                + str(player1_hand[1]) + "\n"  
                                + str(player1_hand[2]) + "\n\n")
            while play not in player1_hand:
                play = input("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO PLAY?\n\n")
            card_index = player1_hand.index(play)
            print("Nice!")
            player1_hand.pop(card_index)
            
        if self.id == 2:
            play = input(("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO PLAY, " + self.name + "?\n\n" 
                            + str(player2_hand[0]) + "\n" 
                            + str(player2_hand[1]) + "\n"  
                            + str(player2_hand[2]) + "\n\n"))
            while play.lower() not in player2_hand:
                play = input("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO PLAY?\n\n")
            card_index = player2_hand.index(play)
            print("Nice!")
            player2_hand.pop(card_index)
            
            
          
    def calling_truco(self):
        pass

#Game
score_list = [0,0]
player_list = []
GameOn = True
RoundOn = True
round_number = 1


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

player1 = Game(name1)
player2 = Game(name2)

while GameOn:
    RoundOn = True
    random.shuffle(shuffler)
    score_list2 = [0,0]
    round_number2 = 0
    player1_hand = [shuffler[0], shuffler[1], shuffler[2]]
    player2_hand = [shuffler[3], shuffler[4], shuffler[5]]
    print("ROUND: " + str(round_number))
    print("\nPOINTS:\n" + player_list[0] + ": " +  str(score_list[0])
              + "\n" + player_list[1] + ": " +  str(score_list[1]))
    while RoundOn:
        round_number2 += 1
        print("\nROUND OF ROUND:", round_number2)
        if round_number%2:
            if round_number2 % 2 == 1:
                print("\n" + player_list[0], "GETS TO PLAY")
                choice = input("YOUR HAND IS:\n\n" 
                                + str(player1_hand[0]) + "\n" 
                                + str(player1_hand[1]) + "\n"  
                                + str(player1_hand[2]) + "\n\n"
                                  "WHAT WOULD YOU LIKE TO DO?\n\n CALL TRUCO\n HIDE CARD\n PLAY CARD\n\n ")
                while choice.title() not in ["Truco", "Hide Card", "Play Card"]:
                    choice = input("WHAT WOULD YOU LIKE TO DO?\n\n")
                if choice.title() == "Play Card":
                    player1.play_card(name1)
                score_list2[0] += 1
                print("SCORES:\n" + player_list[0] + ": " +  str(score_list2[0]) 
                + "\n" + player_list[1] + ": " +  str(score_list2[1]))
                if score_list2[0] >= 2:
                    round_number += 1
                    score_list[0] += 1
                    print(player_list[0], "WINS POINT!\n")
                    RoundOn = False
                    break 
            else:
                print("\n" + player_list[1], "GETS TO PLAY")
                choice2 = input("YOUR HAND IS:\n\n" 
                                + str(player2_hand[0]) + "\n" 
                                + str(player2_hand[1]) + "\n"  
                                + str(player2_hand[2]) + "\n\n"
                                  "WHAT WOULD YOU LIKE TO DO?\n\n CALL TRUCO\n HIDE CARD\n PLAY CARD\n\n ")
                while choice2.title() not in ["Truco", "Hide Card", "Play Card"]:
                    choice2 = input("WHAT WOULD YOU LIKE TO DO?\n\n")
                if choice2.title() == "Play Card":
                    player2.play_card(name2)
                score_list2[1] += 1
                print("SCORES:\n" + player_list[0] + ": " +  str(score_list2[0]) #Maybe turn into function later
                + "\n" + player_list[1] + ": " +  str(score_list2[1]))
                if score_list2[1] >= 2:
                    round_number += 1
                    score_list[1] += 1
                    print(player_list[1], "WINS POINT!\n")
                    RoundOn = False
                    break
        else:
            if round_number2 % 2 == 0:
                print("\n" + player_list[0], "GETS TO PLAY")
                choice = input("YOUR HAND IS:\n\n" 
                                + str(player1_hand[0]) + "\n" 
                                + str(player1_hand[1]) + "\n"  
                                + str(player1_hand[2]) + "\n\n"
                                  "WHAT WOULD YOU LIKE TO DO?\n\n CALL TRUCO\n HIDE CARD\n PLAY CARD\n\n ")
                while choice.title() not in ["Truco", "Hide Card", "Play Card"]:
                    choice = input("WHAT WOULD YOU LIKE TO DO?\n\n")
                if choice.title() == "Play Card":
                    player1.play_card(name1)
                score_list2[0] += 1
                print("SCORES:\n" + player_list[0] + ": " +  str(score_list2[0]) #Maybe turn into function later
                + "\n" + player_list[1] + ": " +  str(score_list2[1]))
                if score_list2[0] >= 2:
                    round_number += 1
                    score_list[0] += 1
                    print(player_list[0], "WINS POINT!\n")
                    RoundOn = False
                    break 
            else:
                print("\n" + player_list[1], "GETS TO PLAY")
                choice2 = input("YOUR HAND IS:\n\n" 
                                + str(player2_hand[0]) + "\n" 
                                + str(player2_hand[1]) + "\n"  
                                + str(player2_hand[2]) + "\n\n"
                                  "WHAT WOULD YOU LIKE TO DO?\n\n CALL TRUCO\n HIDE CARD\n PLAY CARD\n\n ")
                while choice2.title() not in ["Truco", "Hide Card", "Play Card"]:
                    choice2 = input("WHAT WOULD YOU LIKE TO DO?\n\n")
                if choice2.title() == "Play Card":
                    player2.play_card(name2)
                score_list2[1] += 1
                print("SCORES:\n" + player_list[0] + ": " +  str(score_list2[0]) #Maybe turn into function later
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

player1 = Game(name1)
player2 = Game(name2)