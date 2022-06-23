import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.snake import Snake

class Snake2(Snake):


    def same_thing (self):
        super().__init__() #creates the new actor
        super().get_segments()
        super().move_next()
        super().get_head()
        super().grow_tail()


    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)


    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("O")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)
            
            
    # def destroy(self, number_of_segments):
    #     for i in range(number_of_segments):
    #         tail = self._segments[-1]
    #         velocity = tail.get_velocity()
    #         offset = velocity.reverse()
    #         position = tail.get_position().add(offset)
            
    #         segment = Actor()
    #         segment.set_position(position)
    #         segment.set_velocity(velocity)
    #         segment.set_text("")
    #         segment.set_color(constants.GREEN)
    #         self._segments.append(segment)

    # # def turn_head(self, velocity):
    # #     self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        #this is the starting position coordinates x then y
        body = constants.SNAKE_LENGTH
        x = int(constants.MAX_X/-2) #* -1)
        y = int(constants.MAX_Y/-2) #* -1)
        
        print('this is the x in snake2',x)
        print('this is the y in snake2',y)
        
        
        #this will go through the entire length of the snake to start.
        for i in range(constants.SNAKE_LENGTH):
            position = Point(x + i * constants.CELL_SIZE, y)
            velocity = Point(-1*constants.CELL_SIZE,0) #original has 1 and 0
            print(position,velocity,' here is the position and velocity numbers for snake 2')
            text = "O" if i != 0 else "-"
            print(text)
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            #this sets the body
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)