from Actions import attack
import pygame
from Entities import weapons
from Main import window, boolean, colors

speed = 15
cube_x = 700
cube_y = 400
cube_width = 100
cube_height = 100
player_color = colors.green


class player:

    def __init__(self, speed, height, color, width, health, armor=0):   # innit method applies armor and a weapon to a player
        self.weapon_index = 0
        self.weapon = weapons.weapon_list[self.weapon_index]
        self.armor = armor
        self.speed = speed
        self.width = width
        self.height = height
        self.health = health
        self.color = color
        self.count = 5
        self.xp = 0

    def attack(self, weapon, enemy):       # attack method gives the ability to attack enemies
        attack.attack(weapon, enemy)


    def cube(self, x, y):
        pygame.draw.rect(window.window, self.color, [x, y, self.height, self.width])

    def take_damage(self, damage_taken):
        self.health -= damage_taken

    def die(self):
        boolean.dead = True

    def check_color(self):
        if self.count <= 0:
            self.color = player_color
            self.count = 1
        else:
            self.count -= 1
    def check_xp(self):
        if self.xp >= 1:
            self.weapon_index += 1
            self.weapon = weapons.weapon_list[self.weapon_index]

hero = player(10, cube_width, player_color, cube_height, 10)
