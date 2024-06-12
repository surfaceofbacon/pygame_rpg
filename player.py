import attack
import pygame
import window
import colors
speed = 15
cube_x = 700
cube_y = 400
cube_width = 100
cube_height = 100
player_color = colors.green

class player:

    def __init__(self, speed, height, width, armor=0, weapon=0):    # innit method applies armor and a weapon to a player
        self.weapon = weapon
        self.armor = armor
        self.speed = speed
        self.width = width
        self.height = height

    def attack(self, weapon, enemy):       # attack method gives the ability to attack enemies
        attack.attack(weapon, enemy)

    def cube(self, x, y, color):
        pygame.draw.rect(window.window, color, [x, y, self.height, self.width])

hero = player(10, cube_width, cube_height)
