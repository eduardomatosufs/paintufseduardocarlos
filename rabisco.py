from figura import Figura
from dataclasses import dataclass

#Classe concreta Rabisco, herda cores de Figura
@dataclass
class Rabisco(Figura):
    pontos: list # lista de pontos

    # Desenha os pontos com a cor da borda
    def desenha(self, canvas, dash=()):
        canvas.create_line(self.pontos, dash=dash, fill=self.cor_borda )

    # Rabisco vazio(1 ponto ou menos)
    def vazia(self):
        return len(self.pontos) <= 1