import pygame

from face.animations import AnimationPlayer
from face.expressions import get_expression

class FaceEngine:

    def __init__(self, screen):

        self.screen = screen

        self.player = AnimationPlayer()

        self.expression = "sleep"

    def update(self, state, dt):

        self.player.update(state, dt)

        self.expression = self.player.current_expression

    def draw(self):

        expression = get_expression(self.expression)

        expression(self.screen)
