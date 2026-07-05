import pandas as pd
datos = pd.read_csv("estudiantes.csv")

print("\n----- Horas de estudio y Calificacion Final -----")
correlacion = datos["Horas_Estudio"].corr(datos["Calificacion_Final"])
print("correlacion:", correlacion)

print("\n----- Asistencia y Calificacion Final -----")
correlacion = datos["Asistencia"].corr(datos["Calificacion_Final"])
print("correlacion:", correlacion)

print("\n----- Tareas y Calificacion Final -----")
correlacion = datos["Tareas"].corr(datos["Calificacion_Final"])
print("correlacion:", correlacion)

print("\n----- Examen y Calificacion Final -----")
correlacion = datos["Examen"].corr(datos["Calificacion_Final"])
print("correlacion:", correlacion)