import pygame
import sys
import os

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
    ['Count Dooku', 'Darth Maul', 'Darth Vader', 'General Grievous', 'Palpatine', 'Wilhuff'],
    ['Episode I - The Phantom Menace', 'Episode II - Attack of the Clones', 'Episode III - Revenge of the Sith', 'Episode IV - A New Hope', 'Episode V - The Empire Strikes Back', 'Episode VI - Return of the Jedi'],
    ['Accross the Stars', 'Anakin vs. Obi-Wan', 'Imperial March', 'Star Wars (Main Theme)', 'The Throne Room'],
    ['Death Star', 'Millennium Falcon', 'Naboo Starfighter', 'TIE Fighter'],
    ['Alderaan', 'Dagobah', 'Endor', 'Naboo', 'Tatooine'],
    ['Battle Droid', 'C-3PO', 'Droideka', 'R2-D2']]

question_list = [
    " What is your favorite \n    Star Wars hero? \n (type number to answer)",
    'What is your favorite Star Wars villain?',
    'What is your favorite Star Wars Film?',
    'What is your favorite Star Wars soundtrack?',
    'What is your favorite Star Wars spaceship?',
    'What is your favorite planet in Star Wars?',
    'What is your favorite robot in Star Wars?']

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
            user_ans = ''
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(button_list):
                    if button.collidepoint(event.pos):
                        user_ans = words_list[i]
                        #user_ans_list.append(user_ans[3:])
                        count+=1
                    
                    if count<= 5:
                        button_list,words_list = question_screen(count+1,question_list[count],answer_list[count],125,215)
                    else:
                        state = "results"
            print(user_ans_list)

    



    pygame.display.update()

            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_BACKSPACE:
            #        user_text = user_text[:1]
            #    else:
            #        user_text += event.unicode
            
            #pygame.draw.rect(screen,color='white')


        #user_ans=-1
            #while user_ans not in range(1, len(categories_list[count])+1):
            #    print(question_screen(count+1,question_list[count],answer_list[count],125,215))
            #    if len(categories_list[count]) == 9:
            #        if event.type == pygame.KEYDOWN:
            #            if event.key == pygame.K_1: user_ans = 1
            #            if event.key == pygame.K_2: user_ans = 2
        
