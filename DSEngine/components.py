import pygame

# This is a number of included components in the engine
class Renderable:
    def __init__(self, key = "unknown", src: pygame.Rect = None):
        self.key = key
        self.src = src

class Position:
    def __init__(self, x : int = 0, y : int = 0):
        self.x = x
        self.y = y

class PlayerState:
    def __init__(self, state: str):
        self.state = state

class PlayerControllable:
    def __init__(self, input_manager):
        self.im = input_manager