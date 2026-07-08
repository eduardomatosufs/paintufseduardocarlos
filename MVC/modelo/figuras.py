from abc import ABC, abstractmethod
from dataclasses import dataclass

# Classe abstrata Figura, o molde para as figuras
@dataclass
class Figura(ABC):
    cor_borda: str
    cor_preenchimento: str

    # Obriga as subclasses a terem seu proprio desenha
    @abstractmethod
    def desenha(self, canvas, dash=()):
        pass

    # Obriga as subclasses a dizerem quando estao vazias
    @abstractmethod
    def vazia(self):
        pass


# Classe concreta Linha, herda cores de Figura
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

    # Desenha a linha usando a cor da borda
    def desenha(self, canvas, dash=()):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, dash=dash, fill=self.cor_borda)

    # Linha vazia, os dois pontos sao iguais
    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


# Classe concreta Retangulo, herda cores de Figura
@dataclass
class Retangulo(Figura):
    x1: int
    y1: int
    x2: int
    y2: int

    # Junta os 4 valores num so pra formar os pontos
    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    # Desenha o retangulo com a cor da borda e preenchimento
    def desenha(self, canvas, dash=()):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, dash=dash, outline=self.cor_borda, fill=self.cor_preenchimento)

    # Retangulo vazio se virou linha (altura ou largura zero)
    def vazia(self):
       largura = abs(self.x2 - self.x1)
       altura = abs(self.y2 - self.y1)
       return largura == 0 or altura == 0


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
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, dash=dash, outline=self.cor_borda, fill=self.cor_preenchimento)

    # Oval vazio se virou linha(altura ou largura 0)
    def vazia(self):
       largura = abs(self.x2 - self.x1)
       altura = abs(self.y2 - self.y1)
       return largura == 0 or altura == 0


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


# Classe concreta Rabisco, herda cores de Figura
@dataclass
class Rabisco(Figura):
    pontos: list

    # Desenha os pontos com a cor da borda
    def desenha(self, canvas, dash=()):
        canvas.create_line(self.pontos, dash=dash, fill=self.cor_borda)

    # Rabisco vazio (1 ponto ou menos)
    def vazia(self):
        return len(self.pontos) <= 1