from modelo.figuras import *
import pickle

# Classe Desenho, guarda e gerencia todas as figuras (o Model)
class Desenho:
    def __init__(self):
        self.__figuras = []      # todas as figuras desenhadas
        self.__selecionada = None # nenhuma figura selecionada no comeco

    # Adiciona uma figura à lista
    def adiciona_figura(self, figura):
        self.__figuras.append(figura)

    # Limpa o canvas e redesenha todas as figuras salvas
    def desenha_figuras(self, canvas, dash=()):
        canvas.delete("all")
        for figura in self.__figuras:
            figura.desenha(canvas, dash=dash)

    def salvar(self, caminho_arquivo):
      with open(caminho_arquivo, "wb") as arquivo: # escreve em binario, porque pickle nao e legivel
         pickle.dump(self.__figuras, arquivo) # escreve o objeto no arquivo

    def abrir(self, caminho_arquivo):
        with open(caminho_arquivo,"rb") as arquivo:  # le binario
         self.__figuras = pickle.load(arquivo) # reconstroi o objeto
   
    # Marca uma figura como selecionada
    def seleciona(self,figura):
       self.__selecionada = figura
    
    # Retorna a figura selecionada ou None se nao tiver nenhuma
    def selecionada(self):
       return self.__selecionada
    
    # Desmarca a selecao da figura
    def limpa_selecao(self):
      self.__selecionada = None

    # Remove a figura selecionada da lista e desmarca a selecao
    def apaga_selecionada(self):
      if self.__selecionada != None:
         self.__figuras.remove(self.__selecionada)
         self.limpa_selecao()

    # Troca a selecionada de posicao com a proxima (avança uma posicao na frente)
    def selecionada_para_frente(self):
      if self.__selecionada != None:
        posicao = self.__figuras.index(self.__selecionada)
        if posicao < len(self.__figuras) - 1:
            self.__figuras[posicao], self.__figuras[posicao + 1] = self.__figuras[posicao + 1], self.__figuras[posicao]
    
    # Troca a selecionada de posicao com a anterior (recua uma posicao pra tras)
    def selecionada_para_tras(self):
      if self.__selecionada != None:
        posicao = self.__figuras.index(self.__selecionada)
        if posicao > 0:
            self.__figuras[posicao], self.__figuras[posicao - 1] = self.__figuras[posicao - 1], self.__figuras[posicao]

    # Remove a selecionada da posicao atual e adiciona no final da lista 
    def selecionada_para_topo(self):
      if self.__selecionada != None:
        self.__figuras.remove(self.__selecionada)
        self.__figuras.append(self.__selecionada)

    # Remove a selecionada da posicao atual e adiciona no inicio da lista 
    def selecionada_para_fundo(self):
        if self.__selecionada != None:
           self.__figuras.remove(self.__selecionada)
           self.__figuras.insert(0,self.__selecionada)