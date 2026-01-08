import pygame
import sys
import time

# Constants
TICK_RATE = 60  # game updates per second
TICK_TIME = 1.0 / TICK_RATE  # time per update in seconds

class Window:
    def __init__(self, title="DSEngine Window", size: tuple=(1280, 720), icon=pygame.image.load("default.icon.png")):
        # Setup pygame window
        self.surface = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.RESIZABLE)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(title)
        
        self.clock = pygame.time.Clock()
        self.running = True

        # Frame rate independence setup
        self.last_time = time.perf_counter()
        self.accumulator = 0.0

    # Handle all window events here
    def handle_events(self):
        # Update frametiming first, so the game only updates 60 times a second
        now = time.perf_counter()
        frame_time = now - self.last_time
        self.last_time = now
        self.accumulator += frame_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # Call this within your games main funciton to ensure that you only update the game 60 times per second
    def can_update(self) -> bool:
        if self.accumulator >= TICK_TIME:
            self.accumulator -= TICK_TIME
            return True
        
        return False

    # Call this before drawing anything to screen
    def begin_frame(self):
        self.surface.fill(pygame.Color(130, 200, 229))

    # Call this after drawing to the screen
    def end_frame(self):

        pygame.display.update()
        self.clock.tick()

    # Handle shutdown
    def shutdown(self):
        pygame.quit()
        sys.exit()