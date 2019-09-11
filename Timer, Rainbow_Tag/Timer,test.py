import time
import pygame
import snaps

loopinit=True
soundinit=True
looplength=25
pygame.mixer.init()

sound_ob=pygame.mixer.Sound('timer_sound1.wav')
sound_ob.play()
final_countdown=20# ;)
for var_1 in range(0,20):
    snaps.display_message(str(final_countdown))
    final_countdown=final_countdown-1
