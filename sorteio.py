from PySimpleGUI import PySimpleGUI as sg
from random import randint

# função para gerar o numero do sorteio
def gerarNumero():
    sorteio = randint(numero_inicial,numero_final)
    return sorteio

def Reiniciar():
    janela['inicial'].update('')
    janela['final'].update('')
    janela['resultado'].update('')
    janela['ultimos_numeros'].update('')
    ultimos_numeros.clear()

# layout
layout = [
    [sg.Text('Desenvolvido por: Gustavo Monarin dos Santos'), sg.Push(), sg.Text('Versão: 1.00'), sg.Button('reiniciar', key='reiniciar', size = (10,1), font=('arial', 11))],
    [sg.Push(), sg.Text('SORTEIO', font=('arial', 60)),sg.Push()],
    [sg.Push(),sg.Text('Número inicial', font=('Arial', 20)), sg.Push(), sg.Text('Número final', font=('Arial', 20)), sg.Push()],
    [sg.Push(),sg.Input(key='inicial', size=(4,3), font=('Arial', 20)), sg.Push(), sg.Input(key='final', size=(4,3), font=('Arial', 20)),sg.Push()],
    [sg.Text('')],
    [sg.Push(), sg.Button('SORTEIO', key='sorteio', size = (10,1), font=('arial', 20)), sg.Push()],
    [sg.Push(), sg.Text('', key='resultado', font=('arial', 120)), sg.Push()],
    [sg.Push(), sg.Text('Últimos números sorteados', font=('arial', 25)),sg.Push()],
    [sg.Push(), sg.Multiline(size=(170,20), key='ultimos_numeros', font=('arial', 30)), sg.Push()],
    
]

#janela gerada
janela=sg.Window('SORTEIO', layout, size=(700, 700))

# eventos
ultimos_numeros=[]
while True:
    evento, valores = janela.Read()
    try:
        if evento == sg.WIN_CLOSED:
            break

        if evento == 'sorteio':
            numero_inicial=int(valores['inicial'])
            numero_final=int(valores['final'])
            sorteio = gerarNumero()
            janela['resultado'].update(sorteio)

            if sorteio not in ultimos_numeros:
                ultimos_numeros.append(sorteio)
                janela['ultimos_numeros'].update(str(ultimos_numeros)[1:-1])
        
        if evento == 'reiniciar':
            Reiniciar()
    except:
        sg.Popup('VERIFICAR OS CAMPOS E PREENCHER CORRETAMENTE!')

janela.close()