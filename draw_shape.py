import pygame
import window
import math


def draw_triangle(color, start: tuple, size):
    area = size * 1000
    side_length = 2 * math.sqrt(area/(math.sqrt(3)))
    dimension = (start[0], start[1]), (start[0] + side_length/2, start[1] - (math.sqrt(3))*side_length/2), (start[0] + side_length, start[1])
    pygame.draw.polygon(window.window, color, dimension)


def draw_pentagon(color, start, size):
    area = size * 1000
    side_length = 2 * math.sqrt(area / math.sqrt(5 * (5 + (2 * math.sqrt(5)))))
    vert_1 = (start[0], start[1])
    vert_2 = (vert_1[0] + (side_length) * math.cos(math.pi / 5), vert_1[1] - (side_length * math.sin(math.pi / 5)))
    vert_3 = (vert_2[0] + (side_length) * math.cos(math.pi / 5), vert_2[1] + (side_length * math.sin(math.pi / 5)))
    vert_4 = (vert_3[0] - (side_length) * math.sin(math.pi / 10), vert_3[1] + side_length * math.cos(math.pi / 10))
    vert_5 = (vert_4[0] - side_length, vert_4[1])
    dimension = vert_1, vert_2, vert_3, vert_4, vert_5
    pygame.draw.polygon(window.window, color, dimension)

