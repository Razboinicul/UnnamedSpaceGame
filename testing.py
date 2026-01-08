# This is file for testing the new engine
import DSEngine_New as ds

class Velocity:
    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy

class Health:
    def __init__(self, value=100):
        self.value = value


if __name__ == "__main__":
    window = ds.Window()
    input = ds.InputManager()
    timer = ds.Timer(1000)

    # Setup scene
    entity_manager = ds.EntityManager()
    asset_manager = ds.AssetManager()
    asset_manager.load_assets()
    
    ent_player = entity_manager.create_new_entity("player")
    ent_player.add_component(ds.Position(200, 200))
    ent_player.add_component(ds.Renderable("gfx/player"))
    ent_player.add_component(ds.PlayerControllable(input))

    ent_enemy = entity_manager.create_new_entity("enemy")
    ent_enemy.add_component(ds.Position(100, 100))
    ent_enemy.add_component(ds.Renderable("gfx/enemy"))

    render_system = ds.RenderableSystem(entity_manager, window.surface, asset_manager)
    player_input_system = ds.InputSystem(entity_manager)

    font = ds.pygame.font.SysFont("Arial", 48) # Using a system font    
    text_surface = font.render("FPS", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.left = 10
    text_rect.top = 10

    fps = 0
    while window.running:
        window.handle_events()
        timer.update_timer(window.clock.get_time())

        if window.can_update():
            input.update()
            player_input_system.update()

            # Update timer 
            if timer.has_elasped():
                fps = window.clock.get_fps()
                text_surface = font.render(f"FPS: {round(fps)}", True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.left = 10
                text_rect.top = 10


        window.begin_frame()

        render_system.update()

        window.surface.blit(text_surface, text_rect)
        window.end_frame()

    window.shutdown()