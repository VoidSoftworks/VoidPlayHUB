import world, tiles
from player import Player

def play():

    world.load_tiles_Start_Cave()
    player = Player()
    while player.is_alive() and not player.outofcave:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive() and not player.outofcave:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break



if __name__ == "__main__":
    play()
