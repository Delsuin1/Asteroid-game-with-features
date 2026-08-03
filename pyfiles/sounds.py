import pygame
from random import choice
background_music = "audio/asteroid_bgm.wav"
teleport_sound = pygame.mixer.Sound(choice(["audio/teleport.wav", "audio/teleport.wav"]))
destruction_sound = pygame.mixer.Sound(choice(["audio/explode.wav", "audio/explodemini.wav"]))
shot_path = [""]