import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score

#need to change the name of the rider class to rider
from game.casting.rider import Rider
from game.casting.rider2 import Rider2

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
 
from game.scripting.start_game import StartGameAction

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    #rider1 = cast.add_actor("rider1", rider())
    cast.add_actor("rider1", Rider())    
    cast.add_actor("rider2", Rider2())
    #cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    start_game_screen = StartGameAction(keyboard_service)
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))


    director = Director(video_service,start_game_screen)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()