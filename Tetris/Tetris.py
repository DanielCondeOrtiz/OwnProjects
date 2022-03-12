import pygame
from Piece import Piece
from Bottom import Bottom

x_left=187
y_top=94
y_bottom = 385
x_right = 315
size = 13

def main():

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 468))

    imageleft = pygame.image.load('tetrisleft.png')
    imagemiddle = pygame.image.load('tetrismiddle.png')
    imageright = pygame.image.load('tetrisright.png')

    images = []
    images.append(imageleft)
    images.append(imagemiddle)
    images.append(imageright)


    pygame.font.init()
    myfont = pygame.font.SysFont('ArcadeClassic', 30)

    done = False

    bottom = Bottom()
    object = None
    next_object = None
    count=1
    lines = 0
    columns = 11

    total = []

    pause = False
    start = False

    for i in range(0,7):
        total.append(0)

    while not done:
        move = None
        rotate = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE  and start:
                pause = not pause

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE  and start:
                rotate = True
                object.rotate()


        if not pause and start:
            move = 0
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: move = 1
            if pressed[pygame.K_DOWN]: move = 2
            if pressed[pygame.K_LEFT]: move = 3
            if pressed[pygame.K_RIGHT]: move = 4

            done_block = object.move(move, count, bottom)

            if done_block:
                bottom.add(object)
                object = next_object
                next_object = None

            if next_object == None:
                next_object = Piece(columns)

                if object.type == 1:
                    total[0] +=1
                elif object.type == 2:
                    total[5] +=1
                elif object.type == 3:
                    total[1] +=1
                elif object.type == 4:
                    total[6] +=1
                elif object.type == 5:
                    total[3] +=1
                elif object.type == 6:
                    total[4] +=1
                elif object.type == 7:
                    total[2] +=1

            count +=1
            if count == 1201:
                count = 1

            textarray = []
            position_text = []

            for i in range (0,7):
                textarray.append(myfont.render(f'{total[i]:03}', False, (255, 255, 255)))
                position_text.append([96,177 + 31*i])

            textarray.append(myfont.render(f'{lines:02}', False, (255, 255, 255)))
            position_text.append([306 + 14*(columns-11),40])

            silu = bottom.silu(object,move,rotate)

            fps = myfont.render(str(clock.get_fps()), False, (255, 255, 255))

            clock.tick(30)

            draw(bottom, object,screen, images,columns,textarray,position_text,next_object, silu,fps)

            if done_block:
                lines +=  bottom.check_lines()
                pygame.time.wait(150)

                if not done:
                    done = bottom.finish()

        elif pause:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            button = 0

            if mouse[0] > 160 and mouse[0] < 340 and mouse[1] > 60 and mouse[1] < 130:
                button = 1
                if click[0] == 1:
                     pause = False
            elif mouse[0] > 160 and mouse[0] < 340 and mouse[1] > 190 and mouse[1] < 260:
                button = 2
                if click[0] == 1:
                    bottom = Bottom()
                    bottom.set_columns(columns)
                    object = Piece(columns)
                    next_object = None
                    count=1
                    lines = 0

                    total = []

                    pause = False

                    for i in range(0,7):
                        total.append(0)

            elif mouse[0] > 160 and mouse[0] < 340 and mouse[1] > 330 and mouse[1] < 400:
                button = 3
                if click[0] == 1:
                    done = True

            clock.tick(30)
            pause_game(screen,button)

        elif not start:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            button = 0

            if mouse[0] > 160 and mouse[0] < 340 and mouse[1] > 60 and mouse[1] < 130:
                button = 1
                if click[0] == 1:
                     start = True
                     screen = pygame.display.set_mode((500 + 14*(columns-11), 468))
                     bottom.set_columns(columns)
                     object = Piece(columns)


            elif mouse[0] > 86 and mouse[0] < 150 and mouse[1] > 190 and mouse[1] < 260:
                button = 4
                if  click[0] == 1 and columns > 11:
                    columns -=1

            elif mouse[0] > 345 and mouse[0] < 410 and mouse[1] > 190 and mouse[1] < 260:
                button = 2
                if click[0] == 1:
                    columns += 1


            elif mouse[0] > 160 and mouse[0] < 340 and mouse[1] > 330 and mouse[1] < 400:
                button = 3
                if click[0] == 1:
                    done = True

            clock.tick(30)
            start_screen(screen,button, columns)


