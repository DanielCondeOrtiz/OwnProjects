from Grid import Grid
import pygame

def main():

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((900, 600))

    pygame.font.init()
    myfont = pygame.font.SysFont('ArcadeClassic', 30)

    count = 0
    done = False

    pause = False
    start = False
    lost= False
    grid = Grid()

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE  and start:
                pause = not pause

        if not pause and start and not lost:
            move = 0
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: move = 1
            if pressed[pygame.K_DOWN]: move = 2
            if pressed[pygame.K_LEFT]: move = 3
            if pressed[pygame.K_RIGHT]: move = 4

            count +=1
            if count == 1201:
                count = 1

            finish = grid.move(move,count)

            if finish:
                lost = True

            #fps = myfont.render(str(clock.get_fps()), False, (255, 255, 255))

            clock.tick(30)

            draw(screen,grid)

            #pygame.time.wait(150)


        elif pause:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            button = 0

            if mouse[0] > 280 and mouse[0] < 620 and mouse[1] > 75 and mouse[1] < 180:
                button = 1
                if click[0] == 1:
                     pause = False
            elif mouse[0] > 280 and mouse[0] < 620 and mouse[1] > 245 and mouse[1] < 350:
                button = 2
                if click[0] == 1:
                    grid = Grid()
                    pause = False

            elif mouse[0] > 280 and mouse[0] < 620 and mouse[1] > 415 and mouse[1] < 520:
                button = 3
                if click[0] == 1:
                    done = True

            clock.tick(30)
            pause_game(screen,button)

        elif not start:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            button = 0

            if mouse[0] > 280 and mouse[0] < 620 and mouse[1] > 100 and mouse[1] < 260:
                button = 1
                if click[0] == 1:
                    start = True

            elif mouse[0] > 280 and mouse[0] < 620 and mouse[1] > 280 and mouse[1] < 500:
                button = 3
                if click[0] == 1:
                    done = True

            clock.tick(30)
            start_screen(screen,button)

        elif lost:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            button = 0

            if mouse[0] > 80 and mouse[0] < 420 and mouse[1] > 340 and mouse[1] < 500:
                button = 1
                if click[0] == 1:
                    grid = Grid()
                    lost = False

            elif mouse[0] > 480 and mouse[0] < 820 and mouse[1] > 340 and mouse[1] < 500:
                button = 3
                if click[0] == 1:
                    done = True

            clock.tick(30)
            lost_screen(screen,button,grid.length)


def draw(screen,grid):
    screen.fill((0,0,0))

    myfont = pygame.font.SysFont('ArcadeClassic', 300)
    screen.blit(myfont.render(str(grid.length - 1), False, (50, 50, 50)),(300,150))

    i=0
    for row in grid.current:
        j=0
        for square in row:
            if square != 0:
                pygame.draw.rect(screen, (round((square/600)*255),round((square/600)*255),round((square/600)*255)), pygame.Rect(30*i,30*j, round((square/600)*30), round((square/600)*30)))
            j+=1
        i+=1
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(grid.apple[0]*30,grid.apple[1]*30, 30, 30))

    pygame.display.flip()

def pause_game(screen,button):
    screen.fill((0,0,0))

    if button == 1:
        pygame.draw.rect(screen, (100,100,255), pygame.Rect(300,85, 300, 85))
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(300,255, 300, 85))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(300,425, 300, 85))
    elif button == 2:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(300,85, 300, 85))
        pygame.draw.rect(screen, (100,255,100), pygame.Rect(300,255, 300, 85))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(300,425, 300, 85))
    elif button == 3:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(300,85, 300, 85))
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(300,255, 300, 85))
        pygame.draw.rect(screen, (255,100,100), pygame.Rect(300,425, 300, 85))
    else:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(300,85, 300, 85))
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(300,255, 300, 85))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(300,425, 300, 85))


    myfont = pygame.font.SysFont('ArcadeClassic', 60)
    screen.blit(myfont.render("Continue", False, (0, 0, 0)),(320,95))
    screen.blit(myfont.render("Restart", False, (0, 0, 0)),(335,265))
    screen.blit(myfont.render("Quit", False, (0, 0, 0)),(380,435))

    pygame.display.flip()

def start_screen(screen,button):

    screen.fill((0,0,0))

    if button == 1:
        pygame.draw.rect(screen, (100,100,255), pygame.Rect(300,120, 300, 120))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(300,360, 300, 120))
    elif button == 3:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(300,120, 300, 120))
        pygame.draw.rect(screen, (255,100,100), pygame.Rect(300,360, 300, 120))
    else:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(300,120, 300, 120))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(300,360, 300, 120))


    myfont = pygame.font.SysFont('ArcadeClassic', 100)
    screen.blit(myfont.render("Start", False, (0, 0, 0)),(320,125))
    screen.blit(myfont.render("Quit", False, (0, 0, 0)),(350,365))

    pygame.display.flip()


def lost_screen(screen,button, score):

    screen.fill((0,0,0))

    myfont = pygame.font.SysFont('ArcadeClassic', 200)
    screen.blit(myfont.render("You lost", False, (255, 255, 255)),(60,40))

    myfont3 = pygame.font.SysFont('ArcadeClassic', 100)
    screen.blit(myfont3.render("Score " + str(score -1), False, (255, 255, 255)),(250,220))


    if button == 1:
        pygame.draw.rect(screen, (100,100,255), pygame.Rect(100,360, 300, 120))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(500,360, 300, 120))
    elif button == 3:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(100,360, 300, 120))
        pygame.draw.rect(screen, (255,100,100), pygame.Rect(500,360, 300, 120))
    else:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(100,360, 300, 120))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(500,360, 300, 120))


    myfont2 = pygame.font.SysFont('ArcadeClassic', 75)
    screen.blit(myfont2.render("Restart", False, (0, 0, 0)),(110,375))
    screen.blit(myfont2.render("Quit", False, (0, 0, 0)),(560,375))

    pygame.display.flip()

if __name__== "__main__":
  main()
