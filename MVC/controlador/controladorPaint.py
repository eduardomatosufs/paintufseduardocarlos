from estado.ferramenta import *
from estado.ferramentas import *
from modelo.figuras import *
from modelo.desenho import *
from visao.janelaPaint import *

#  Classe ControladorPaint: recebe os eventos do mouse, atualiza o Model (desenho)
# e pede que a View (visao) mostre o resultado
class ControladorPaint:
    def __init__(self, desenho, visao):
        self.desenho = desenho
        self.visao = visao
        self.canvas = self.visao.canvas
        self.ferramentas = {
            "Linha": Linha_Ferramenta(visao, desenho),
            "Retângulo": Retangulo_Ferramenta(visao, desenho),
            "Círculo": Circulo_Ferramenta(visao, desenho),
            "Oval": Oval_Ferramenta(visao, desenho),
            "Rabisco": Rabisco_Ferramenta(visao, desenho),
            "Quadrado": Quadrado_Ferramenta(visao, desenho),
        }
        self.estado = self.ferramentas["Linha"]  # ferramenta inicial

        self.canvas.bind("<ButtonPress-1>", self.mouse_pressionado)
        self.canvas.bind("<B1-Motion>", self.mouse_arrastado)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_solto)

    def mouse_pressionado(self, event):
        tipo = self.visao.tipo_figura_var.get()
        self.estado = self.ferramentas[tipo]
        self.estado.mouse_pressionado(event)

    def mouse_arrastado(self, event):
      self.estado.mouse_arrastado(event)
      self.desenho.desenha_figuras(self.canvas)
      self.estado.figura_nova.desenha(self.canvas, dash=(4, 2))
    
    
    def mouse_solto(self, event):
        self.estado.mouse_solto(event)
        self.desenho.desenha_figuras(self.canvas)