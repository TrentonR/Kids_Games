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

#The following loop checks to see if input is in mm:ss integer format has a slot for expansion into hhmmss format
initialize_var = True
checker_var = True
int_check=True
input_validate=True

while initialize_var:
    while input_validate:
        color1=random.randint(0, 255)
        color2=random.randint(0, 255)
        color3=random.randint(0, 255)
        snaps.setup(title='Custom Timer')
        time_input=snaps.get_string('Enter timer length as integers. (ss or mm:ss)    ', size=40, margin=10, color=(color1,color2,color3),
                         horiz='left', vert='bottom', cursor='_')
        time_array=str.split(time_input, ':')
        
        for i in range(0, len(time_array)):
            try:
                integer_check=int(time_array[i])
                int_check = True
            except ValueError:
                int_check=False
        if int_check == False:
            snaps.display_message ("ERROR  Possible problems:\n Wrong format or Input wasn't an integer\nTry Again", size=40)
            time.sleep(3)
            continue
        if int_check == True:
            break

        
    while checker_var:
        if len(time_array)>2:
            snaps.display_message('Invalid Entry')
            time.sleep(2)
            break
        if len(time_array)==1:
            check_var = snaps.get_string(time_array[0]+'sec?\n(y/n)   ', cursor='_')
            sec_var=int(time_array[0]);tot_time=sec_var
        if len(time_array)==2:
            check_var = snaps.get_string(time_array[0]+'min '+time_array[1]+'sec?\n(y/n)   ', cursor='_')
            min_var=int(time_array[0])*60;sec_var=int(time_array[1]);tot_time=min_var+sec_var
        
        if check_var != 'y' and check_var != 'n':
            continue
        if check_var == 'y':
            initialize_var=False
            break
        if check_var == 'n':
            break

snaps.display_message('ta dah')
