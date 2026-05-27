import time

from config import DOUBLE_TOUCH_DELAY

class StateManager:

    def __init__(self):

        self.current_state = "sleep"

        self.last_touch = 0

        self.touch_count = 0

        self.is_terminal_open = False

    def register_touch(self):

        now = time.time()

        if now - self.last_touch < DOUBLE_TOUCH_DELAY:
            self.touch_count += 1
        else:
            self.touch_count = 1

        self.last_touch = now

    def update(self, dt):

        if self.current_state == "sleep":

            if self.touch_count >= 2:

                self.current_state = "waking"

                self.touch_count = 0

        elif self.current_state == "waking":

            self.current_state = "awake"

            self.is_terminal_open = True
