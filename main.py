from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

# Quando mouse é pressionado
def iniciar_figura_nova(event):
    global figura_nova
    if tipo_figura_var.get() == 'Linha':
         figura_nova = ("linha", (event.x, event.y, event.x, event.y),(cor_borda,cor_preenchimento))
    elif tipo_figura_var.get() == "Retângulo":
         figura_nova = ("retangulo", (event.x, event.y, event.x, event.y),(cor_borda,cor_preenchimento))
    elif tipo_figura_var.get() == "Círculo":
         figura_nova = ("circulo", (event.x,event.y),(cor_borda,cor_preenchimento))
    elif tipo_figura_var.get() == "Oval":
         figura_nova = ("oval", (event.x,event.y, event.x, event.y),(cor_borda,cor_preenchimento))
    else:
         figura_nova = ("rabisco", [(event.x, event.y)],(cor_borda,cor_preenchimento))

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "circulo":
         centro_x = figura_nova[1][0]
         centro_y = figura_nova[1][1]
         raio = ((event.x-centro_x)**2 + (event.y - centro_y)**2)**0.5 # Distância entre o centro e a posicao do mouse
         figura_nova = ("circulo",(centro_x,centro_y,raio), figura_nova[2])
    else:
        figura_nova = (figura_nova[0], (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2])
    desenhar_figuras()
    desenhar_figura_nova()
    

# Adiciona a figura à lista 
def incluir_figura_nova(event):
    if not incompleta(figura_nova):
        figuras.append(figura_nova)
    desenhar_figuras()

# Limpa a tela e redesenha todas as figuras salvas
def desenhar_figuras():
    canvas.delete("all")
    for fig, values,cores in figuras:
        cor_borda = cores[0]
        cor_preenchimento = cores[1]
        if fig == 'linha':
            canvas.create_line(values[0], values[1], values[2], values[3],fill=cor_borda)
        elif fig == 'retangulo':
            canvas.create_rectangle(values[0], values[1], values[2], values[3],outline=cor_borda,fill=cor_preenchimento)
        elif fig == 'circulo':
             canvas.create_oval(values[0]-values[2],values[1]-values[2],values[0]+values[2],values[1]+values[2],outline=cor_borda,fill=cor_preenchimento)
        elif fig == 'oval':
             canvas.create_oval(values[0],values[1],values[2],values[3],outline=cor_borda,fill=cor_preenchimento)
        else:
            canvas.create_line(values,fill=cor_borda)

# Desenha o tracejado da figura nova
def desenhar_figura_nova():
    fig, values, cores = figura_nova
    cor_borda = cores[0]
    cor_preenchimento = cores[1]
    if fig == 'linha':
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=cor_borda)
    elif fig == 'retangulo':
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2),outline=cor_borda,fill=cor_preenchimento)
    elif fig == 'circulo':
        canvas.create_oval(values[0]-values[2],values[1]-values[2],values[0]+values[2],values[1]+values[2], dash=(4,2),outline=cor_borda,fill=cor_preenchimento)
    elif fig == 'oval':
        canvas.create_oval(values[0],values[1],values[2],values[3], dash=(4, 2),outline=cor_borda,fill=cor_preenchimento)
    else:
        canvas.create_line(values, dash=(4, 2),fill=cor_borda)

# Olha se a figura é válida
def incompleta(figura):
    fig, values, cores = figura
    if fig == 'rabisco':
        return len(values) <= 1
    elif fig == 'circulo':
        return len(values) <= 2 or values[2] == 0
    else:
        return (values[0], values[1]) == (values[2], values[3])
    
# Abre o seletor das cores e guarda a escolhida para a borda
def escolher_cor_borda():
   global cor_borda 
   cor = colorchooser.askcolor()
   cor_borda = cor[1]

# Abre o seletor das cores e guarda a escolhida para o preenchimento
def escolher_cor_preenchimento():
    global cor_preenchimento
    cor = colorchooser.askcolor()
    cor_preenchimento = cor[1]

#******* MAIN *******#
figuras = []        # Todas as figuras desenhadas
figura_nova = None  # Figura sendo desenhada, ainda não incluída em figuras
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