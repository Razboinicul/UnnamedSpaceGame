import pygame
import pygame_gui

pygame.init()

# Window setup
window_size = (800, 600)
window_surface = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame GUI Example")
background = pygame.Surface(window_size)
background.fill(pygame.Color('#1c1c1c'))

# Create GUI manager
manager = pygame_gui.UIManager(window_size)

# Create UI elements
hello_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 275), (100, 50)),
    text='Say Hello',
    manager=manager
)

text_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((300, 200), (200, 50)),
    manager=manager
)

# Main game loop
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print(f"Hello {text_input.get_text()}!")
                    
        # Pass events to GUI manager
        manager.process_events(event)
        
    # Update GUI
    manager.update(time_delta)
    
    # Draw everything
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    
    pygame.display.update()