def mcd(n, m):
    """
    Calcula el máximo común divisor (MCD) entre dos número.

    Parámetros
    ----------
    n : int
    El primer número
    m : int
    El segundo número

    Retorna
    ----------
    El MCD de los dos números
    """
    # Verificamos que ambos números sean enteros
    if type(n) == int and n>0 and type(m) == int and m>0 :

        # Verificamos que, si los números son iguales, el MCD es el mismo número
        if n == m:
            mcd = n
            return mcd

        if n > m:
            mayor = n
            menor = m
        elif n < m:
            mayor = m
            menor = n

        resto = mayor % menor

        # Definimos que si el resto de la división es cero, el MCD es el divisor
        if resto == 0:
            mcd = menor
            return mcd

        elif resto != 0:
            divisor = menor
             # Ocupamos un ciclo while donde se aplique el algoritmo de Euclides para calcular el MCD, que seria el ultimo divisor
            while resto != 0:
                n_res = divisor % resto
                ult_div = resto
                divisor = resto
                resto = n_res           
            mcd = ult_div
            return mcd
            
    # Si el valor ingresado no es es un entero
    else:
        print("ERROR: Valores Inválidos, ingresa enteros")
        return None
