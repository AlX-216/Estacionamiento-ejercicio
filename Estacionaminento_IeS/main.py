from Models.lugar import Lugar
from Models.vehiculo import Vehiculo
from Models.ticket import Ticket

vehiculo = Vehiculo("ABC-123", "Automovil")
lugar = Lugar(1)
lugar.ocupar()
ticket = Ticket(1001, vehiculo, lugar)
ticket.mostrar()