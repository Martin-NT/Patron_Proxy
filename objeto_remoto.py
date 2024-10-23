# REAL SUBJECT: define el objeto real 
from iguardar import IGuardar

class ObjetoRemoto(IGuardar):
    def save(self, datos_a_guardar):
        print("Guardando datos en el objeto remoto...")
