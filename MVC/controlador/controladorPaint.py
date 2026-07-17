from estado.ferramenta import *
from estado.ferramentas import *
from modelo.figuras import *
from modelo.desenho import *
from visao.janelaPaint import *
from tkinter import filedialog
from controlador.controladorSelecao import *

#  Classe ControladorPaint: recebe os eventos do mouse, atualiza o Model (desenho)
# e pede que a View (visao) mostre o resultado
class ControladorPaint:
    def __init__(self, desenho, visao):
        self.desenho = desenho
        self.visao = visao
        self.canvas = self.visao.canvas
    
        # Dicionario com uma instancia de cada Ferramenta
        self.ferramentas = {
            "Linha": Linha_Ferramenta(visao, desenho),
            "Retângulo": Retangulo_Ferramenta(visao, desenho),
            "Círculo": Circulo_Ferramenta(visao, desenho),
            "Oval": Oval_Ferramenta(visao, desenho),
            "Rabisco": Rabisco_Ferramenta(visao, desenho),
            "Quadrado": Quadrado_Ferramenta(visao, desenho),
        }
        self.estado = self.ferramentas["Linha"]  # ferramenta inicial

        # Liga os eventos do mouse a area de desenho
        self.canvas.bind("<ButtonPress-1>", self.mouse_pressionado)
        self.canvas.bind("<B1-Motion>", self.mouse_arrastado)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_solto)

        # Liga os botoes de Salvar e Abrir aos metodos do controlador
        self.visao.botao_salvar.config(command=self.salvar)
        self.visao.botao_abrir.config(command=self.abrir)

        # Cria o controlador de selecao (liga as teclas do teclado)
        self.controlador_selecao = ControladorSelecao(self.desenho, self.visao)

    # Troca o estado atual baseado na ferramenta escolhida na interface,
    # e transfere o clique pra ferramenta criar a figura_nova
    def mouse_pressionado(self, event):
        tipo = self.visao.tipo_figura_var.get()
        self.estado = self.ferramentas[tipo]
        self.estado.mouse_pressionado(event)

    # Transfere a atualizacao da figura pra ferramenta atual,
    # depois redesenha tudo
    def mouse_arrastado(self, event):
        self.estado.mouse_arrastado(event)
        self.desenho.desenha_figuras(self.canvas)
        self.estado.figura_nova.desenha(self.canvas, dash=(4, 2))

    # Transfere a inclusao da figura pra ferramenta atual, e redesenha o resultado final
    def mouse_solto(self, event):
        self.estado.mouse_solto(event)
        self.desenho.desenha_figuras(self.canvas)

    # Abre o seletor de arquivo e pede pro Desenho salvar as figuras nele
    def salvar(self):
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".pkl")
        if caminho_arquivo:
            self.desenho.salvar(caminho_arquivo)

    # Abre o seletor de arquivo, pede pro Desenho carregar as figuras salvas
    # e redesenha o canvas com o resultado
    def abrir(self):
        caminho_arquivo = filedialog.askopenfilename()
        if caminho_arquivo:
            self.desenho.abrir(caminho_arquivo)
            self.desenho.desenha_figuras(self.canvas)