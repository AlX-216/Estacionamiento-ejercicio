from Models.lugar import Lugar
from Models.vehiculo import Vehiculo
from services.estacionamiento_service import EstacionamientoService
    

lugares = [
    Lugar(1),
    Lugar(2),
    Lugar(3)
]
estacionamiento = EstacionamientoService(lugares)
vehiculo = Vehiculo("ABC-123", "Automovil")
ticket = estacionamiento.registrar_entrada(vehiculo)
ticket.mostrar()