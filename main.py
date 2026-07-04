from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

from figura import Figura
from linha import Linha
from rabisco import Rabisco
from retangulo import Retangulo
from circulo import Circulo
from oval import Oval

# Cria o objeto da figura no clique
def iniciar_figura_nova(event):
    global figura_nova
    if tipo_figura_var.get() == "Linha":
        figura_nova = Linha(cor_borda,cor_preenchimento,event.x,event.y,event.x,event.y)
    elif tipo_figura_var.get() == "Retângulo":
        figura_nova = Retangulo(cor_borda,cor_preenchimento,event.x,event.y,event.x,event.y)
    elif tipo_figura_var.get() == "Círculo":
        figura_nova = Circulo(cor_borda,cor_preenchimento,event.x,event.y,0)
    elif tipo_figura_var.get() == "Oval":
        figura_nova = Oval(cor_borda,cor_preenchimento,event.x,event.y,event.x,event.y)
    else:
        figura_nova = Rabisco(cor_borda,cor_preenchimento,[(event.x,event.y)])

# Atualiza quando arrasta
def atualizar_figura_nova(event):
    global figura_nova
    if isinstance(figura_nova,Rabisco):
       figura_nova.pontos.append((event.x,event.y))
    elif isinstance(figura_nova,Circulo):
        raio = ((event.x-figura_nova.centro_x)**2 + (event.y - figura_nova.centro_y)**2)**0.5 # Distancia entre o centro e o mouse 
        figura_nova.raio = raio
    else:
        figura_nova.x2 = event.x
        figura_nova.y2 = event.y
    desenhar_figuras()
    desenhar_figura_nova()

# Salva a figura na lista se nao for vazia
def incluir_figura_nova(event):
   if not figura_nova.vazia():
       figuras.append(figura_nova)
   desenhar_figuras()

# Limpa a tela e cada objeto se desenha
def desenhar_figuras():
    canvas.delete("all")
    for figura in figuras:
        figura.desenha(canvas)

# Cada objeto faz o tracejado
def desenhar_figura_nova():
    figura_nova.desenha(canvas, dash=(4,2))

# Seletor e guarda a cor da borda
def escolher_cor_borda():
    global cor_borda
    cor = colorchooser.askcolor()
    cor_borda = cor[1]

# Seletor e guarda a cor de preenchimento
def escolher_cor_preenchimento():
    global cor_preenchimento
    cor = colorchooser.askcolor()
    cor_preenchimento = cor[1]


#******* MAIN *******#
figuras = []        # lista de objetos Figura
figura_nova = None  # figura sendo desenhada, ainda não incluída na lista
cor_borda = "black" # cor inicial da borda
cor_preenchimento = "" # "" quer dizer sem preenchimento

root = Tk()
frame = Frame(root)

paddings = {'padx': 5, 'pady': 5}

label = ttk.Label(frame, text='Tipo de figura:')
label.grid(column=0, row=0, sticky=W, **paddings)

tipo_figura_var = StringVar(root)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Retângulo','Círculo', 'Oval')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

botao_borda = ttk.Button(frame, text='Cor da borda', command=escolher_cor_borda)
botao_borda.grid(column=0, row=2, **paddings)

botao_preenchimento = ttk.Button(frame, text='Cor de preenchimento', command=escolher_cor_preenchimento)
botao_preenchimento.grid(column=1, row=2,**paddings)

frame.pack()

canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)


root.mainloop()