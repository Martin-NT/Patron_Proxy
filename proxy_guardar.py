#PROXY: controla la creacion y el acceso del objeto real
from iguardar import IGuardar
from connection_manager import ConnectionManager
from guardar_disco_duro import GuardarDiscoDuro
from objeto_remoto import ObjetoRemoto

class ProxyGuardar(IGuardar):
    def __init__(self, tipo_guardado="hd"):
        if tipo_guardado == "hd":
            self._guardar_real = GuardarDiscoDuro()
        elif tipo_guardado == "remoto":
            self._guardar_real = ObjetoRemoto()
        else:
            raise ValueError("Tipo de guardado no reconocido.")

    def save(self, datos_a_guardar):
        if ConnectionManager.hay_conexion():
            self._guardar_real.save(datos_a_guardar)
        else:
            print("No hay conexión, no se pueden guardar los datos.")
