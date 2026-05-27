import time

class AnimationPlayer:

    def __init__(self):

        self.current_expression = "sleep"

        self.timer = 0

        self.sequence = []

        self.index = 0

    def update(self, state, dt):

        self.timer += dt

        if state == "sleep":
            self.current_expression = "sleep"

        elif state == "waking":
            self.sequence = [
                ("line_dim", 0.2),
                ("line_bright", 0.2),
                ("split", 0.15),
                ("dots", 0.2),
                ("alert", 0.25),
                ("thinking", 0.3),
                ("awake", 0.2)
            ]

            self.play_sequence(dt)

        elif state == "awake":
            self.current_expression = "awake"

        elif state == "thinking":
            self.current_expression = "thinking"

    def play_sequence(self, dt):

        if self.index >= len(self.sequence):
            return

        expression, duration = self.sequence[self.index]

        self.current_expression = expression

        if self.timer >= duration:

            self.timer = 0

            self.index += 1
