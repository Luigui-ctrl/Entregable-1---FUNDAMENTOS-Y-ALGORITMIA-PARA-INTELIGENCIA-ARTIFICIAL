import numpy as np

# Variables globales para almacenar últimos datos generados
ultimo_vector = None
ultima_matriz = None

# Generación de vectores o matrices

def crear_matriz(filas, columnas, minimo=0, maximo=10):
    if filas <= 0 or columnas <= 0:
        raise ValueError("Las dimensiones deben ser mayores que cero.")
    return np.random.randint(minimo, maximo + 1, size=(filas, columnas))

def capturar_matriz(nombre="matriz"):
    try:
        filas = int(input(f"Ingrese el número de filas de la {nombre}: "))
        columnas = int(input(f"Ingrese el número de columnas de la {nombre}: "))
    except ValueError:
        raise ValueError("Debe ingresar números enteros válidos.")

    print(f"Ingrese los datos fila por fila, separados por espacios:")

    matriz = []
    for i in range(filas):
        fila = input(f"Fila {i + 1}: ").strip().split()
        if len(fila) != columnas:
            raise ValueError(f"Se esperaban {columnas} valores en la fila {i + 1}.")
        matriz.append([int(x) for x in fila])

    matriz_np = np.array(matriz)
    verificar_matriz(matriz_np)
    return matriz_np

def seleccionar_modo_entrada(nombre="vector o matriz"):
    while True:
        modo = input(f"\n¿Desea ingresar el {nombre} manualmente (m) o generarlo aleatoriamente (a)? [m/a]: ").strip().lower()
        if modo == "m":
            return "manual"
        elif modo == "a":
            return "aleatorio"
        else:
            print("Opción inválida. Escriba 'm' o 'a'.")

def obtener_vector(nombre="vector"):
    modo = seleccionar_modo_entrada(nombre)
    if modo == "manual":
        return capturar_vector(nombre)
    else:
        tamaño = int(input(f"Ingrese el tamaño del {nombre}: "))
        return crear_matriz(tamaño, 1).flatten()

def obtener_matriz(nombre="matriz"):
    modo = seleccionar_modo_entrada(nombre)
    if modo == "manual":
        return capturar_matriz(nombre)
    else:
        filas = int(input(f"Ingrese el número de filas de la {nombre}: "))
        columnas = int(input(f"Ingrese el número de columnas de la {nombre}: "))
        return crear_matriz(filas, columnas)

# Captura y validación

def capturar_vector(nombre="vector"):
    entrada = input(f"Introduzca los valores del {nombre} separados por espacios: ").strip().split()
    vector = np.array([int(i) for i in entrada])
    verificar_vector(vector)
    return vector

def verificar_vector(v):
    if v is None or v.ndim != 1 or np.any(np.isnan(v)) or v.size == 0:
        raise ValueError("Vector inválido. Asegúrese de que sea unidimensional, sin NaN y con datos.")

def verificar_matriz(m):
    if m is None or m.ndim != 2 or np.any(np.isnan(m)) or m.size == 0:
        raise ValueError("Matriz inválida. Asegúrese de que sea bidimensional, sin NaN y con datos.")

# Propiedades Algebraicas

def propiedad_conmutativa(v1, v2, tipo="suma"):
    verificar_vector(v1)
    verificar_vector(v2)
    if v1.shape != v2.shape:
        raise ValueError("Ambos vectores deben tener el mismo tamaño.")
    
    if tipo == "suma":
        lado1 = v1 + v2
        lado2 = v2 + v1
    elif tipo == "multiplicacion":
        lado1 = v1 * v2
        lado2 = v2 * v1
    else:
        raise ValueError("Operación inválida. Use 'suma' o 'multiplicacion'.")

    print(f"\n Comprobación de la propiedad conmutativa ({tipo}):")
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Lado 1:", lado1)
    print("Lado 2:", lado2)
    print("¿Se verifica?:", "Sí" if np.array_equal(lado1, lado2) else "No")

