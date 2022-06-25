import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the rider collides
    with the food, or the rider collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._fault =''

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            #self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    # def _handle_food_collision(self, cast): #this can get added back in when power-up (food) gets added in.
    #     """Updates the score nd moves the food if the rider collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     #score = cast.get_first_actor("scores")
    #     #food = cast.get_first_actor("foods")
        
    #     rider1 = cast.get_first_actor("rider1")
    #     rider2 = cast.get_first_actor("rider2")
        
        
    #     points = 0
    #     s2points = 0

        
    #     if self._is_game_over == False:
    #         points += 1
    #         s2points += 1
    #         print('these are thee s1 points',points)
    #         print('s2 points are',s2points)
    #         rider1.grow_tail(points)
    #         rider2.grow_tail(s2points)
            
            
        
        

        #Leaving this in case we want to doing something where the "food" will be a power up
        # if head.get_position().equals(food.get_position()):
        #     points = food.get_points()
        #     rider.grow_tail(points)
        #     score.add_points(points)
        #     food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the rider collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        rider1 = cast.get_first_actor("rider1")
        rider2 = cast.get_first_actor("rider2")
        
        
        points = 0
        s2points = 0

        
        if self._is_game_over == False:
            points += 1
            s2points += 1
            #print('these are thee s1 points',points)
            #print('s2 points are',s2points)
            rider1.grow_tail(points)
            rider2.grow_tail(s2points)
            
            
        
        

        rider1 = cast.get_first_actor("rider1")
        rider2 = cast.get_first_actor('rider2')
        head1 = rider1.get_segments()[0]
        head2 = rider2.get_segments()[0]
        segments1 = rider1.get_segments()[1:]
        segments2 = rider2.get_segments()[1:]
        
        
        if head1.get_position().equals(head2.get_position()):
            print('head on collision')
            self._fault = 'draw'
            self._is_game_over = True
        
            
        for segment1 in segments1:
           #print('this is seg in con 1',segment)
            if head1.get_position().equals(segment1.get_position()):
                print('player 1 colided with yourself')
                self._fault = 'player1'
                self._is_game_over = True
                
                
        for segment2 in segments2:
            #print('thisis the seg in con2,',segment)
            if head1.get_position().equals(segment2.get_position()):# or head2.get_position().equals(segment.get_position()):
                
                print('player 1 hit player 2')
                self._fault = 'player1'
                self._is_game_over = True
                
        for segment1 in segments1:
            #print('thisis the seg in con2,',segment)
            if head2.get_position().equals(segment1.get_position()):# or head2.get_position().equals(segment.get_position()):
                print('second player hit player 1')
                self._fault = 'player2'
                self._is_game_over = True
                
        for segment2 in segments2:
            #print('this is seg in con 3',segment)
            if head2.get_position().equals(segment2.get_position()):
                print('player 2 colided with itself')
                self._fault = 'player2'
                self._is_game_over = True
        
        #og code
        # rider = cast.get_first_actor("riders")
        # head = rider.get_segments()[0]
        # segments = rider.get_segments()[1:]
        
        # for segment in segments:
        #     if head.get_position().equals(segment.get_position()):
        #         self._is_game_over = True
                
                
                
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the rider and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        if self._is_game_over:
            rider1 = cast.get_first_actor("rider1")
            rider2 = cast.get_first_actor('rider2')
            segments1 = rider1.get_segments()
            segments2 = rider2.get_segments()
            #food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
           
            message.set_position(position)
            cast.add_actor("messages", message)

            #changes every part of the body to white 
            if self._fault == 'player1':
                for segment in segments1:
                    segment.set_color(constants.WHITE)
                    message.set_text("PLAYER 2 WINS!")
                    #self._rider1body._prepare_body.x = 0
                    
            elif self._fault == 'player2':
                for segment in segments2:
                    segment.set_color(constants.WHITE)
                    message.set_text("PLAYER 1 WINS!")
                    
                    
                
            else:
                for segment in segments1:
                    segment.set_color(constants.WHITE)
                for segment in segments2:
                    segment.set_color(constants.WHITE)
                message.set_text("IT'S A DRAW!!!")
        
        # #og code below
        # if self._is_game_over:
        #     rider = cast.get_first_actor("riders")
        #     segments = rider.get_segments()
        #     food = cast.get_first_actor("foods")

        #     x = int(constants.MAX_X / 2)
        #     y = int(constants.MAX_Y / 2)
        #     position = Point(x, y)

        #     message = Actor()
        #     message.set_text("Game Over!")
        #     message.set_position(position)
        #     cast.add_actor("messages", message)

        #     for segment in segments:
        #         segment.set_color(constants.WHITE)
        #     food.set_color(constants.WHITE)