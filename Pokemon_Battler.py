import random

type_chart = {
    "Fire": {"Grass": 2.0, "Water": 0.5, "Fire": 1},
    "Water": {"Fire": 2.0, "Grass": 0.5, "Water": 1},
    "Grass": {"Water": 2.0, "Fire": 0.5, "Grass": 1}
}


class player():
    def __init__(self, name, your_team):
        self.your_team = your_team
        self.name = name

    def __str__(self):
        return self.name

 
class rival(player):
    def __init__(self, name, your_team):
        super().__init__(name, your_team)




class Pokemon():
    def __init__(self, name, hp, type):
        self.hp = hp
        self.type = type
        self.name = name
        self.basedamage = 3
        self.moves = {}

    def attack(self, target, name, move_type): #add move_power in the future
        advantages = type_chart.get(move_type, {})       #|
        multiplier = advantages.get(target.type, 1.0)    #|       
                                                         #V
        damage = self.basedamage * multiplier #damage = (self.basedamage + move_power) * multiplier 
        target.hp -=damage
        print(f"{self.name} used {name} on {target.name}")

        if multiplier > 1:
            print("Its super effective!")

        elif multiplier < 1:
            print("Its not very effective...")
 
    def __str__(self):
        return self.name



class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 20, "Fire")
        self.moves = {
            "Ember": "Fire",
            "Scratch" : "Normal"
            }


    def attackEmber(self, target):
        super().attack(target, "Ember", "Fire")

    def attackScratch(self, target):
        super().attack(target, "Scratch", "Normal")


class Squirtle(Pokemon):

    def __init__(self):
        super().__init__("Squirtle", 25, "Water")
        self.moves = {
            "Bubble": "Water",
            "Tackle": "Normal"
        }

    def attackBubble(self, target):
        super().attack(target, "Bubble", "Water")

    def attackTackle(self, target):
        super().attack(target, "Tackle", "Normal")


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 30, "Grass" )
        self.moves = {
            "Razor Leaf": "Grass",
            "Headbutt": "Normal"
        }

    def attackRazorLeaf(self, target):
        super().attack(target, "Razor Leaf", "Grass")

    def attackHeadbutt(self, target):
        super().attack(target, "Headbutt", "Normal")



starter_PKMN = [Charmander(), Squirtle(), Bulbasaur()]
def choosePKMN(currentPlayer):
    while True:
        answer = input(f"Which starter do you want to pick? \n{starter_PKMN[0]}\n{starter_PKMN[1]}\n{starter_PKMN[2]}")
        if answer in [pkmn.name for pkmn in starter_PKMN]:
            question = input("Are you sure? y/n")
            if question == "y":
                print(f"You have chosen {answer}")
                for pkmn in starter_PKMN: 
                    if pkmn.name == answer:
                        currentPlayer.your_team.append(pkmn)
                break
            else:
                continue
        else: print("Please choose one of the displayed pokemon ")


def rivalChoose(yourRival):
    choice = random.randint(0,2)
    yourRival.your_team.append(starter_PKMN[choice])



def initiateBattle(playerYou, player_rival):
    p1 = playerYou.your_team[0]
    p2 = player_rival.your_team[0]
    print(f"{playerYou.name} VS {player_rival.name} ")
    while p1.hp > 0 and p2.hp > 0: 
        moves = list(p1.moves.keys())
        rival_moves = list(p2.moves.keys())
        rival_action = random.choice(rival_moves)
        action = input(f"Which move do want to use? {moves}")
        if action == "Ember":
            p1.attackEmber(p2)
        elif action =="Scratch":
            p1.attackScratch(p2)
            
#Fix this, change how the attack works
        if rival_action == "Ember":
            p2.attackEmber(p1)
        elif rival_action == "Scratch":
            p2.attackScratch(p1)
        elif rival_action =="Headbutt":
            p2.attackHeadbutt(p1)
        elif rival_action =="Tackle":
            p2.attackTackle(p1)
        elif rival_action == "Bubble":
            p2.attackBubble(p1)
        elif rival_action == "Razor Leaf":
            p2.attackRazorLeaf(p1)

        print(f"{p2.name} has {p2.hp}hp left")
        print(f"{p1.name} has {p1.hp}hp left")

    if p1.hp <= 0:
        print(f"{p1.name} has fainted! You have lost the battle, {p2.name} is the winner!")
    else: 
        print(f"{p2.name} has fainted! You have won the battle, {p1.name} is the winner!")




while True:
    name = input("Enter your name")
    rivalName = input("Enter your rivals name")
    player_rival = rival(rivalName, [])
    playerYou = player(name, [])
    print(f"Welome to Pokemon pocket edition {playerYou.name} \nThis is a demo and you will be able to choose a pokemon and battle with your rival {player_rival.name}\n")
    choosePKMN(playerYou)
    rivalChoose(player_rival)
    while True:
        if len(playerYou.your_team) > 0:
            print(f"Prof. Tree: Ah so you have chosen {playerYou.your_team[0].name} and your rival {player_rival.name} has chosen {player_rival.your_team[0].name}")
            ready = input("Are you ready for battle? y/n")
            if ready == "y":
                print("Let the battle begin!")
                initiateBattle(playerYou, player_rival)
                break  
    print("Thank you for playing")
    break

    

        
        
  



