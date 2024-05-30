# Teleporter Maze Game

This repository contains a maze game developed using Pygame. The game features mazes where players must navigate through various obstacles and use teleporters to reach the goal. The game includes two levels, each with increasing difficulty and challenges.

## Features

- Two challenging maze levels
- Teleporters to enhance gameplay
- Timer to track completion time
- Star rating system based on time taken to complete each level

## Gameplay

- Navigate through the maze using arrow keys.
- Use teleporters (marked in blue) to move across the maze quickly.
- Reach the green chest box to complete the level.
- Earn stars based on your completion time.

## How to Run

1. Ensure you have Python and Pygame installed:
    ```bash
    pip install pygame
    ```
2. Clone the repository:
    ```bash
    git clone https://github.com/kushalMundra26/Teleportor-Maze-Game
    ```
3. Navigate to the project directory:
    ```bash
    cd Teleporter-Maze-Game
    ```
4. Run the game:
    ```bash
    python tele_maze.py
    ```

## Code Overview

### Main Game Loop

The main game loop is responsible for rendering the maze, updating the player's position, checking for collisions, and handling user input.

### Maze Levels

The game includes two levels defined by `maze_level_1` and `maze_level_2` arrays. Each character in the arrays represents different elements in the maze:
- `X`: Wall
- `.`: Path
- `T`: Teleporter
- `$`: Chest Box (Goal)

### Functions

- **`chest_box_possi(maze)`**: Finds the position of the chest box in the maze.
- **`teleportors_find(maze)`**: Finds pairs of teleporters in the maze.
- **`start_timer()` and `stop_timer()`**: Manages the game timer.
- **`calculate_stars(elapsed_time, level)`**: Determines the star rating based on the time taken to complete the level.
- **`display_next_level_screen(elapsed_time, level)`**: Displays the completion screen with the star rating.
- **`draw_maze(maze)`**: Renders the maze on the screen.
- **`draw_player()`**: Draws the player on the screen.
- **`check_teleportation(maze)`**: Checks for player collisions with teleporters.
- **`check_chest_collision()`**: Checks for player collisions with the chest box.
