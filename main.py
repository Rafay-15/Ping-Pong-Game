import pygame, sys,random
pygame.init()
clock = pygame.time.Clock()


def ball_movement():
    global ball_speed_x,ball_speed_y,player1_score,player2_score
    ball.x+=ball_speed_x
    ball.y+=ball_speed_y
    if ball.top<=0 or ball.bottom>=screen_height:
        sound.play()
        ball_speed_y*=-1
    if ball.left<=0:
     game_over_sound.play()
     ball_reset()
     player1_score+=1
    if ball.right>=screen_width:
        game_over_sound.play()
        ball_reset()
        player2_score+=1
    if ball.colliderect(player1)or ball.colliderect(player2):
        ball_speed_x*=-1
        sound.play()




def ball_reset():
    global ball_speed_x,ball_speed_y
    if ball.left<=0 or ball.right>=screen_width:
        ball.x=screen_width/2-15
        ball.y=screen_height/2-15
        pygame.event.get()
        ball_speed_y=0
        ball_speed_x=0



def draw_score():
    player1_text = game_font.render(f"{player1_score}", True, (0, 0, 250))
    screen.blit(player1_text, (310, 350))
    player2_text = game_font.render(f"{player2_score}", True, (0, 0, 250))
    screen.blit(player2_text, (280, 350))



def players_animations():
    player1.y += player1_speed
    player2.y += player2_speed
    if player1.top<=0:
        player1.top=0
    if player1.bottom>=screen_height:
        player1.bottom=screen_height
    if player2.top<=0:
        player2.top=0
    if player2.bottom>=screen_height:
        player2.bottom=screen_height



screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ping Pong')
blue=(0,0,250)
ball=pygame.Rect(screen_width/2-15,screen_height/2-15,20,20)
player2=pygame.Rect(0,200,10,100)
player1=pygame.Rect(590,200,10,100)
ball_speed_x = 0
ball_speed_y = 0
player1_speed = 0
player2_speed = 0
player1_score = (0)
player2_score = (0)
game_font=pygame.font.Font(None,25)
background=pygame.image.load('graphics/background_image.jpg')
sound=pygame.mixer.Sound('graphics/bat_hit_ball.wav')
game_over_sound=pygame.mixer.Sound('graphics/game_over_sound.wav')
#start screen
start_screen = False

while start_screen == False:

    title_screen = pygame.image.load('graphics/pong_intro.png')
    title_screen= pygame.transform.scale(title_screen, (screen_width, screen_height))
    screen.blit(title_screen, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                start_screen = True
#Main Loop To run the Game
while  start_screen == True:
    ball_speed_x == 0 and ball_speed_y == 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                ball_speed_x=random.choice((1,-1))*5
                ball_speed_y=random.choice((1,-1))*5

            if event.key==pygame.K_DOWN:
                player1_speed+=7
            if event.key==pygame.K_UP:
                player1_speed-=7
            if event.key==pygame.K_w:
                player2_speed-=7
            if event.key==pygame.K_s:
                player2_speed+=7
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                player1_speed-=7
            if event.key==pygame.K_UP:
                player1_speed+=7
            if event.key==pygame.K_w:
                player2_speed+=7
            if event.key==pygame.K_s:
                player2_speed-=7




    screen.fill('green')
    screen.blit(background,(0,0))
    ball_movement()
    players_animations()
    pygame.draw.rect(screen,blue,player2)
    pygame.draw.rect(screen,blue,player1)
    pygame.draw.ellipse(screen,(250,0,0),ball)
    pygame.draw.aaline(screen,(0,0,200),(screen_width/2,0),(screen_width/2,screen_height))
    draw_score()
    pygame.display.flip()
    clock.tick(60)