'''welcome to my paddle ball game most of the source code is obtained from the
python book "Hello World"; however, a lot of it his been altered to make the game
more fun and interacitve. Enjoy! - Yossi Gisis 4/28/2023'''

import pygame, sys
from random import choice

"""
Class for ball sprite, utilizes pygame Sprite superclass. This modified version
changes out a ball image with a surface object function to give the game a more 
retro look.
"""
class Ball(pygame.sprite.Sprite):
    def __init__(self, speed, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([15, 15])
        image_surface.fill([255, 255, 255])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    """
    This block detects collisions with the left, top and right boundries. Collisons with 
    the paddle and bottom are later. When there is a collision in the x or y vector, x or y
    velocity is reversed. 
    """

    def move(self):
        if not done:
            self.rect = self.rect.move(self.speed)
            if self.rect.left < 0 or self.rect.right > screen.get_width():
                self.speed[0] = - self.speed[0]
            if self.rect.top <= 0:
                self.speed[1] = - self.speed[1]

"""
Class for paddle sprite, utilizes the pygame sprite superclass.
This class takes paddle width as an argument to allow for a decrease in the paddle size 
to increase difficulty. 
"""
class Paddle(pygame.sprite.Sprite):
    def __init__(self, paddle_width, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([paddle_width, 5])
        image_surface.fill([255, 255, 255])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()

display_size = (screen_width, screen_height) = (640, 480)
screen = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()
#choice sets the ball in a right or left direction
ball_speed = [choice([-5, 5]), 3]
"""
Initializes a ball, paddle, and group object. The ball's location is randomized to eleven potential
starting points.
The paddle_wid variable controls the difficulty by decreasing the width of the paddle everytime the timer
is set off.
"""
myBall = Ball(ball_speed, [choice([50, 185, 215, 245, 275, \
                        305, 335, 365, 395, 425, 575]), 30])
ballGroup = pygame.sprite.Group(myBall)
paddle_wid = 125
paddle = Paddle(paddle_wid, (((screen_width - paddle_wid) // 2), (screen_height - 30)))
lives = 5
#sets font for score board
score = 0
score_banner = 'score:  ' + str(score)
score_font = pygame.font.Font(None, 35)
score_surf = score_font.render(score_banner, 1, (255, 255, 255))
score_pos = [10, 10]
#allows user to hold down directional key
pygame.key.set_repeat(1, 10)
#variable controls frame rate to increase dificulty
rate_initial = 80
#this creates an event to increase the difficulty every 12 seconds. 24 is the first available USEREVENT
pygame.time.set_timer(24, 12000)


#done tests if the user is out of lives and displays the GAME OVER message if true
done = False

#the code below flashes a "get ready" message for the player
screen.fill([0, 0, 30])
for i in range(6):
    for k in range(140):
        ready_font = pygame.font.Font(None, 70)
        ready_surf = ready_font.render('GET READY!', 1, (255, 255, 255))
        screen.blit(ready_surf, [screen_width // 2 - \
                            ready_surf.get_width()//2, 200])
        pygame.display.flip()
    for j in range(80):
        screen.fill([0, 0, 30])
        pygame.display.flip()

#this is the start of the main program loop         
running = True
while running:
    #rate_intial increaes every 12 seconds
    clock.tick(rate_initial)
    screen.fill([0, 0, 30])

    #event input segment
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #event input for paddle movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and paddle.rect.right <= screen.get_width():
                paddle.rect.centerx = paddle.rect.centerx + 7
            elif event.key == pygame.K_LEFT and paddle.rect.left >= 0:
                paddle.rect.centerx = paddle.rect.centerx - 7
        #timed event to increase difficulty
        #tests if event.type (24) is true and if the player has any lives left
        elif event.type == pygame.USEREVENT and done == False:
            #increments frame rate by 6 every 12 seconds
            rate_initial = rate_initial + 6
            #slowly decreases paddle width my 4 pixels until the paddle reaches 75 pixels
            if paddle_wid > 75:
                paddle_wid = paddle_wid - 4
            #the variable below ensures the paddle is blitted into the position it was before
            previous_pos = paddle.rect.left
            #creates a new paddle object
            #previous_pos + 2 shrinks the paddle by 2 pixels on each side
            paddle = Paddle(paddle_wid,[(previous_pos + 2), 450])

    #checks if the ball hit the paddle and if it has hit the side. the and condition checks\
    #if the bottom of the ball is below the top of the paddle. note that 454 is not not the top\
    #of the paddle. when the integer is set to 450 the ball always passes through the paddle. \
    #note this number changes as the speed of the ball changes. when the ball hits the "side"\
    #of the paddle, the balls x speed reverses and falls off the screen. For collisions with the\
    #top of the paddle reverses the balls y speed. a collision with the paddle also results in an\
    #increment of the score count, and an update of the score_banner and score_surf
    if not done:
        if pygame.sprite.spritecollide(paddle, ballGroup, False)and myBall.rect.bottom > 454:
            myBall.speed[0] = - myBall.speed[0]
        elif pygame.sprite.spritecollide(paddle, ballGroup, False):
            myBall.speed[1] = - myBall.speed[1]
    
            score = score + 10
            score_banner = 'score:  ' + str(score)
            score_surf = score_font.render(score_banner, 1, (255, 255, 255))
    #after checking for events and collisions with the paddle, the self.move function is called\
    #which moves the ball and checks for collisions
    myBall.move()

    #while the player still has lives the ball, paddle, and score board is blitted
    if not done:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_surf, score_pos)
        #creates balls in top right corner to represent remaining lives and blits them
        for i in range (lives):
            width = screen.get_width()
            screen.blit(myBall.image, [width - 30 * i, 20])
        #refreshes display 
        pygame.display.flip()

    #checks if the ball has fallen off the screen and deducts lives if true
    if myBall.rect.top >= screen.get_rect().bottom:
        lives = lives - 1

        #when the player runs out of lives the game over message is displayed
        if lives == 0:
            #myBall.rect.left, myBall.rect.top = [0, 0]
            final_text1 = 'GAME OVER!'
            final_text2 = 'Your final score is: ' + str(score)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(final_text1, 1, (255, 255, 255))
            ft2_font = pygame.font.Font(None, 70)
            ft2_surf = ft2_font.render(final_text2, 1, (255, 255, 255))
            screen.blit(ft1_surf, [screen.get_width()//2 - \
                                   ft1_surf.get_width()//2, 100])
            screen.blit(ft2_surf, [screen.get_width()//2 - \
                                   ft2_surf.get_width()//2, 200])
            pygame.display.flip()
            #once done is assigned true, the program no longer blits the paddle, ball, and scoreboard\
            #and the game over message remains  until the window is closed
            done = True
        #while the player still has lives remaining a get ready messsage is flashed and a new paddle\
        #is created at the center and a new is initialized
        else:
            if not done:
                screen.fill([0, 0, 30])
                for i in range(3):
                    for k in range(140):
                        ready_font = pygame.font.Font(None, 70)
                        ready_surf = ready_font.render('GET READY!', 1, (255, 255, 255))
                        screen.blit(ready_surf, [screen.get_width()//2 - \
                                            ready_surf.get_width()//2, 200])
                        pygame.display.flip()
                    for j in range(80):
                        screen.fill([0, 0, 30])
                        pygame.display.flip()
                paddle = Paddle(paddle_wid, [270, 450])
                screen.blit(paddle.image, paddle.rect)
            myBall = Ball(ball_speed, [choice([185, 215, 245, 275, 305, 335, 365, 395, 425]), 50])
            ballGroup.add(myBall)

#the window closing function is called
pygame.quit()
