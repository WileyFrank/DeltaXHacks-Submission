import pygame
import time
import sys
from pynput import mouse
from pynput.mouse import Listener
import random

screen_height = 540
screen_width = 960
pixel_standard = 1
frame_speed = 1/60
run = True
background_x = 0
background_ground = 0
game_speed = 10
player_speed = 1
grid_size = 30
player_state = 0 #this is his state. 0 is standing, 1 is jumping and 2 is standing
player_x = 10
player_y = 10
player_position = 0
difficulty = 1
object_count = 20
length_apart = 15
gunner = False
animation = 0
start_menu_background_color = (0,0,0)
difficulty_button = 0
start_button = 0
retry_button = 0
menu_button = 0
next_button = 0
left_button_color = (0, 255, 255)
right_button_color = (0, 255, 255)
button_height = 105
button_width = 280
border_size = 140
button_gap = 120
button_start_height = screen_height - (border_size/2) - button_height

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

background = pygame.transform.scale((pygame.image.load(r"RunGame\imgs\Background2.png")),(screen_width,screen_height))
ground = pygame.transform.scale((pygame.image.load(r"RunGame\imgs\ground.png")),(screen_width,screen_height))

screen.blit(background, (0,0))
pygame.display.update()


run_frames_list = []
slide_frames_list = []
jump_frames_list = []
enemy_art_list = []
button_list = []
run_placement_list = (15,25,23,15,20,15,25,23,15,21)

run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame0.png'))
run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame1.png'))
run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame2.png'))
run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame3.png'))
run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame4.png'))
run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame5.png'))
run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame6.png'))
run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame7.png'))
run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame8.png'))
run_frames_list.append(pygame.image.load(r'RunGame\imgs\RunningFrames\Frame9.png'))
slide_frames_list.append(pygame.image.load(r'RunGame\imgs\SlidingFrames\Frame0.png'))
slide_frames_list.append(pygame.image.load(r'RunGame\imgs\SlidingFrames\Frame1.png'))
slide_frames_list.append(pygame.image.load(r'RunGame\imgs\SlidingFrames\Frame2.png'))
jump_frames_list.append(pygame.image.load(r'RunGame\imgs\JumpingFrames\Frame0.png'))
jump_frames_list.append(pygame.image.load(r'RunGame\imgs\JumpingFrames\Frame1.png'))
jump_frames_list.append(pygame.image.load(r'RunGame\imgs\JumpingFrames\Frame2.png'))
jump_frames_list.append(pygame.image.load(r'RunGame\imgs\JumpingFrames\Frame3.png'))

enemy_art_list.append(pygame.transform.scale(pygame.image.load(r'RunGame\imgs\Enemies\Obstacle.png'), (grid_size * 2, grid_size * 2)))
enemy_art_list.append(pygame.transform.scale(pygame.image.load(r'RunGame\imgs\Enemies\Runner.png'), (grid_size*2, grid_size*2)))
enemy_art_list.append(pygame.transform.scale(pygame.image.load(r'RunGame\imgs\Enemies\Gunner.png'), (grid_size * 2, grid_size * 2)))
enemy_art_list.append(pygame.transform.scale(pygame.image.load(r'RunGame\imgs\Enemies\Blade.png'), (grid_size * 2, grid_size * 2)))
enemy_art_list.append(pygame.transform.scale(pygame.image.load(r'RunGame\imgs\Enemies\Bullet.png'), (grid_size, grid_size)))

