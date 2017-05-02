import random

class Droeloe:
    def __init__(self):
        self.enemyhealth = random.randrange(8, 15)
        self.enemydamage = random.randrange(1, 6)
        self.player_health = 20
        self.playerdamage = random.randrange(0, 6)
        self.turn = True

    def Start(self):
        print(self.enemyhealth)
        print(self.player_health)
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
        doing = str(input("1. Attack, 2. Defend, 3. Run:  "))
        if doing == "Attack":
            self.Atk()
        elif doing == "Defense":
            self.Dfnd()
        elif doing == "Run":
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
                self.Moves()
        elif self.turn == False:
            if self.player_health < 1:
                print("You lost")
            else:
                self.player_health = self.player_health - self.enemydamage
                print("Enemy dealt", self.enemydamage)
                print("You got", self.player_health, "left")
                self.turn = True
                self.Moves()
        else:
            self.Start()

    def Term(self):
        print(self.enemyhealth)

Game = Droeloe()
Game.Start()
