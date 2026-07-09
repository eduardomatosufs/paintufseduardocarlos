from modelo.figuras import *
from modelo.desenho import *
from visao.janelaPaint import *

#  Classe ControladorPaint: recebe os eventos do mouse, atualiza o Model (desenho)
# e pede que a View (visao) mostre o resultado
class ControladorPaint:
    def __init__(self, desenho: Desenho, visao: JanelaPaint):
        self.desenho = desenho
        self.visao = visao
        self.figura_nova = None  # figura que está sendo desenhada, mas ainda não foi incluída em figuras
        self.canvas = self.visao.canvas

        # Liga os eventos do mouse a area de desenho
        self.canvas.bind("<ButtonPress-1>", self.iniciar_figura_nova)
        self.canvas.bind("<B1-Motion>", self.atualizar_figura_nova)
        self.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)

    # Cria o objeto da figura no clique
    def iniciar_figura_nova(self, event):
        cor_borda = self.visao.cor_borda
        cor_preenchimento = self.visao.cor_preenchimento
        tipo = self.visao.tipo_figura_var.get()
        if tipo == "Linha":
            self.figura_nova = Linha(cor_borda, cor_preenchimento, event.x, event.y, event.x, event.y)
        elif tipo == "Retângulo":
            self.figura_nova = Retangulo(cor_borda, cor_preenchimento, event.x, event.y, event.x, event.y)
        elif tipo == "Círculo":
            self.figura_nova = Circulo(cor_borda, cor_preenchimento, event.x, event.y, 0)
        elif tipo == "Oval":
            self.figura_nova = Oval(cor_borda, cor_preenchimento, event.x, event.y, event.x, event.y)
        else:
            self.figura_nova = Rabisco(cor_borda, cor_preenchimento, [(event.x, event.y)])

    # Atualiza a figura enquanto o mouse arrasta
    def atualizar_figura_nova(self, event):
        if isinstance(self.figura_nova, Rabisco):
            self.figura_nova.pontos.append((event.x, event.y))
        elif isinstance(self.figura_nova, Circulo):
            raio = ((event.x - self.figura_nova.centro_x)**2 + (event.y - self.figura_nova.centro_y)**2)**0.5
            self.figura_nova.raio = raio
        else:
            self.figura_nova.x2 = event.x
            self.figura_nova.y2 = event.y
        self.desenho.desenha_figuras(self.canvas) # redesenha as figuras já incluídas
        self.figura_nova.desenha(self.canvas, dash=(4, 2))

    # Salva a figura na lista se nao for vazia
    def incluir_figura_nova(self, event):
        if not self.figura_nova.vazia():
            self.desenho.adiciona_figura(self.figura_nova)
        self.desenho.desenha_figuras(self.canvas)