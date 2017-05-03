import random

class Droeloe:
    def __init__(self):
        #Battle
        self.enemyhealth = random.randrange(8, 15)
        self.enemydamage = random.randrange(1, 6)
        self.playerdamage = random.randrange(0, 6)
        self.turn = True
        self.won = False

        #Stats
        self.currentlevel = 5
        self.player_health = 20
        self.currentprogress = 75
        self.levelup = 100
        self.attackpower = 4
        self.defensepower = 4

    def Update_stat(self):
        if self.won == True:
            self.currentprogress = self.currentprogress + 25
            if self.currentprogress >= self.levelup:
                self.currentprogress = self.currentprogress - self.levelup
                self.currentlevel += 1
                self.attackpower = self.attackpower / 100 * 150
                self.defensepower = self.defensepower / 100 * 150
                self.levelup = self.levelup / 100 * 120
                print("You're level up!")
                self.Stats()
            else:
                self.Stats()
        else:
            self.Stats()

    def Stats(self):
        print("--------------------------------------------------------------")
        print(" - Stats -")
        print("Level:", int(self.currentlevel))
        print("Attackpower add:", int(self.attackpower))
        print("Defensepower add", int(self.defensepower))
        print("Progress:", int(self.currentprogress), "/", int(self.levelup))
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
        elif doing == "defend":
            self.Dfnd()
        elif doing == "stats":
            self.Update_stat()
        elif doing == "run":
            print("Running away")
            exit

    def Dfnd(self):
        # print("Defend")
        #if self.turn == True:
            if random.randint(0,100) < 36:
                print("Failed to defend")
                print("Enemy dealt", self.enemydamage)
                self.Moves()
            else:
                print("Succesfully defended from the enemy!")
                self.Moves()                
            

    def Atk(self):
        if self.turn == True:
            self.enemyhealth = self.enemyhealth - self.playerdamage
            if self.enemyhealth < 1:
                print("--------------------------------------------------------------")
                print("You dealt", self.playerdamage, "damage")
                print("Enemy has", self.enemyhealth, "lives left")
                print('You won, good job')
                self.update_stat
                exit
                self.won = True
                self.Update_stat()
            else:
                self.turn == False
                print("--------------------------------------------------------------")
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