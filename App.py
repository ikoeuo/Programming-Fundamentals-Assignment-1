import random
import KnightRole
import WizardRole
import Game


def darkForest():
    d1 = random.randint(1, 10)
    d2 = random.randint(1, 10)
 
    if (Game.roleasn==('Knight')) or (Game.roleasn==('knight')):

        dSpeed = KnightRole.speed + d1 + d2

        if dSpeed >= 15:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile if was tough with all of your armour you were able to outrun the witch! Congrats {name}')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\n You tripped over all of your gear and were not able to outrun the witch better luck next time {name}')
            print('\nGAME OVER')
            exit()
            
    if (Game.roleasn==('Wizard')) or (Game.roleasn==('wizard')):

        dSpeed = WizardRole.speed + d1 + d2

        if dSpeed >= 15:   
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile it was not easy you were able to speed through the forest on your broom and outrun the witch! Congrats {name}')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile looking back you flew into a tree and were not able to outrun the witch, better luck next time {name}.')
            print('\nGAME OVER')
            exit()


def dungeonTrap():
    pass

def dragonFight():
    pass