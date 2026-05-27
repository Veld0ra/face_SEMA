import pygame

from config import *

class Terminal:

    def __init__(self, screen):

        self.screen = screen

        self.font = pygame.font.SysFont("Consolas", 18)

        self.input_text = ""

        self.response = ""

    def handle_event(self, event, state):

        if not state.is_terminal_open:
            return

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:

                self.response = "SEMA processando..."

                self.input_text = ""

            elif event.key == pygame.K_BACKSPACE:

                self.input_text = self.input_text[:-1]

            else:

                self.input_text += event.unicode

    def draw(self):

        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        overlay.fill((0, 0, 0, 180))

        self.screen.blit(overlay, (0,0))

        y = 20

        for line in [
            "> Pergunte ao SEMA:",
            "",
            self.input_text,
            "",
            self.response
        ]:

            text = self.font.render(line, True, WHITE)

            self.screen.blit(text, (20, y))

            y += 30
