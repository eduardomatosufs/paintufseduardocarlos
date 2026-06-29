from tkinter import *
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event):
    global figura_nova
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y))
    elif tipo_figura_var.get() == "Retângulo":
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y))
    elif tipo_figura_var.get() == "Círculo":
         figura_nova = ("circulo", (event.x,event.y))
    elif tipo_figura_var.get() == "Oval":
         figura_nova = ("oval", (event.x,event.y, event.x, event.y))
    else:
        figura_nova = ("rabisco", [(event.x, event.y)])

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "circulo":
         centro_x = figura_nova[1][0]
         centro_y = figura_nova[1][1]
         raio = ((event.x-centro_x)**2 + (event.y - centro_y)**2)**0.5
         figura_nova = ("circulo",(centro_x,centro_y,raio))
    else:
        figura_nova = (figura_nova[0], (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    desenhar_figuras()
    desenhar_figura_nova()
    

# Quando mouse é solto
def incluir_figura_nova(event):
    if not incompleta(figura_nova):
        figuras.append(figura_nova)
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values in figuras:
        if fig == 'linha':
            canvas.create_line(values[0], values[1], values[2], values[3])
        elif fig == 'retangulo':
            canvas.create_rectangle(values[0], values[1], values[2], values[3])
        elif fig == 'circulo':
             canvas.create_oval(values[0]-values[2],values[1]-values[2],values[0]+values[2],values[1]+values[2])
        elif fig == 'oval':
             canvas.create_oval(values[0],values[1],values[2],values[3])
        else:
            canvas.create_line(values)

def desenhar_figura_nova():
    fig, values = figura_nova
    if fig == 'linha':
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == 'retangulo':
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == 'circulo':
        canvas.create_oval(values[0]-values[2],values[1]-values[2],values[0]+values[2],values[1]+values[2], dash=(4,2))
    elif fig == 'oval':
        canvas.create_oval(values[0],values[1],values[2],values[3], dash=(4, 2))
    else:
        canvas.create_line(values, dash=(4, 2))

def incompleta(figura):
    fig, values = figura
    if fig == 'rabisco':
        return len(values) <= 1
    elif fig == 'circulo':
        return len(values) <= 2 or values[2] == 0
    else:
        return (values[0], values[1]) == (values[2], values[3])

#******* MAIN *******#
figuras = []        # Todas as figuras desenhadas
figura_nova = None  # Figura sendo desenhada, ainda não incluída em figuras

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

frame.pack()

canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)


root.mainloop()