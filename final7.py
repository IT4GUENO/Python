numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

print("La lista de los números son", numeros)
print("La suma de los números s0n", sum(numeros))