
class ConnectionManager:
    _hay_conexion = False

    def __init__(self):
        self._hay_conexion = False

    @staticmethod
    def conectate():
        # se abre la conexión
        ConnectionManager._hay_conexion = True

    @staticmethod
    def desconectate():
        # se cierra la conexión
        ConnectionManager._hay_conexion = False

    @staticmethod
    def hay_conexion():
        return ConnectionManager._hay_conexion
