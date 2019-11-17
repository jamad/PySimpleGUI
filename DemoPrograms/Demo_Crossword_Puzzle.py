from PySimpleGUI import Text,Graph,Button,Window
import random,string
#Demo to show how to draw rectangles and letters on a Graph 

w,h=5,5 # BOX_SIZE 
n = w*h
L = [[Text('Crossword Puzzle'), Text('', key='-OUTPUT-')],
    [Graph((350, 350), (0, 150), (150, 0), key='-G-',change_submits=True, drag_submits=False)]
    ]
W = Window('Window Title', L, finalize=True)
g = W['-G-']

for i in range(h):
    for j in range(w):
        color=('red','white')[random.randint(0,10)>1]
        g.draw_rectangle((j*n + 5, i*n+3),(j*n+n+5,i*n+n+3),line_color='black',fill_color=color)
        g.draw_text(str(i*w+j+1),(j*n+10,i*n+8))

while True:             # E Loop
    E, V = W.read()
    if E in (None, 'Exit'):break
    if E == '-G-':
        M=V['-G-']
        if M==(None,None):continue
        x,y = M[0]//n,M[1]//n
        if x<h and y<w:
            ch=random.choice(string.ascii_uppercase)
            g.draw_text('{}'.format(ch), (x*n+18,y*n+17), font='Courier 25')
W.close()