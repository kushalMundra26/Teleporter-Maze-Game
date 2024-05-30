import pygame
import sys

pygame.init()

# Define constants
WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize the screen and set the caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

star_image = pygame.image.load("star_transperent.png")
star_image = pygame.transform.scale(star_image, (70, 70))


# Maze level 1
maze_level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X...............X..T....X",
    "X.XXXXXXXXXXXXXXX.XXXXX.X",
    "X....X.................XX",
    "XXXX.XXXXXXXXXXX.X.XXXXXX",
    "X..........X............X",
    "X.XXXXXXXXXXXXXXXXXXX.XXX",
    "X.......................X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X...........T..X........X",
    "X.XXXXXXXXXXXXXXXXXXXXX.X",
    "X.......................X",
    "X.XXXXXXXXXXXXXXXXXXXXX.X",
    "X..........X............X",
    "X.XXXXXXXXX.XXXXXXXXX...X",
    "X..........X............X",
    "XXXX.XXXXXXXXXXX.X.XXXXXX",
    "X....X.....$.....X......X",
    "X.XXXXXXXXXXXXXXX.XXXXX.X",
    "X........X..............X",
    "X.X.XXXXXX.XXXX.XXX.X...X",
    "X..........X........X.X.X",
    "X.XXXXXXXXXXXXXXXXXXX.XXX",
    "X.X.................X...X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Maze level 2
maze_level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X......X.........X..XT..X",
    "X..XX..XXXX.XXXXXX.XXXX.X",
    "X......X.........X.X....X",
    "XXXXXX.XXX.X.X.XXX.X.XXXX",
    "X..........X.......X....X",
    "X.XXXXX.XXXXXXXXXX.XXXX.X",
    "X...................X...X",
    "X.XXXXXXXXXXXXXXXXXXX.XXX",
    "X.......................X",
    "XXXXXXXXXXXXXXXXXXXXX...X",
    "X...................XXXXX",
    "X.XXXXXX.XXXXXXXXXX.X...X",
    "X...X....X....T.X...X.X.X",
    "X.XXX.XXXXXXX.XXX.XXX.X.X",
    "X.TX...X..........X...X.X",
    "XXXXX.XX.XXXXXXXXXX.XXX.X",
    "X...X....X....X..$X.X.X.X",
    "X.X.XXXXXX.XXXX.XXX.X...X",
    "X.X........X........X.X.X",
    "X.XXXXXXXXXXXXXXXXXXX.XXX",
    "X.X...............T.X...X",
    "X.XXX.XXXXXXXXXXXXXXXXX.X",
    "X.......................X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Not to change the player size as the math is being used in collision detection
player_size = 10
player_pos = [30, 30]
player_speed = 5

def chest_box_possi(maze):
    # Chect Box Position
    chest_box_pos = None
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == "$":
                chest_box_pos = [x * 20, y * 20]
                break
        if chest_box_pos:
            break
    return chest_box_pos

def teleportors_find(maze):
    # Finding pairs of teleproters in the maze
    teleporters = []
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == "T":
                teleporters.append((x, y))

    # Checking if teleporters are in pairs because you need a entry and an exit teleporter
    if len(teleporters) % 2 != 0:
        raise ValueError("Teleporters must be in pairs")

    # Separating entry and exit teleporters
    entry_teleporters = teleporters[::2]
    exit_teleporters = teleporters[1::2]

    return entry_teleporters, exit_teleporters

start_time = None
end_time = None

def start_timer():
    global start_time
    start_time = pygame.time.get_ticks()

def stop_timer():
    global end_time
    end_time = pygame.time.get_ticks()
    elapsed_time = (end_time - start_time) / 1000
    return elapsed_time

def calculate_stars(elapsed_time, level):
    if level == 1:
        if elapsed_time <= 17:
            return 3
        elif elapsed_time <= 22:
            return 2
        else:
            return 1
    elif level == 2:
        if elapsed_time <= 29:
            return 3
        elif elapsed_time <= 34:
            return 2
        else:
            return 1

