import PySimpleGUI as sg
import random

#class TelaPython:
    #def __init__(self):
sg.theme('DarkAmber')   # Add a touch of color
avalores=[1,2]
        # All the stuff inside your window.
layout1 = [
    [sg.Image('/home/haniel/development/python-projects/ednaldo-pereira/ednaldo-pereira.png')],
    [sg.Text('Pergunte ao Ednaldo Pereira!')],
    [sg.Input(size=(12,0), key='entrada1'), sg.Text(' ou '), sg.Input(size=(12,0),key='entrada2')],
    [sg.Button('Adivinhar',size=(28,1))]
]

layout2 = [
    [sg.Image('/home/haniel/development/python-projects/ednaldo-pereira/ednaldo-pereira.png')],
    [sg.Text('Pergunte ao Ednaldo Pereira!')],
    [sg.Text(size=(12, 0), key='saida1',justification='right'), sg.Text(' ou '), sg.Text(size=(12, 0), key='saida2')],
    [sg.Text('O Ednaldo Pereira disse:')],
    #[sg.Text({random.choice(avalores)}, key='escolha')],
    [sg.Text('Ednaldo Pereira', key='resultado')],
    [sg.Button('Tentar novamente', key='tryagain')]
]

layout = [[sg.Column(layout1, key='-COL1-',element_justification='center'), sg.Column(layout2, visible=False, key='-COL2-',element_justification='center')]
        ]

        # Create the Window
window = sg.Window('Pergunte ao Ednaldo Pereira', layout,font=("Helvetica", 20),location=(550,150), size = (900,700), resizable=True, finalize=True,element_justification='c')

    #element_justification = 'c'
    #def Iniciar(self):
layout = 1  # The currently visible layout
while True:
            # Extrair os dados
        button, values = window.Read()
        valores = values
        avalores = []
        avalores.append(valores['entrada1'])
        avalores.append(valores['entrada2'])
        decisao = random.choice(avalores)
        if button == sg.WINDOW_CLOSED:
            break
        if button == 'Adivinhar':
            window[f'-COL{layout}-'].update(visible=False)
            layout = 2
            window[f'-COL{layout}-'].update(visible=True)

            window['saida1'].update(values['entrada1'])
            window['saida2'].update(values['entrada2'])
            window['resultado'].update(decisao) # ATUALIZA O CAMPO RESULTADO COM A DECISÃO ENTRE OS 2 CAMPOS
            print(f'escolhido: {decisao}') #printa na ide
        if button in 'tryagain':
            window[f'-COL{layout}-'].update(visible=False)
            layout = 1
            window[f'-COL{layout}-'].update(visible=True)

window.close()








        # Event Loop to process "events" and get the "values" of the inputs
        # while True:
        #     event, values = window.read()
        #     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        #         break
        #     print('You entered ', values[0])

        #window.close()