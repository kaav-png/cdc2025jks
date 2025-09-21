
# pop_culture = Table().read_table('Pop_Culture.csv')

"""import csv
import pandas as pd
import os

data = list()
with open('Pop_Culture.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    hear = next(csvreader)
    for row in csvreader:
        data.append(row)

print(data[0])"""

# ask the user a series of questions
# print the options on another line (make them choose the number like an automated phone call)
# user input on next line

hero_answer = ''
while hero_answer not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    print('What is your favorite Star Wars hero? (type number to answer)')
    print('1: Anakin Skywalker, 2: Chewbacca, 3: Han Solo, 4: Jar Jar Binks, 5: Leia, 6: Luke Skywalker, 7: Obi-Wan Kenobi, 8: Qui-Gon Jinn, 9: Yoda')
    hero_answer = input('')
hero_answer = int(hero_answer)

villain_answer = ''
while villain_answer not in ['1', '2', '3', '4', '5', '6']:
    print('What is your favorite Star Wars villain?')
    print('1: Count Dooku, 2: Darth Maul, 3: Darth Vader, 4: General Grievous, 5: Palpatine, 6: Wilhuff Tarkin')
    villain_answer = input('')
villain_answer = int(villain_answer)

film_answer = ''
while film_answer not in ['1', '2', '3', '4', '5', '6']:
    print('What is your favorite Star Wars Film?')
    print('1: Episode I - The Phantom Menace, 2: Episode II - Attack of the Clones, 3: Episode III - Revenge of the Sith, 4: Episode IV - A New Hope, 5: Episode V - The Empire Strikes Back, 6: Episode VI - Return of the Jedi')
    film_answer = input('')
film_answer = int(film_answer)

soundtrack_answer = ''
while soundtrack_answer not in ['1', '2', '3', '4', '5']:
    print('What is your favorite Star Wars soundtrack?')
    print('1: Accross the Stars, 2: Anakin vs. Obi-Wan, 3: Imperial March, 4: Star Wars (Main Theme), 5: The Throne Room')
    soundtrack_answer = input('')
soundtrack_answer = int(soundtrack_answer)

spaceship_answer = ''
while spaceship_answer not in ['1', '2', '3', '4']:
    print('What is your favorite Star Wars spaceship?')
    print('1: Death Star, 2: Millennium Falcon, 3: Naboo Starfighter, 4: TIE Fighter')
    spaceship_answer = input('')
spaceship_answer = int(spaceship_answer)

planet_answer = ''
while planet_answer not in ['1', '2', '3', '4', '5']:
    print('What is your favorite planet in Star Wars?')
    print('1: Alderaan, 2: Dagobah, 3: Endor, 4: Naboo, 5: Tatooine')
    planet_answer = input('')
planet_answer = int(planet_answer)

robot_answer = ''
while robot_answer not in ['1', '2', '3', '4']:
    print('What is your favorite robot in Star Wars?')
    print('1: Battle Droid, 2: C-3PO, 3: Droideka, 4: R2-D2')
    robot_answer = input('')
robot_answer = int(robot_answer)