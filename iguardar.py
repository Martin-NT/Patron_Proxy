#SUBJECT: interfaz o clase abstracta que da acceso
from abc import ABC, abstractmethod

class IGuardar(ABC):
    @abstractmethod
    def save(self, datos_a_guardar):
        pass
