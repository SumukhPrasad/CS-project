import PySimpleGUI as sg

sg.theme('DarkTeal10')


layout = [  [sg.Text('Create new game/Restore from DB', font='Helvetica 20 bold')],
            [sg.Text('Board name?', font='Helvetica 14 bold'), sg.InputText()],
            [sg.Button('LAUNCH'), sg.Button('CANCEL')] ]

window = sg.Window('inferno_launch', layout)

while True:
     event, values = window.read()
     if event == sg.WIN_CLOSED or event == 'CANCEL': # if user closes window or clicks cancel
          break
     elif event == 'LAUNCH':
          print('You entered ', values[0])
          window.close()