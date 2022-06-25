import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the rider.
    
    The responsibility of ControlActorsAction is to get the direction and move the rider's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        
        self._direction1 = Point(constants.CELL_SIZE, 0) #starts moving to the right
        self._direction2 = Point(-constants.CELL_SIZE, 0) #starts moving to the left


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        rider1 = cast.get_first_actor("rider1")
        current_direction1 = rider1.get_head().get_velocity()
        print(f"direction1:  ({current_direction1.get_x()}, {current_direction1.get_y()})")

        rider2 = cast.get_first_actor("rider2")
        current_direction2 = rider1.get_head().get_velocity()
        print(f"direction2:  ({current_direction2.get_x()}, {current_direction2.get_y()})")

      

        #p1 controls
        # left
        if self._keyboard_service.is_key_down('j'):           
            self._direction1 = Point(-constants.CELL_SIZE, 0)
            
               
        
        # right
        if self._keyboard_service.is_key_down('l'):            
            self._direction1 = Point(constants.CELL_SIZE, 0)
           
                    
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction1 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction1 = Point(0, constants.CELL_SIZE)
            
        #p1 left controls below
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction2= Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction2 = Point(0, constants.CELL_SIZE)
        
        print(f"direction1 pressed:  ({self._direction1.get_x()}, {self._direction1.get_y()})")
        print(f"direction2 pressed:  ({self._direction2.get_x()}, {self._direction2.get_y()})")
        
        rider1 = cast.get_first_actor("rider1")
        rider1.turn_head(self._direction1)
        
        rider2 = cast.get_first_actor("rider2")
        rider2.turn_head(self._direction2)
