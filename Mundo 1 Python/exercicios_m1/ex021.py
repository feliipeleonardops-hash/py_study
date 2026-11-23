
# TODO: Desafio 021 - Tocando um MP3: Criar um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play()
pygame.event.wait()
