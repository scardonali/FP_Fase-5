def calcular_y_clasificar_jornada(matriz_recursos, umbral_horas=40.0):
    """
    Módulo (función) encargado de calcular la suma total de horas semanales 
    por recurso y clasificar su jornada laboral basándose en las reglas de negocio.
    """
    informe_resultados = []
    
    # Recorrido iterativo de la estructura matricial
    for fila in matriz_recursos:
        nombre = fila[0]
        # Slicing para extraer y sumar las horas laboradas de Lunes a Viernes
        horas_diarias = fila[1:]
        total_horas = sum(horas_diarias)
        
        # Estructura de control selectiva (Lógica de Negocio)
        if total_horas > umbral_horas:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar"
            
        # Almacenamiento estructurado de los resultados procesados
        informe_resultados.append({
            "nombre": nombre,
            "total_horas": total_horas,
            "clasificacion": clasificacion
        })
        
    return informe_resultados

def generar_reporte(informe):
    """
    Módulo de salida encargado de presentar los datos consolidados 
    y formateados de manera tabular en la terminal de comandos.
    """
    print("=" * 65)
    print(f"{'REPORTE DE JORNADAS LABORALES SEMANALES':^65}")
    print("=" * 65)
    print(f"{'Nombre del Recurso':<25} | {'Total Horas':<12} | {'Clasificación':<18}")
    print("-" * 65)
    
    for registro in informe:
        print(f"{registro['nombre']:<25} | {registro['total_horas']:<12.1f} | {registro['clasificacion']:<18}")
        
    print("=" * 65)

def main():
    """
    Componente principal de control. Inicializa la matriz de datos con 
    los registros del equipo y coordina las llamadas de ejecución.
    """
    # Matriz inicializada con un mínimo de 4 recursos y sus horas diarias (Lunes a Viernes)
    matriz_horas_trabajadas = [
        ["Santiago Cardona", 8.0, 9.5, 8.0, 10.0, 8.5],
        ["Liliana Restrepo", 8.0, 8.0, 7.5, 8.0, 8.0],
        ["Carlos Mendoza", 10.0, 10.0, 9.0, 8.5, 9.5],
        ["Ana Maria Gómez", 6.0, 7.0, 8.0, 6.5, 7.0]
    ]
    
    # Procesar la lógica de negocio mediante llamada modular
    informe_calculado = calcular_y_clasificar_jornada(matriz_horas_trabajadas)
    
    # Desplegar los resultados por pantalla
    generar_reporte(informe_calculado)

