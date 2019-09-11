#   Timer developed for use with Rainbow Tag
#   First user Teen group @ Gateway Baptist Church
#   Trenton Rice
#   Development start date: 190824
#   Release date:
#   Version 1.0

import time
import random
import pygame
import snaps
#import pdb

#pdb.set_trace()
pygame.mixer.init()
sound1=pygame.mixer.Sound('timer_sound1.wav')
sound2=pygame.mixer.Sound('timer_sound2.wav')
E_msg_time=2
snaps.setup(title='Custom Timer')
#The following loop checks to see if input is in mm:ss format
initialize_var = True
checker_var = True
int_check=True
input_validate=True
    
while initialize_var:
    
    while input_validate:
        c1=random.randint(0, 255)
        c2=random.randint(0, 255)
        c3=random.randint(0, 255)
        length_check=True
        format_check=True
        
        time_input=snaps.get_string('Enter timer length as integers. (ss or mm:ss)    ', size=40, margin=10, color=(c1,c2,c3), horiz='left', vert='bottom', cursor='_')
        time_array=str.split(time_input, ':')
        i=0
        
        while i < len(time_array):
            try:
                int(time_array[i])
                int_check = True
                i=i+1
            except ValueError:
                int_check=False
            if int_check == False:
                snaps.display_message ("ERROR\nPossible problems:\n Wrong format or Input wasn't an integer\nTry Again", size=40)
                time.sleep(E_msg_time)
                i=len(time_array)+1
        if int_check == True:
             input_validate = False

    while checker_var:
        input_validate = True

        if len(time_array)>2:
            length_check=False
            break
        if len(time_array)==1:   
            min_var=0;sec_var=int(time_array[0]);tot_time=sec_var
            if tot_time > 3600:
                length_check=False
            if sec_var >= 60:
                format_check = True
            else:
                format_check = False
                check_opt=1
            while format_check:
                if sec_var >= 60:
                    sec_var=sec_var-60
                    min_var=min_var+1
                    check_opt=2
                else:
                    break
            
        if len(time_array) == 2:
            check_opt=2
            min_var=int(time_array[0]);sec_var=int(time_array[1]);tot_time=(min_var*60)+sec_var
            if tot_time > 3600:
                length_check=False
            if sec_var >= 60:
                format_check = True
            else:
                format_check = False
            while format_check:
                if sec_var >= 60:
                    sec_var=sec_var-60
                    min_var=min_var+1
                else:
                    break

        if length_check == False:
            snaps.display_message('Error\nOnly accepts time less than one hour', size=40)
            time.sleep(E_msg_time)
        if length_check == True and check_opt == 1:
            user_check = snaps.get_string(str(sec_var)+'sec?\n(y/n)   ', cursor='_')
            init_message=str(sec_var-20)
        if length_check == True and check_opt == 2:
            user_check = snaps.get_string(str(min_var)+'min'+str(sec_var)+'sec?\n(y/n)   ', cursor='_')
            init_message=str(min_var)+'min'+str(sec_var-20)+'sec'
        if user_check != 'y' and user_check != 'n':
            continue
        if user_check == 'y':
            initialize_var=False
            break
        if user_check == 'n':
            break
Enter_timer=True
stored_time=tot_time
if tot_time>60:
    tot_time=tot_time-60
tot_time=tot_time-20
snaps.display_message(init_message)
time.sleep(tot_time)
sound2.play()
#while Enter_timer:
snaps.display_message('ONE\nMINUTE')
time.sleep(40)
sound1.play()
final_countdown=20# ;)
for var_1 in range(0,20):
    snaps.display_message(str(final_countdown))
    final_countdown=final_countdown-1
    time.sleep(1)
    
snaps.display_message('ta dah')
