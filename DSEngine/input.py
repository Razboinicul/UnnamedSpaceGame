# Contains all the input management code for keyboards, mice and controllers
import pygame

class InputManager:
    def __init__(self):
        self.keys = None

    def update(self):
        self.prev_keys = self.keys
        self.keys = pygame.key.get_pressed()
        
    def is_key_down(self, key) -> bool:
        return self.keys[key]
    
    def is_key_pressed(self, key: int) -> bool:
        return self.keys[key] and not self.prev_keys[key]
    
    def get_mouse_pos(self) -> pygame.Vector2:
        x, y = pygame.mouse.get_pos()
        return pygame.Vector2(x, y)