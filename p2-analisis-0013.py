# Importar librerias
import pandas as pd
import numpy as np
print("---- Analisis de datos de Pacientes Meredith Aguirre NC = 0013 ----")
pacientes = {
    "Nombre": ["Ana", "Luis", "Marta", "Roberto", "Carla", "Javier"],
    "Presion_Arterial": [120, 140, 135, 110, 150, 125],
    "Fumador": [False, True, False, False, True, True],
    "Nivel_Riesgo": ["Bajo", "Alto", "Medio", "Bajo", "Alto", "Medio"]
}
df = pd.DataFrame(pacientes)
print(df)
print("-+-+-+- Agrupar por una sola columna Presion_Arterial-+-+-+-")
agrupado = df.groupby('Presion_Arterial')
print(agrupado)
print("-+-+-+- Promedio de pacientes fumadores -+-+-+-")
# Promedio de pacientes fumadores
print(agrupado['Fumador'].mean())
print("-+-+-+- Nivel de riesgo maximo a pacientes -+-+-+-")
# Nivel de riesgo maximo a pacientes
print(agrupado['Nivel_Riesgo'].max())