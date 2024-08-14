import pygame
import weapons
from Entities import player
from Main import window, colors
import math
bullets = []
bullet_position = []
class Weapon:    # creates weapon class

    def __init__(self, modifier, damage, crit_chance, range):  # assigns modifier, damage, and crit_chance to
        # the instance of a weapon
        self.modifier = modifier
        self.damage = damage
        self.crit_chance = crit_chance
        self.range = range


iron_sword = Weapon(3, 5, 3, 150)    # creates an instance of a weapon and assigns it to a iron sword


class Bullet:

    def __init__(self, player_position: tuple):
        self.player_position = player_position
        self.speed = 10
        self.x_distance = (bullet_position[0][0] - self.player_position[0])
        self.y_distance = (bullet_position[0][1] - self.player_position[1])
        self.angle = math.atan(self.y_distance / self.x_distance)
        if self.x_distance > 0:
            self.angle += math.pi
        print(player_position)

    def draw(self):
        rectangle = (bullet_position[0][0], bullet_position[0][1], 10, 10)
        pygame.draw.rect(window.window, colors.black, rectangle)

    def move_bullet(self):
        bullet_position[0][0] += self.speed * math.cos(self.angle)
        bullet_position[0][1] += self.speed * math.sin(self.angle)


def spawn_bullet(enemy):
    bullet_position.append(enemy.position)
    bullet = weapons.Bullet((player.cube_x, player.cube_y))
    weapons.bullets.append(bullet)
