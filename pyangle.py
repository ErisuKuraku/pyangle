import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('First side (CM)', sg.Input())],
          [sg.Text('Second side (CM)', sg.Input())],
          [sg.Text('Third side (CM)', sg.Input())],
          [sg.Submit()]
          ]
window = sg.Window('Windows Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        window.close()
    if event == 'Submit':
        a = float(values[0])
        b = float(values[1])
        c = float(values[2])

        s = (a + b + c) / 2

        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        sg.popup('The area is %0.5f' % area)
    if event == sg.WIN_CLOSED:
        window.close()
