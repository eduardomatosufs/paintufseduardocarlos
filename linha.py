from dataclasses import dataclass
from figura import Figura

# Classe concreta linha, herda cores de Figura
@dataclass
class Linha(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    
    # Junta os 4 valores num so pra formar os pontos
    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)
    
    # Desenha a linha com a cor da borda
    def desenha(self, canvas, dash=()):
        canvas.create_line(self.pontos, dash=dash,fill = self.cor_borda)
    
    # Linha vazia, os dois pontos sao iguais
    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)
