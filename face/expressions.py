import pygame

from config import *

def draw_line(screen, thickness):

    pygame.draw.line(
        screen,
        BLUE,
        (80, HEIGHT // 2),
        (400, HEIGHT // 2),
        thickness
    )

def draw_split(screen):

    pygame.draw.line(
        screen,
        BLUE,
        (80, HEIGHT // 2),
        (200, HEIGHT // 2),
        5
    )

    pygame.draw.line(
        screen,
        BLUE,
        (280, HEIGHT // 2),
        (400, HEIGHT // 2),
        5
    )

def draw_dots(screen):

    pygame.draw.circle(screen, BLUE, (170, HEIGHT//2), 6)

    pygame.draw.circle(screen, BLUE, (310, HEIGHT//2), 6)

def draw_alert(screen):

    pygame.draw.circle(screen, BLUE, (170, HEIGHT//2), 20)

    pygame.draw.circle(screen, BLUE, (310, HEIGHT//2), 20)

def draw_awake(screen):

    pygame.draw.rect(screen, BLUE, (150, HEIGHT//2-30, 25, 60), border_radius=10)

    pygame.draw.rect(screen, BLUE, (305, HEIGHT//2-30, 25, 60), border_radius=10)

    pygame.draw.arc(
        screen,
        BLUE,
        (210, HEIGHT//2-5, 60, 40),
        3.14,
        6.28,
        4
    )

def draw_thinking(screen):

    pygame.draw.circle(screen, BLUE, (170, HEIGHT//2), 18)

    pygame.draw.circle(screen, BLUE, (310, HEIGHT//2), 18)

    pygame.draw.line(screen, BLUE, (220, HEIGHT//2), (260, HEIGHT//2), 3)

def get_expression(name):

    expressions = {

        "sleep": lambda s: draw_line(s, 4),

        "line_dim": lambda s: draw_line(s, 2),

        "line_bright": lambda s: draw_line(s, 8),

        "split": draw_split,

        "dots": draw_dots,

        "alert": draw_alert,

        "awake": draw_awake,

        "thinking": draw_thinking
    }

    return expressions[name]
