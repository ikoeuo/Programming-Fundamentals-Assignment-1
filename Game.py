#Dnd text game
import KnightRole
import WizardRole
import App

print('Hello fellow traveler, welcome To your quest to find The Lost Treasure!')
print('\nWhat path will you choose to follow today?')

while True:
#loop to make player choose their role

    roleasn = (input('\nWill you be the “Brave Dashing Knight” or the “Powerful Wizard”? '))

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

    question2 = (input(f'\nSo {name} would you like to roll your dice? '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print(f'\nYou must roll the dice to continue{name}')


App.darkForest()
