import pygame
import sys

from config import *
from face.engine import FaceEngine
from states.manager import StateManager
from terminal.console import Terminal
from serial_comm.dwin import DWIN

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SEMA")
clock = pygame.time.Clock()
face = FaceEngine(screen)
state = StateManager()
terminal = Terminal(screen)
dwin = DWIN()
running = True

while running:
  dt = clock.tick(FPS) / 1000
  screen.fill(BLACK)
  touch = dwin.read_touch()
  if touch:
    state.register_touch()
  for event in pygame.event.get();
    if event.type == pygame.QUIT: 
      running = False
    terminal.handle_event(event, state)
  state.update(dt)
  face.update(state.current_state, dt)
  face.draw()
  if state.is_terminal_open:
    terminal.draw()
  pygame.display.flip()
pygame.quit()
sys.exit()

   
