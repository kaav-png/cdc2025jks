import pygame
import sys
import os
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#colors
black = (0,0,0)
blue = (46,102,194)

beginningScreen = True

pygame.init()
screen = pygame.display.set_mode((750, 1000))

#Window name
pygame.display.set_caption("Who's Your Star Wars Match?")
        
categories_list = [
    ['Anakin Skywalker', 'Chewbacca', 'Han Solo', 'Jar Jar Binks', 'Leia', 'Luke Skywalker', 'Obi-Wan Kenobi', 'Qui-Gon Jinn', 'Yoda'],
    ['Count Dooku', 'Darth Maul', 'Darth Vader', 'General Grievous', 'Palpatine', 'Wilhuff Tarkin'],
    ['Episode I - The Phantom Menace', 'Episode II - Attack of the Clones', 'Episode III - Revenge of the Sith', 'Episode IV - A New Hope', 'Episode V - The Empire Strikes Back', 'Episode VI - Return of the Jedi'],
    ['Accross the Stars', 'Anakin vs. Obi-Wan', 'Imperial March', 'Star Wars (Main Theme)', 'The Throne Room'],
    ['Death Star', 'Millennium Falcon', 'Naboo Starfighter', 'TIE Fighter'],
    ['Alderaan', 'Dagobah', 'Endor', 'Naboo', 'Tatooine'],
    ['Battle Droid', 'C-3PO', 'Droideka', 'R2-D2']]

question_list = [
    " What is your favorite \n    Star Wars hero? \n (type number to answer)",
    ' What is your favorite \n    Star Wars villain?',
    ' What is your favorite \n    Star Wars Film?',
    ' What is your favorite \n    Star Wars soundtrack?',
    ' What is your favorite \n    Star Wars spaceship?',
    ' What is your favorite \n    planet in Star Wars?',
    ' What is your favorite \n    robot in Star Wars?']

answer_list = [
    ['1: Anakin Skywalker, 2: Chewbacca, 3: Han Solo, 4: Jar Jar Binks, 5: Leia, 6: Luke Skywalker, 7: Obi-Wan Kenobi, 8: Qui-Gon Jinn, 9: Yoda'],
    ['1: Count Dooku, 2: Darth Maul, 3: Darth Vader, 4: General Grievous, 5: Palpatine, 6: Wilhuff Tarkin'],
    ['1: Episode I - The Phantom Menace, 2: Episode II - Attack of the Clones, 3: Episode III - Revenge of the Sith, 4: Episode IV - A New Hope, 5: Episode V - The Empire Strikes Back, 6: Episode VI - Return of the Jedi'],
    ['1: Accross the Stars, 2: Anakin vs. Obi-Wan, 3: Imperial March, 4: Star Wars (Main Theme), 5: The Throne Room'],
    ['1: Death Star, 2: Millennium Falcon, 3: Naboo Starfighter, 4: TIE Fighter'],
    ['1: Alderaan, 2: Dagobah, 3: Endor, 4: Naboo, 5: Tatooine'],
    ['1: Battle Droid, 2: C-3PO, 3: Droideka, 4: R2-D2']] 

ans_range_list = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
     ['1', '2', '3', '4', '5', '6']]

def set_background(s_name):
    background = pygame.image.load(os.path.join(s_name))
    screen.blit(background, (0,0))
    return background

