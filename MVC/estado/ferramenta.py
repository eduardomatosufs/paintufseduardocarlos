from dataclasses import dataclass
from abc import ABC, abstractmethod
from visao.janelaPaint import JanelaPaint
from modelo.desenho import Desenho


# Classe abstrata Ferramenta(State): define os comportamento das funcoes de desenho
@dataclass
class Ferramenta(ABC):
    visao: JanelaPaint
    desenho: Desenho

    def __post_init__(self):
        self.canvas = self.visao.canvas

    @abstractmethod
    def mouse_pressionado(self, event):
        pass

    @abstractmethod
    def mouse_arrastado(self, event):
        pass

    @abstractmethod
    def mouse_solto(self, event):
        pass