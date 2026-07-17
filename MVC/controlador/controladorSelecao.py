from modelo.desenho import *
from visao.janelaPaint import *


class ControladorSelecao:
    def __init__(self,desenho,visao):
      self.desenho = desenho
      self.visao = visao
      self.visao.root.bind("<Delete>", self.apaga)
      self.visao.root.bind("<Control-c>", self.copia)
      self.visao.root.bind("<Control-v>", self.cola)
      self.visao.root.bind("<Right>", self.para_frente)
      self.visao.root.bind("<Left>", self.para_tras)
      self.visao.root.bind("<Up>", self.para_topo)
      self.visao.root.bind("<Down>", self.para_fundo)


    # Apaga a figura selecionada
    def apaga(self, event):
        self.desenho.apaga_selecionada()

    # Copia a figura selecionada
    def copia(self, event):
        self.desenho.copiar_selecionada()
    
    # Cola a figura 
    def cola(self,event):
       self.desenho.colar()
       self.desenho.desenha_figuras(self.visao.canvas)

    # Move a selecionada uma posicao pra frente
    def para_frente(self, event):
      self.desenho.selecionada_para_frente()
      self.desenho.desenha_figuras(self.visao.canvas)

   # Move a selecionada uma posicao pra tras
    def para_tras(self, event):
     self.desenho.selecionada_para_tras()
     self.desenho.desenha_figuras(self.visao.canvas)

   # Move a selecionada pro topo (fica na frente de todas)
    def para_topo(self, event):
     self.desenho.selecionada_para_topo()
     self.desenho.desenha_figuras(self.visao.canvas)

   # Move a selecionada pro fundo (fica atras de todas)
    def para_fundo(self, event):
     self.desenho.selecionada_para_fundo()
     self.desenho.desenha_figuras(self.visao.canvas)