def dtc(list1:list):
    """MACHING LEARNING HERE"""
    data = list()

        #formatting the dataset
    with open('Pop_Culture.csv','r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for row in csvreader:
            data.append(row)

        #converting to dataframe
    data_df = pd.DataFrame(data)

        #naming columns
    data_df.columns = ['review_id','fav_heroe','fav_villain',"fav_film","fav_soundtrack", "fav_spaceship", "fav_planet", "fav_robot"]

        #making x and y and preprocessing data
    from sklearn.preprocessing import OneHotEncoder

    x = data_df[["fav_film", "fav_soundtrack", "fav_spaceship", "fav_planet", "fav_robot"]]
    encoded = OneHotEncoder()
    x_mod = encoded.fit_transform(x)
    y = data_df["fav_heroe"]

        #splitting dataset and training
    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(x_mod, y, test_size = 0.2, random_state=60)

        #testing data
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score

    mL = DecisionTreeClassifier(max_depth=18, random_state=42)
    mL.fit(x_train, y_train)

    y_pred = mL.predict(x_test)
    #accuracy_score(y_test, y_pred)

    # change dashes based on what the user input is
    user_input = pd.DataFrame([{
        "fav_film": list1[0],
        "fav_soundtrack": list1[1],
        "fav_spaceship": list1[2],
        "fav_planet": list1[3],
        "fav_robot": list1[4] 
        }])
## split user input into x and y..
        #this ranks the probabilities of matches based on user responses
    user_mod = encoded.fit_transform(user_input)
    prediction = mL.predict(user_mod)

    probability = (mL.predict_proba(user_input) * 100)
    match = mL.classes_
    match = match

    sample_index = 0
    sample_probs = probability[0]

    ranking = pd.DataFrame({ 
        "Match": match,
        "Probability" : sample_probs
    }).sort_values("Probability", ascending=False)

    print(ranking)



def buttonMaker(font,color,textColor,words,x,y,width,height):
    button_rect = pygame.draw.rect(screen,color,(x,y,width,height))
    font = pygame.font.Font('SUSEMono-VariableFont_wght.ttf',font)
    text = font.render(words,True,textColor)
    button_rect = text.get_rect(center=button_rect.center)
    screen.blit(text,button_rect)
    return button_rect

def question_screen(num,question,answers,x_pos,y_pos):
    set_background('Backgrounds/questions.png')
    buttonMaker(40,"white",black,str(num),490,45,125,100)

    #ans_range_list[num-1]:
    #range(1,len(categories_list[num-1])+1)
    #user_ans = -1

    #while user_ans not in range(1,len(categories_list[num-1])+1):
    """code to ask question"""
    font = pygame.font.Font('SUSEMono-VariableFont_wght.ttf',35)
    lines = question.split("\n")
    #writes each line separately
    for i, line in enumerate(lines):
        line_surface = font.render(line,True,black)
        screen.blit(line_surface,(x_pos,y_pos+ i*50))

    """code to tell answer choices"""
    font = pygame.font.Font('SUSEMono-VariableFont_wght.ttf',18)
    lines = str(answers)[2:-2]
    lines = lines.split(", ")

    buttons = list()
    words = list()
    left = 1
    for i, line in enumerate(lines):
        if left == 1:
            buttons.append(buttonMaker(15,blue,"white",line,x_pos+50,(y_pos*2 - 70) + i*45,width=150,height=60))
            words.append(line)
            left = 0
        else: #right
            buttons.append(buttonMaker(15,blue,"white",line,x_pos+250,(y_pos*2-115) + i *45,width=150,height=60))
            words.append(line)
            left = 1
    return buttons, words

def is_int(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False



#input_rect = pygame.Rect(200,200,140,32)
count = 0
user_ans_list = list()
ml_ran = False
state = "" 

while True:
    events = pygame.event.get()
    for event in events:
        

        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if beginningScreen:

            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos): #white button is clicked
                print("Button Clicked!")
                beginningScreen = False

            set_background('Backgrounds/background1.jpeg')
            start_button = buttonMaker(40,"white",black,'Start',375-112.5,475,225,100)
        else:
            
            if count == 0:
                button_list,words_list = question_screen(count+1,question_list[count],answer_list[count],125,215)
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                for i, button in enumerate(button_list):
                    if button.collidepoint(event.pos):
                        user_ans = words_list[i]
                        user_ans_list.append(user_ans[3:])
                        count+=1
                        if count<= 5:
                            button_list,words_list = question_screen(count+1,question_list[count],answer_list[count],125,215)
                        else:
                            state = "results"
    pygame.display.update()

    if state == "results" and not ml_ran: #not ml_ran and 
        print(user_ans_list)
        ml_ran = True
        dtc(user_ans_list)
        