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

class block:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

Box = block(100, 100, 120, 120)
border = block(0, 0, WindowWidth, WindowHeight)
Stick = block(370, 0, 470, 10) 
side1 = block(0, 0, 10, 280)
side2 = block(790, 0, 800, 280)
sideX= 0
sideY= 350
blockList = []
sidelist=[]
x = 15
y = 350

def init():
    glClearColor(255, 255, 255, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WindowWidth, 0, WindowHeight, 0, 1)  

    glMatrixMode(GL_MODELVIEW)

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

def BoxAndWall(Box, wall):  
    global FromRight
    global FromLeft
    global FromTop
    global FromBottom

    if Box.right >= wall.right-50:
        return FromRight
    if Box.left <= wall.left+50:
        return FromLeft
    if Box.top >= wall.top-50:
        return FromTop
    if Box.bottom <= wall.bottom:
        return FromBottom

def BoxAndPlayer(Box, player):  
    if Box.bottom <= player.top and Box.left >= player.left and Box.right <= player.right:
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
        glClearColor(1, 1, 1, 1)
        exit = False
        score=0
        Lives = 2
        defaultValues()

mouse_x = 0
# mouse_y = 0
def MouseMotion(x, y):
    global mouse_x
    # global mouse_y
    mouse_x = x
    # mouse_y = y
    

def Timer(v):
    Display()

    glutTimerFunc(TimeInterval, Timer, 1)

Lives = 2
pause = True
score= 0
move=0

def Display():
    global score
    global Lives
    global playerResult
    global FromRight
    global FromLeft
    global FromTop
    global FromBottom
    global DeltaX
    global DeltaY
    global pause
    global blockList
    global move
    global sidelist

    if (Lives > 0 and exit == False):
        glClear(GL_COLOR_BUFFER_BIT)

        if (pause and Lives  >0):
            string = "press space to play Q to exit"
            drawText(string, 270, 250)

        Drawrectangleangle(block(0,WindowHeight-14,WindowWidth,WindowHeight),0,0,1)
        Drawrectangleangle(block(0,WindowHeight-120,14,WindowHeight-10),0,0,1)
        Drawrectangleangle(block(WindowWidth-14,WindowHeight-120,WindowWidth,WindowHeight-10),0,0,1)
        Drawrectangleangle(block(0, WindowHeight - 240, 14, WindowHeight - 120), 1, 1, 1)
        Drawrectangleangle(block(WindowWidth-14,WindowHeight-240,WindowWidth,WindowHeight-120),1,1,1)
        Drawrectangleangle(block(0, WindowHeight - 360, 14, WindowHeight - 240), 1, 1, 0)
        Drawrectangleangle(block(WindowWidth - 14, WindowHeight - 360, WindowWidth, WindowHeight - 240), 1, 1, 0)
        Drawrectangleangle(block(0, WindowHeight - 490, 14, WindowHeight - 360), 1, 0, 0)
        Drawrectangleangle(block(WindowWidth - 14, WindowHeight - 490, WindowWidth, WindowHeight - 360), 1, 0, 0)
        Drawrectangleangle(block(0, 0, 14, 10), 0, 1, 0)
        Drawrectangleangle(block(WindowWidth - 14, 0 , WindowWidth, 10), 0, 1, 0)
       
        for x in blockList:  
            r = 0
            b = 1
            g = 0
            if (x.bottom <= WindowHeight - 120 and x.bottom > WindowHeight - 240):
                r = 1
                b = 1
                g = 1
            elif (x.bottom <= WindowHeight - 240 and x.bottom > WindowHeight - 360):
                r = 1
                b = 0
                g = 1
            elif (x.bottom <= WindowHeight - 360 and x.bottom > WindowHeight - 490):
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

            Box.left = Box.left + DeltaX  
            Box.right = Box.right + DeltaX
            Box.top = Box.top + DeltaY
            Box.bottom = Box.bottom + DeltaY

            if BoxAndPlayer(Box, Stick) == True:
                if (Stick.right - 50 < Box.left):
                    DeltaY = 1
                    DeltaX = 1
                else:
                    DeltaY = 1
                    DeltaX = -1

            # Ini untuk kotak dan dinding
            if BoxAndWall(Box, border) == FromRight:
                DeltaX = -1

            if BoxAndWall(Box, border) == FromLeft:
                DeltaX = 1

            if BoxAndWall(Box, border) == FromTop:
                DeltaY = -1

            if BoxAndWall(Box, border) == FromBottom:
                DeltaY = 1
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

            if (((Box.top == x.bottom or Box.bottom == x.top) and (
                    (Box.right >= x.left and Box.right <= x.right) or (
                    Box.left <= x.right and Box.left >= x.left))) or ((
                    (Box.right == x.left or Box.left == x.right) and (
                    (Box.top >= x.bottom and Box.top <= x.top) or (
                    Box.bottom >= x.bottom and Box.bottom <= x.top))))):

                if (Box.top == x.bottom):
                    DeltaY = -1
                elif (Box.right == x.left):
                    DeltaX = -1
                elif (Box.left == x.right):
                    DeltaX = 1
                else:
                    DeltaY = 1

                x.left = 0
                x.bottom = 0
                x.top = 0
                x.right = 0

        glColor(1, 1, 1)

        Drawrectangleangle(Box,0,1,0)

        Stick.left = mouse_x - 50
        Stick.right = mouse_x + 50
        # Stick.top = mouse_y + 10
        # Stick.bottom = mouse_y - 10

        if Stick.left <= 14:
            Stick.left = 14
            Stick.right = 114

        if Stick.right >= WindowWidth-14:
            Stick.right = WindowWidth-14
            Stick.left = WindowWidth - 114
        
        Drawrectangleangle(Stick,0,1,0)

        string = "Lives : " + str(Lives)
        drawText(string, 680, 20)
        string = "Score : " + str(score)
        drawText(string, 680, 40)
        glutSwapBuffers()

        i=0
        for x in blockList:
            if(x.left>0):
                i+=1;
    
        if(i==0):
            glClearColor(1, 0, 0, 1)
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
    glutInitWindowSize(WindowWidth, WindowHeight)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Break Block")
    glutDisplayFunc(Display)
    glutTimerFunc(TimeInterval, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(MouseMotion)
    init()
    glutMainLoop()


main()
