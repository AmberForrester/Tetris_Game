<a id="readme-top"></a>

<h1 align='center'>Tetris_Game :joystick:</h1> 

<div align='center'>

<img src='/TetrisImg.png' alt='Picture of the classic Tetris game as your starting to build with the grid you are playing on to the left, with coloured blocks lining the bottom, and showing your score on the top right side with the next piece coming directly below that.'>

<p align='center'>Embark on a nostalgic journey building the classic game of Tetris using Python and Pygame. <br/>

<a href='https://github.com/AmberForrester/Tetris_Game'><strong>Source Code »</strong></a>
<br />
<br />
<a href='https://github.com/AmberForrester/Tetris_Game/issues/new?assignees=&labels=bug&projects=&template=bug-report-%F0%9F%90%9E.md'>Report Bug</a>
.
<a href='https://github.com/AmberForrester/Tetris_Game/issues/new?assignees=&labels=enhancement&projects=&template=feature-request-%F0%9F%9A%80.md'>Request Feature</a>
</p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-this-project">About This Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>






# About This Project
This game was built using Python as the programming language and its cross-platform set of modules Pygame, used to create video games! This partnership creates the perfect demonstration of a game development library with the various functions for graphics, audio, and input handling that Pygame has to offer. 

<p align="right">(<a href="#readme-top">top of page</a>)</p>

## Getting Started
A good understanding of Python and Pygame would be beneficial to helping you create this project. However, it is always good practice to refer to the Documentation available when developing ***any*** project. 

_Please refer to the [Python Documentation](https://docs.python.org/3/) and the [PyGame Documentation](https://www.pygame.org/docs/) for your reference._

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


<p align="right">(<a href="#readme-top">top of page</a>)</p>



## Contributing

I have learned that contributions are the heart of what makes the open source community such an amazing place! We are constantly able to learn, grow, inspire eachother, and create incredible things. Any contributions you make are **greatly appreciated**, we are so lucky to be here together.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! I appreciate you!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">top of page</a>)</p>



## Acknowledgments

Please take some time to check out the links below! I found value in each and every one of them, so my hope is that you will to!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#animal-bug)

<p align="right">(<a href="#readme-top">top of page</a>)</p>