from PySimpleGUI import Canvas,Window,Popup,Text,Button
import random, time
#   Pong Original code: https://www.pygame.org/project/3649/5739

class Ball:
    def __init__(self, canvas, bat, bat2):
        self.C = canvas
        self.bat = bat
        self.bat2 = bat2
        self.id=self.C.create_oval(10, 10, 35, 35, fill='white')

        self.x=random.choice([-2.5, 2.5])
        self.y=-2.5

        self.score1 = self.score2 = 0
        self.scoreText1 = self.C.create_text(550, 50, font=('freesansbold.ttf', 40), text='0', fill='magenta')
        self.scoreText2= self.C.create_text(170, 50, font=('freesansbold.ttf', 40), text='0', fill='orange')

    def checkwin(self):return self.score1 >= 10 and 'Player left'or self.score2 >= 10 and 'Player Right'or None

    def hit_bat(self,i,a,c,d):
        A,B,C,D = self.C.coords(i)
        if A <= c and a <= C:return B <= d <= D

    def draw(self):
        self.C.move(self.id, self.x, self.y)
        a,b,c,d= self.C.coords(self.id)
        if b <= 0:self.y = 4 # wall reflect
        if self.C.winfo_height() <= d:self.y = -4 # wall reflect
        if self.hit_bat(self.bat.id,a,c,d):self.x = 4 # player reflect
        if self.hit_bat(self.bat2.id,a,c,d):self.x = -4 # player reflect
        if a <= 0:# ball escaped left
            self.score2 += 1
            self.C.move(self.id, 327, 220)
            self.x = 4
#           self.scoreText1.text=str(self.score2) # this doesn't work but the following works
#           https://stackoverflow.com/questions/55731450/how-to-create-text-on-a-tkinter-canvas-and-change-the-text-in-the-canvas
            self.C.itemconfigure(self.scoreText1, text=str(self.score2))
        if c >= self.C.winfo_width():# ball escaped right
            self.score1 += 1
            self.C.move(self.id, -327, -220)
            self.x = -4
            self.C.itemconfigure(self.scoreText2, text=str(self.score1))

class pongbat():
    def __init__(self, canvas, color,x,y):
        self.C = canvas
        self.id = self.C.create_rectangle(x, 200, y, 310, fill=color)
        self.dy = 0
    def mv(self,v):self.dy=v
    def draw(self):
        self.C.move(self.id, 0, self.dy)
        pos = self.C.coords(self.id)
        if pos[1]<=0 or 400<=pos[3]:self.dy = 0 # at the edge

# ------------- Define GUI layout -------------
L = [[Canvas(size=(700, 400),background_color='black', key='canvas')],[Text(''), Button('Quit')]]
W = Window('The Classic Game of Pong', L,return_keyboard_events=True, finalize=True)

# ------------- Create line down center, the bats and ball -------------
C = W['canvas'].TKCanvas
C.create_line(350, 0, 350, 400, fill='cyan')

P = pongbat(C, 'orange',40,25)
Q = pongbat(C, 'magenta',680,660)
B = Ball(C, P, Q)

while 1:# ------------- Event Loop -------------
    B.draw()
    P.draw()
    Q.draw()
    
    E,_= W.read(timeout=0)
    if E in(None,'Quit'):break
    if 'TIMEOUT' not in E:print(E)
#    Q.mv(E.startswith('Up')and -5 or E.startswith('Down')and 5)
#    P.mv(E == 'w' and -5 or E == 's' and 5)
    if 'Up'in E:      Q.mv(-5)
    elif 'Down'in E:  Q.mv(5)
    elif E == 'w':    P.mv(-5)
    elif E == 's':    P.mv(5)
    if B.checkwin():
        Popup('Game Over', B.checkwin() + ' won!!')
        break
    C.after(10)
W.close()