from estado.ferramenta import Ferramenta
from modelo.figuras import *
from dataclasses import dataclass

# Classe concreta Linha_Ferramenta: cria e atualiza uma Linha (herda o comportamento de Ferramenta)
@dataclass
class Linha_Ferramenta(Ferramenta):
    def mouse_pressionado(self, event):
        cor_borda = self.visao.cor_borda
        cor_preenchimento = self.visao.cor_preenchimento
        self.figura_nova = Linha(cor_borda, cor_preenchimento, event.x, event.y, event.x, event.y)

    def mouse_arrastado(self, event):
        self.figura_nova.x2 = event.x
        self.figura_nova.y2 = event.y

    def mouse_solto(self, event):
        if not self.figura_nova.vazia():
            self.desenho.adiciona_figura(self.figura_nova)

# Classe concreta Retangulo_Ferramenta: cria e atualiza um Retangulo (herda o comportamento de Ferramenta)
@dataclass
class Retangulo_Ferramenta(Ferramenta):
    def mouse_pressionado(self, event):
        cor_borda = self.visao.cor_borda
        cor_preenchimento = self.visao.cor_preenchimento
        self.figura_nova = Retangulo(cor_borda, cor_preenchimento, event.x, event.y, event.x, event.y)

    def mouse_arrastado(self, event):
        self.figura_nova.x2 = event.x
        self.figura_nova.y2 = event.y

    def mouse_solto(self, event):
        if not self.figura_nova.vazia():
            self.desenho.adiciona_figura(self.figura_nova)

# Classe concreta Oval_Ferramenta: cria e atualiza um Oval (herda o comportamento de Ferramenta)
@dataclass
class Oval_Ferramenta(Ferramenta):
    def mouse_pressionado(self, event):
        cor_borda = self.visao.cor_borda
        cor_preenchimento = self.visao.cor_preenchimento
        self.figura_nova = Oval(cor_borda, cor_preenchimento, event.x, event.y, event.x, event.y)

    def mouse_arrastado(self, event):
        self.figura_nova.x2 = event.x
        self.figura_nova.y2 = event.y

    def mouse_solto(self, event):
        if not self.figura_nova.vazia():
            self.desenho.adiciona_figura(self.figura_nova)

# Classe concreta Circulo_Ferramenta: cria e atualiza um Circulo (herda o comportamento de Ferramenta)
@dataclass
class Circulo_Ferramenta(Ferramenta):
    def mouse_pressionado(self, event):
        cor_borda = self.visao.cor_borda
        cor_preenchimento = self.visao.cor_preenchimento
        self.figura_nova = Circulo(cor_borda, cor_preenchimento, event.x, event.y, 0)

    
    def mouse_arrastado(self, event):
        raio = ((event.x - self.figura_nova.centro_x)**2 + (event.y - self.figura_nova.centro_y)**2)**0.5
        self.figura_nova.raio = raio

    
    def mouse_solto(self, event):
        if not self.figura_nova.vazia():
            self.desenho.adiciona_figura(self.figura_nova)

# Classe concreta Circulo_Ferramenta: cria e atualiza um Rabisco (herda o comportamento de Ferramenta)
@dataclass 
class Rabisco_Ferramenta(Ferramenta):
    def mouse_pressionado(self, event):
        cor_borda = self.visao.cor_borda
        cor_preenchimento = self.visao.cor_preenchimento
        self.figura_nova = Rabisco(cor_borda,cor_preenchimento,[(event.x,event.y)])

    def mouse_arrastado(self, event):
        self.figura_nova.pontos.append((event.x, event.y))
        

    
    def mouse_solto(self, event):
        if not self.figura_nova.vazia():
            self.desenho.adiciona_figura(self.figura_nova)

# Classe concreta Quadrado_Ferramenta: cria e atualiza um Quadrado (herda o comportamento de Ferramenta)
@dataclass
class Quadrado_Ferramenta(Ferramenta):
    def mouse_pressionado(self, event):
        cor_borda = self.visao.cor_borda
        cor_preenchimento = self.visao.cor_preenchimento
        self.figura_nova = Quadrado(cor_borda, cor_preenchimento, event.x, event.y, event.x, event.y)
    

    def mouse_arrastado(self, event):
        dx = event.x - self.figura_nova.x1   #Olha o quanto moveu em x (dx) e o quanto moveu em y (dy), e o maior dos dois vira o tamanho do lado. 
        dy = event.y - self.figura_nova.y1
        lado = max(abs(dx), abs(dy))

        if dx >= 0:    # Se moveu pra direita, cresce pra direita; se moveu pra esquerda, cresce pra esquerda.Se moveu pra cima, cresce pra cima, pra baixo, cresce pra baixo
          self.figura_nova.x2 = self.figura_nova.x1 + lado
        else:
          self.figura_nova.x2 = self.figura_nova.x1 - lado
        if dy >= 0:
          self.figura_nova.y2 = self.figura_nova.y1 + lado
        else:
          self.figura_nova.y2 = self.figura_nova.y1 - lado


    def mouse_solto(self, event):
        if not self.figura_nova.vazia():
            self.desenho.adiciona_figura(self.figura_nova)