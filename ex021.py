import playsound

playsound.playsound(r'C:\Users\Leandro\Downloads\pastoral.wav')


###################
import pygame
pygame.init()
pygame.mixer.music.load('pastoral.wav')
pygame.mixer.music.play()
pygame.event.wait()
################################














