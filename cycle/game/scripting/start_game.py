import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class StartGameAction(Action):
    """
    This will show before the game start
    """

    def __init__(self, keyboard_service):
        """Constructs a new StartGameAction."""
        self._is_game_start = False
        self._keyboard_service = keyboard_service
        self.start_game = Actor()

    def execute(self, cast, script):
        """Executes the handle start game action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
    
        if not self._is_game_start:
            """
            actions here if the game is not start
            """
            self._handle_initial_game_screen(cast)

        if self._keyboard_service.is_key_down('space'):
            self._is_game_start = True
            cast.remove_actor("messages",self.start_game)

    def _handle_initial_game_screen(self, cast):
        """
        Handle the initial state of the screen when the game is initiated

        Args:
            cast (Cast): The cast of Actors in the game.
        """
    
        #rider = cast.get_first_actor("rider")
        #segments = rider.get_segments()
        #food = cast.get_first_actor("foods")

        x = int(constants.MAX_X / 2)
        y = int((constants.MAX_Y / 2) - (((constants.FONT_SIZE * 2))*3/2))
        position = Point(x, y)

        text = "Press spacebar to start the game!"
        player1 = "Player 1 is on the right controls: J,I,K,L." 
        player2 = "Player 2 is on the left controls: A,W,S,D"
        
        self.start_game.set_text(f"{text : ^15}\n{player1 : ^15}\n{player2 : ^15}")
        self.start_game.set_position(position)
        self.start_game.set_font_size(constants.FONT_SIZE * 2)
        cast.add_actor("messages", self.start_game)

        """
        for segment in segments:
            segment.set_color(constants.WHITE)
        food.set_color(constants.WHITE)
        """

    def get_is_game_start(self):
        return self._is_game_start

    

