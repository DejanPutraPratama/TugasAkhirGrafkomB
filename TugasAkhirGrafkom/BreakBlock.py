from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

fromRight = 1
fromLeft = 2
fromTop = 3
fromBottom = 4
windowWitdh = 800
windowHeight = 500
deltaX = 1
deltaY = 1
time_interval = 5

class block:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

ball = block(100, 100, 120, 120)
border = block(0, 0, windowWitdh, windowHeight)
Stick = block(370, 0, 470, 10) 
side1 = block(0, 0, 10, 280)
side2 = block(790, 0, 800, 280)
blockList = []
sidelist=[]
x = 15
y = 350
sideX=0
sideY=350

for i in range(0, 156):
    if (i % 13 == 0):
        x = 15
        y += 30
    if(i%39==0):
        y+=50

    blockList.append(block(x, y, x + 50, y + 20))
    x += 60

def defaultValues():
    global sidelist
    global blockList
    global x
    global y
    global move
    global pause
    global sideX
    global sideY
    blockList.clear()
    sidelist.clear()

    move=0
    pause = True
    x = 15
    y = 350

    for i in range(0, 156):
        if (i % 13 == 0):
            x = 15
            y += 30
        if (i % 39 == 0):
            y += 50
        blockList.append(block(x, y, x + 50, y + 20))
        x += 60

def init():
    glClearColor(255, 255, 255, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, windowWitdh, 0, windowHeight, 0, 1)  

    glMatrixMode(GL_MODELVIEW)

def Drawrectangleangle(rectangle,r,g,b):
    glLoadIdentity()
    glColor(0,0,255)

    glBegin(GL_QUADS)
    glVertex(rectangle.left, rectangle.bottom, 0)  # Left - Bottom
    glVertex(rectangle.right, rectangle.bottom, 0)
    glVertex(rectangle.right, rectangle.top, 0)
    glVertex(rectangle.left, rectangle.top, 0)
    glEnd()

def drawText(string, x, y):
    glLineWidth(2)
    glColor(0, 255, 0)  
    glLoadIdentity()  
    glTranslate(x, y, 0)
    glScale(0.13, 0.13, 1)
    string = string.encode()  
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def drawEndText(string, x, y):
    glLineWidth(2.5)
    glColor(255,0,0)  
    glLoadIdentity()  
    glTranslate(x, y, 0)
    glScale(0.15, 0.15, 1)
    string = string.encode()  
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def BallAndWall(ball, wall):  
    global fromRight
    global fromLeft
    global fromTop
    global fromBottom

    if ball.right >= wall.right-14:
        return fromRight
    if ball.left <= wall.left+14:
        return fromLeft
    if ball.top >= wall.top-14:
        return fromTop
    if ball.bottom <= wall.bottom:
        return fromBottom

def BallAndPlayer(ball, player):  
    if ball.bottom <= player.top and ball.left >= player.left and ball.right <= player.right:
        return True
    return False

exit = False

def keyboard(key, x, y):
    global pause
    global Lives
    global exit
    global score
    if key == b"q":
        exit = True
    elif key == b" ":
        pause = not pause
    elif key == b"p":
        glClearColor(0, 0, 0, 1)
        exit = False
        score=0
        Lives = 3
        defaultValues()

mouse_x = 0
def MouseMotion(x, y):
    global mouse_x
    mouse_x = x

def Timer(v):
    Display()

    glutTimerFunc(time_interval, Timer, 1)

Lives = 3
pause = True
score= 0
move=0

