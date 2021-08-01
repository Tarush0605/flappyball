import sys, pygame, time
pygame.init()

screen_size = (screen_width, screen_height) = (800,600);

ball_size = (ball_width, ball_height) = (100,100);
speed = [3, 0];
acceleration = [0, .2];

white = (255,255,255);
black = (0,0,0);
score = 0;
max_score = 0;
font1 = pygame.font.Font('freesansbold.ttf', 32);
font2 = pygame.font.Font('freesansbold.ttf', 16);
text1 = font1.render('Score', True, black);
text2 = font2.render('Highscore', True, black);
text1_rect = text1.get_rect();
text2_rect = text2.get_rect();
text1_rect.center = (400,20);
text2_rect.center = (700,20);

screen = pygame.display.set_mode(screen_size);
pygame.display.set_caption('Football Game');

ball = pygame.image.load('football game/football.jpg');
ball = pygame.transform.scale(ball, ball_size);
ball_rectangle = ball.get_rect();
ball_rectangle = ball_rectangle.move((250, 100));

cnt=0;

while True:
    time.sleep(0.01);
    cnt = cnt+1;

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            sys.exit();
    
    speed[1] += acceleration[1];
    ball_rectangle = ball_rectangle.move(speed);
    if ball_rectangle.left <= 0 or ball_rectangle.right >= screen_width:
        speed[0] *= -1;
    if ball_rectangle.top <= 0:
        speed[1] *= -1;
    if ball_rectangle.bottom >= screen_height:
        speed[1] = -speed[1]+2;
        max_score = max(max_score, score);
        score = 0;

    ball_rectangle.left = max(ball_rectangle.left, 0);
    ball_rectangle.right = min(ball_rectangle.right, screen_width);
    ball_rectangle.top = max(ball_rectangle.top, 0);
    ball_rectangle.bottom = min(ball_rectangle.bottom, screen_height);

    if(cnt > 10):
        if event.type == pygame.MOUSEBUTTONDOWN:
            cnt=0;
            mouse_position = x,y = pygame.mouse.get_pos();
            # if(x < ball_rectangle.left + ball_width/2 and y > ball_rectangle.top + ball_height/2):
            #     speed[0] = abs(speed[0]);
            #     speed[1] = min(-7,speed[1]);
            #     score += 1;
            # elif(x > ball_rectangle.left + ball_width/2 and y > ball_rectangle.top + ball_height/2):
            #     speed[0] = -1*abs(speed[0]);
            #     speed[1] = min(-7,speed[1]);
            #     score += 1;
            if(x>ball_rectangle.left-20 and x<ball_rectangle.right+20 and y<ball_rectangle.bottom+20 and y>ball_rectangle.top-20):
                speed[1] = min(speed[1],-7);
                score += 1;

    text3 = font1.render(str(score), True, black);
    text4 = font2.render(str(max_score), True, black);
    text3_rect = text3.get_rect();
    text4_rect = text4.get_rect();
    text3_rect.center = (400,55);
    text4_rect.center = (700,45);

    screen.fill(white);
    screen.blit(ball, ball_rectangle);
    screen.blit(text1, text1_rect);
    screen.blit(text2, text2_rect);
    screen.blit(text3, text3_rect);
    screen.blit(text4, text4_rect);
    pygame.display.flip();
