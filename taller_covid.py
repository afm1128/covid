# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 08:25:33 2021

@author: Verde
"""


import numpy as np
import pandas as pd

url = "Casos_positivos_de_COVID-19_en_Colombia.csv"
df = pd.read_csv(url)

df.drop(['Código ISO del país','Nombre del grupo étnico','Pertenencia étnica',
         'Tipo de recuperación', 'Nombre del país' ],
axis =1, inplace = True)

df.loc[df['Ubicación del caso'] == 
       'CASA', 'Ubicación del caso'] = 'Casa'
df.loc[df['Ubicación del caso'] == 
       'casa', 'Ubicación del caso'] = 'Casa'
df.loc[df['Estado'] == 
       'leve', 'Estado'] = 'Leve'
df.loc[df['Estado'] == 
       'LEVE', 'Estado'] = 'Leve'
df.loc[df['Recuperado'] == 
       'fallecido', 'Recuperado'] = 'Fallecido'
df.loc[df['Nombre departamento'] == 
       'BARRANQUILLA', 'Nombre departamento'] = 'ATLANTICO'
df.loc[df['Nombre departamento'] == 
       'CARTAGENA', 'Nombre departamento'] = 'BOLIVAR'
df.loc[df['Nombre departamento'] == 
       'STA MARTA D.E ', 'Nombre departamento'] = 'MAGDALENA'
# Punto 1: Número de casos de Contagiados en el País.
C = df[df['Ubicación del caso']== 'Casa'].shape[0]
H = df[df['Ubicación del caso']== 'Hospital'].shape[0]
U = df[df['Ubicación del caso']== 'Hospital UCI'].shape[0]
F = df[df['Ubicación del caso']== 'Fallecido'].shape[0]
G = C + H + U + F
print(f'El número de contagiados en colombia es: {G}' ) 

#Punto 2: Número de Municipios Afectados
B = df.groupby('Nombre municipio').size()
print(f'De los 1.103 municipos de Colombia, han sido afectados: {len(B)}' )

#Punto 4: Número de personas que se encuentran en atención en casa
S = df[df['Ubicación del caso']=='Casa'].shape[0]
print(f'El número de personas que estan en atención en casa: {S}' )

#Punto 5: Número de personas que se encuentran recuperados
R =  df[df['Recuperado'] == 'Recuperado'].shape[0]
print(f'El número de personas recuperados es: {R}' )

#Punto 6: Número de personas que ha fallecido
F = df[df['Recuperado'] == 'Fallecido'].shape[0]
print(f'El número de personas que han fallecido es: {F}')

#Punto 7: Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)
df.groupby('Tipo de contagio').size().sort_values(ascending = False)

#Punto 8: Número de departamentos afectados
D = df.groupby('Nombre departamento').size()
print(f'De los 33 departamentos de Colombia, han sido afectados: {len(D)}')

#Punto 9: Liste los departamentos afectados(sin repetirlos)
D = df.groupby('Nombre departamento').size()

#Punto 10: Ordene de mayor a menor por tipo de atención
df.groupby('Ubicación del caso').size().sort_values(ascending = False)

#Punto 11: Liste de mayor a menor los 10 departamentos con mas casos de contagiados
df.groupby('Nombre departamento').size().sort_values(ascending = False).head(10)

#Punto 12: Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
df[df['Estado'] =='Fallecido']['Nombre departamento'].value_counts().head(10)

#Punto 13: Liste de mayor a menor los 10 departamentos con mas casos de recuperados
df[df['Recuperado'] =='Recuperado']['Nombre departamento'].value_counts().head(10)

#Punto 14: Liste de mayor a menor los 10 municipios con mas casos de contagiados
df.groupby('Nombre municipio').size().sort_values(ascending = False).head(10)

#Punto 15: Liste de mayor a menor los 10 municipios con mas casos de fallecidos
df[df['Estado'] =='Fallecido']['Nombre municipio'].value_counts(ascending = False).head(10)

#Punto 16: Liste de mayor a menor los 10 municipios con mas casos de recuperados
df[df['Recuperado'] =='Recuperado']['Nombre municipio'].value_counts(ascending = False).head(10)

