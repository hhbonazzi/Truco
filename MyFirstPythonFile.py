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
print(shuffler)

#Player vs Player
score_list = [0,0]
round_number = 0
player_list = []
GameOn = True

while GameOn:
    round_number += 1
    print("ROUND:", round_number)
    if round_number%2 == 0:
        print(player_list[0], "GETS TO PLAY")
    else:
        print(player_list[1], "GETS TO PLAY")

#Game class
class Game:

    def __init__(self, name):
        self.name = name
