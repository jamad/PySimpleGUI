from PySimpleGUI import Canvas,Window,Popup,Text,Button
import random, time
#   Pong Original code: https://www.pygame.org/project/3649/5739

class Ball:
    def __init__(self, canvas, bat, bat2, color):
        self.canvas = canvas
        self.bat = bat
        self.bat2 = bat2
        self.playerScore = 0
        self.player1Score = 0
        self.drawP1 = None
        self.drawP = None
        self.id = self.canvas.create_oval(10, 10, 35, 35, fill=color)
        self.canvas.move(self.id, 327, 220)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.x = random.choice([-2.5, 2.5])
        self.y = -2.5

    def checkwin(self):
        winner = None
        if self.playerScore >= 10:
            winner = 'Player left wins'
        if self.player1Score >= 10:
            winner = 'Player Right'
        return winner

    def updatep(self, val):
        self.canvas.delete(self.drawP)
        self.drawP = self.canvas.create_text(170, 50, font=(
            'freesansbold.ttf', 40), text=str(val), fill='white')

    def updatep1(self, val):
        self.canvas.delete(self.drawP1)
        self.drawP1 = self.canvas.create_text(550, 50, font=(
            'freesansbold.ttf', 40), text=str(val), fill='white')

    def hit_bat(self, pos):
        bat_pos = self.canvas.coords(self.bat.id)
        if pos[2] >= bat_pos[0] and pos[0] <= bat_pos[2]:
            if pos[3] >= bat_pos[1] and pos[3] <= bat_pos[3]:
                return True
            return False

    def hit_bat2(self, pos):
        bat_pos = self.canvas.coords(self.bat2.id)
        if pos[2] >= bat_pos[0] and pos[0] <= bat_pos[2]:
            if pos[3] >= bat_pos[1] and pos[3] <= bat_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 4
        if pos[3] >= self.canvas_height:
            self.y = -4
        if pos[0] <= 0:
            self.player1Score += 1
            self.canvas.move(self.id, 327, 220)
            self.x = 4
            self.updatep1(self.player1Score)
        if pos[2] >= self.canvas_width:
            self.playerScore += 1
            self.canvas.move(self.id, -327, -220)
            self.x = -4
            self.updatep(self.playerScore)
        if self.hit_bat(pos):
            self.x = 4
        if self.hit_bat2(pos):
            self.x = -4


class pongbat():
    def __init__(self, canvas, color,x=40,y=25):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(x, 200, y, 310, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0

    def up(self, evt):self.y = -5

    def down(self, evt):self.y = 5

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:self.y = 0
        if pos[3] >= 400:self.y = 0


class pongbat2():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(680, 200, 660, 310, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0

    def up(self, evt):
        self.y = -5

    def down(self, evt):
        self.y = 5

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0


# ------------- Define GUI layout -------------
L = [[Canvas(size=(700, 400),background_color='black', key='canvas')],[Text(''), Button('Quit')]]
W = Window('The Classic Game of Pong', L,return_keyboard_events=True, finalize=True)

canvas = W['canvas'].TKCanvas
# ------------- Create line down center, the bats and ball -------------
canvas.create_line(350, 0, 350, 400, fill='white')
P = pongbat(canvas, 'orange')
Q = pongbat2(canvas, 'magenta')
B = Ball(canvas, P, Q, 'white')

while 1:# ------------- Event Loop -------------
    B.draw()
    P.draw()
    Q.draw()

    E,_= W.read(timeout=0)
    if E in(None,'Quit'):break
    if E is not None:
        if E.startswith('Up'):      Q.up(2)
        elif E.startswith('Down'):  Q.down(2)
        elif E == 'w':              P.up(1)
        elif E == 's':              P.down(1)
    if B.checkwin():
        Popup('Game Over', B.checkwin() + ' won!!')
        break

    canvas.after(10)

W.close()