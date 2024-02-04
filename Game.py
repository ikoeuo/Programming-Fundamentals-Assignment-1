#Dnd text game
import KnightRole
import WizardRole
import App

print('Hello fellow traveler, welcome To your quest to find The Lost Treasure!')
print('\nWhat path will you choose to follow today?')

while True:
#loop to make player choose their role

    roleasn = (input('\nWill you be the “Brave Dashing Knight” or the “Powerful Wizard”? (Knight/Wizard)'))

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
        print('\nSorry traveller that is not one of the roles you must pick today so,')

#Used to get the players name
name = input('\nNow that your role is decided, what will I call you through this quest? ')

print(f'\n{name} what a fine name indeed traveler!')
print('\nNow that all formalities are out of the way it is time for your first quest')
print('\nIn total there are 3 quests to reach The Lost Treasure and they all depend on your luck')


while True:    

    question = (input(f'\nSo {name} are you ready for your first quest? '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print(f'You must say yes to continue {name}')


#challenge one   
print('\nFor your first quest you must run through the dark forest but there lies an evil witch, beware for if you are caught there is no turning back')
while True:    

    question2 = (input(f'\nSo {name} would you like to roll your dice? \n*You can role 2 dice, each one with 10 sides 1-10*'))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print(f'\nYou must roll the dice to continue{name}')

App.darkForest()

#challenge two
while True:    

    question = (input(f'\n{name} Your next quest will be more challenging are you ready for the challenge? '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print(f'You must say yes to continue {name}')

    
print('\nFor this quest you must make your way through the treasures dungeon you must be quick and ovoid all the traps')
while True:    

    question2 = (input(f'\nSo {name} would you like to roll your dice? '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print(f'\nYou must roll the dice to continue{name}')

App.dungeonTrap()

#challenge three
while True:    

    question = (input(f'Your are strong indeed {name} no one else has made it this far, are you ready for your last quest? '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print(f'\nYou must say yes to continue {name}')

    
print('\nFor this quest your strength and defence will be crucial \nFor this quest you will have to slay the dragon protecting The Lost Treasure')
while True:    

    question2 = (input(f'\nSo {name} would you like to take on this challenge and roll your dice? '))

    if (question == ('Yes')) or (question == ('yes')):
        break
    elif (question == ('give up')):
        print(f'It was a good try {name} better luck next time.')
        exit()
    else:
        print(f'\nYou must roll the dice to continue or give up {name}')

App.dragonFight()
    



