import pygame
import random
import sys

pygame.init()
# GLOBAL VARIABLES
fps = 60
screen_len = 1327
screen_height = 1164
screen = pygame.display.set_mode((screen_len, screen_height))   # game window
# COLORS
red = (255, 0, 0)
yellow = (255, 255, 153)
lemon_green = (172, 230, 0)
green = (204, 255, 51)
game_sprites = {}
game_sounds = {}
g_logo = 'C:\Coding Stuff\Python\python prgs\python games\Dodge Ball\gallery\logo.jpg'
player = 'C:/Coding Stuff/Python/python prgs/python games/Dodge Ball/gallery/player.jpg'
bground = 'C:\Coding Stuff\Python\python prgs\python games\Dodge Ball\gallery/background.jpg'
opponent = {"opp1": 'C:\Coding Stuff\Python\python prgs\python games\Dodge Ball\gallery\opponent.png',
            "opp2": 'C:\Coding Stuff\Python\python prgs\python games\Dodge Ball\gallery\opponent.png',
            "opp3": 'C:\Coding Stuff\Python\python prgs\python games\Dodge Ball\gallery\opponent.png'}
ball_radius = 10
myfont = pygame.font.SysFont('arial', 10)   # use default system font, size 10


def welcome_screen():                   # for the front/home screen of the game
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:   # for player to press cross button of game window
                pygame.quit()           # quit from pygame module/lib
                sys.exit()              # quit the game program

            elif e.type == pygame.KEYDOWN:  # if any key is pressed to start the game
                return  # return and call the main_game() function

            else:
                # play the theme song
                game_sounds['Game_theme'].play()
                # blit logo image on game frame
                screen.blit(game_sprites['Logo'], (190, 0))
                screen_text_display('PRESS ANY KEY', green, 0, 0)
                pygame.display.update()
                fpsclock.tick(fps)


def main_game():    # main code of the game
    b1_x = 0
    b1_y = 0
    b2_x = 0
    b2_y = 0
    b3_x = 0
    b3_y = 0
    score = 0

    # POSITIONS
    # position of player on x-axis
    playerx = int(screen_len/205)
    # position of player on y-axis
    playery = int((screen_height - 181)/2)
    # position of opponent_1 on x-axis
    opponent1_x = int(screen_len/1.2)
    # position of opponent_1 on x-axis
    opponent1_y = int((screen_height - 181)/5.49)
    # position of opponent_2 on x-axis
    opponent2_x = int(screen_len/1.2)
    # position of opponent_2 on x-axis
    opponent2_y = int((screen_height - 181)/2.15)
    # position of opponent_3 on x-axis
    opponent3_x = int(screen_len/1.2)
    # position of opponent_3 on x-axis
    opponent3_y = int((screen_height - 181)/1.365)

    # VELOCITIES
    b1_velo = 0  # ball's velocity from opponent 1
    b2_velo = 0  # ball's velocity from opponent 2
    b3_velo = 0  # ball's velocity from opponent 3
    player_velo_x = 0
    player_velo_y = 0

    # GAME LOOP
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                # player's velocity and postion control
                if e.key == pygame.K_UP:
                    player_velo_y = -5
                    player_velo_x = 0

                if e.key == pygame.K_DOWN:
                    player_velo_y = 5
                    player_velo_x = 0

                if e.key == pygame.K_LEFT:
                    player_velo_x = -5
                    player_velo_y = 0

                if e.key == pygame.K_RIGHT:
                    player_velo_x = 5
                    player_velo_y = 0

            # ball's velocity and postion control
            # randomly genererate ball's position
            flag = random.randrange(1, 4)
            if flag == 1:
                b1_x = screen_len/1.2
                b1_y = 235
                b1_velo = -5
                        
            elif flag == 2:
                b2_x = screen_len/1.2
                b2_y = 515
                b2_velo = -5 

            elif flag == 3:
                b3_x = screen_len/1.2
                b3_y = 780
                b3_velo = -5  

        collision_test = iscollide(
            playerx, playery, b1_x, b1_y, b2_x, b2_y, b3_x, b3_y)
        if collision_test == True:
            screen.fill(yellow)  # screen is filled by light yellow color
            screen_text_display(
                "GAME OVER\nPLAY AGAIN? [y/n]", red, screen_len/2, screen_height/2)

        # MOVEMENT OF IMAGES ON SCREEN
        playerx += player_velo_x
        playery += player_velo_y
        b1_x += b1_velo
        b2_x += b2_velo
        b3_x += b3_velo

        # Bound the image motion within game screen
        if playerx < 5 or playerx >= screen_len:
            playerx = 0
        if playery <= 0 or playery >= screen_height - 10:
            playery = 0

        # BLITTING THE SPRITES ON GAME FRAME
        # blit bground image on game frame
        screen.fill((0,0,0))
        screen.blit(game_sprites['Bground'], (180, 163))
        # blit player image on game frame
        screen.blit(game_sprites['Player'], (playerx, playery))
        # blit opponent 1 on screen
        screen.blit(game_sprites['Opponent1'], (opponent1_x, opponent1_y))
        # blit opponent 1 on screen
        screen.blit(game_sprites['Opponent2'], (opponent2_x, opponent2_y))
        # blit opponent 1 on screen
        screen.blit(game_sprites['Opponent3'], (opponent3_x, opponent3_y))
        pygame.draw.circle(screen, lemon_green, (b1_x, b1_y), 20)
        pygame.draw.circle(screen, lemon_green, (b2_x, b2_y), 20)
        pygame.draw.circle(screen, lemon_green, (b3_x, b3_y), 20)

        pygame.display.update()
        fpsclock.tick(fps)

