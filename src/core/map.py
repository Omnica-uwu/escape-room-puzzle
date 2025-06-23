import cocos
import pytmx
import os
from cocos.tiles import load_tmx

# Constants for layer names
FLOOR_LAYER_NAME = "floor"
WALL_LAYER_NAME = "wall"
OBJECT_LAYER_NAME = "object"

class Map(cocos.layer.ScrollableLayer):
    def __init__(self, map_name):
        super().__init__()

        # Build the map path
        map_path = os.path.join("contents", "maps", f"{map_name}.tmx")

        # Load the TMX file
        self.tmx_map = load_tmx(map_path, identifier=map_name)

        # Get layers by name
        self.floor_layer = self.tmx_map[FLOOR_LAYER_NAME]
        self.wall_layer = self.tmx_map[WALL_LAYER_NAME]
        self.object_layer = self.tmx_map[OBJECT_LAYER_NAME]

        # Add only visible layers to this scrollable layer
        self.add(self.floor_layer, z=0)
        self.add(self.wall_layer, z=1)
        self.add(self.object_layer, z=2)

        # Store unwalkable positions for wall and object layers
        self.blocked_positions = self._get_blocked_positions()

    def _get_blocked_positions(self):
        blocked = set()
        for layer in [self.wall_layer, self.object_layer]:
            for x, y, gid in layer.tiles():
                if gid != 0:
                    blocked.add((x, y))
        return blocked

    def is_blocked(self, x, y):
        return (x, y) in self.blocked_positions

    def get_objects(self):
        # Future extension for behavior integration
        objects = []
        for obj in self.object_layer.objects:
            properties = obj.properties
            # Placeholder for Behavior mixin
            game_object = {
                'name': obj.name,
                'x': obj.x,
                'y': obj.y,
                'properties': properties
            }
            objects.append(game_object)
        return objects
