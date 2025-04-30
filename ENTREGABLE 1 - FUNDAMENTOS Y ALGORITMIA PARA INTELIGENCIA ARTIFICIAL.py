import numpy as n
  
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
    # Se genera una matriz
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
