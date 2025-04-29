import numpy as np

# Función para generar matrices
def generar_matriz(filas, columnas, min_valor=0, max_valor=10):
    if filas <= 0 or columnas <= 0:
        raise ValueError("Las dimensiones deben ser mayores que cero.")
    if min_valor > max_valor:
        raise ValueError("El valor mínimo no puede ser mayor que el máximo.")
    return np.random.randint(min_valor, max_valor+1, size=(filas, columnas))

# Función para generar vectores
def generar_vector(longitud, min_valor=0, max_valor=10):
    if longitud <= 0:
        raise ValueError("La longitud debe ser mayor que cero.")
    if min_valor > max_valor:
        raise ValueError("El valor mínimo no puede ser mayor que el máximo.")
    return np.random.randint(min_valor, max_valor+1, size=(longitud,))

# Validar vectores
def validar_vectores(*vectores):
    for vector in vectores:
        if vector is None:
            raise ValueError("Uno de los vectores es None.")
        if not isinstance(vector, np.ndarray):
            raise TypeError("Todos los argumentos deben ser vectores numpy.")
        if np.isnan(vector).any():
            raise ValueError("Uno de los vectores contiene valores nulos.")
        if vector.size == 0:
            raise ValueError("Uno de los vectores está vacío.")
        if len(vector.shape) != 1:
            raise ValueError("Se esperaba un vector (arreglo unidimensional).")

# Propiedades con vectores
def propiedad_conmutativa(A, B):
    validar_vectores(A, B)
    if A.shape != B.shape:
        raise ValueError("Los vectores deben tener la misma longitud para la suma.")
    suma_AB = A + B
    suma_BA = B + A
    return np.array_equal(suma_AB, suma_BA)

def propiedad_asociativa(A, B, C):
    validar_vectores(A, B, C)
    if A.shape != B.shape or B.shape != C.shape:
        raise ValueError("Los vectores deben tener la misma longitud para la suma.")
    lado1 = (A + B) + C
    lado2 = A + (B + C)
    return np.array_equal(lado1, lado2)

def propiedad_distributiva(A, B, escalar):
    validar_vectores(A, B)
    if A.shape != B.shape:
        raise ValueError("Los vectores deben tener la misma longitud para la suma.")
    lado1 = escalar * (A + B)
    lado2 = escalar * A + escalar * B
    return np.array_equal(lado1, lado2)

def inverso_aditivo(A):
    validar_vectores(A)
    inverso = -A
    suma = A + inverso
    return np.array_equal(suma, np.zeros_like(A))

# Ejemplo de uso
if __name__ == "__main__":
    # Se genera una matriz (aunque no se usa en propiedades, porque las propiedades son con vectores)
    matriz = generar_matriz(2, 3)
    print("Matriz generada (2x3):\n", matriz)

    # Generar vectores para comprobar propiedades
    A = generar_vector(4)
    B = generar_vector(4)
    C = generar_vector(4)
    escalar = 3

    print("\nVector A:", A)
    print("Vector B:", B)
    print("Vector C:", C)

    print("\nPropiedad Conmutativa:", propiedad_conmutativa(A, B))
    print("Propiedad Asociativa:", propiedad_asociativa(A, B, C))
    print("Propiedad Distributiva:", propiedad_distributiva(A, B, escalar))
    print("Inverso Aditivo (Vector A):", inverso_aditivo(A))