difficulty_list = []
button_list.append([(pygame.image.load(r'RunGame\imgs\Buttons\StartEmpty.png')),(pygame.image.load(r'RunGame\imgs\Buttons\StartHover.png'))])
button_list.append([(pygame.image.load(r'RunGame\imgs\Buttons\NextEmpty.png')),(pygame.image.load(r'RunGame\imgs\Buttons\NextHover.png'))])
button_list.append([(pygame.image.load(r'RunGame\imgs\Buttons\MenuEmpty.png')),(pygame.image.load(r'RunGame\imgs\Buttons\MenuHover.png'))])
difficulty_list.append([(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\1Empty.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\1Hover.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\1Click.png'))])
difficulty_list.append([(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\2Empty.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\2Hover.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\2Click.png'))])
difficulty_list.append([(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\3Empty.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\3Hover.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\3Click.png'))])
difficulty_list.append([(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\4Empty.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\4Hover.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\4Click.png'))])
difficulty_list.append([(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\5Empty.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\5Hover.png')),(pygame.image.load(r'RunGame\imgs\Buttons\Difficulty\5Click.png'))])
button_list.append(difficulty_list)
button_list.append([(pygame.image.load(r'RunGame\imgs\Buttons\RetryEmpty.png')),(pygame.image.load(r'RunGame\imgs\Buttons\RetryHover.png'))])

for i in range(3):
    for j in range(2):
        button_list[i][j] = pygame.transform.scale(button_list[i][j], (button_width,button_height))

for i in range(5):
    for j in range(3):
        button_list[3][i][j] = pygame.transform.scale(button_list[3][i][j], (button_width,button_height))
for j in range(2):
    button_list[4][j] = pygame.transform.scale(button_list[4][j], (button_width,button_height))

def main_reset(grid):
    main()

def display_start_menu(difficulty, start_button, difficulty_button):

    global button_height, button_width, border_size, button_gap, screen_height
    screen.blit(background, (0,0))
    screen.blit(button_list[3][difficulty-1][difficulty_button], (int(border_size),int(button_start_height)))
    screen.blit(button_list[0][start_button], (int(border_size + button_width + button_gap),int(button_start_height)))
    pygame.display.update()

def start_menu():
    global difficulty, difficulty_button, start_button, button_height, button_width, button_gap, border_size, screen_height, screen_width
    while True:
        display_start_menu(difficulty, start_button, difficulty_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            (mouse_x,mouse_y) = pygame.mouse.get_pos()
            if mouse_x >= border_size and mouse_x <= (border_size + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                # left_hover = True
                if difficulty_button == 0:
                    difficulty_button = 1
            else:
                # left_hover = False
                difficulty_button = 0
            if mouse_x >= (border_size + button_width + button_gap) and mouse_x <= (border_size + button_width + button_gap + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                # right_hover = True
                start_button = 1
            else:
                start_button = 0
            #     # right_hover = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #if scrolling up
                    (mouse_x,mouse_y) = pygame.mouse.get_pos()
                    if mouse_x >= border_size and mouse_x <= (border_size + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                        difficulty_button = 2
                        if difficulty < 5:
                            difficulty += 1
                        elif difficulty >= 5:
                            difficulty = 1
                    if mouse_x >= (border_size + button_width + button_gap) and mouse_x <= (border_size + button_width + button_gap + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                        main()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if mouse_x >= border_size and mouse_x <= (border_size + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                        difficulty_button = 1
                    else:
                        difficulty_button = 0
            # return start_button, difficulty_button, difficulty
def display_death_menu(retry_button, menu_button):

    global button_height, button_width, border_size, button_gap, screen_height
    screen.blit(background, (0,0))
    screen.blit(button_list[4][menu_button], (int(border_size),int(button_start_height)))
    screen.blit(button_list[2][retry_button], (int(border_size + button_width + button_gap),int(button_start_height)))
    pygame.display.update()

def death_menu():
    global menu_button, retry_button, button_height, button_width, button_gap, border_size, screen_height, screen_width
    while True:
        display_death_menu(retry_button, menu_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            (mouse_x,mouse_y) = pygame.mouse.get_pos()
            if mouse_x >= border_size and mouse_x <= (border_size + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                # left_hover = True
                if menu_button == 0:
                    menu_button = 1
            else:
                # left_hover = False
                menu_button = 0
            if mouse_x >= (border_size + button_width + button_gap) and mouse_x <= (border_size + button_width + button_gap + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                # right_hover = True
                retry_button = 1
            else:
                retry_button = 0
            #     # right_hover = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #if scrolling up
                    (mouse_x,mouse_y) = pygame.mouse.get_pos()
                    if mouse_x >= border_size and mouse_x <= (border_size + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                        main()
                    if mouse_x >= (border_size + button_width + button_gap) and mouse_x <= (border_size + button_width + button_gap + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                        start_menu()
            # return start_button, difficulty_button, difficulty
def display_win_menu(next_button, menu_button):

    global button_height, button_width, border_size, button_gap, screen_height
    screen.blit(background, (0,0))
    screen.blit(button_list[2][menu_button], (int(border_size),int(button_start_height)))
    screen.blit(button_list[1][next_button], (int(border_size + button_width + button_gap),int(button_start_height)))
    pygame.display.update()

def win_menu():
    global menu_button, next_button, button_height, button_width, button_gap, border_size, screen_height, screen_width, difficulty
    while True:
        display_win_menu(next_button, menu_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            (mouse_x,mouse_y) = pygame.mouse.get_pos()
            if mouse_x >= border_size and mouse_x <= (border_size + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                # left_hover = True
                if menu_button == 0:
                    menu_button = 1
            else:
                # left_hover = False
                menu_button = 0
            if mouse_x >= (border_size + button_width + button_gap) and mouse_x <= (border_size + button_width + button_gap + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                # right_hover = True
                next_button = 1
            else:
                next_button = 0
            #     # right_hover = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #if scrolling up
                    (mouse_x,mouse_y) = pygame.mouse.get_pos()
                    if mouse_x >= border_size and mouse_x <= (border_size + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                        start_menu()
                    if mouse_x >= (border_size + button_width + button_gap) and mouse_x <= (border_size + button_width + button_gap + button_width) and mouse_y >= (button_start_height) and mouse_y <= (button_start_height + button_height):
                        if difficulty < 5:
                            difficulty += 1
                        main()
            # return start_button, difficulty_button, difficulty
def create_grid():
  grid = [[[False,False,False,False,False,[0,0]] for x in range(32)] for y in range(18)]
  return grid

def create_hitbox(hitboxes = {}):
    for x in range(player_x, player_x + 2):
        for y in range(player_y, player_y + 4):
            hitboxes[(x,y)] = 1
    return hitboxes

def jump_hitbox(hitboxes):
    for x in range(player_x, player_x + 2):
        for y in range(player_y + 2, player_y + 4):
            del hitboxes[(x,y)]
    for x in range(player_x + 2, player_x + 4):
        for y in range(player_y, player_y + 2):
            hitboxes[(x,y)] = 1
    return hitboxes

def slide_hitbox(hitboxes):
    for x in range(player_x, player_x + 2):
        for y in range(player_y, player_y + 2):
            del hitboxes[(x,y)]
    for x in range(player_x + 2, player_x + 4):
        for y in range(player_y + 2, player_y + 4):
            hitboxes[(x,y)] = 1
    return hitboxes

def make_times_list():
    global object_count, length_apart
    times_list = []
    spread_value = int(590/object_count)
    for i in range(object_count):
        times_list.append(spread_value * i)
    for x, value in enumerate(times_list):
        times_list[x] = value + random.randint(-5,5)
    return times_list, False

def make_level(times_list):
    enemy_list = []
    for value in times_list:
        enemy = random.randint(0,3)
        if enemy == 3:
            enemy = random.randint(0,3)
        enemy_list.append([value,enemy])
    return enemy_list

def place_enemy(enemy, grid):
    global gunner
    if enemy == 0:
        height = random.randint(0,1)
        y_pos = 10 + height * 2
        x_pos = 31
        grid[y_pos][x_pos][0] = True
    elif enemy == 1:
        y_pos = 12
        x_pos = 31
        grid[y_pos][x_pos][1] = True
    elif enemy == 2:
        y_pos = 10
        x_pos = 31
        grid[y_pos][x_pos][2] = True
        gunner = True
    elif enemy == 3:
        y_pos = -1
        x_pos = random.randint(0,16)
        grid[y_pos][x_pos][3] = True
        grid[y_pos][x_pos][5][0] = (x_pos * grid_size)
        grid[y_pos][x_pos][5][1] = (y_pos * grid_size)
    return grid

def move_background():
    global background_x, background_ground, screen_width, player_position
    background_x -= player_speed * pixel_standard * game_speed / 5
    background_ground -= player_speed * pixel_standard * game_speed
    if background_x % 6 == 0:
        player_position += 1
    if background_x <= ((0 - screen_width) + 10):
        background_x = 0
    if background_ground <=((0 - screen_width) + 10):
        background_ground = 0

def update_positions(grid):
    global pixel_standard, game_speed, player_speed, gunner
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x][0]:
                grid[y][x][5][0] += pixel_standard * game_speed * player_speed
                new_x = min(31 - int(grid[y][x][5][0]/grid_size - 1/(player_speed*4)), 31)
                if new_x < -5:
                    new_x = -5
                if new_x != x:
                    grid[y][new_x] = grid[y][x]
                    grid[y][x] = [False, False, False, False, False, [0,0]]
            elif grid[y][x][2]:
                grid[y][x][5][0] += pixel_standard * game_speed * player_speed - .25
                new_x = min(31 - int(grid[y][x][5][0]/grid_size - 1/(player_speed*4)), 31)
                if new_x <= 10:
                    gunner = False
                else:
                    gunner = True
                if new_x < -5:
                    new_x = -5
                if new_x != x:
                    grid[y][new_x] = grid[y][x]
                    grid[y][x] = [False, False, False, False, False, [0,0]]

            elif grid[y][x][1] or grid[y][x][4]: #checks for runner or bullet
                grid[y][x][5][0] += pixel_standard * game_speed * player_speed * 2
                new_x = min(31 - int(grid[y][x][5][0]/grid_size - 1/(player_speed*4)), 31)
                if new_x < -5:
                    new_x = -5
                if new_x != x:
                    grid[y][new_x] = grid[y][x]
                    grid[y][x] = [False, False, False, False, False, [0,0]]
            elif grid[y][x][3]: #checks if blade
                grid[y][x][5][0] += pixel_standard * game_speed * player_speed
                new_x = min(31 - int(grid[y][x][5][0]/grid_size - 1/(player_speed*4)), 31)
                if new_x < -5:
                    new_x = -5
                grid[y][x][5][1] += pixel_standard * game_speed * .75
                new_y = max(int(grid[y][x][5][1]/grid_size - 1/(player_speed*4)), 0)
                if new_y > 17:
                    new_y = 17
                if new_y != y:
                    if new_x != x:
                        grid[new_y][new_x] = grid[y][x]
                        grid[y][x] = [False, False, False, False, False, [0,0]]
                    else:
                        grid[new_y][x] = grid[y][x]
                        grid[y][x] = [False, False, False, False, False, [0,0]]
                else:
                    if new_x != x:
                        grid[y][new_x] = grid[y][x]
                        grid[y][x] = [False, False, False, False, False, [0,0]]

            else:
                pass
    return grid

def draw_character(move_frames):
    global player_x, player_y, grid_size, background_x, screen_width, player_state, run_frames_list, run_placement_list, animation
    standing_position = [int(player_x * grid_size), int(player_y * grid_size)]
    sliding_position = [int(int(player_x) * grid_size), int(int(player_y + 2) * grid_size)]
    if player_state == 0: #if standing
        current_frame = int(animation) % (len(run_frames_list))
        standing_position = [int(player_x * grid_size) - run_placement_list[current_frame], int(player_y * grid_size)]
        screen.blit(run_frames_list[current_frame], (standing_position[0],standing_position[1]))
        # pygame.draw.rect(screen, (0,255,255), (standing_position[0],standing_position[1],int(grid_size * 2),int(grid_size *4))) #draw the dude
    if player_state == 1:
        if move_frames <= 2:
            screen.blit(jump_frames_list[0], (standing_position[0], standing_position[1] - 14))
        elif move_frames >= 57:
            screen.blit(jump_frames_list[0], (standing_position[0], standing_position[1]))
        else:
            screen.blit(jump_frames_list[1], (standing_position[0], standing_position[1])) #if jumping
         #draw the dude

    if player_state == 2: #if sliding
        if move_frames <= 2 or move_frames >= 58:
            screen.blit(slide_frames_list[0], (sliding_position[0], sliding_position[1] - 21))
        elif move_frames <= 4 or move_frames >= 56:
            screen.blit(slide_frames_list[1], (sliding_position[0], sliding_position[1]))
        else:
            screen.blit(slide_frames_list[2], (sliding_position[0], sliding_position[1]))
        # pygame.draw.rect(screen, (0,255,255), (sliding_position[0],sliding_position[1],int(grid_size * 4),int(grid_size *2))) #draw the dude
def draw_window(grid, move_frames):

    global player_x, player_y, grid_size, background_x, background_ground, screen_width, enemy_art_list
    ground_height = player_y - 4
    screen.fill((0,0,0))
    screen.blit(background, (int(background_x), 0))
    background2_x = screen_width + background_x
    screen.blit(background, (int(background2_x), 0))
    screen.blit(ground, (int(background_ground), 0))
    background2_ground = screen_width + background_ground
    screen.blit(ground, (int(background2_ground), 0))
    draw_character(move_frames)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x][0]: #drqaw obstacle
                position = [int(screen_width - grid[y][x][5][0]), int(y * grid_size)]
                screen.blit(enemy_art_list[0], (position[0],position[1]))
                # pygame.draw.rect(screen, (255,255,0), (position[0],position[1],int(grid_size *2),int(grid_size *2)))
            elif grid[y][x][1]:
                if grid[y][x][2]: #draw end of level if both are present, which i normally impossible
                    position = [int(screen_width - grid[y][x][5][0]), int(y * grid_size)]
                    pygame.draw.rect(screen, (0,0,100), (position[0],position[1],int(grid_size *2),int(grid_size *4))) #draw door
                    pygame.display.update()
                    return
                position = [int(screen_width - grid[y][x][5][0]), int(y * grid_size)]
                screen.blit(enemy_art_list[1],(position[0],position[1]))
                # pygame.draw.rect(screen, (255,0,0), (position[0],position[1],int(grid_size *2),int(grid_size *2)))
            elif grid[y][x][2]: #draw gunner
                position = [int(screen_width - grid[y][x][5][0]), int(y * grid_size)]
                screen.blit(enemy_art_list[2], (position[0],position[1]))
                # pygame.draw.rect(screen, (0,255,0), (position[0],position[1],int(grid_size *2),int(grid_size *2)))
            elif grid[y][x][3]: #draw blade
                position = [int(screen_width - grid[y][x][5][0]), int(grid[y][x][5][1])]
                screen.blit(enemy_art_list[3],(position[0],position[1]))
                # pygame.draw.rect(screen, (0,0,255), (position[0],position[1],int(grid_size *2),int(grid_size *2)))
            elif grid[y][x][4]: #draw bullet
                position = [int(screen_width - grid[y][x][5][0]), int(y * grid_size)]
                screen.blit(enemy_art_list[4], (position[0],position[1]))
                # pygame.draw.rect(screen, (255,0,255), (position[0],position[1],int(grid_size *1),int(grid_size *1)))
            else:
                pass
    pygame.display.update() #draw everything

def get_occupied(grid):
    occupied_positions = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x][4] == True:
                occupied_positions.append((x,y))
            elif grid[y][x] != [False, False, False, False, False, [0,0]]:
                occupied_positions.append((x,y))
                occupied_positions.append((x+1,y))
                occupied_positions.append((x,y+1))
                occupied_positions.append((x+1,y+1))
    return occupied_positions

def check_collision(occupied_positions, hitboxes):
    for value in occupied_positions:
        if value in hitboxes:
            return True
    return False

def fire_shot(grid):
    y = 11
    for x in range(len(grid[y]) - 1,10,-1):
        if grid[y-1][x][2] == True:
            grid[y][x][4] = True
            grid[y][x][5][0] = screen_width - (x-1)*grid_size
    return grid

def level_clear(grid, clear, x):
    if not clear:
        x = 31
        y = 10
        grid[y][x][1] = True
        grid[y][x][2] = True
        grid[y][x][5][0] = 0
        clear = True
    else:
        grid[10][x][5][0] += pixel_standard * game_speed * player_speed
        new_x = min(31 - int(grid[10][x][5][0]/grid_size - 1/(player_speed*4)), 31)
        if new_x != x:
            grid[10][new_x] = grid[10][x]
            grid[10][x] = [False, False, False, False, False, [0,0]]
            x = new_x
            if new_x <= 11:
                win_menu()
    return grid, clear, x

def main():
  global frame_speed, player_state, player_speed, player_position, gunner, animation, object_count, length_apart, difficulty
  object_count = (difficulty * 5) + 20
  length_apart = 10
  animation = 0
  player_position = 0
  grid = create_grid()
  hitboxes = create_hitbox()
  failed = True
  while failed:
      times_list, failed = make_times_list()
  times_list.sort()
  print(times_list)
  enemy_list = make_level(times_list)
  clock_time = 0
  frame_count = 0
  move_time = 60
  run = True
  placed = []
  reload_time = 0
  clear = False
  exit_pos = 0
  move_frames = 0

  while run:
      if player_position in times_list and player_position not in placed:
          print(player_position)
          placed.append(player_position)
          enemy_count = times_list.index(player_position)
          enemy = enemy_list[enemy_count][1]
          grid = place_enemy(enemy, grid)

      while clock_time/1000 < frame_speed:
          clock_time += clock.get_rawtime()
          clock.tick()
      frame_count += 1
      animation += .34
      score = (1/(.05 * animation)) * 3000
      frame_count = frame_count % 60
      clock_time = 0
      if gunner:
          reload_time += 1
          if reload_time >= 40:
              reload_time = 0
              grid = fire_shot(grid)
      if player_state != 0:
          move_frames += 1
          if move_frames == move_time:
              player_state = 0
              hitboxes.clear()
              create_hitbox()
      if player_position >= 590:
          grid, clear, exit_pos = level_clear(grid, clear, exit_pos)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_w:
                  if player_state == 0:
                      player_state = 1
                      move_frames = 0
                      hitboxes = jump_hitbox(hitboxes)
              elif event.key == pygame.K_s:
                  if player_state == 0:
                      player_state = 2
                      move_frames = 0
                      hitboxes = slide_hitbox(hitboxes)
          elif event.type == pygame.MOUSEBUTTONDOWN:
              if event.button == 4: #if scrolling up
                  player_speed = min(player_speed * 1.189, 2)
              elif event.button == 5: #if scrolling down
                  player_speed = max(player_speed / 1.189, .5)
      move_background()
      if not clear:
          grid = update_positions(grid)
      draw_window(grid, move_frames)
      occupied_positions = get_occupied(grid)
      if check_collision(occupied_positions, hitboxes):
          run = False
          death_menu()

# main()
start_menu()
main()
