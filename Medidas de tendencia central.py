import pandas as pd
tdc = pd.read_csv('estudiantes.csv')

print("\n----- EDAD -----")
print("La media de Edad es:", tdc["Edad"].mean())#media
print("La mediana de la Edad es:", tdc["Edad"].median())#mediana
print("La moda de Edad es:", tdc["Edad"].mode()[0])#Moda

print("\n----- ASISTENCIA -----")
print("La media de Asistencia es:", tdc["Asistencia"].mean())#media
print("La mediana de la Asistencia es:", tdc["Asistencia"].median())#mediana
print("La moda de Asistencia es:", tdc["Asistencia"].mode()[0])#Moda

print("\n----- TAREAS -----")
print("La media de Tareas es:", tdc["Tareas"].mean())#media
print("La mediana de la Tareas es:", tdc["Tareas"].median())#mediana
print("La moda de Tareas es:", tdc["Tareas"].mode()[0])#Moda

print("\n----- EXAMEN -----")
print("La media de Examen es:", tdc["Examen"].mean())#media
print("La mediana de la Examen es:", tdc["Examen"].median())#mediana
print("La moda de Examen es:", tdc["Examen"].mode()[0])#Moda

print("\n----- CALIFICACION FINAL -----")
print("La media de la Calificacion Final es:", tdc["Calificacion_Final"].mean())#media
print("La mediana de la Calificacion Final es:", tdc["Calificacion_Final"].median())#mediana
print("La moda de la Calificacion Final es:", tdc["Calificacion_Final"].mode()[0])#Moda

print("\n----- HORAS DE ESTUDIO -----")
print("La media de Horas de estudio es:", tdc["Horas_Estudio"].mean())#media
print("La mediana de Horas de estudio es:", tdc["Horas_Estudio"].median())#mediana
print("La moda de Horas de estudio es:", tdc["Horas_Estudio"].mode()[0])#Moda