from dataclasses import dataclass
from figura import Figura

# Classe concreta Oval, herda cores de Figura
@dataclass
class Oval(Figura):
    x1: int
    y1: int
    x2: int
    y2: int

    # Junta os 4 valores num so pra formar os pontos
    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    # Desenha o oval com a cor da borda e preenchimento
    def desenha(self, canvas, dash=()):
        canvas.create_oval(self.pontos, dash=dash, outline=self.cor_borda, fill=self.cor_preenchimento)

    # Oval vazio, os 2 pontos sao iguais
    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)