def draw(bottom,object, screen, images,columns,textarray,position_text,next_object, silu, fps):
    screen.fill((0,0,0))
    screen.blit(images[0], (0,0))

    for i in range(0,columns -10):
        screen.blit(images[1], (186 + 14*i,0))

    screen.blit(images[2], (200 + 14*(columns-11),0))

    for j in range(1,23):
        pygame.draw.line(screen, (40,40,40), [x_left, y_top + 14*j -1], [x_right+27 + 14*(columns-11), y_top + 14*j-1], 1)

    pygame.draw.line(screen, (40,40,40), [x_left, y_top + 14*22 +3], [x_right+27 + 14*(columns-11), y_top + 14*22 + 3], 8)

    for i in range(1,columns):
        pygame.draw.line(screen, (40,40,40), [x_left+14*i-1, y_top], [x_left+14*i-1, y_bottom+ 23], 1)


    for i in range(len(textarray)):
        screen.blit(textarray[i], position_text[i])

    #screen.blit(fps, [0,0])

    for theobject in bottom.get_all():
        for square in theobject.pos:
            if square[2] == 0:
                pygame.draw.rect(screen, theobject.color, pygame.Rect(square[0],square[1], 13, 13))

    if object is not None:
        for square in object.pos:
            pygame.draw.rect(screen, object.color, pygame.Rect(square[0],square[1], 13, 13))

    if silu is not None:
        for square in silu.pos:
            pygame.draw.rect(screen, silu.color, pygame.Rect(square[0],square[1], 11, 11),2)

    if next_object is not None:
        if next_object.type == 4:
            sumx = 135
        elif next_object.type == 5:
            sumx = 145
        else:
            sumx = 140

        for square in next_object.pos:
            pygame.draw.rect(screen, next_object.color, pygame.Rect(square[0]+sumx - (round((columns -11)/2)*14) + 14*(columns-11),square[1]+140, 13, 13))

    pygame.display.flip()

def pause_game(screen,button):
    screen.fill((0,0,0))

    if button == 1:
        pygame.draw.rect(screen, (100,100,255), pygame.Rect(166,66, 166, 66))
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(166,198, 166, 66))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(166,330, 166, 66))
    elif button == 2:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(166,66, 166, 66))
        pygame.draw.rect(screen, (100,255,100), pygame.Rect(166,198, 166, 66))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(166,330, 166, 66))
    elif button == 3:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(166,66, 166, 66))
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(166,198, 166, 66))
        pygame.draw.rect(screen, (255,100,100), pygame.Rect(166,330, 166, 66))
    else:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(166,66, 166, 66))
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(166,198, 166, 66))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(166,330, 166, 66))


    myfont = pygame.font.SysFont('ArcadeClassic', 35)
    screen.blit(myfont.render("Continue", False, (0, 0, 0)),(173,79))
    screen.blit(myfont.render("Restart", False, (0, 0, 0)),(186,210))
    screen.blit(myfont.render("Quit", False, (0, 0, 0)),(208,342))

    pygame.display.flip()

def start_screen(screen,button,columns):
    s = pygame.Surface((500,468))
    s.fill((0,0,0))

    screen.blit(s, (0, 0))

    if button == 1:
        pygame.draw.rect(screen, (100,100,255), pygame.Rect(166,66, 166, 66))
        pygame.draw.rect(screen, (23, 73, 26), pygame.Rect(166,198, 166, 66))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(166,330, 166, 66))
        pygame.draw.rect(screen, (41, 141, 155), pygame.Rect(352,198, 60, 66))
        pygame.draw.rect(screen, (196, 9, 96), pygame.Rect(86,198, 60, 66))
    elif button == 2:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(166,66, 166, 66))
        pygame.draw.rect(screen, (23, 73, 26), pygame.Rect(166,198, 166, 66))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(166,330, 166, 66))
        pygame.draw.rect(screen, (55, 185, 204), pygame.Rect(352,198, 60, 66))
        pygame.draw.rect(screen, (196, 9, 96), pygame.Rect(86,198, 60, 66))
    elif button == 4:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(166,66, 166, 66))
        pygame.draw.rect(screen, (23, 73, 26), pygame.Rect(166,198, 166, 66))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(166,330, 166, 66))
        pygame.draw.rect(screen, (41, 141, 155), pygame.Rect(352,198, 60, 66))
        pygame.draw.rect(screen, (255, 10, 124), pygame.Rect(86,198, 60, 66))
    elif button == 3:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(166,66, 166, 66))
        pygame.draw.rect(screen, (23, 73, 26), pygame.Rect(166,198, 166, 66))
        pygame.draw.rect(screen, (255,100,100), pygame.Rect(166,330, 166, 66))
        pygame.draw.rect(screen, (41, 141, 155), pygame.Rect(352,198, 60, 66))
        pygame.draw.rect(screen, (196, 9, 96), pygame.Rect(86,198, 60, 66))
    else:
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(166,66, 166, 66))
        pygame.draw.rect(screen, (23, 73, 26), pygame.Rect(166,198, 166, 66))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(166,330, 166, 66))
        pygame.draw.rect(screen, (41, 141, 155), pygame.Rect(352,198, 60, 66))
        pygame.draw.rect(screen, (196, 9, 96), pygame.Rect(86,198, 60, 66))


    myfont = pygame.font.SysFont('ArcadeClassic', 35)
    myfontlittle = pygame.font.SysFont('ArcadeClassic', 28)
    arial = pygame.font.SysFont('Arial', 35)
    screen.blit(myfont.render("Start", False, (0, 0, 0)),(203,79))
    screen.blit(myfontlittle.render(str(columns) + " columns", False, (0, 0, 0)),(177,215))
    screen.blit(arial.render("+", False, (0, 0, 0)),(372,210))
    screen.blit(arial.render("-", False, (0, 0, 0)),(111,210))
    screen.blit(myfont.render("Quit", False, (0, 0, 0)),(208,342))

    pygame.display.flip()

if __name__== "__main__":
  main()
