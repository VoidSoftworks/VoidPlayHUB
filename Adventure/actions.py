import player


class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        return"{}: {}" .format(self.hotkey, self.name)

class MoveNorth(Action):
    def __init__(self):
        super().__init__(method = Player.move_north, name = 'Move north', hotkey = 'w')

class MoveSouth(Action):
    def __init__(self):
        super().__init__(method = Player.move_south, name = 'Move South', hotkey = 's')

class MoveEast(Action):
    def __init__(self):
        super().__init__(method = Player.move_south, name = 'Move East', hotkey = 'd')

class MoveWest(Action):
    def __init__(self):
        super().__init__(method = Player.move_west, name = 'Move West', hotkey = 'a')

class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method = Player.print_inventory, name = 'View inventory', hotkey = 'i')

class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method = Player.attack, name = 'Attack', hotkey = 'f', enemy = enemy)
