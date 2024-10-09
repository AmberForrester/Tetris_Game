import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render('Score', True, Colors.white)
next_surface = title_font.render('Next', True, Colors.white)
game_over_surface = title_font.render('GAME OVER!', True, Colors.white)
play_again_surface = title_font.render('Play Again?', True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
play_again_rect = pygame.Rect(330, 500, 140, 50)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption('Python Tetris')

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
GAME_OVER_FLASH = pygame.USEREVENT + 1
PLAY_AGAIN_DELAY = pygame.USEREVENT + 2

pygame.time.set_timer(GAME_UPDATE, 300)
pygame.time.set_timer(GAME_OVER_FLASH, 500)

game_over_visible = True
show_play_again = False
play_again_timer_started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and game.game_over:
            game.game_over = False
            game.reset()
            show_play_again = False
            play_again_timer_started = False
            pygame.mixer.music.play(-1)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()

        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

        if event.type == GAME_OVER_FLASH and game.game_over:
            game_over_visible = not game_over_visible
            if not play_again_timer_started:
                pygame.time.set_timer(PLAY_AGAIN_DELAY, 1200)
                play_again_timer_started = True

        if event.type == PLAY_AGAIN_DELAY:
            show_play_again = True
            pygame.time.set_timer(PLAY_AGAIN_DELAY, 0)

        if event.type == pygame.MOUSEBUTTONDOWN and game.game_over and show_play_again:
            if play_again_rect.collidepoint(event.pos):
                game.game_over = False
                game.reset()
                show_play_again = False  
                play_again_timer_started = False
                pygame.mixer.music.play(-1)

    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over and game_over_visible:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    # Draw the "Play Again?" button if the game is over and the delay has expired
    if game.game_over and show_play_again:
        play_again_text_rect = play_again_surface.get_rect(centerx=score_rect.centerx, centery=550)
        screen.blit(play_again_surface, play_again_text_rect)

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)