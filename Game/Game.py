#Dnd text game
import App

print('Hello fellow traveler, welcome To your quest to find The Lost Treasure!')
print('\nWhat path will you choose to follow today?')

#intro
App.role()

#challenge one   
print('\nFor your first quest you must run through the dark forest but there lies an evil witch, beware for if you are caught there is no turning back')

App.darkForest()

#challenge two
App.dungeonTrap()

#challenge three
App.dragonFight()

print(f'\nThe Lost treasure is now all yours Congrats!')
print('\nWINNER')
exit()



