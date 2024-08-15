<h1 align='center'>Tetris_Game :joystick:</h1> 

<div align='center'>
<img src='/TetrisImg.png' alt='Picture of the classic Tetris game as your starting to build with the grid you are playing on to the left, with coloured blocks lining the bottom, and showing your score on the top right side with the next piece coming directly below that.'>

<p align='center'>Embark on a nostalgic journey building the classic game of Tetris using Python and its cross-platform module Pygame. <br/>
<a href='https://github.com/AmberForrester/Tetris_Game'><strong>Source Code »</strong></a>
<br />
<br />
<a href='https://github.com/AmberForrester/Tetris_Game/issues/new?assignees=&labels=bug&projects=&template=bug-report-%F0%9F%90%9E.md'>Report Bug</a>
.
<a href='https://github.com/AmberForrester/Tetris_Game/issues/new?assignees=&labels=enhancement&projects=&template=feature-request-%F0%9F%9A%80.md'>Request Feature</a>
</p>



</div>







## About This Project
This game was built using Python as the programming language and it's Pygame library! Alongside the Pygame library, I was able to use it's various functions for the graphics, audio, and input handling for the Tetris game. 

Installing Pygame: 
```
pip install pygame-ce 
```

Receiving confirmation that it was successfully installed should render in your terminal:
```
Successfully installed pygame-ce-2.5.1 
```

Start using and initialize Pygame writing the following within `main.py`:
```
pygame.init()
```

## Set up the Game Structure  
Definitions:
- [ ] Defining the variables needed
- [ ] Creating the game objects 

Game Loop:
- [ ] Updating the positions of the game objects
- [ ] Checking for collisions 
- [ ] Consists of 3 steps: 

1. Event Handling -
    - Check for any events that occur in the game = quitting the game, a key pressed on the keyboard, etc. Using the Pygame event handling system. 

2. Updating Positions -
    - Update the positions of all the game objects (the blocks) based on the events we detected in Step 1 Event Handling. 

3. Drawing Objects -
    - Draw all the game objects in their new positions on the screen. Using the Pygame graphics functions to render the objects in the display. 

**By following 3 steps, we can create a dynamic and interactive game that responds to user inputs and updates its state accordingly.**


Game Window: (Display Surface) - 
    - Create the blank canvas to draw our game objects by using -> screen = pygame.display.set_mode((300, 600))
    - Set Mode method takes a tuple as an argument ((width, height))

Coordinate Systems to draw on the display surface - 
    - Computer Graphics - The origin of display is located at the top left corner (0, 0)
    - X Coordinate increases as we move to the RIGHT (X, 0)
    - Y Coordinate increases as we move DOWN (0, Y)

Set the Game Title using:
```
pygame.display.set_caption('Python Tetris Game')
```

Create a clock object using:
```
clock = pygame.time.Clock() 
```

**Make sure Clock has a capital C to control the frame rate of the game - _"How fast the game will run"_**


