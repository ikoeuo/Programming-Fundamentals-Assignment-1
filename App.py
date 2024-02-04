import random
import KnightRole
import WizardRole
import Game


def darkForest():
    d1 = random.randint(1, 10)
    d2 = random.randint(1, 10)
 
    if (Game.roleasn==('Knight')) or (Game.roleasn==('knight')):

        dDefence = KnightRole.defence + d1 + d2

        if dDefence >= 15:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile if was tough with all of your armour you were able to outrun the witch! Congrats {Game.name}')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\n You tripped over all of your gear and were not able to outrun the witch better luck next time {Game.name}')
            print('\nGAME OVER')
            exit()
            
    if (Game.roleasn==('Wizard')) or (Game.roleasn==('wizard')):

        dDefence = WizardRole.defence + d1 + d2

        if dDefence >= 15:   
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile it was not easy you were able to speed through the forest on your broom and outrun the witch! Congrats {Game.name}')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile looking back you flew into a tree and were not able to outrun the witch, better luck next time {Game.name}.')
            print('\nGAME OVER')
            exit()


def dungeonTrap():
    d1 = random.randint(1, 10)
    d2 = random.randint(1, 10)
 
    if (Game.roleasn==('Knight')) or (Game.roleasn==('knight')):
        
        dSpeed = KnightRole.speed + d1 + d2

        if dSpeed >= 20:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nYou were able to speed through and dungeon dodging all of the traps')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nThough you were quick there was one trap you were not able to see, with such a wound there is no way youll make it, better luck next time {Game.name}')
            print('\nGAME OVER')
            exit()
            
    if (Game.roleasn==('Wizard')) or (Game.roleasn==('wizard')):

        dSpeed = WizardRole.speed + d1 + d2

        if dSpeed >= 20:   
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWith your great speed you were able to dodge the traps even the sneaky ones')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile flying through the dungeon you were caught off guard by a floor trap, there is no ecaping from this \nbetter luck nect time {Game.name}')
            print('\nGAME OVER')
            exit()


def dragonFight():
    d1 = random.randint(1, 10)
    d2 = random.randint(1, 10)
 
    if (Game.roleasn==('Knight')) or (Game.roleasn==('knight')):

        dSpeed = KnightRole.power + KnightRole.defence + d1 + d2

        if dSpeed >= 30:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nThough it was tough with your armour and sword you were able to slay the dragon')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nYou were not strong enough to defeat the dragon and with these injuries there is going back, better luck next time {Game.name}')
            print('\nGAME OVER')
            exit()
            
    if (Game.roleasn==('Wizard')) or (Game.roleasn==('wizard')):

        dSpeed = WizardRole.power + WizardRole.defence + d1 + d2

        if dSpeed >= 30:   
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWith your magic abilities you were able to swiftly slay the dragon')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nEven with your great power one hit from the dragon toom you out due to your low defence, better luck next time {Game.name}')
            print('\nGAME OVER')
            exit()
                       
print(f'\nThe Lost treasure is now all yours {Game.name} Congrats!')
print('\nWINNER')
exit()
    


