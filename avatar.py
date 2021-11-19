import random
import pygame
from pygame.math import Vector2

class Avatar:
    def __init__(self):
        self.position = Vector2(700,425)
        self.rayon = 10
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 100
        self.vitesse = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxacc = 0.5
        self.l0 = 10
        self.k = 0.001
        self.vitessmin = 50
        self.vitessmax = 500
        self.taillemax = 300

    def show(self,screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)
