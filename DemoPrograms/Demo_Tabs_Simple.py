from PySimpleGUI import Text,Input,TabGroup,Tab,Button,Window,popup_non_blocking
# Simple example of TabGroup element
T1=[[Text('Put your L in here')],
    [Text('Input here'), Input(key='_IN')]]
T2=[[Button('Tab2')],
    [Button('Tab2')],
    [Button('Tab2')],
    [Button('Tab2')]]
TG=TabGroup([
    [Tab('Tab 1', T1),Tab('Tab 2', T2)]
    ], key='_TG')
L=[[TG],[Button('Read')]]
W=Window('Demo Tab', L,default_element_size=(12, 1))
while 1:
    E,V=W.read()
    print(E,V)
    popup_non_blocking('button = %s' % E,'Values dictionary',V)
    if not E:break
W.close()