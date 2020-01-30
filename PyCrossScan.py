#!/usr/bin/python3
# V.1.0.18 alpha 30-01-2020
# add Letter in Images  scr00.png,scr01.png etc
import codecs
import sys
import os
import csv

sys.path.insert(0, '../../')


from random import randrange
from Sprites_Buttons import Button, ButtonI, ButtonIL

import pygame

from pygame.locals import *
import pygameMenu


xx = pygame.init()
global screen
global main_menu
global clock
global txt_label
txt_label = "My Game 'Scanword&Crossword' alpha v.1.0.18 30-01-2020"
WINDOW_SIZE = (1000, 600)
#screen = pygame.display.set_mode(WINDOW_SIZE)


# -----------------------------------------------------------------------------
# Constants and global variables
# -----------------------------------------------------------------------------
ABOUT = ['pygameMenu {0}'.format(pygameMenu.__version__),
         'Author: @{0}'.format(pygameMenu.__author__),
         pygameMenu.locals.TEXT_NEWLINE,
         'Email: {0}'.format(pygameMenu.__email__)]
COLOR_BACKGROUND = (128, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255,0,0)

DIFFICULTY = ['EASY']
FPS = 33.0
MENU_BACKGROUND_COLOR = (122,122,122)
#WINDOW_SIZE = (800, 600)
WINDOW_MESS = (200, 100)


clock = None
main_menu = None
surface = None

# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------



def change_difficulty(value, difficulty):
    """
    Change difficulty of the game.

    :param value: Tuple containing the data of the selected object
    :type value: tuple
    :param difficulty: Optional parameter passed as argument to add_selector
    :type difficulty: basestring
    :return: None
    """
    selected, index = value
    print('Selected difficulty: "{0}" ({1}) at index {2}'.format(selected, difficulty, index))
    DIFFICULTY[0] = difficulty


