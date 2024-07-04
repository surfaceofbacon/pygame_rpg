import attack   # imports the attack module to apply that to enemies
import math

import colors
import draw_shape
import player
triangle_tick_speed = 5
triangle_color = colors.red
enemies_list = []
class Enemy:   # class of an enemy

    def __init__(self, AC, health, speed, weapon_damage, range, tick_speed: int, color, position: list):     # innit method gives the instance of an enemy armor class and health
        self.AC = AC
        self.health = health
        self.speed = speed
        self.damage = weapon_damage
        self.range = range
        self.tick_speed = tick_speed
        self.color = color
        self.position = position
        self.alive = True
        self.count = 1

    def attack(self):           # attack method gives enemies the ability to attack
        player.hero.take_damage(self.damage)
        player.hero.color = colors.white
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
        draw_shape.draw_triangle(self.color, self.position, size)

    def check_color(self):
        if self.count <= 0:
            self.color = triangle_color
            self.count = 1
        else:
            self.count -= 1
