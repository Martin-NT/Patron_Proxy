
from iguardar import IGuardar
from connection_manager import ConnectionManager
from objeto_remoto import ObjetoRemoto
from guardar_disco_duro import GuardarDiscoDuro

class GuardarDatos(IGuardar):
    def save(self, datos_a_guardar):
        if ConnectionManager.hay_conexion():
            ObjetoRemoto().save(datos_a_guardar)
        else:
            GuardarDiscoDuro().save(datos_a_guardar)