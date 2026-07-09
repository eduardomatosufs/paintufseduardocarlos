from modelo.desenho import *
from visao.janelaPaint import *
from controlador.controladorPaint import *

####### MAIN #######
# Cria as tres camadas do MVC e liga tudo:
# a View (interface), o Model (dados) e o Controller (coordenacao)
visao = JanelaPaint()
desenho = Desenho()
controlador = ControladorPaint(desenho, visao)
visao.root.mainloop()