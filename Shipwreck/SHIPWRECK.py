# 20190114 Trenton Rice
# Shipwreck for AWANA;

import snaps
import time
import random
import pygame

counter_max=int(input('Max Number of Directions (Min is 2):   '))
#min_delay=int(input('Min Delay:   '))
#max_delay=int(input('Max Delay:   '))

background='background.jpg'

snaps.setup(width=1280, height=720, title='Shipwreck')
snaps.display_image(background)

snaps.get_string('To Begin Press  ', cursor='ENTER')
snaps.display_image(background) 
pygame.mixer.Sound.play(pygame.mixer.Sound('Pacman_Introduction_Music.wav'))
time.sleep(4.5)
prev_command=0
loopy=True
tone=pygame.mixer.Sound('A-Tone.wav')
bell=pygame.mixer.Sound('Ship_bell.wav')
crash=pygame.mixer.Sound('Crash_Large.wav')
while loopy:
    counter=0
    command_num=random.randint(2, counter_max)

    while counter <= command_num:
        command=random.randint(1, 6)
        pygame.mixer.init()
        
        if prev_command == command:
            continue
        if command == 1:
            tone.play(loops=1)
            snaps.display_message('PORT',color=(0,0,255),vert='bottom')
        if command == 2:
            tone.play(loops=1)
            snaps.display_message('BOW',color=(255,0,0),vert='bottom')
        if command == 3:
            bell.play()
            snaps.display_message('MAN OVERBOARD',color=(255,255,255),vert='bottom')
        if command == 4:
            tone.play(loops=1)
            snaps.display_message('STARBOARD',color=(255,255,0),vert='bottom')
        if command == 5:
            snaps.display_message('SHIPWRECK',color=(10,10,10),vert='bottom')
            crash.play()
            time.sleep(1)
            crash.fadeout(800)
        if command == 6:
            tone.play(loops=1)
            snaps.display_message('STERN',color=(0,255,0),vert='bottom')
        counter=counter+1
        prev_command=command
        delay=random.randint(5, 10)
        time.sleep(delay/8+1)
        time_var=(0.6*delay)+1
        snaps.display_image(background) 
        time.sleep(time_var)

    loop_check=snaps.get_string('Start Next Round:  ', cursor='?')
    snaps.display_image(background)
    if loop_check != '':
        snaps.display_image('Looney_themed_The_End.jpg')
        time.sleep(4)
        break
