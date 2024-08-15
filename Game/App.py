import random
import KnightRole
import WizardRole


def role():
    while True:

        global roleasn
        roleasn = (input('\nWill you be the “Brave Dashing Knight” or the “Powerful Wizard”? (Knight/Wizard) '))
        
        if (roleasn==('Knight')) or (roleasn==('knight')):
            print('Oh I see you choosen the Knight wise choice!')
            print('Your stats are:')
            print(f'\nDefense: {KnightRole.defence}\nPower: {KnightRole.power}\nSpeed: {KnightRole.speed}')
            print('\nall of your stats are measured on a scale from 0 to 10')
            break


        elif (roleasn==('Wizard')) or (roleasn==('wizard')):
            print('Oh I see you choosen the Wizard wise choice!')
            print('Your stats are:')
            print(f'\nDefense: {WizardRole.defence}\nPower:{WizardRole.power}\nSpeed: {WizardRole.speed}')
            print('\nall of your stats are measured on a scale from 0 to 10')
            break

        else:
            print('\nSorry traveller that is not one of the roles you must pick today')

    #Used to get the players name
    global name
    name = str(input('\nNow that your role is decided, what will I call you through this quest? '))
    

    print(f'\n{name} what a fine name indeed traveler!')
    print('\nNow that all formalities are out of the way it is time for your first quest')
    print('\nIn total there are 3 quests to reach The Lost Treasure and they all depend on your luck')

def darkForest():

    while True:    

        question = (input(f'\nSo {name} are you ready for your first quest? (yes/no) '))

        if (question == ('Yes')) or (question == ('yes')):
            break

        else:
            print(f'You must say yes to continue')

    while True:    

        question = (input('\nSo would you like to roll your dice? (yes/no) \n\n*You can role 2 dice, each one with 10 sides 1-10* '))

        if (question == ('Yes')) or (question == ('yes')):
            break

        else:
            print(f'\nYou must roll the dice to continue')

    d1 = random.randint(1, 10)
    d2 = random.randint(1, 10)
 
    if (roleasn==('Knight')) or (roleasn==('knight')):

        dDefence = KnightRole.defence + d1 + d2

        if dDefence >= 15:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile if was tough with all of your armour you were able to outrun the witch! Congrats {name}')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\n You tripped over all of your gear and were not able to outrun the witch better luck next time {name}')
            print('\nGAME OVER')
            exit()
            
    if (roleasn==('Wizard')) or (roleasn==('wizard')):

        dDefence = WizardRole.defence + d1 + d2

        if dDefence >= 15:   
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile it was not easy you were able to speed through the forest on your broom and outrun the witch! Congrats {name}')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile looking back you flew into a tree and were not able to outrun the witch, better luck next time {name}.')
            print('\nGAME OVER')
            exit()

def dungeonTrap():
    while True:    

        question = (input('\n Your next quest will be more challenging are you ready for the challenge? '))

        if (question == ('Yes')) or (question == ('yes')):
            break

        else:
            print('You must say yes to continue')

    
    print('\nFor this quest you must make your way through the treasures dungeon you must be quick and avoid all the traps')
    while True:    

        question = (input('\nSo would you like to roll your dice? '))

        if (question == ('Yes')) or (question == ('yes')):
            break

        else:
            print('\nYou must roll the dice to continue')

    d1 = random.randint(1, 10)
    d2 = random.randint(1, 10)
 
    if (roleasn==('Knight')) or (roleasn==('knight')):
        
        dSpeed = KnightRole.speed + d1 + d2

        if dSpeed >= 20:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nYou were able to speed through and dungeon dodging all of the traps')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nThough you were quick there was one trap you were not able to see, with such a wound there is no way youll make it, better luck next time {name}')
            print('\nGAME OVER')
            exit()
            
    if (roleasn==('Wizard')) or (roleasn==('wizard')):

        dSpeed = WizardRole.speed + d1 + d2

        if dSpeed >= 20:   
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWith your great speed you were able to dodge the traps even the sneaky ones')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWhile flying through the dungeon you were caught off guard by a floor trap, there is no ecaping from this \nbetter luck nect time {name}')
            print('\nGAME OVER')
            exit()

def dragonFight():
    while True:    

        question = (input('Your\'e are strong indeed no one else has made it this far, are you ready for your last quest? '))

        if (question == ('Yes')) or (question == ('yes')):
            break

        else:
            print(f'\nYou must say yes to continue')

    
    print('\nFor this quest your strength and defence will be crucial \nFor this quest you will have to slay the dragon protecting The Lost Treasure')
    while True:    

        question = (input(f'\nSo would you like to take on this challenge and roll your dice? (yes/give up) '))

        if (question == ('Yes')) or (question == ('yes')):
            break
        elif (question == ('give up')):
            print('It was a good try better luck next time.')
            exit()
        else:
            print(f'\nYou must roll the dice to continue or give up')
        d1 = random.randint(1, 10)
        d2 = random.randint(1, 10)
 
    if (roleasn==('Knight')) or (roleasn==('knight')):

        dPower = KnightRole.power + KnightRole.defence + d1 + d2

        if dPower >= 30:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nThough it was tough with your armour and sword you were able to slay the dragon')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nYou were not strong enough to defeat the dragon and with these injuries there is going back, better luck next time {name}')
            print('\nGAME OVER')
            exit()
            
    if (roleasn==('Wizard')) or (roleasn==('wizard')):

        dPower = WizardRole.power + WizardRole.defence + d1 + d2

        if dPower >= 30:   
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nWith your magic abilities you were able to swiftly slay the dragon')

        else:
            print(f'\nYour dice landed on {d1} and {d2}')
            print(f'\nEven with your great power one hit from the dragon took you out due to your low defence, better luck next time {name}')
            print('\nGAME OVER')
            exit()
                       


    


