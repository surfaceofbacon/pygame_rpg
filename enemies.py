import attack   # imports the attack module to apply that to enemies
import math

import colors
import draw_shape
import player
triangle_tick_speed = 20
enemies_list = []
class Enemy:   # class of an enemy

    def __init__(self, AC, health, speed, weapon_damage, range, tick_speed, position: list):     # innit method gives the instance of an enemy armor class and health
        self.AC = AC
        self.health = health
        self.speed = speed
        self.damage = weapon_damage
        self.range = range
        self.tick_speed = tick_speed
        self.position = position
        self.alive = True


    def attack(self):           # attack method gives enemies the ability to attack
        player.hero.take_damage(self.damage)
        print(player.hero.health)

    def kill(self):
        self.alive = False

    def move(self, current_player_position: tuple, current_enemy_position: tuple):
        x_distance = (current_enemy_position[0] - current_player_position[0])
        y_distance = (current_enemy_position[1] - current_player_position[1])
        angle = math.atan(y_distance/x_distance)
        if x_distance > 0:
            angle += math.pi
        self.position[0] += self.speed * math.cos(angle)
        self.position[1] += self.speed * math.sin(angle)

class Triangle(Enemy):

    def draw(self, size):
        draw_shape.draw_triangle(colors.red, self.position, size)