def display_next_level_screen(elapsed_time, level):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("Level Completed", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(text, text_rect)
    time_text = font.render("Time taken: {:.2f} seconds".format(elapsed_time), True, (0, 0, 0))
    time_rect = time_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(time_text, time_rect)
    
    stars = calculate_stars(elapsed_time, level)
    star_spacing = 60
    for i in range(stars):
        screen.blit(star_image, (WIDTH // 2 - 95 + i * star_spacing, HEIGHT // 2 - 30))

    next_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 50, WIDTH // 4, 50)
    quit_button = pygame.Rect(WIDTH // 2, HEIGHT // 2 + 50, WIDTH // 4, 50)
    pygame.draw.rect(screen, GREEN, next_button)
    pygame.draw.rect(screen, RED, quit_button)
    next_text = font.render("Next Level", True, BLACK)
    next_text_rect = next_text.get_rect(center=next_button.center)
    screen.blit(next_text, next_text_rect)
    quit_text = font.render("Quit", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(quit_text, quit_text_rect)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if next_button.collidepoint(mouse_pos):
                    return True
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.time.Clock().tick(30)


# Maze Drawing Function
def draw_maze(maze):
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == "X":
                pygame.draw.rect(screen, BLACK, (x*20, y*20, 20, 20))
            elif col == ".":
                pygame.draw.rect(screen, WHITE, (x*20, y*20, 20, 20))
            elif col == "T":
                pygame.draw.rect(screen, BLUE, (x*20, y*20, 20, 20))
            elif col == "$":
                pygame.draw.rect(screen, GREEN, (x*20, y*20, 20, 20))

# Drawing the player
def draw_player():
    pygame.draw.circle(screen, RED, (player_pos[0], player_pos[1]), player_size)

# Checking collision between player and teleporter
def check_teleportation(maze):
    entry_teleporters,exit_teleporters = teleportors_find(maze)
    for entry_teleporter, exit_teleporter in zip(entry_teleporters, exit_teleporters):
        entry_rect = pygame.Rect(entry_teleporter[0] * 20, entry_teleporter[1] * 20, 20, 20)
        exit_rect = pygame.Rect(exit_teleporter[0] * 20 + 10, exit_teleporter[1] * 20 + 10, 20, 20)
        if pygame.Rect(player_pos[0], player_pos[1], player_size, player_size).colliderect(entry_rect):
            return exit_rect.topleft
    return None

# Checking collision between player and chest box
def check_chest_collision():
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    chest_box_rect = pygame.Rect(chest_box_pos[0], chest_box_pos[1], 20, 20)
    return player_rect.colliderect(chest_box_rect)

# Main game loop
def play_level(maze):
    global player_pos
    global chest_box_pos
    global start_time
    player_size = 10
    player_pos = [30, 30]
    player_speed = 5

    chest_box_pos= chest_box_possi(maze)
    entry_teleporters,exit_teleporters = teleportors_find(maze)

    start_timer()

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Moving the player and collision checks
        if keys[pygame.K_UP]:
            if player_pos[1] - player_speed >= player_size and maze[int((player_pos[1] - player_speed - player_size) / 20)][int(player_pos[0] / 20)] != "X" and maze[int((player_pos[1] - player_speed - player_size) / 20)][int((player_pos[0] - 10) / 20)] != "X" and maze[int((player_pos[1] - player_speed - player_size) / 20)][int((player_pos[0] + 9) / 20)] != "X":
                player_pos[1] -= player_speed
        if keys[pygame.K_DOWN]:
            if player_pos[1] + player_speed + player_size < HEIGHT and maze[int((player_pos[1] + player_speed + player_size//2) / 20)][int(player_pos[0] / 20)] != "X" and maze[int((player_pos[1] + player_speed + player_size//2) / 20)][int((player_pos[0] - 10) / 20)] != "X" and maze[int((player_pos[1] + player_speed + player_size//2) / 20)][int((player_pos[0] + 9) / 20)] != "X":
                player_pos[1] += player_speed
        if keys[pygame.K_LEFT]:
            if player_pos[0] - player_speed >= player_size and maze[int(player_pos[1] / 20)][int((player_pos[0] - player_speed - player_size) / 20)] != "X" and maze[int((player_pos[1] - 10) / 20)][int((player_pos[0] - player_speed - player_size) / 20)] != "X" and maze[int((player_pos[1] + 9) / 20)][int((player_pos[0] - player_speed - player_size) / 20)] != "X":
                player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            if player_pos[0] + player_speed + player_size < WIDTH and maze[int(player_pos[1] / 20)][int((player_pos[0] + player_speed + player_size//2) / 20)] != "X" and maze[int((player_pos[1] - 10) / 20)][int((player_pos[0] + player_speed + player_size//2) / 20)] != "X" and maze[int((player_pos[1] + 9) / 20)][int((player_pos[0] + player_speed + player_size//2) / 20)] != "X":
                player_pos[0] += player_speed

        # Check if the player collides with the chest box
        if check_chest_collision():
            elapsed_time = stop_timer()
            return elapsed_time

        # Checking teleportation
        teleport_destination = check_teleportation(maze)
        if teleport_destination:
            player_pos = list(teleport_destination)

        # Draw the maze and player
        draw_maze(maze)
        draw_player()

        pygame.display.update()

        pygame.time.Clock().tick(30)

# Play level 1
time_level_1 = play_level(maze_level_1)
next_level = display_next_level_screen(time_level_1,1)

# Play level 2
if next_level:
    time_level_2 = play_level(maze_level_2)
    display_next_level_screen(time_level_2,2)

pygame.quit()
sys.exit()