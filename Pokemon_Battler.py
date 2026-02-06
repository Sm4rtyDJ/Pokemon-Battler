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
        self.basedamage = 10

    def attack(self, target):
        advantages = type_chart.get(self.type, {})
        multiplier = advantages.get(target.type, 1.0)

        damage = self.basedamage * multiplier
        target.hp -=damage
        print(f"{self.name} attacked {target.name}")
 
    def __str__(self):
        return self.name



class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 20, "Fire")


class Squirtle(Pokemon):

    def __init__(self):
        super().__init__("Squirtle", 25, "Water")


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 30, "Grass" )



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


#def initiateBattle(playerYou, player_rival):



while True:
    name = input("Enter your name")
    rivalName = input("Enter your rivals name")
    player_rival = rival(rivalName, [])
    playerYou = player(name, [])
    print(f"Welome to Pokemon pocket edition {playerYou.name} \nThis is a demo and you will be able to choose a pokemon and battle with your rival {player_rival.name}\n")
    choosePKMN(playerYou)
    rivalChoose(player_rival)
    if len(playerYou.your_team) > 0:
        print(f"Prof. Tree: Ah so you have chosen {playerYou.your_team[0].name} and your rival {player_rival.name} has chosen {player_rival.your_team[0].name}")
        
  



