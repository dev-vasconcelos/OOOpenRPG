import random

class Character:
    #definitivamente not a Constructor
    def createCharacter(self, name, clss, life, atck, lucky, dex, armor, maxHP):
        self.name = name
        self.clss = clss
        self.life = life
        self.atck = atck
        self.lucky = lucky
        self.dex = dex
        self.armor = armor
        self.maxHP = maxHP

    #Return all data as String
    def toString(self):
        return "[Name: {}, Class: {}; life: {}; armor: {}; atack: {}; lucky: {}; dex: {}, maxHP: {}]".format(self.name, self.clss, self.life, self.armor, self.atck, self.lucky, self.dex, self.maxHP)

    #Generates a random weak enemy
    def randomCharacter(self, lvl):
        names = ["Merek", "Carac", "Ulric", "Tybalt", "Borin"] # names = ["Sadon", "terrowin", "Rowan", "Althalos", "Brom"]
        ichosen = random.randint(0,4)
        chosen = names[ichosen]
        self.name = chosen
        self.clss = "warrior"
        self.maxHP = 100 * lvl - (lvl * 10)
        self.life = self.maxHP - 30*lvl
        self.lucky = lvl*4
        self.dex = 8
        self.armor = 8
        self.atck = lvl * 5

    def createWarrior(self, name, lvl):
        self.name = name
        self.clss = "warrior"
        self.maxHP = 100 * lvl - (lvl * 10)
        self.life = self.maxHP - 30*lvl
        self.lucky = lvl*4
        self.dex = 6 + lvl
        self.armor = 10 + lvl

    def createArcher(self, lvl):
        names = ["Sadon", "terrowin", "Rowan", "Althalos", "Brom"]
        ichosen = random.randint(0,4)
        chosen = names[ichosen]
        self.clss = "archer"
        self.name = chosen
        self.clss = "archer"
        self.maxHP = 100 * lvl - (lvl * 5)
        self.life = self.maxHP - 10*lvl
        self.lucky = lvl*4
        self.dex = 10 + lvl
        self.armor = 6 + lvl