def Display():
    global score
    global Lives
    global playerResult
    global fromRight
    global fromLeft
    global fromTop
    global fromBottom
    global deltaX
    global deltaY
    global pause
    global blockList
    global move
    global sidelist

    if (Lives > 0 and exit == False):
        glClear(GL_COLOR_BUFFER_BIT)

        if (pause and Lives>0):
            string = "press space to play ' Q ' to exit"
            drawText(string, 250, 250)

        Drawrectangleangle(block(0,windowHeight-14,windowWitdh,windowHeight),0,0,1)
        Drawrectangleangle(block(0,windowHeight-120,14,windowHeight-10),0,0,1)
        Drawrectangleangle(block(windowWitdh-14,windowHeight-120,windowWitdh,windowHeight-10),0,0,1)
        Drawrectangleangle(block(0, windowHeight - 240, 14, windowHeight - 120), 1, 1, 1)
        Drawrectangleangle(block(windowWitdh-14,windowHeight-240,windowWitdh,windowHeight-120),1,1,1)
        Drawrectangleangle(block(0, windowHeight - 360, 14, windowHeight - 240), 1, 1, 0)
        Drawrectangleangle(block(windowWitdh - 14, windowHeight - 360, windowWitdh, windowHeight - 240), 1, 1, 0)
        Drawrectangleangle(block(0, windowHeight - 490, 14, windowHeight - 360), 1, 0, 0)
        Drawrectangleangle(block(windowWitdh - 14, windowHeight - 490, windowWitdh, windowHeight - 360), 1, 0, 0)
        Drawrectangleangle(block(0, 0, 14, 10), 0, 1, 0)
        Drawrectangleangle(block(windowWitdh - 14, 0 , windowWitdh, 10), 0, 1, 0)
       
        for x in blockList:  
            r = 0
            b = 1
            g = 0
            if (x.bottom <= windowHeight - 120 and x.bottom > windowHeight - 240):
                r = 1
                b = 1
                g = 1
            elif (x.bottom <= windowHeight - 240 and x.bottom > windowHeight - 360):
                r = 1
                b = 0
                g = 1
            elif (x.bottom <= windowHeight - 360 and x.bottom > windowHeight - 490):
                r = 1
                b = 0
                g = 0

            Drawrectangleangle(x, r, g, b)

        if (pause == False):

            move += 10
            if (move % 300 == 0):
                for x in blockList:
                    x.bottom -= 1
                    x.top -= 1
                for x in sidelist:
                    x.bottom-=1
                    x.top-=1

            ball.left = ball.left + deltaX  
            ball.right = ball.right + deltaX
            ball.top = ball.top + deltaY
            ball.bottom = ball.bottom + deltaY

            if BallAndPlayer(ball, Stick) == True:
                if (Stick.right - 50 < ball.left):
                    deltaY = 1
                    deltaX = 1
                else:
                    deltaY = 1
                    deltaX = -1

            # Ini untuk bola dan dinding
            if BallAndWall(ball, border) == fromRight:
                deltaX = -1

            if BallAndWall(ball, border) == fromLeft:
                deltaX = 1

            if BallAndWall(ball, border) == fromTop:
                deltaY = -1

            if BallAndWall(ball, border) == fromBottom:
                deltaY = 1
                Lives = Lives - 1

            for x in blockList:
                if (x.left == 0):
                    score += 1
                    x.left = -10
                elif(x.right==-5):
                    score-=1
                    x.right=-4
                if(x.bottom==Stick.top):
                    x.bottom=-5
                    x.top=-5
                    x.left=-5
                    x.right=-5

        for x in blockList:

            if (((ball.top == x.bottom or ball.bottom == x.top) and (
                    (ball.right >= x.left and ball.right <= x.right) or (
                    ball.left <= x.right and ball.left >= x.left))) or ((
                    (ball.right == x.left or ball.left == x.right) and (
                    (ball.top >= x.bottom and ball.top <= x.top) or (
                    ball.bottom >= x.bottom and ball.bottom <= x.top))))):

                if (ball.top == x.bottom):
                    deltaY = -1
                elif (ball.right == x.left):
                    deltaX = -1
                elif (ball.left == x.right):
                    deltaX = 1
                else:
                    deltaY = 1

                x.left = 0
                x.bottom = 0
                x.top = 0
                x.right = 0

        glColor(0, 1, 0)

        Drawrectangleangle(ball,0,1,0)

        Stick.left = mouse_x - 50
        Stick.right = mouse_x + 50

        if Stick.left <= 14:
            Stick.left = 14
            Stick.right = 114

        if Stick.right >= windowWitdh-14:
            Stick.right = windowWitdh-14
            Stick.left = windowWitdh - 114

        Drawrectangleangle(Stick,0,1,0)

        string = "Lives : " + str(Lives)
        drawText(string, 680, 20)
        string = "Score : " + str(score)
        drawText(string, 680, 50)
        glutSwapBuffers()

        i=0
        for x in blockList:
            if(x.left>0):
                i+=1;
    
        if(i==0):
            glClearColor(0, 1, 0, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            string = "press P to play again"
            drawText(string, 250, 250)
            string = "Nice Work"
            drawText(string, 250, 250)
            glutSwapBuffers()

    elif (Lives == 0 and exit == False):
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        string = "press P to play again"
        drawText(string, 320, 250)
        string = "Game Over"
        drawText(string, 360, 300)
        glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(windowWitdh, windowHeight)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Brick Block")
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(MouseMotion)
    init()
    glutMainLoop()


main()
