import random

#Card organization
cards = { 70: ["3", "3", "3", "3"], 60 : ["2", "2", "2", "2"], 50 : ["A", "A", "A", "A"],
         40 : ["K", "K", "K", "K"], 30 : ["J", "J", "J", "J"], 
        20 : [ "Q",  "Q",  "Q", "Q"], 10 : ["7", "7", "7", "7"], 0: []}

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
choices = []
choices_player1 = []
choices_player2 = []

#Players Hand
player1_hand = [shuffler[0], shuffler[1], shuffler[2]]
player2_hand = [shuffler[3], shuffler[4], shuffler[5]]
      
#Game class
class Game:
    
    Truco = 0
    player_count = 0

    def __init__(self, name):
        self.name = name
        Game.player_count += 1
        self.id = Game.player_count
        
    def play_card(self, name):
        self.name = name
        if self.id == 1:
            play = input("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO PLAY, " + self.name + "?\n\n" 
                                + str(player1_hand[0]) + "\n" 
                                + str(player1_hand[1]) + "\n"  
                                + str(player1_hand[2]) + "\n\n")
            while play not in player1_hand:
                play = input("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO PLAY?\n\n")
            choices.append(play)
            choices_player1.append(play)
            card_index = player1_hand.index(play)
            player1_hand.pop(card_index)
            player1_hand.append(" ")  
        if self.id == 2:
            play = input(("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO PLAY, " + self.name + "?\n\n" 
                            + str(player2_hand[0]) + "\n" 
                            + str(player2_hand[1]) + "\n"  
                            + str(player2_hand[2]) + "\n\n"))
            while play not in player2_hand:
                play = input("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO PLAY?\n\n")
            choices.append(play)
            choices_player2.append(play)
            card_index = player2_hand.index(play)
            player2_hand.pop(card_index)
            player2_hand.append(" ")
        

    def hide_card(self, name):
        self.name = name
        if self.id == 1:
            hide = input("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO HIDE, " + self.name + "?\n\n" 
                                + str(player1_hand[0]) + "\n" 
                                + str(player1_hand[1]) + "\n"  
                                + str(player1_hand[2]) + "\n\n")
            while hide not in player1_hand:
                hide = input("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO HIDE?\n\n")
            cards[0] = "hide"
            choices.append("hide")
            choices_player1.append("hide")
            print(choices)
            card_index = player1_hand.index(hide)
            player1_hand.pop(card_index)
            player1_hand.append(" ")    
        if self.id == 2:
            hide = input(("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO HIDE, " + self.name + "?\n\n" 
                            + str(player2_hand[0]) + "\n" 
                            + str(player2_hand[1]) + "\n"  
                            + str(player2_hand[2]) + "\n\n"))
            while hide not in player2_hand:
                hide = input("WHICH ONE OF YOUR CARDS WOULD YOU LIKE TO HIDE?\n\n")
            cards[0] = "hide"
            choices.append("hide")
            choices_player2.append("hide")
            card_index = player2_hand.index(hide)            
            player2_hand.pop(card_index)
            player2_hand.append(" ")

    def calling_truco(self):
        if self.id == 1:
            truco = input(player_list[1] + " WOULD YOU LIKE TO: \n\n ACCEPT \n RUN \n CALL 3 MORE \n\n")
            if truco.title() not in ["Accept", "Run", "Call 3 More"]:
                truco = input("WOULD YOU LIKE TO: \n\n ACCEPT \n RUN \n CALL 3 MORE \n\n")
            if truco.title() == "Accept":
                    Game.Truco += 3
                    print("ROUND IS NOW WORTH, " + str(Game.Truco) + "!!")
            elif truco.title() == "Run":
                score_list2[0] += 2
            elif truco.title() == "Call 3 More":
                Game.Truco += 6
                player2.adding3()
        if self.id == 2:
            truco = input(player_list[0] + " WOULD YOU LIKE TO: \n\n ACCEPT \n RUN \n CALL 3 MORE \n\n")
            if truco.title() not in ["Accept", "Run", "Call 3 More"]:
                truco = input("WOULD YOU LIKE TO: \n\n ACCEPT \n RUN \n CALL 3 MORE \n\n")
            if truco.title() == "Accept":
                Game.Truco += 3
                print("ROUND IS NOW WORTH, " + str(Game.Truco) + "!!")
            elif truco.title() == "Run":
                score_list2[1] += 2
            elif truco.title() == "Call 3 More":
                Game.Truco += 6
                player1.adding3()
                 
    def adding3(self):
        if self.id == 1:
            truco = input(player_list[1] + " WOULD YOU LIKE TO: \n\n ACCEPT \n RUN \n CALL 3 MORE \n\n")
            if truco.title() not in ["Accept", "Run", "Call 3 More"]:
                truco = input("WOULD YOU LIKE TO: \n\n ACCEPT \n RUN \n CALL 3 MORE \n\n")
            if truco.title() == "Accept":
                print("ROUND IS NOW WORTH, " + str(Game.Truco) + "!!")
            if truco.title() == "Run":
                score_list2[0] += 2
            if truco.title() == "Call 3 More":
                Game.Truco += 3
                player2.adding3()
        if self.id == 2:
            truco = input(player_list[0] + " WOULD YOU LIKE TO: \n\n ACCEPT \n RUN \n CALL 3 MORE \n\n")
            if truco.title() not in ["Accept", "Run", "Call 3 More"]:
                truco = input("WOULD YOU LIKE TO: \n\n ACCEPT \n RUN \n CALL 3 MORE \n\n")
            if truco.title() == "Accept":
                print("ROUND IS NOW WORTH, " + str(Game.Truco) + "!!")
            if truco.title() == "Run":
                score_list2[1] += 2
            if truco.title() == "Call 3 More":
                Game.Truco += 3
                player1.adding3()
                
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
    #Game setup
    Game.Truco = 0
    RoundOn = True
    score_list2 = [0,0]
    round_number2 = 1
    print("ROUND: " + str(round_number))
    print("\nPOINTS:\n" + player_list[0] + ": " +  str(score_list[0])
              + "\n" + player_list[1] + ": " +  str(score_list[1]))
    #Highest card
    random.shuffle(shuffler)
    biggest_card = shuffler[6]
    lst_key_bcard = [key for key, value in cards.items() if biggest_card in value]
    for key_bcard in lst_key_bcard:
        cards[80] = cards[key_bcard]
    print("THE HIGHEST CARD OF THIS ROUND IS :\n", cards[80][0])
    cards[0] = {} 
    print(shuffler)
    print(cards)
    #Giving out cards
    player1_hand = [shuffler[0], shuffler[1], shuffler[2]]
    player2_hand = [shuffler[3], shuffler[4], shuffler[5]]
    while RoundOn:
        if round_number%2:
            #Play System
            if len(choices) >= 2:
                lst_choice = [key for key, value in cards.items() if choices_player1[0] in value]
                lst_choice2 = [key for key, value in cards.items() if choices_player2[0] in value]
                lst_choice.reverse()
                lst_choice2.reverse()
                print(lst_choice)
                print(lst_choice2)
                if lst_choice[0] > lst_choice2[0]:
                    score_list2[0] += 1
                elif lst_choice[0] < lst_choice2[0]:
                     score_list2[1] += 1
                else:
                    score_list2[0] += 1 
                choices.pop()
                choices.pop()
                choices_player1.pop()
                choices_player2.pop()
            print("\nSCORES:\n" + player_list[0] + ": " +  str(score_list2[0]) #Maybe turn into function later
                + "\n" + player_list[1] + ": " +  str(score_list2[1]))
            #Playing System
            if round_number2 % 2 == 1:
                #Winning Point System
                if score_list2[0] >= 2:
                    round_number += 1
                    if Game.Truco == 3:
                        score_list[0] += 3
                    elif Game.Truco == 6:
                        score_list[0] += 6
                    elif Game.Truco == 9:
                        score_list[0] += 9
                    elif Game.Truco == 12:
                        score_list[0] += 12
                    else:
                        score_list[0] += 1
                    print(player_list[0], "WINS POINT!\n")
                    RoundOn = False
                    break
                if score_list2[1] >= 2:
                    round_number += 1  
                    if Game.Truco == 3:
                        score_list[1] += 3
                    elif Game.Truco == 6:
                        score_list[1] += 6
                    elif Game.Truco == 9:
                        score_list[1] += 9
                    elif Game.Truco == 12:
                        score_list[1] += 12
                    else:
                        score_list[1] += 1
                    print(player_list[1], "WINS POINT!\n")
                    RoundOn = False
                    break   
                #Playing
                print("\n" + player_list[0], "GETS TO PLAY")
                choice = input("YOUR HAND IS:\n\n" 
                                + str(player1_hand[0]) + "\n" 
                                + str(player1_hand[1]) + "\n"  
                                + str(player1_hand[2]) + "\n\n"
                                 "WHAT WOULD YOU LIKE TO DO?\n\n CALL TRUCO\n HIDE CARD\n PLAY CARD\n\n ")
                while choice.title() not in ["Call Truco", "Hide Card", "Play Card"]:
                    choice = input("WHAT WOULD YOU LIKE TO DO?\n\n")
                if choice.title() == "Play Card":
                    player1.play_card(name1)
                elif choice.title() == "Hide Card":
                    player1.hide_card(name1)
                elif choice.title() == "Call Truco":
                    player1.calling_truco()
                #Next round system 
                round_number2 += 1
            else:
                #Winning Point System 
                if score_list2[0] >= 2:
                    round_number += 1
                    if Game.Truco == 3:
                        score_list[0] += 3
                    elif Game.Truco == 6:
                        score_list[0] += 6
                    elif Game.Truco == 9:
                        score_list[0] += 9
                    elif Game.Truco == 12:
                        score_list[0] += 12
                    else:
                        score_list[0] += 1
                    print(player_list[0], "WINS POINT!\n")
                    RoundOn = False
                    break
                if score_list2[1] >= 2:
                    round_number += 1  
                    if Game.Truco == 3:
                        score_list[1] += 3
                    elif Game.Truco == 6:
                        score_list[1] += 6
                    elif Game.Truco == 9:
                        score_list[1] += 9
                    elif Game.Truco == 12:
                        score_list[1] += 12
                    else:
                        score_list[1] += 1
                    print(player_list[1], "WINS POINT!\n")
                    RoundOn = False
                    break  
                #Playing  
                print("\n" + player_list[1], "GETS TO PLAY")
                choice2 = input("YOUR HAND IS:\n\n" 
                                + str(player2_hand[0]) + "\n" 
                                + str(player2_hand[1]) + "\n"  
                                + str(player2_hand[2]) + "\n\n"
                                 "WHAT WOULD YOU LIKE TO DO?\n\n CALL TRUCO\n HIDE CARD\n PLAY CARD\n\n ")
                while choice2.title() not in ["Call Truco", "Hide Card", "Play Card"]:
                    choice2 = input("WHAT WOULD YOU LIKE TO DO?\n\n")
                if choice2.title() == "Play Card":
                    player2.play_card(name2)
                elif choice2.title() == "Hide Card":
                    player2.hide_card(name2)
                elif choice2.title() == "Call Truco":
                    player2.calling_truco()
                #Next round system  
                round_number2 += 1  
        else:
            #Score System
            if len(choices) >= 2:
                lst_choice = [key for key, value in cards.items() if choices_player1[0] in value]
                lst_choice2 = [key for key, value in cards.items() if choices_player2[0] in value]
                lst_choice.reverse()
                lst_choice2.reverse()
                print(lst_choice)
                print(lst_choice2)
                if lst_choice[0] > lst_choice2[0]:
                    score_list2[0] += 1
                elif lst_choice[0] < lst_choice2[0]:
                     score_list2[1] += 1
                else:
                    score_list2[0] += 1 
                choices.pop()
                choices.pop()
                choices_player1.pop()
                choices_player2.pop()
            print("\nSCORES:\n" + player_list[0] + ": " +  str(score_list2[0]) #Maybe turn into function later
                + "\n" + player_list[1] + ": " +  str(score_list2[1]))
            if round_number2 % 2 == 0:
                #Winning Point System 
                if score_list2[0] >= 2:
                    round_number += 1
                    if Game.Truco == 3:
                        score_list[0] += 3
                    elif Game.Truco == 6:
                        score_list[0] += 6
                    elif Game.Truco == 9:
                        score_list[0] += 9
                    elif Game.Truco == 12:
                        score_list[0] += 12
                    else:
                        score_list[0] += 1
                    print(player_list[0], "WINS POINT!\n")
                    RoundOn = False
                    break
                if score_list2[1] >= 2:
                    round_number += 1  
                    if Game.Truco == 3:
                        score_list[1] += 3
                    elif Game.Truco == 6:
                        score_list[1] += 6
                    elif Game.Truco == 9:
                        score_list[1] += 9
                    elif Game.Truco == 12:
                        score_list[1] += 12
                    else:
                        score_list[1] += 1
                    print(player_list[1], "WINS POINT!\n")
                    RoundOn = False
                    break  
                #Playing
                print("\n" + player_list[0], "GETS TO PLAY")
                choice = input("YOUR HAND IS:\n\n" 
                                + str(player1_hand[0]) + "\n" 
                                + str(player1_hand[1]) + "\n"  
                                + str(player1_hand[2]) + "\n\n"
                                  "WHAT WOULD YOU LIKE TO DO?\n\n CALL TRUCO\n HIDE CARD\n PLAY CARD\n\n ")
                while choice.title() not in ["Call Truco", "Hide Card", "Play Card"]:
                    choice = input("WHAT WOULD YOU LIKE TO DO?\n\n")
                if choice.title() == "Play Card":
                    player1.play_card(name1)
                elif choice.title() == "Hide Card":
                    player1.hide_card(name1)
                elif choice.title() == "Call Truco":
                    player1.calling_truco()
                #Next round system
                round_number2 += 1
            else:
                #Winning Point System
                if score_list2[0] >= 2:
                    round_number += 1
                    if Game.Truco == 3:
                        score_list[0] += 3
                    elif Game.Truco == 6:
                        score_list[0] += 6
                    elif Game.Truco == 9:
                        score_list[0] += 9
                    elif Game.Truco == 12:
                        score_list[0] += 12
                    else:
                        score_list[0] += 1
                    print(player_list[0], "WINS POINT!\n")
                    RoundOn = False
                    break
                if score_list2[1] >= 2:
                    round_number += 1  
                    if Game.Truco == 3:
                        score_list[1] += 3
                    elif Game.Truco == 6:
                        score_list[1] += 6
                    elif Game.Truco == 9:
                        score_list[1] += 9
                    elif Game.Truco == 12:
                        score_list[1] += 12
                    else:
                        score_list[1] += 1
                    print(player_list[1], "WINS POINT!\n")
                    RoundOn = False
                    break    
                #Playing  
                print("\n" + player_list[1], "GETS TO PLAY")
                choice2 = input("YOUR HAND IS:\n\n" 
                                + str(player2_hand[0]) + "\n" 
                                + str(player2_hand[1]) + "\n"  
                                + str(player2_hand[2]) + "\n\n"
                                  "WHAT WOULD YOU LIKE TO DO?\n\n CALL TRUCO\n HIDE CARD\n PLAY CARD\n\n ")
                while choice2.title() not in ["Call Truco", "Hide Card", "Play Card"]:
                    choice2 = input("WHAT WOULD YOU LIKE TO DO?\n\n")
                if choice2.title() == "Play Card":
                    player2.play_card(name2)
                elif choice2.title() == "Hide Card":
                    player2.hide_card(name2)
                elif choice2.title() == "Call Truco":
                    player2.calling_truco()
                #Next round system
                round_number2 += 1  
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

#CHANGE "HIDE" (REMOVE AFTER USING)