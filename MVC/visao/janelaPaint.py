from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

# Classe JanelaPaint: cria a interface grafica (a View)
class JanelaPaint:
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)

        paddings = {'padx': 5, 'pady': 5}

        # Menu pra escolher o tipo de figura
        self.label = ttk.Label(self.frame, text='Tipo de figura:')
        self.label.grid(column=0, row=0, sticky=W, **paddings)

        self.tipo_figura_var = StringVar(self.root)
        self.option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,
                                           'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Círculo', 'Oval', 'Quadrado')
        self.option_menu.grid(column=1, row=0, sticky=W, **paddings)

        # Area de desenho
        self.canvas = Canvas(self.frame, bg='white', width=600, height=600)
        self.canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

        # Botoes que abrem o seletor de cores
        self.botao_borda = ttk.Button(self.frame, text='Cor da borda', command=self.escolher_cor_borda)
        self.botao_borda.grid(column=0, row=2, **paddings)

        self.botao_preenchimento = ttk.Button(self.frame, text='Cor de preenchimento', command=self.escolher_cor_preenchimento)
        self.botao_preenchimento.grid(column=1, row=2, **paddings)

        self.frame.pack()

        # cores atuais escolhidas pelo usuario
        self.cor_borda = "black"
        self.cor_preenchimento = ""

    # Abre o seletor e guarda a cor da borda
    def escolher_cor_borda(self):
        cor = colorchooser.askcolor()
        self.cor_borda = cor[1]

    # Abre o seletor e guarda a cor de preenchimento
    def escolher_cor_preenchimento(self):
        cor = colorchooser.askcolor()
        self.cor_preenchimento = cor[1]