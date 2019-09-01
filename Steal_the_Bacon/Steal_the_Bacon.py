# Steal the Bacon
# Trenton Rice 2019 01 16

import snaps
import pygame
import random
import time
import pygame
pygame.mixer.init()
num_max=int(input('Number of kids per team:   '))
snaps.setup(width=1350, height=670, title='STEAL THE BACON')
sound_ob=pygame.mixer.Sound('A-Tone_mod.wav')
snaps.get_key()
past_num=[0]
counter=0
while True:
    num_called=(random.randint(1, num_max))
    num_str=str(num_called)
    if counter == 0:
        past_num[0]=num_called
        key_code='n'
    else:
        past_num.append(num_called)
        run_check=past_num[counter] == past_num[counter-1] and past_num[counter] == past_num[counter-2]
        if run_check == True:
            snaps.display_message('oops')
            snaps.get_key()
            continue
    
    time.sleep(0.25)
    sound_ob.play()
    color_change_r=random.randint(0,255)
    color_change_g=random.randint(0,255)
    snaps.display_message('Number\n'+num_str, vert='bottom', horiz='center',size=250,color=(color_change_r,color_change_g,255))
    time.sleep(3)
    snaps.clear_display()
    counter=counter+1
    #add in keydown recognition
    advance = False
    while advance == False:
        event = pygame.event.wait()
        if event.type == 2:
         # Event 2 is keydown
            key_code = event.dict['unicode']

            if key_code == 'n':
                advance = True
            if key_code == 'e':
                snaps.display_message('Numbers called\n'+ str(past_num[:]), size=100, vert='top', horiz='center',color=(255,255,255))
                time.sleep(10)
                pygame.quit()
            else:
                snaps.display_message('wrong key')
    
    snaps.display_message('The Next Number is...',vert='bottom', horiz='center',size=250,color=(125,175,175))
    delay=random.randint(2,6)/3
    time.sleep(delay)
