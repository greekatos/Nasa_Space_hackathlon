from glob import glob
import pygame_gui
from player import Player
from logos import Star_1_logo, Star_2_logo, Star_3_logo, Star_4_logo, Star_5_logo, Star_6_logo
from logos import Quiz_logo, About_us_logo, Video_logo, About_us_info, Video_info
from logos import Presentation_1,Presentation_2,Presentation_3,Presentation_4,Presentation_5,Presentation_6
import os
import sys
import pygame, time
import math 
import my_main
SCREEN_SIZE = (1200, 720)

def draw_subtitles():
    font = pygame.font.Font(None, 30)
    text_star_1 = font.render('Cepheids', True, "white")
    textRect_1 = text_star_1.get_rect(center=(600, 130))

    text_star_2 = font.render('Light Curves', True, "white")
    textRect_2 = text_star_2.get_rect(center=(900, 300))

    text_star_3 = font.render('Shine bright...', True, "white")
    textRect_3 = text_star_3.get_rect(center=(900, 520))

    text_star_4 = font.render('Twinkle Twinkle!', True, "white")
    textRect_4 = text_star_4.get_rect(center=(600, 710))

    text_star_5 = font.render('Unique Stars', True, "white")
    textRect_5 = text_star_5.get_rect(center=(300, 520))

    text_star_6 = font.render('Cataclysmic Variables', True, "white")
    textRect_6 = text_star_6.get_rect(center=(300, 290))

    window.blit(text_star_1, textRect_1)
    window.blit(text_star_2, textRect_2)
    window.blit(text_star_3, textRect_3)
    window.blit(text_star_4, textRect_4)
    window.blit(text_star_5, textRect_5)
    window.blit(text_star_6, textRect_6)

def event_listener():

    global key_pressed_is, info_elem, esc_elem, test_or_info_opened, star_bool
    key_pressed_is = pygame.key.get_pressed()

    #For quiting and keyboard inputs for movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move Player depending the input    
    if key_pressed_is[pygame.K_UP]:
        player.move_Up()
    if key_pressed_is[pygame.K_DOWN]:
        player.move_Down()
    if key_pressed_is[pygame.K_LEFT]:
        player.move_Left()
    if key_pressed_is[pygame.K_RIGHT]:
        player.move_Right()
    if key_pressed_is[pygame.K_w]:
        player.move_Up()
        #player.move_forward()
    if key_pressed_is[pygame.K_s]:
        player.move_Down()
        #player.move_backward()     
    if key_pressed_is[pygame.K_d]:
        player.move_Right()
        #player.rotate_right()
    if key_pressed_is[pygame.K_a]:
        player.move_Left()        
        #player.rotate_left()  
    if key_pressed_is[pygame.K_ESCAPE]:
        info_elem.visible = 0
        esc_elem.visible = 0
        test_or_info_opened = False
        star_bool = False
    
def collisions():
    
    global test_or_info_opened,elem,info_elem,esc_elem,star_index,star_bool

    touching_at_least_one_star = False

    if (player.rect.colliderect(stars_1)):
        touching_at_least_one_star = True
        if key_pressed_is[pygame.K_SPACE]:
            star_index = 0 # stars_1
            star_bool = True
            elem.visible = 0
            info_elem.visible = 1
            esc_elem.visible = 1
            test_or_info_opened = True

    if (player.rect.colliderect(stars_2)):
        touching_at_least_one_star = True
        if key_pressed_is[pygame.K_SPACE]:
            star_index = 1 # stars_2
            star_bool = True
            elem.visible = 0
            info_elem.visible = 1
            esc_elem.visible = 1
            test_or_info_opened = True

    if (player.rect.colliderect(stars_3)):
        touching_at_least_one_star = True
        if key_pressed_is[pygame.K_SPACE]:
            star_index = 2 # stars_3
            star_bool = True
            elem.visible = 0
            info_elem.visible = 1
            esc_elem.visible = 1
            test_or_info_opened = True

    if (player.rect.colliderect(stars_4)):
        touching_at_least_one_star = True
        if key_pressed_is[pygame.K_SPACE]:
            star_index = 3 # stars_4
            star_bool = True
            elem.visible = 0
            info_elem.visible = 1
            esc_elem.visible = 1
            test_or_info_opened = True
    
    if (player.rect.colliderect(stars_5)):
        touching_at_least_one_star = True
        if key_pressed_is[pygame.K_SPACE]:
            star_index = 4 # stars_5
            star_bool = True
            elem.visible = 0
            info_elem.visible = 1
            esc_elem.visible = 1
            test_or_info_opened = True

    if (player.rect.colliderect(stars_6)):
        touching_at_least_one_star = True
        if key_pressed_is[pygame.K_SPACE]:
            star_index = 5 # stars_6
            star_bool = True
            elem.visible = 0
            info_elem.visible = 1
            esc_elem.visible = 1
            test_or_info_opened = True

    if (player.rect.colliderect(about_us_logo)):
        touching_at_least_one_star = True
        if key_pressed_is[pygame.K_SPACE]:
            star_index = 6 # About us
            star_bool = True
            elem.visible = 0
            info_elem.visible = 1
            esc_elem.visible = 1
            test_or_info_opened = True

    if (player.rect.colliderect(quiz_logo)):
        touching_at_least_one_star = True
        if key_pressed_is[pygame.K_SPACE]:
            star_index = 7 # quiz
            star_bool = True
            elem.visible = 0
            #info_elem.visible = 0
            #esc_elem.visible = 0
            #test_or_info_opened = False
    
    if (player.rect.colliderect(video_logo)):
        touching_at_least_one_star = True
        if key_pressed_is[pygame.K_SPACE]:
            star_index = 8 # video
            star_bool = True
            elem.visible = 0
            info_elem.visible = 1
            esc_elem.visible = 1
            test_or_info_opened = True     

    if not test_or_info_opened and touching_at_least_one_star:
        touching_at_least_one_star = False
        elem.visible = 1
        info_elem.visible = 0
        esc_elem.visible = 0
    else:
        elem.visible = 0
    