# to check the collition between the player and the ball
def iscollide(playerx, playery, b1_x, b1_y, b2_x, b2_y, b3_x, b3_y):
    # checking the coordinates of balls and player. If they become equal, the player has collided with the ball
    if b1_x == playerx + 10 and b1_y == playery + 10:
        game_sounds['Ball_hit'].play()
        return True

    if b2_x == playerx + 10 and b2_y == playery + 10:
        game_sounds['Ball_hit'].play()
        return True

    if b3_x == playerx + 10 and b3_y == playery + 10:
        game_sounds['Ball_hit'].play()
        return True


# to display text on game frame/screen
def screen_text_display(text, color, x, y):
    screen_text = myfont.render(text, True, red)    # for antialiasing (True)
    # for updating it all on game window/screen
    screen.blit(screen, (x, y))


if __name__ == '__main__':
    pygame.init()
    fpsclock = pygame.time.Clock()
    pygame.display.set_caption("DODGE BALL")

    # GAME IMAGES
    game_sprites['Player'] = pygame.image.load(player).convert(screen)
    game_sprites['Opponent1'] = pygame.image.load(
        opponent["opp1"]).convert_alpha()
    game_sprites['Opponent2'] = pygame.image.load(
        opponent["opp2"]).convert_alpha()
    game_sprites['Opponent3'] = pygame.image.load(
        opponent["opp3"]).convert_alpha()
    game_sprites['Bground'] = pygame.image.load(bground).convert_alpha()
    game_sprites['Logo'] = pygame.image.load(g_logo).convert_alpha()

    # GAME SOUNDS
    game_sounds['Game_theme'] = pygame.mixer.Sound(
        'C:\Coding Stuff\Python\python prgs\python games\Dodge Ball/audio/game_theme.mp3')
    game_sounds['Ball_hit'] = pygame.mixer.Sound(
        'C:\Coding Stuff\Python\python prgs\python games\Dodge Ball/audio/ball_hit.mp3')
    game_sounds['Ball_throw'] = pygame.mixer.Sound(
        'C:\Coding Stuff\Python\python prgs\python games\Dodge Ball/audio/swoosh.mp3')
    game_sounds['Game_over'] = pygame.mixer.Sound(
        'C:\Coding Stuff\Python\python prgs\python games\Dodge Ball/audio/game_over.mp3')

    while True:
        welcome_screen()
        main_game()
