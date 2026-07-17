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

    @abstractmethod
    def contem_ponto(self, x, y):
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
    
    # Olha se o ponto (x, y) ta perto o suficiente da linha (precisa de uma mergem de tolerancia)
    def contem_ponto(self, x, y):
       margem = 5
       dx = self.x2 - self.x1
       dy = self.y2 - self.y1
       comprimento_quadrado = dx**2 + dy**2

       if comprimento_quadrado == 0:
        # a linha "virou" um ponto (x1,y1 == x2,y2)
        distancia = ((x - self.x1)**2 + (y - self.y1)**2)**0.5
       else:
        # calcula o quanto o ponto se projeta ao longo do segmento (t entre 0 e 1)
        t = ((x - self.x1) * dx + (y - self.y1) * dy) / comprimento_quadrado
        t = max(0, min(1, t))  # trava a projecao dentro do segmento
        proj_x = self.x1 + t * dx
        proj_y = self.y1 + t * dy
        distancia = ((x - proj_x)**2 + (y - proj_y)**2)**0.5

        return distancia <= margem

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

   # Verifica se o ponto (x, y) ta dentro da area do retangulo
    def contem_ponto(self, x, y):
      x_min = min(self.x1, self.x2)
      x_max = max(self.x1, self.x2)
      y_min = min(self.y1, self.y2)
      y_max = max(self.y1, self.y2)
      return x_min <= x <= x_max and y_min <= y <= y_max


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
    
    # Verifica se o ponto (x, y) ta dentro da area do oval
    def contem_ponto(self, x, y):
      x_min = min(self.x1, self.x2)
      x_max = max(self.x1, self.x2)
      y_min = min(self.y1, self.y2)
      y_max = max(self.y1, self.y2)
      return x_min <= x <= x_max and y_min <= y <= y_max


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
    
    # # Verifica se o ponto (x, y) ta dentro da area do circulo
    def contem_ponto(self, x, y):
      distancia = ((x - self.centro_x)**2 + (y - self.centro_y)**2)**0.5
      return distancia <= self.raio



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
    
    # Olha se o ponto (x,y) ta perto o suficiente do rabisco (usa a caixa dos pontos + margem)
    def contem_ponto(self, x, y):
       margem = 5
       xs = []
       ys = []
       for ponto in self.pontos:
        xs.append(ponto[0])
        ys.append(ponto[1])
       x_min = min(xs) - margem
       x_max = max(xs) + margem
       y_min = min(ys) - margem
       y_max = max(ys) + margem
       return x_min <= x <= x_max and y_min <= y <= y_max
    
# Classe concreta Quadrado, herda esttutura e comportamento de Retangulo
@dataclass
class Quadrado(Retangulo):
      pass