def draw_presentations():
    
    global star_bool,star_index,  one_time_draw

    if(star_bool == True):
        if(star_index == 0):
            presentation_1 = Presentation_1(600,370)
            sprite_list_presentation = pygame.sprite.Group()
            sprite_list_presentation.add(presentation_1)
            sprite_list_presentation.draw(window)
        elif(star_index == 1):
            presentation_2 = Presentation_2(600,370)
            sprite_list_presentation = pygame.sprite.Group()
            sprite_list_presentation.add(presentation_2)
            sprite_list_presentation.draw(window)
        elif(star_index == 2):
            presentation_3 = Presentation_3(600,370)
            sprite_list_presentation = pygame.sprite.Group()
            sprite_list_presentation.add(presentation_3)
            sprite_list_presentation.draw(window)
        elif(star_index == 3):
            presentation_4 = Presentation_4(600,370)
            sprite_list_presentation = pygame.sprite.Group()
            sprite_list_presentation.add(presentation_4)
            sprite_list_presentation.draw(window)
        elif(star_index == 4):
            presentation_5 = Presentation_5(600,370)
            sprite_list_presentation = pygame.sprite.Group()
            sprite_list_presentation.add(presentation_5)
            sprite_list_presentation.draw(window)
        elif(star_index == 5):
            presentation_6 = Presentation_6(600,370)
            sprite_list_presentation = pygame.sprite.Group()
            sprite_list_presentation.add(presentation_6)
            sprite_list_presentation.draw(window)
        elif(star_index == 6):
            about_us_info = About_us_info(600,370) # about ut
            sprite_list_presentation = pygame.sprite.Group()
            sprite_list_presentation.add(about_us_info)
            sprite_list_presentation.draw(window)
        elif(star_index == 7) :
            my_main.custom_main()
            star_index = 800

            

        elif(star_index == 8):
            video_info = Video_info(600,370) # video
            sprite_list_presentation = pygame.sprite.Group()
            sprite_list_presentation.add(video_info)
            sprite_list_presentation.draw(window)
    

global star_bool
star_bool= False


def main():

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    global CAPTION 
    CAPTION = "Nasa Space apps"
    global test_or_info_opened
    test_or_info_opened = False
    pygame.display.set_caption(CAPTION)
    global window
    window = pygame.display.set_mode(SCREEN_SIZE)
    global clock
    clock = pygame.time.Clock()


    global manager
    manager = pygame_gui.UIManager(SCREEN_SIZE)

    global fps
    fps = 180



    global player_velocity
    player_velocity = 150 #cmeters / second #<----------------------------------------------------------------------
    
    # Create walls and target objects
    global player, quiz_logo,about_us_logo, video_logo,stars_1,stars_2,stars_3,stars_4,stars_5,stars_6
    
    stars_1 = Star_1_logo(600, 70)
    stars_2 = Star_2_logo(900, 240)
    stars_3 = Star_3_logo(900, 460)
    stars_4 = Star_4_logo(600, 650)
    stars_5 = Star_5_logo(300, 460)
    stars_6 = Star_6_logo(300, 240)
    
    quiz_logo = Quiz_logo(1110,640)
    about_us_logo = About_us_logo(1110,80)
    video_logo = Video_logo(90,80)

    player = Player()

    global elem,info_elem, esc_elem
    elem = pygame_gui.elements.UITextBox("<b>PLEASE PRESS SPACE FOR LANDING</b>", manager=manager, visible=0,
                                     relative_rect=pygame.Rect((0, SCREEN_SIZE[1]*11/12), (SCREEN_SIZE[0]/4, SCREEN_SIZE[1])))
    

    info_elem = pygame_gui.elements.UITextBox(
        "", manager=manager,visible=0, relative_rect=pygame.Rect((50, 50), (1100, 620)))
    
    esc_elem = pygame_gui.elements.UITextBox(
        "<b>YOU MAY PRESS ESC TO LAUNCH </b>", manager=manager,visible=0, relative_rect=pygame.Rect((0, SCREEN_SIZE[1]*45/48), (SCREEN_SIZE[0]/4, SCREEN_SIZE[1])))
    
    global background_img
    background_img = pygame.image.load('Images/background.jpg')
    background_img = pygame.transform.scale(background_img,(1200,720))

    # Variables in display_fps()
    global delta, prev_time 
    delta = 1
    prev_time = time.time()
    
    global main_loop_bool,sprite_list_player
    main_loop_bool = True
    sprite_list = pygame.sprite.Group()
    sprite_list_player = pygame.sprite.Group()
    

    sprite_list.add(stars_1)
    sprite_list.add(stars_2)
    sprite_list.add(stars_3)
    sprite_list.add(stars_4)
    sprite_list.add(stars_5)
    sprite_list.add(stars_6)

    sprite_list.add(quiz_logo)
    sprite_list.add(about_us_logo)
    sprite_list.add(video_logo)
    sprite_list_player.add(player)
    
    global one_time_draw

    while main_loop_bool:
        
        time_delta = clock.tick(60)/1000.0
        window.blit(background_img, (0, 0))
        event_listener()
        sprite_list.draw(window)
        sprite_list_player.draw(window)
        draw_subtitles()
        collisions()
        
        manager.update(time_delta)
        manager.draw_ui(window)
        draw_presentations()
        pygame.display.update()
        

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    