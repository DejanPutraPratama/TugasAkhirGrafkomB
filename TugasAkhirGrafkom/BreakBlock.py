from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

FromRight = 1
FromLeft = 2
FromTop = 3
FromBottom = 4
WindowWidth = 800
WindowHeight = 500
DeltaX = 1
DeltaY = 1
TimeInterval = 5

class Block:
    def __init__(self, right, left, top, bottom):
        self.right = right
        self.left = left
        self.top = top
        self.bottom = bottom

ball = Block(100, 100, 120, 120)
border = Block(0, 0, WindowWidth, WindowHeight)
stick = Block(370, 0, 470, 10)
side1 = Block(0, 0, 10, 280)
side2 = Block(790, 0, 800, 280)
sideX = 0
sideY = 350
BlockList = []
SideList = []
x = 15
y = 350

def init():
    glClearColor(1, 0, 0, 0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WindowWidth, 0, WindowHeight, 0, 1)

    glMatrixMode(GL_MODELVIEW)

for i in range(0, 156):
    if (i % 13 == 0):
        x = 15
        y += 30
    if (i % 39 == 0):
        y += 50
    
    BlockList.append(Block(x, y, x + 50, y + 20))
    x += 60

    Move = 0
    Pause = True

def DefaultValues():
    global SideList
    global BlockList
    global x
    global y
    global sideX
    global sideY
    global Move
    global Pause

    for z in range (0, 156):
        if (z % 13 == 0):
            x = 15 
            y += 30
        if (z % 39 == 0):
            y += 50
        BlockList.append(Block(x, y, x + 50, y + 20))
        x += 60

def DrawRectangle(rectangle, r, g, b):
    glLoadIdentity()
    glColor(r, g, b)
    glColor(0, 255, 255)

    glBegin(GL_QUADS)
    glVertex(rectangle.left, rectangle.bottom, 0)
    glVertex(rectangle.right, rectangle.bottom, 0)
    glVertex(rectangle.right, rectangle.top, 0)
    glVertex(rectangle.left, rectangle.top, 0)
    glEnd()

def DrawText(String, x, y):
    glLineWidth(2)
    glColor(255, 255, 0)
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.13, 0.13, 1)
    String = String.encode()
    for c in String:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def DrawEndText(String, x, y):
    glLineWidth(2.5)
    glColor(255, 255, 0)
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.15, 0.15, 1)
    String = String.encode()
    for c in String:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def BallAndPlayer(Ball, PLayer):
    if Ball.bottom <= PLayer.top and Ball.left >= PLayer.left and Ball.right <= PLayer.right:
        return True
    return False

exit = False

def BallAndWall(Ball, Wall):
    global FromRight
    global FromLeft
    global FromTop
    global FromBottom

    if Ball.right >= Wall.right - 14:
        return FromRight
    if Ball.left <= Wall.left + 14:
        return FromLeft
    if Ball.top >= Wall.top - 14:
        return FromTop
    if Ball.bottom <= Wall.bottom:
        return FromBottom

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