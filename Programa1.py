print("ESTO ES UNA PRUEBA")

print("ASIGNACION:")
mensaje = "Hi"
mensaje += " - "
mensaje += "Estoy practicando mucho" 
print(mensaje)

print("find")
valor = "mucho"
buscar = mensaje.find(valor)
print("El valor buscado se encuentre en la posicion:  ")
print(buscar)

print("EXTRAE")

extrae = mensaje[int(buscar):25]
print(extrae)

print("CONCATENACION:")
nombre = "Juan"
espacio = " - "
apellido = " Mallarino"
print(mensaje + " // " + nombre + espacio + apellido )

print("COMPARACION")
mensaje1 = "Juan"
mensaje2 = "Juan"
print(mensaje1 == mensaje2)

