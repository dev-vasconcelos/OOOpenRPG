import Character as chh
import PVE as pv
import time
                            #      PERSONAGENS REALIZAM AÇÃO
enemy = chh.Character()     #  Entidade personagem usando uma função que 
enemy.randomCharacter(1)    #  não é dele em um "arquivo" que não é dele

pedro = chh.Character()
pedro.createCharacter('pedro', 'warrior', 100, 5, 5, 10, 15, 200)

while pedro.life > 0 and enemy.life > 0:
    # pass # Just for me to remember this exists
    battle = pv.PVE(pedro, enemy)
    battle.enemyTurn()
    battle.playerTurn()

print("Andando mais a frente nota-se o quanto o mundo começa a se distorcer... VOCÊ CAIU NUM GENJUSTSY")
time.sleep(1)
print("preparesse para mais uma batalha!!!")
time.sleep(1)

enemy2 = chh.Character()
enemy2.randomCharacter(2)
while pedro.life > 0 and enemy2.life > 0:
    print("O INIMIGO PARECE MAIS FORTE")
    # pass # Just for me to remember this exists
    battle = pv.PVE(pedro, enemy2)
    battle.playerTurn()
    battle.enemyTurn()



print("CONCLUIDO")