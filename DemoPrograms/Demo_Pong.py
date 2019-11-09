from PySimpleGUI import Canvas,Window,Popup,Text,Button
import random, time
#   Pong Original code: https://www.pygame.org/project/3649/5739

class Ball:
    def __init__(self, canvas, bat, bat2, color):
        self.C = canvas
        self.bat = bat
        self.bat2 = bat2
        self.id = self.C.create_oval(10, 10, 35, 35, fill=color)

        self.score1 = self.score2 = 0
        self.drawPlayer1 = self.drawPlayer2= None

        self.C.move(self.id, 327, 220)
        self.x=random.choice([-2.5, 2.5])
        self.y=-2.5

    def checkwin(self):return self.score1 >= 10 and 'Player left'or self.score2 >= 10 and 'Player Right'or None

    def updatep(self, val):
        self.C.delete(self.drawPlayer2)
        self.drawPlayer2= self.C.create_text(170, 50, font=('freesansbold.ttf', 40), text=str(val), fill='orange')

    def updatep1(self, val):
        self.C.delete(self.drawPlayer1)
        self.drawPlayer1 = self.C.create_text(550, 50, font=('freesansbold.ttf', 40), text=str(val), fill='magenta')

    def hit_bat(self, a,b,c,d):
        BP = self.C.coords(self.bat.id)
        if BP[0] <= c and a <= BP[2]:return BP[1] <= d <= BP[3]

    def hit_bat2(self, a,b,c,d):
        BP = self.C.coords(self.bat2.id)
        if BP[0] <= c and a <= BP[2]:return BP[1] <= d <= BP[3]

    def draw(self):
        self.C.move(self.id, self.x, self.y)
        a,b,c,d= self.C.coords(self.id)
        if b <= 0:self.y = 4
        if d >= self.C.winfo_height():self.y = -4
        if a <= 0:
            self.score2 += 1
            self.C.move(self.id, 327, 220)
            self.x = 4
            self.updatep1(self.score2)
        if c >= self.C.winfo_width():
            self.score1 += 1
            self.C.move(self.id, -327, -220)
            self.x = -4
            self.updatep(self.score1)
        if self.hit_bat(a,b,c,d):self.x = 4
        if self.hit_bat2(a,b,c,d):self.x = -4

class pongbat():
    def __init__(self, canvas, color,x=40,y=25):
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
P = pongbat(C, 'orange')
Q = pongbat(C, 'magenta',680,660)
B = Ball(C, P, Q, 'white')

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