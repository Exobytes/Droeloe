import os
import random
import configparser

class Droeloe:
    def __init__(self):
        # Battle
        self.enemyhealth = random.randrange(8, 15)
        self.turn = True
        self.won = False
        self.lost = False

        # Stats
        savefile = open('save.txt')
        self.currentlevel = int(savefile.readline().split('=')[1])
        self.player_health = int(savefile.readline().split('=')[1])
        self.current_progress = int(savefile.readline().split('=')[1])
        self.levelup = int(savefile.readline().split('=')[1])
        self.attackpower = int(savefile.readline().split('=')[1])
        self.defensepower = int(savefile.readline().split('=')[1])
        savefile.close()

        # self.currentlevel = 5
        # self.player_health = 20
        # self.currentprogress = 75
        # self.levelup = 100
        # self.attackpower = 4
        # self.defensepower = 4

    def Save_Progress(self):
        savefile = open('save.txt')
        savefile.write("currentlevel=%s" % (self.currentlevel))
        savefile.write("player_health=%s" % (self.player_health))
        savefile.write("current_progress=%s" % (self.current_progress))
        savefile.write("levelup=%s" % (self.levelup))
        savefile.write("attackpower=%s" % (self.attackpower))
        savefile.write("defensepower=%s" % (self.defensepower))

    def Update_stat(self):
        if self.won == True:
            self.current_progress = self.current_progress + 25
            if self.current_progress >= self.levelup:
                self.current_progress = self.current_progress - self.levelup
                self.currentlevel += 1
                self.attackpower = self.attackpower / 100 * 150
                self.defensepower = self.defensepower / 100 * 150
                self.levelup = self.levelup / 100 * 120
                print("You leveled up!")
                self.Stats()
            else:
                self.Stats()
        elif self.lost == True:
            self.Stats()
        else:
            self.lost == False
            self.Stats

    def Stats(self):
        print("--------------------------------------------------------------")
        print(" - Stats -")
        print("Level:", int(self.currentlevel))
        print("Attackpower add:", int(self.attackpower))
        print("Defensepower add", int(self.defensepower))
        print("Progress:", int(self.current_progress), "/", int(self.levelup))
        print("--------------------------------------------------------------")
        if self.lost == True:
            exit()
        else:
            self.Moves()

    def Start(self):
        print(self.currentlevel)
        print("--------------------------------------------------------------")
        print("Enemy has:", self.enemyhealth, "lives")
        print("You have:", self.player_health, "lives")
        print("--------------------------------------------------------------")
        self.Moves()

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
            self.clear()
            self.Atk()
        elif doing == "defend":
            self.clear()
            self.Dfnd()
        elif doing == "stats":
            self.clear()
            self.Update_stat()
        elif doing == "run":
            self.clear()
            self.Run()
        else:
            self.clear()
            print("Error: invalid input")
            self.Moves()

    def Dfnd(self):
        # if self.turn == True:
        if random.randint(0, 100) < 10:
            print("Failed to defend")
            print("Enemy dealt", self.enemydamage)
            self.Moves()
        else:
            print("Succesfully defended from the enemy!")
            self.Moves()

    def Atk(self):
        self.enemydamage = random.randrange(1, 6)
        self.playerdamage = random.randrange(0, 6)
        if self.turn == True:
            self.enemyhealth = self.enemyhealth - self.playerdamage
            if self.enemyhealth < 1:
                print("--------------------------------------------------------------")
                print("You dealt", self.playerdamage, "damage")
                print("Enemy has", self.enemyhealth, "lives left")
                print('You won, good job')
                self.enemyhealth = random.randrange(8, 15)
                self.Update_stat()
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
            self.player_health = self.player_health - self.enemydamage
            if self.player_health < 1:
                self.clear()
                print("--------------------------------------------------------------")
                print("You lost")
                self.won = False
                self.lost = True
                self.Update_stat()
            else:
                print("--------------------------------------------------------------")
                print("Enemy dealt", self.enemydamage)
                print("You got", self.player_health, "left")
                print("--------------------------------------------------------------")
                self.turn = True
                self.Moves()
        else:
            self.Start()

    def Run(self):
        print("Running away")
        exit()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


Game = Droeloe()
Game.Start()
