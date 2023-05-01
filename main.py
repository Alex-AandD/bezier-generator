import pygame
import sys
from lg.vector import Vector2
from bezier.curve import calc_curve
from typing import List, Tuple
import random


def draw_controls(surface, color: pygame.Color, r: int, controls: List[Vector2]) -> List[pygame.Rect]:
    rects = []
    for control in controls:
        rect = pygame.draw.circle(surface, color, (control.x, control.y), r)
        control.rect = rect
        rects.append(rect)
    pygame.display.update(rects)
    return rects

def get_control_rect(v: Vector2, r: int) -> pygame.rect:
    left = v.x - r
    top = v.y - r
    return pygame.Rect(left, top, 2 * r, 2 * r)

def control_is_clicked(rect_control: pygame.Rect, mouse_pos: Tuple[int, int]) -> bool:
    posx = mouse_pos[0]
    posy = mouse_pos[1]
    rect_left = rect_control.left
    rect_top = rect_control.top
    rect_width = rect_control.width
    rect_height = rect_control.height
    return (posx >= rect_left) and (posx <= rect_left + rect_width) and (posy >= rect_top) and (
        rect_top + rect_height >= posy)

def run():
    width = 800
    height = 800
    window = pygame.display.set_mode((width, height))
    running = True

    controls = [Vector2(100, 200), Vector2(400, 300), Vector2(200, 600), Vector2(300, 400)]

    points = calc_curve(controls, 2000)
    c_radius = 10
    control_rects = draw_controls(window, (255, 255, 0), c_radius, controls)

    pygame.draw.lines(window, (255, 0, 0), False, points)
    pygame.display.update()

    index_control = -1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x = random.randint(0, width - 20)
                    y = random.randint(0, height - 20)
                    controls.append(Vector2(x, y))
                    points = calc_curve(controls, 1000)
                    window.fill((0, 0, 0))

                    control_rects = draw_controls(window, (255, 255, 0), c_radius, controls)
                    pygame.draw.lines(window, (255, 0, 0), False, points)
                    pygame.display.update()

        if index_control != -1:
            control = controls[index_control]
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos != (control.x, control.y):
                controls[index_control].x = mouse_pos[0]
                controls[index_control].y = mouse_pos[1]
                window.fill((0, 0, 0))
                control_rects = draw_controls(window, (255, 255, 0), c_radius, controls)
                # recalculate the curve
                points = calc_curve(controls, 2000)
                pygame.draw.lines(window, (255, 0, 0), False, points)
                pygame.display.update()

        if pygame.mouse.get_pressed()[0]:
            if index_control != -1:
                index_control = -1
            else:
                # handle activating the control point
                mouse_pos = pygame.mouse.get_pos()
                for i, control_rect in enumerate(control_rects):
                    if control_is_clicked(control_rect, mouse_pos):
                        index_control = i
                        break

    pygame.quit()

if __name__ == "__main__":
    run()