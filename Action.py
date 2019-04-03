import Dice as dd
import time

def attack(attacker,defensor):
    defensor.life -=  dd.dmgLucky(attacker.atck, attacker.lucky, attacker.dex)

def heal(character, healValue):
    heal = dd.heal(healValue)
    print(heal)
    if character.life + heal > character.maxHP:
        character.life = character.maxHP
    else:
        character.life += heal

#hability
def duel(ch1, ch2):
    #TOCAR 1 HOUR SWORD ART ONLINE
    while ch1.life > 0 and ch2.life > 0:
        attack(ch1, ch2)
        attack(ch2, ch1)
        print(ch1.toString())
        print(ch2.toString())
        print("----------------------")
        time.sleep(.5)
    if ch1.life > 0:
        winner = ch1
    else:
        winner = ch2
    #PARAR DE TOCAR
    return winner

