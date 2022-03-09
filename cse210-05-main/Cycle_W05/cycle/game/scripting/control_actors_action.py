import constants
from game.scripting.action import Action
from game.shared.point import Point

LEFT = Point(-constants.CELL_SIZE, 0)
RIGHT = Point(constants.CELL_SIZE, 0)
UP = Point(0, -constants.CELL_SIZE)
DOWN = Point(0, constants.CELL_SIZE)

class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction_one = UP
        self._direction_two = DOWN

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction_one = LEFT
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction_one = RIGHT
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction_one = UP
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction_one = DOWN
        
        snake_one = cast.get_first_actor("snakes")
        snake_one.turn_head(self._direction_one)


        # Snake 2
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction_two = LEFT

        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction_two = RIGHT
            
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction_two = UP
            
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction_two = DOWN

        
        snake_two = cast.get_second_actor("snakes")
        snake_two.turn_head(self._direction_two)