import items, enemies, actions, world

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all moves actions for adjacent tiles"""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        you can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("The {} does {} damage. you have {} HP remaining." .format(self.enemy.name, self.enemy.damage, the_player.hp))

class BanditCaveRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.bandit())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A bandit is in this section of the cave. He sees you and attacks!
            """
        else:
            return """
            The corpse of a bandit lay rotting on the floor of the cave.
            """

class FindIronSwordCaveRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Iron_Sword())

    def intro_text(self):
        return """
        You notice something shining in the corner of the cave.
        It's an iron sword, this could come in handy in such a dangerous place.
        """


class EmptyCaveRoom(MapTile):
    def intro_text(self):
        return """
        It doesn't seem like anything is in this part of the cave, you must press on.
        """

    def modify_player(self, player):
        #room has no action on player
        pass

class CaveEscapeRoom(MapTile):
    def intro_text(self):
        return """
        As you find the exit to the cave. Its is a old wooden door. As you swing it open light floods the cave room you are in.
        Blinking sharply your eyes adjust to see a mountain vista, it looks like a town is nestled at the base of the range.
        You move forward into this world of ADVENTURE!
        """

    def modify_player(self, player):
        player.victory = True