def random_color():
    """
    Return random color.

    :return: Color tuple
    :rtype: tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def play_function(difficulty, font, test=False):
    """
    Main game function.

    :param difficulty: Difficulty of the game
    :type difficulty: basestring
    :param font: Pygame font
    :type font: pygame.font.FontType
    :param test: Test method, if true only one loop is allowed
    :type test: bool
    :return: None
    """
    assert isinstance(difficulty, (tuple, list))
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)



    font = pygame.font.Font(None, 25)
    fontP = pygame.font.Font(None, 25)
    if difficulty == 'EASY':
        nx = 0
        ny = 0
        image_array = []
        file_image = []
        fi = ''
        i = 0
        for i in range(0,11):
            if i<10:
                fi =  "iks0"+str(i)+".png"
                file_image.append(fi)
            else:
                fi = "iks"+str(i)+".png"
                file_image.append(fi)
            image_array.append(pygame.image.load(os.path.join('images',file_image[i])))

        image_arrayL = []
        file_imageL = []
        fi = ''
        i = 0
        for i in range(0,31):
            if i<10:
                fi =  "scr0"+str(i)+".png"
                file_imageL.append(fi)
            else:
                fi = "scr"+str(i)+".png"
                file_imageL.append(fi)
            image_arrayL.append(pygame.image.load(os.path.join('images/Letters',file_imageL[i])))

        text = ""
        kr = []
        rt = []
        def csv_dict_reader(file_obj):  # чтение файла csv
            reader = csv.DictReader(file_obj, delimiter=',')
            i = 0
            for line in reader:
                kr.append(line["shablon"])
 #               print("N=",i,": ",line["shablon"],"kr: ",kr[i]," len= ",len(kr[i]))
                r = i + 1
        with open("rshabl.csv") as f_obj:
            csv_dict_reader(f_obj)

        def csv_dict_reader(file_obj):  # чтение файла csv
            reader = csv.DictReader(file_obj, delimiter=',')
            i = 0
            for line in reader:
                rt.append(line["shablon"])
#                print("N=",i,": ",line["shablon"],"rt: ",rt[i]," len= ",len(rt[i]))
                i = i + 1
        if os.path.exists("rtext_current.csv"):
            with open("rtext_current.csv") as f_obj:
                csv_dict_reader(f_obj)
        else:
            with open("rtext.csv") as f_obj:
                csv_dict_reader(f_obj)

        def csv_dict_writer(path, fieldnames, data):
#        """
#        Writes a CSV file using DictWriter
#        """
            with open(path,"w") as out_file:
      #          out_file.write(codecs.BOM_UTF8)
                writer = csv.DictWriter(out_file, lineterminator='\r\n', delimiter=',', fieldnames=fieldnames)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
                out_file.close()

        def write_rtext():
            my_list = []
            data = []

            for row in range(0,len(rt)):
                data.append({"shablon":rt[row]})
            fieldnames = data[0]
            path = "rtext_current.csv"
            csv_dict_writer(path, fieldnames, data)

        mess = []
        def csv_dict_reader(file_obj):  # чтение файла csv
            reader = csv.DictReader(file_obj, delimiter=',')
            i = 0
            for line in reader:
                mess.append((line["message"],line["slovo"]))
                i = i + 1

        with open("rmess.csv") as f_obj:
            csv_dict_reader(f_obj)

        mapfrm = []
        def csv_dict_reader(file_obj):  # чтение файла csv
            reader = csv.DictReader(file_obj, delimiter=',')
            i = 0
            for line in reader:
                mapfrm.append((line["sh1"],line["sh2"],line["sh3"],line["sh4"]))
                i = i + 1

        with open("mapfrm.csv") as f_obj:
            csv_dict_reader(f_obj)

        mass_rul = []
        def csv_dict_reader(file_obj):  # чтение файла csv
            reader = csv.DictReader(file_obj, delimiter=',')
            i = 0
            for line in reader:
                mass_rul.append((line["n1"],line["n2"],line["n3"]))
                i = i + 1
            #    print("i= ",i,"n1x= ",line["n1"]," n2y= ",line["n2"]," n3= ",line["n3"])
        with open("rules.csv") as f_obj:
            csv_dict_reader(f_obj)

        mass_abc = []
        def csv_dict_reader(file_obj):  # чтение файла csv
            reader = csv.DictReader(file_obj, delimiter=',')
            i = 0
            for line in reader:
                mass_abc.append((line["letter"]))
                i = i + 1
           #     print("i= ",i,"letter= ",line["letter"])
        with open("Abc.csv") as f_obj:
            csv_dict_reader(f_obj)

        def input_letter(kx,ky,logic_lett, logbit):
             global nx
             global ny
             if logic_lett:
           #      print("Истина")

                 lett = '_'
                 txt = "отладка ввода буквы"
            # nx, ny позиции в таблице по горизонали и вертикали
                 if not logbit :
                     nx=kx//20 - 1  # поправки -1
                     ny=ky//20 - 1  # с учетом оступов на 20  слева и сверху
            #         print("txt= ",txt,"к-ты: ",nx,ny)
                 else:
                     n2x=kx//20 - 1  # поправки -1
                     #rt[nx].replace('_',mass_abc[n2x])
                     rtnew1=rt[ny][0:nx]
             #        print("rtnew1= ",rtnew1)
                     rtnew2=rt[ny][nx+1:]
              #       print("rtnew2= ",rtnew2)
                     rtnew =rtnew1+mass_abc[n2x]+rtnew2
               #      print("rtnew= ",rtnew)
                     rt[ny] = rtnew
                #     print("rt[ny]= ",rt[ny])
                 #    print("Текущий шаблон ",rt)
                     reload_abc(ny,nx)
             else:
                 print("Повторите ввод")
                 logic_lett = True

        # загрузка спрайта стрелок
        def load_Isprite(ni,nj,nks):
            mprm = mapfrm[nks][2]
            mp =int(mprm)
            filename = file_image[mp]

            p1 = int(mass_rul[mp][0]) # смещение по х
            p2 = int(mass_rul[mp][1]) # смещение по у
            spritesImg.add(ButtonI(pygame.Color('dodgerblue2'),
                                   pygame.Color('green'),
                                   pygame.Rect(20+p1*20+nj*20,20+p2*20+ni*20, 20, 20),
                                   lambda b: print(f"Button '{b.text}' was clicked"),
                                   "I2",
                                   pygame.Color('black'),
                                   filename))
        # загрузка  спрайта букв
        def load_ILsprite(ni,nj,nks):
            filename = file_imageL[nks]

            spritesLetters.add(ButtonIL(pygame.Color('dodgerblue2'),
                                   pygame.Color('green'),
                                   pygame.Rect(20+nks*20,520, 20, 20),
                                   lambda b: print(f"Button '{b.text}' was clicked"),
                                   mass_abc[nks][0],
                                   pygame.Color('black'),
                                   filename))
        def reload_abc(i,j):   # выяснить как удалить старый спрайт
            sprites.add(Button(pygame.Color('green'),
                               pygame.Color(128,128,128),
                               pygame.Rect(22+j*20,22+i*20, 16, 16),
                               lambda b: print(f"Button '{b.text}' was clicked"),
                               rt[i][j],
                               pygame.Color('black')))


        # загрузка спрайта подсказок
        def load_sprite(vpos,vtxt):
            ruby = Button(pygame.Color('dodgerblue2'),
                          pygame.Color('green'),
                          pygame.Rect(vpos[0],vpos[1], 300, 25),
                          lambda b: print(f"Button '{b.text}' was clicked"),
                          vtxt,
                          pygame.Color('black'))

            spritesTmp.add(ruby)
            spritesOne.draw(screen)
            sprites.draw(screen)
            spritesMsg.draw(screen)
            spritesImg.draw(screen)
            spritesTmp.draw(screen)
            spritesLetters.draw(screen)
            pygame.display.update()
      #       print(spritesTmp.sprites())
            # pygame.display.flip()
            pygame.time.delay(1200)
            spritesTmp.remove(ruby)
            return None

        # функция вызываемая из спрайтов для вывода
        # контекстной подсказки к блокам помеченным "?"
        def print_sprite(kx,ky,vks,vv):
            nx = 0
            ny = 0
            pos = pygame.mouse.get_pos()
            # nx, ny позиции в таблице по горизонали и вертикали
            nx=pos[0]//20 - 1  # поправки -1
            ny=pos[1]//20 - 1  # с учетом оступов на 20  слева и сверху
            nomvopros = 0
            m = 0
            for m in range(0,len(msg_list)):
                txt = ' тест = не найдено'
                if (msg_list[m][0] == (nx,ny)) and (vv == 0):
       #             print("vks= "+str(vks)+" 0= "+str(vv))
                    print("Координаты: ",msg_list[m][0][0],msg_list[m][0][1])
                    nomvopros = m
                    txt = mess[m][0]
                    load_sprite(pos,txt)
                    return None
                if (msg_list[m][0] == (nx,ny)) and (vv == 1):
        #            print("vks= "+str(vks)+" 1= "+str(vv))
                    print("Верхняя ячейка")
                    nomvopros = m
                    txt = mess[m][0]
                    load_sprite(pos,txt)
                    return None
                if (msg_list[m][0] == (nx,ny)) and (vv == 2):
                    print("vks= "+str(vks)+" 2= "+str(vv))
                    print("Нижняя ячейка")
                    txt = mess[m+1][0]
                    load_sprite(pos,txt)
                    return None
            return None

        message =""
        text = ''
        font = pygame.font.SysFont('comicsans', 16)
        f = font.render("Разгадай сканворд.",True,BLACK)
        textA = font.render("Режим разработки и тестирования",True,PINK)
        textQ = font.render("?",True,PINK)
        textP = font.render(message,True,GREEN)
        text = font.render(text,True,BLACK)
