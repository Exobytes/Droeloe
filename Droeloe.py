import random

class Droeloe:
    def __init__(self):
        #Battle
        self.enemyhealth = random.randrange(8, 15)
        self.enemydamage = random.randrange(1, 6)
        self.playerdamage = random.randrange(0, 6)
        self.turn = True

        #Stats
        self.currentlevel = 5
        self.player_health = 20
        self.currentprogress = 0
        self.levelup = 100
        self.attackpower = 4
        self.defensepower = 4
    
    def Stats(self):
        print("--------------------------------------------------------------")
        print(" - Stats -")
        print("Level:", self.currentlevel)
        print("Attackpower add:", self.attackpower)
        print("Defensepower add", self.defensepower)
        print("Progress:", self.currentprogress)
        print("--------------------------------------------------------------")
        self.Turn()

    def Start(self):
        print("--------------------------------------------------------------")
        print("Enemy has:", self.enemyhealth, "lives")
        print("You have:", self.player_health, "lives")
        print("--------------------------------------------------------------")
        self.Turn()

    def Turn(self):
        if self.turn == True:
            print("Its your turn")
            self.Moves()
        else:
            print("Enemy's turn")
            self.turn = False
            self.Atk()

    def Moves(self):
        doing = str.lower(input("1. Attack, 2. Defend, 3. Stats, 4. Run: "))
        if doing == "attack":
            self.Atk()
        elif doing == "defense":
            self.Dfnd()
        elif doing == "stats":
            self.Stats()
        elif doing == "run":
            print("Running away")
            exit

    def Dfnd(self):
        print("Defend")

    def Atk(self):
        if self.turn == True:
            self.enemyhealth = self.enemyhealth - self.playerdamage
            if self.enemyhealth < 1:
                print("You dealt", self.playerdamage, "damage")
                print("Enemy has", self.enemyhealth, "lives left")
                print('You won, good job')
                exit
            else:
                self.turn == False
                print("You dealt", self.playerdamage, "damage")
                print("Enemy has", self.enemyhealth, "lives left")
                self.turn = False
                self.Atk()
        elif self.turn == False:
            if self.player_health < 1:
                print("--------------------------------------------------------------")
                print("You lost")
                print("--------------------------------------------------------------")
            else:
                self.player_health = self.player_health - self.enemydamage
                print("--------------------------------------------------------------")
                print("Enemy dealt", self.enemydamage)
                print("You got", self.player_health, "left")
                print("--------------------------------------------------------------")
                self.turn = True
                self.Moves()
        else:
            self.Start()

Game = Droeloe()
Game.Start()