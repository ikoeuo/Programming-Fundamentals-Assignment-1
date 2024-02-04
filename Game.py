#Dnd text game
import App

print('Hello fellow traveler, welcome To your quest to find The Lost Treasure!')
print('\nWhat path will you choose to follow today?')

print(App.role())

while True:    

    question = (input('\nSo are you ready for your first quest? (yes/no) '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print(f'You must say yes to continue')


#challenge one   
print('\nFor your first quest you must run through the dark forest but there lies an evil witch, beware for if you are caught there is no turning back')
while True:    

    question2 = (input('\nSo would you like to roll your dice? (yes/no) \n\n*You can role 2 dice, each one with 10 sides 1-10* '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print(f'\nYou must roll the dice to continue')

print(App.darkForest())

#challenge two
while True:    

    question = (input('\n Your next quest will be more challenging are you ready for the challenge? '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print('You must say yes to continue')

    
print('\nFor this quest you must make your way through the treasures dungeon you must be quick and ovoid all the traps')
while True:    

    question2 = (input('\nSo would you like to roll your dice? '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print('\nYou must roll the dice to continue')

print(App.dungeonTrap())

#challenge three
while True:    

    question = (input('Your are strong indeed no one else has made it this far, are you ready for your last quest? '))

    if (question == ('Yes')) or (question == ('yes')):
        break

    else:
        print(f'\nYou must say yes to continue')

    
print('\nFor this quest your strength and defence will be crucial \nFor this quest you will have to slay the dragon protecting The Lost Treasure')
while True:    

    question2 = (input(f'\nSo would you like to take on this challenge and roll your dice? '))

    if (question == ('Yes')) or (question == ('yes')):
        break
    elif (question == ('give up')):
        print('It was a good try better luck next time.')
        exit()
    else:
        print(f'\nYou must roll the dice to continue or give up')

App.dragonFight()

print(f'\nThe Lost treasure is now all yours Congrats!')
print('\nWINNER')
exit()



