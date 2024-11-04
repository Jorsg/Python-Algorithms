"""
Algorithm that calculate stadistis like average, variance and deviation
"""

def calcular_estadisticas(datos):
    # args: datos list: list numbs
    
    # 1. calcula el promedio
    n = len(datos)
    promedio = sum(datos) / n

    # 2. calcula la varianza
    #suma de las diferencias al cuadrado entre valor y promedio
    sum_diferen_cuadra = sum((x - promedio) ** 2 for x in datos)
    varianza = sum_diferen_cuadra / n

    #3. calcular la desviacion standar
    #raiz cuadrada de la varianza

    desviacion = varianza ** 0.5

    return promedio, varianza, desviacion

if __name__ == "__main__":
    # Datos de ejemplo
    datos_ejemplo = [2, 4, 4, 4, 5, 5, 7, 9]
    
    # Calcular estadísticas
    promedio, varianza, desviacion = calcular_estadisticas(datos_ejemplo)
    
    # Mostrar resultados
    print(f"Datos: {datos_ejemplo}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Varianza: {varianza:.2f}")
    print(f"Desviación Estándar: {desviacion:.2f}")
