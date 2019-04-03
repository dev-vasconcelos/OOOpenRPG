import Character as chh
import PVE as pv
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