from figura import Figura
from dataclasses import dataclass

# Classe concreta Circulo, herda cores de Figura
@dataclass
class Circulo(Figura):
    centro_x: int
    centro_y: int
    raio: float

    # Monta a caixa do oval por centro e raio e desenha
    def desenha(self, canvas, dash=()):
        canvas.create_oval(self.centro_x-self.raio, self.centro_y-self.raio, self.centro_x+self.raio, self.centro_y+self.raio, dash=dash, outline=self.cor_borda, fill=self.cor_preenchimento)

    # Circulo vazio (raio 0)
    def vazia(self):
        return self.raio == 0