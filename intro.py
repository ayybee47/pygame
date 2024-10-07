import pygame, sys, random
from sys import exit
pygame.init()
clock = pygame.time.Clock()

#main window
screen_width = 1280
screen_length = 600
screen = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption("PONG")


#game rectangles
ball = pygame.Rect(screen_width/2 - 10,screen_length/2 - 10, 15,15)
player = pygame.Rect(screen_width - 20, screen_length - 500 ,10, 100)
opponent = pygame.Rect(10, screen_length - 500,10, 100)


#color
bg_color = pygame.Color("grey12")
light_gray = (200,200,200)
green = (0, 255,0)
white =( 255, 255, 255)


#game variables
ball_speed_x = 5  
ball_speed_y = 5 
player_speed = 0
opponent_speed = 4
 

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_length/2)
    
    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_gray)
        screen.blit(number_three, (screen_width/2 + 20, screen_length/2 + -10))
    
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, light_gray)
        screen.blit(number_two, (screen_width/2 +20, screen_length/2 -10))
    
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, light_gray)
        screen.blit(number_one, (screen_width/2 +20, screen_length/2 -10))


    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_x = 6*random.choice((1,-1))
        ball_speed_y = 5*random.choice((1,-1))
        score_time = None
    
    


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    #lot of global statements generally bad for program, in a well designed program 
    #use return statements or make specific classes of balls

    ball.x += ball_speed_x 
    ball.y += ball_speed_y 

    if ball.top <= 0 or ball.bottom >= screen_length:
        ball_speed_y *= -1
    if ball.left <= 0:
        
        player_score +=1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        
        opponent_score +=1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
         ball_speed_x *= -1
        


def player_anim():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_length:
        player.bottom = screen_length

def opponent_anim():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.top > ball.y:
        opponent.top -= opponent_speed

    
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_length:
        opponent.bottom = screen_length


#text variables

player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

#score timer
score_time = None


# operations

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
 
    

    #game logic
    ball_animation()
    
    player_anim()
    
    opponent_anim()
    
   

    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_gray, player)
    pygame.draw.rect(screen,light_gray, opponent)
    pygame.draw.ellipse(screen, green, ball)
    pygame.draw.aaline(screen,light_gray, (screen_width/2,0), (screen_width/2,screen_length))

    # successive elements are drawn on top of another
    if score_time:
        ball_restart()
    player_text = game_font.render(f"{player_score}", True, white)
    screen.blit(player_text,(660,350)) # blit puts one surface on another
    
    opponent_text = game_font.render(f"{opponent_score}", False, white)
    screen.blit(opponent_text,(602,350))
    # framerate        
    pygame.display.update()
    clock.tick(60)