# Вывести сделанную картинку на экран в точке (250, 250)

        spritesOne = pygame.sprite.Group()
        sprites = pygame.sprite.Group()
        spritesMsg = pygame.sprite.Group()
        spritesTmp = pygame.sprite.Group()
        spritesImg = pygame.sprite.Group()
        spritesLetters = pygame.sprite.Group()
        spritesMenu = pygame.sprite.Group()
        main_background()
        spritesOne.add(Button(pygame.Color('dodgerblue2'),
                                       pygame.Color('lightskyblue3'),
                                       pygame.Rect(15,15,450,470),
                                       lambda b: print(f"Button '{b.text}' was clicked"),
                                       '',
                                       pygame.Color('black')))
        #mxi = 22
        #myj = 22
        spritesMenu.add(Button(pygame.Color('GREEN'),
                                       pygame.Color('BLUE'),
                                       pygame.Rect(470,15,250,25),
                                       lambda a: write_rtext(),
                                       'Сохранение введенных данных',
                                       pygame.Color('black')))

        ks  = 0
        msg_list = []
        btn_array = []
        i = 0
        j = 0
        m = 0
        for i in range(0,23):
#            stroka = ''
            for j in range(0,22):
  #              stroka = stroka + kr[i][j]
                if kr[i][j] == "1":
                   # mxi = 22 + i * 20
                    #myj = 22 + j * 20
                    if rt[i][j] == '_':
                        sprites.add(Button(pygame.Color('blue'),
                                           pygame.Color(255,255,255),
                                           pygame.Rect(22+j*20,22+i*20, 16, 16),
                                           lambda b: print(f"Button '{b.text}' was clicked"),
                                           rt[i][j],
                                           pygame.Color('blue')))
                    else:
                        reload_abc(i,j)
                    m = m + 1 # номер ячейки в списке
                else:
                    if kr[i][j] == "?":
                        msg_list.append([(j,i),ks])
                        load_Isprite(i,j,ks)
                        btn_array.append(Button(pygame.Color(0+ks,125,125),
                                                pygame.Color('YELLOW'),
                                                pygame.Rect(22+j*20,22+i*20, 16, 16),
                                                lambda a: print_sprite(i,j,ks,0),
                                                rt[i][j],
                                                pygame.Color('black')))

                        ks = ks + 1
                    else:
                        if kr[i][j] == "2":    # вариант для двойной ячейки
                            msg_list.append([(j,i),ks])
                            load_Isprite(i,j,ks)
                            btn_array.append(Button(pygame.Color(0+ks,125,125),
                                                    pygame.Color('blue'),
                                                    pygame.Rect(22+j*20,22+i*20,16, 7),
                                                    lambda a: print_sprite(i,j,ks,1),
                                                    "?",
                                                    pygame.Color('black')))
                            ks = ks + 1
                            msg_list.append([(j,i),ks])
                            load_Isprite(i,j,ks)
                            btn_array.append(Button(pygame.Color(0+ks,125,125),
                                                    pygame.Color('blue'),
                                                    pygame.Rect(22+j*20,31+i*20,16, 7),
                                                    lambda a: print_sprite(i,j,ks,2),
                                                    "?",
                                                    pygame.Color('black')))
                            ks = ks + 1
 #           print(stroka)
