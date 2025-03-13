meses = ("Enero", "febrero", "Marzo", "Abril", "Mayo", "Junio", "julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
num_mes = int(input("Ingrese un numero del mes del 1 al 12: "))

if 1 <= num_mes <= 12:
    print(f"El mes corresponde a {meses[num_mes - 1]}")
else:
    print("Número inválido")