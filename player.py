import attack
import pygame
import window # imports attack to the player can attack\
import main
speed = 5
class player:

    def __init__(self, speed, height, width, armor=0, weapon=0):    # innit method applies armor and a weapon to a player
        self.weapon = weapon
        self.armor = armor
        self.speed = speed
        self.width = width
        self.height = height

    def attack(self, weapon, enemy):       # attack method gives the ability to attack enemies
        attack.attack(weapon, enemy)

    def cube(self, x, y):
        pygame.draw.rect(window.window, (0, 255, 0), [x, y, self.height, self.width])