# CLIENTE: solicitan el servicio a través del proxy y se comunican con el objeto real.
from connection_manager import ConnectionManager
from proxy_guardar import ProxyGuardar

def main():
    datos_a_guardar = "Datos importantes"

    # Intentamos guardar los datos sin conexión
    ConnectionManager.desconectate()
    proxy_guardar = ProxyGuardar("remoto")
    proxy_guardar.save(datos_a_guardar)

    # Intentamos guardar los datos con conexión
    ConnectionManager.conectate()
    proxy_guardar = ProxyGuardar("remoto")
    proxy_guardar.save(datos_a_guardar)

if __name__ == "__main__":
    main()