#        print(msg_list)
        for i in range(0,len(btn_array)):
            spritesMsg.add(btn_array[i])

        for i in range(0,31):
            load_ILsprite(0,0,i)


        pos = pygame.mouse.get_pos()

       # btnI = ButtonI(pos,'images/iks09.png')
#        pygame.display.update()
        spritesOne.draw(screen)
        sprites.draw(screen)
        spritesMsg.draw(screen)
        spritesImg.draw(screen)
        spritesTmp.draw(screen)
        spritesLetters.draw(screen)
        spritesMenu.draw(screen)

     #   for j in range(0,len(mapfrm)):      # прорисовка стрелок
     #       if mapfrm[j][2] == "09" :
     #           screen.blit(image_array[9], (40 + int(mapfrm[j][1])*20,20 + 20*int(mapfrm[j][0])))
     #       if mapfrm[j][2] == "08":
     #           screen.blit(image_array[8], (20 + int(mapfrm[j][1])*20,40 + 20*int(mapfrm[j][0])))
        pos = pygame.mouse.get_pos()
        screen.blit(textA, [500,20])
   #     screen.blit(text, [25,42])
        screen.blit(f, [500,56])
        pygame.display.flip()
     #   pygame.display.update()

        textP = font.render(message,True,BLACK)
        screen.blit(textP, [500,1+8*i])
        pygame.time.delay(33)
        pygame.display.update()
        pygame.display.flip()

        #main_menu.mainloop(events, disable_loop=test)

    elif difficulty == 'СРЕДНИЙ':
        f = font.render('Playing as a kid (medium)', 1, WHITE)
    elif difficulty == 'СЛОЖНЫЙ':
        f = font.render('Playing as a champion (hard)', 1, WHITE)
    else:
        raise Exception('Unknown difficulty {0}'.format(difficulty))

    # Draw random color and text
    bg_color = random_color()
    f_width = f.get_size()[0]

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
        clock.tick(1)

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN :
               print("нажата кнопка # ", e.button," координаты ", e.pos)
               if (e.pos[0]>19 and e.pos[0]<461) and (e.pos[1]>19 and e.pos[1]<481):
                   input_letter(e.pos[0],e.pos[1],True, False)
                   obrabotka = True
               if (e.pos[0]>19 and e.pos[0]<661) and (e.pos[1]>519 and e.pos[1]<541):
                   if obrabotka == True :
                       input_letter(e.pos[0],e.pos[1],True, True)
                       obrabotka = False

            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 317
                    return

        # Pass events to main_menu


        # Continue playing
        screen.fill(GRAY)
        spritesOne.update(events)
        sprites.update(events)     # ????? ЁЁЁЁЁ
        spritesMsg.update(events)
        spritesImg.update(events)
        spritesTmp.update(events)
        spritesLetters.update(events)
        spritesMenu.update(events)
        spritesOne.draw(screen)
        sprites.draw(screen)
        spritesMsg.draw(screen)
        spritesImg.draw(screen)
        spritesTmp.draw(screen)
        spritesLetters.draw(screen)
        spritesMenu.draw(screen)

        pos = pygame.mouse.get_pos()
       # btnI = ButtonI(pos,"images/iks09.png")
        pygame.display.flip()     #  1
        pygame.display.update()   #  2
   #     screen.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))


        main_menu.mainloop(events)
        # If test returns
        if test:
            break


