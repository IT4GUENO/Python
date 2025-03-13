notas = {"Juan" : 85, "María": 90, "Pedro" : 78, "Ana": 92}
name = input("Ingresa el nombre del estudiante: ")

if name in notas:
    print(f"La nota de {name} es {notas[name]}")
else:
    print("Estudiante no encontrado")