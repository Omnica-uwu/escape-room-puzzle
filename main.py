import cocos
from src.core.map import Map  # Make sure this path matches your actual project

class GameLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True  # To support keyboard/mouse input later

    def __init__(self):
        super().__init__()

        # Load the map
        self.map_layer = Map("bedroom")

        # Add the map to this layer
        self.add(self.map_layer)

        # Example: Access blocked tiles
        blocked = self.map_layer.blocked_positions
        print(f"Blocked positions: {blocked}")

class GameScene(cocos.scene.Scene):
    def __init__(self):
        # Create a scrollable manager
        scroll_manager = cocos.layer.ScrollingManager()

        # Create game layer with the map
        game_layer = GameLayer()
        scroll_manager.add(game_layer)

        # Set scrolling bounds to map size
        map_width = game_layer.map_layer.tmx_map.px_width
        map_height = game_layer.map_layer.tmx_map.px_height
        scroll_manager.set_focus(0, 0)
        scroll_manager.set_scale(1)
        scroll_manager.set_world_limits(0, 0, map_width, map_height)

        super().__init__(scroll_manager)

if __name__ == "__main__":
    cocos.director.director.init(width=800, height=600, caption="Escape Room Puzzle")
    cocos.director.director.run(GameScene())