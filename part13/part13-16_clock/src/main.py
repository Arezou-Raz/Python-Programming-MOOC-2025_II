import pygame
import math
import datetime

pygame.init()

window_width = 400
window_height = 400
clock_radius = 180
center = (window_width // 2, window_height // 2)

black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Clock")

clock = pygame.time.Clock()

def draw_clock_face():
    pygame.draw.circle(window, red, center, clock_radius, 2)
    pygame.draw.circle(window, red, center, 6)

def draw_hand(angle, length, color):
    x = center[0] + length * math.cos(math.radians(angle))
    y = center[1] + length * math.sin(math.radians(angle))
    pygame.draw.line(window, color, center, (x, y), 2)

def get_time_angle():
    now = datetime.datetime.now()
    second_angle = (now.second * 6) - 90
    minute_angle = (now.minute * 6) + (now.second * 0.1) - 90
    hour_angle = ((now.hour % 12) * 30) + (now.minute * 0.5) - 90
    return hour_angle, minute_angle, second_angle

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(black)

    draw_clock_face()

    hour_angle, minute_angle, second_angle = get_time_angle()

    draw_hand(hour_angle, clock_radius * 0.5, blue)
    draw_hand(minute_angle, clock_radius * 0.8, blue)
    draw_hand(second_angle, clock_radius * 0.9, blue)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
