def calcular_promedio(lista):
    total = sum(lista)
    promedio = total / len(lista)
    return promedio

def main():
    numeros = []
    for i in range(10):
        numero = float(input("Ingresa el número {}: ".format(i + 1)))
        numeros.append(numero)
    
    print("Lista de números ingresados:", numeros)
    
    promedio = calcular_promedio(numeros)
    print("El promedio de los números ingresados es:", promedio)

if __name__ == "__main__":
    main()
