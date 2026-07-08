from modelo.figuras import *

# Classe Desenho, guarda e gerencia todas as figuras (o Model)
class Desenho:
    def __init__(self):
        self.__figuras = []      # todas as figuras desenhadas

    # Adiciona uma figura à lista
    def adiciona_figura(self, figura):
        self.__figuras.append(figura)

    # Limpa o canvas e redesenha todas as figuras salvas
    def desenha_figuras(self, canvas, dash=()):
        canvas.delete("all")
        for figura in self.__figuras:
            figura.desenha(canvas, dash=dash)