def main_background():
    """
    Function used by menus, draw on background while menu is active.

    :return: None
    """
    global screen
#    screen.fill(COLOR_BACKGROUND)
    screen.fill(GRAY)
def main(test=False):
    """
    Main program.

    :param test: Indicate function is being tested
    :type test: bool
    :return: None
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global clock
    global main_menu
    global screen
    # -------------------------------------------------------------------------
    # Init pygame
    # -------------------------------------------------------------------------
#    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Create pygame screen and objects
    screen = pygame.display.set_mode(WINDOW_SIZE)
#    pygame.display.set_caption('Example - Game Selector')
    pygame.display.set_caption(txt_label)
    font = pygame.font.Font(None, 25)
    fontP = pygame.font.Font(None, 12)
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus
    # -------------------------------------------------------------------------

    # Play menu
    play_menu = pygameMenu.Menu(screen,
                                bgfun=main_background,
                                color_selected=WHITE,
                                font=pygameMenu.font.FONT_PT_SERIF,
                                font_color=BLACK,
                                font_size=20,
                                menu_alpha=40,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.7),
                                menu_width=int(WINDOW_SIZE[0] * 0.9),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Меню игры "Сканворды"',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    play_submenu = pygameMenu.Menu(screen,
                                   bgfun=main_background,
                                   color_selected=WHITE,
                                   font=pygameMenu.font.FONT_PT_SERIF,
                                   font_color=BLACK,
                                   font_size=12,
                                   menu_alpha=30,
                                   menu_color=MENU_BACKGROUND_COLOR,
                                   menu_height=int(WINDOW_SIZE[1] * 0.5),
                                   menu_width=int(WINDOW_SIZE[0] * 0.7),
                                   option_shadow=False,
                                   title='Задания',
                                   window_height=WINDOW_SIZE[1],
                                   window_width=WINDOW_SIZE[0]
                                   )
    #for m in CROSS:
        #play_menu.add_line(m)
   # play_submenu.add_line(pygameMenu.locals.TEXT_NEWLINE)
            #st = str(i)
           # message = st+" - "+mess[i]
           # play_submenu.add_selector('Выбор: ', [(message, NULL)])
    #play_submenu.add_option('Вернуться', pygameMenu.events.BACK)

    play_menu.add_option('Старт',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_function,
                         DIFFICULTY,
                         pygame.font.Font(pygameMenu.font.FONT_FRANCHISE, 14))
    play_menu.add_selector('Выбор: ',
                           [('1 - Легкие уровни ', 'EASY'),
                            ('2 - Средние уровни', 'MEDIUM'),
                            ('3 - Сложные уровни', 'HARD')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')
    play_menu.add_option('Другие меню          ', play_submenu)
    play_menu.add_option('Воврат в главное меню', pygameMenu.events.BACK)

    # About menu
    about_menu = pygameMenu.TextMenu(screen,
                                     bgfun=main_background,
                                     color_selected=WHITE,
                                     font=pygameMenu.font.FONT_PT_SERIF,
                                     font_color=BLACK,
                                     font_size_title=14,
                                     font_title=pygameMenu.font.FONT_8BIT,
                                     menu_color=MENU_BACKGROUND_COLOR,
                                     menu_color_title=WHITE,
                                     menu_height=int(WINDOW_SIZE[1] * 0.6),
                                     menu_width=int(WINDOW_SIZE[0] * 0.6),
                                     onclose=pygameMenu.events.DISABLE_CLOSE,
                                     option_shadow=False,
                                     text_color=BLACK,
                                     text_fontsize=14,
                                     title='О нас',
                                     window_height=WINDOW_SIZE[1],
                                     window_width=WINDOW_SIZE[0]
                                     )
    for m in ABOUT:
        about_menu.add_line(m)
    about_menu.add_line(pygameMenu.locals.TEXT_NEWLINE)
    about_menu.add_option('Возврат в главное меню', pygameMenu.events.BACK)

    # Main menu
    main_menu = pygameMenu.Menu(screen,
                                bgfun=main_background,
                                color_selected=WHITE,
                                font=pygameMenu.font.FONT_PT_SERIF,
                                font_color=BLACK,
                                font_size=14,
                                menu_alpha=30,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.6),
                                menu_width=int(WINDOW_SIZE[0] * 0.6),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Главное меню',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    main_menu.add_option('Сканворды', play_menu)
    main_menu.add_option('О нас', about_menu)
    main_menu.add_option('Выход', pygameMenu.events.EXIT)

    # Configure main menu
    main_menu.set_fps(FPS)
    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
       # update all sprites
    # it now doesn't matter if we have one or 200 Buttons
    #    sprites.update(events)
    # clear the screen
#        screen.fill(pygame.Color('white'))
    # draw all sprites/Buttons
        #sprites.draw(screen)
        #spritesTmp.draw(screen)
        pygame.display.flip()
        pygame.display.update()
    # limit framerate to 60 FPS
         # Main menu
        pygame.display.flip()
        main_menu.mainloop(events, disable_loop=test)

        # Flip screen


        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()
