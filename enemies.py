import attack   # imports the attack module to apply that to enemies
import math

import colors
import draw_shape


class Enemy:   # class of an enemy

    def __init__(self, AC, health, speed, position: list):     # innit method gives the instance of an enemy armor class and health
        self.AC = AC
        self.health = health
        self.speed = speed
        self.position = position
        self.alive = True

    def attack(self, weapon):           # attack method gives enemies the ability to attack
        pass

    def kill(self):
        self.alive = False

    def move(self, current_player_position: tuple, current_enemy_postion: tuple):
        x_distance = (current_enemy_postion[0] - current_player_position[0])
        y_distance = (current_enemy_postion[1] - current_player_position[1])
        angle = math.atan(y_distance/x_distance)
        if x_distance > 0:
            angle += math.pi
        self.position[0] += self.speed * math.cos(angle)
        self.position[1] += self.speed * math.sin(angle)

class Triangle(Enemy):

    def draw(self, size):
        draw_shape.draw_triangle(colors.red, self.position, size)


triangle_enemy = Triangle(10, 10, 1, [100, 100])
