from PySimpleGUI import Text,change_look_and_feel,Input,TabGroup,Tab,Output,Frame,Col,Button,Window
# Yet another example of TabGroup element
change_look_and_feel('GreenTan')

tab1_L = [[Text('Type something here and click button'), Input(key='in')]]
tab2_L = [[Text('This is inside tab 2')],[Text('Tabs can be anywhere now!')]]
TG12=   TabGroup([[Tab('Tab 1', tab1_L), Tab('Tab 2', tab2_L)]])

tab3_L = [[Text('I am tab 3')]]
tab4_L = [[Text('I am tab 4')]]
TG34=TabGroup([[Tab('Tab3', tab3_L), Tab('Tab 4', tab4_L)]])

tab5_L = [[Text('Watch this W')] , [Output(size=(40,5))]]

tab6a_L = [[Text('This is inside of a tab')]]
tab6b_L = [[Text('This is inside of a tab')]]
TG = TabGroup([[Tab('Tab 7', tab6a_L), Tab('Tab 8', tab6b_L)]])
tab6_L = [[Text('This is inside tab 6')] , [Text('How about a second row of stuff in tab 6?'), TG]]

L = [[Frame('A Frame', layout=[[TG12, TG34]])],
    [Text('This text is on a row with a column'),Col(layout=[[Text('In a column')],
    [TabGroup([[Tab('Tab 5', tab5_L), Tab('Tab 6', tab6_L)]])],[Button('Click me')]])],]

W = Window('My W with tabs', L, default_element_size=(12,1), finalize=True)
print('Are there enough tabs for you?')
while 1:
    E, V = W.read()
    print(E, V)
    if E is None:break
W.close()