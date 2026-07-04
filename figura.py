from abc import ABC, abstractmethod
from dataclasses import dataclass

# Classe abstrata figura serve de modelo para as figuras
@dataclass
class Figura(ABC):
    cor_borda: str 
    cor_preenchimento: str

    # Metodo abstrato obriga cada figura a ter seu proprio desenhar
    @abstractmethod
    def desenha(self, canvas, dash=()):
        pass

    # Metodo abstrato para cada figura dizer quando ta vazia
    @abstractmethod
    def vazia(self):
        pass