def propiedad_asociativa(v1, v2, tipo="suma"):
    verificar_vector(v1)
    verificar_vector(v2)
    if v1.shape != v2.shape:
        raise ValueError("Ambos vectores deben tener el mismo tamaño.")

    if tipo == "suma":
        lado1 = (v1 + v2) + v2
        lado2 = v1 + (v2 + v2)
    elif tipo == "multiplicacion":
        lado1 = (v1 * v2) * v2
        lado2 = v1 * (v2 * v2)
    else:
        raise ValueError("Operación inválida. Use 'suma' o 'multiplicacion'.")

    print(f"\n Evaluando propiedad asociativa ({tipo}):")
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Lado 1:", lado1)
    print("Lado 2:", lado2)
    print("¿Es correcta?:", "Se cumple" if np.array_equal(lado1, lado2) else "No se cumple")

def propiedad_distributiva(v1, v2):
    verificar_vector(v1)
    verificar_vector(v2)
    if v1.shape != v2.shape:
        raise ValueError("Ambos vectores deben tener el mismo tamaño.")

    lado1 = v1 * (v2 + v1)
    lado2 = (v1 * v2) + (v1 * v1)

    print("\n Verificación de la propiedad distributiva:")
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Lado 1:", lado1)
    print("Lado 2:", lado2)
    print("¿Resultado correcto?:", "Sí" if np.array_equal(lado1, lado2) else "No")

def propiedad_inversa(v, tipo="suma"):
    verificar_vector(v)
    if tipo == "suma":
        inverso = -v
        resultado = v + inverso
        esperado = np.zeros_like(v)
    elif tipo == "multiplicacion":
        if np.any(v == 0):
            raise ValueError("No se puede calcular el inverso multiplicativo con ceros.")
        inverso = 1 / v
        resultado = v * inverso
        esperado = np.ones_like(v)
    else:
        raise ValueError("Operación inválida. Use 'suma' o 'multiplicacion'.")

    print(f"\n Demostración de la propiedad inversa ({tipo}):")
    print("Vector:", v)
    print("Inverso:", inverso)
    print("Resultado:", resultado)
    print("Valor esperado:", esperado)
    print("¿Se cumple?:", "Sí" if np.allclose(resultado, esperado) else "No")

# Menú Interactivo

def seleccionar_operacion():
    operacion = input("Seleccione tipo de operación ('s' para suma o 'm' para multiplicación): ").strip().lower()
    if operacion == "s":
        return "suma"
    elif operacion == "m":
        return "multiplicacion"
    else:
        raise ValueError("Operación inválida. Ingrese solamente 's' o 'm'.")

def principal():
    global ultimo_vector, ultima_matriz

    while True:
        print("\n MENÚ DE PROPIEDADES ALGEBRAICAS")
        print("1. Crear vector (manual o aleatorio)")
        print("2. Crear matriz (manual o aleatoria)")
        print("3. Conmutativa")
        print("4. Asociativa")
        print("5. Distributiva")
        print("6. Inversa")
        print("7. Salir")

        opcion = input("Elija una opción (1-7): ").strip()
        try:
            if opcion == "1":
                ultimo_vector = obtener_vector("vector")
                print("Vector generado:", ultimo_vector)

            elif opcion == "2":
                ultima_matriz = obtener_matriz("matriz")
                print("Matriz generada:\n", ultima_matriz)

            elif opcion == "3":
                v1 = obtener_vector("vector 1")
                v2 = obtener_vector("vector 2")
                tipo = seleccionar_operacion()
                propiedad_conmutativa(v1, v2, tipo)

            elif opcion == "4":
                v1 = obtener_vector("vector 1")
                v2 = obtener_vector("vector 2")
                tipo = seleccionar_operacion()
                propiedad_asociativa(v1, v2, tipo)

            elif opcion == "5":
                v1 = obtener_vector("vector 1")
                v2 = obtener_vector("vector 2")
                tipo = seleccionar_operacion()
                propiedad_distributiva(v1, v2)

            elif opcion == "6":
                v = obtener_vector("vector")
                tipo = seleccionar_operacion()
                propiedad_inversa(v, tipo)

            elif opcion == "7":
                print("Programa finalizado.")
                break

            else:
                print("Opción incorrecta, intente nuevamente.")

        except Exception as e:
            print(f"Error detectado: {e}")

if __name__ == "__main__":
    principal()
