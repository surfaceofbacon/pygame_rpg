import pygame
import window
import math


def draw_triangle(color, start: tuple, size):
    area = size * 1000
    side_length = 2 * math.sqrt(area/(math.sqrt(3)))
    start_x = start[0]
    start_y = start[1]
    dimension = (start_x, start_y), (start_x + (side_length / math.sqrt(2)), start_y + (side_length / math.sqrt(2))), (start_x + 2*(side_length / math.sqrt(2)), start_y)
    pygame.draw.polygon(window.window, color, dimension)
