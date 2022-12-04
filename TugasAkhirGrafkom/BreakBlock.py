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

