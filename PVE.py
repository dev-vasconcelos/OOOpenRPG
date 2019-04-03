import time
import Action as ac
import os

class PVE:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def printStats(self):
        print("PLAYER STATUS \n")
        print(self.player.toString())
        print(" ======[]==O")
        print("ENEMY STATUS \n")
        print(self.enemy.toString())
        print("  )  >-----|>")

        if(self.enemy.life <= 0):
            print("PLAYER WINS")
        elif(self.player.life <= 0):
            print("you loose")
            
        
    #delay ANd pureOO example
    def enemyTurn(self):
        time.sleep(.5)
        if (self.enemy.life < 5):
            ac.heal(self.enemy, 8)
        ac.attack(self.enemy, self.player)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.printStats()
        

    #switch case ex
    def playerTurn(self):
        # 1 - attck
        # 2 - duel
        # 3 - heal
        # 4 - goBrasil
        #Next step ::: Put Hability as an array in Character
        # and call for the hability number
        print("1 - ATTACK   2 - DUEL")
        print("3 - HEAL   4 - goBrasil")
        action = input()
        time.sleep(1)
        action = int(action)
        while (action <= 0 and action >= 5):
            print("this was entered wrong")
            return 0

        if(action == 1):
            ac.attack(self.player, self.enemy)
        elif(action == 2):
            ac.duel(self.player, self.enemy)
        elif(action == 3):
            ac.heal(self.player, 15)
        elif action == 4:
            ac.goBrasil(self.player)
        
        self.printStats()
        