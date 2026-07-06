import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("estudiantes.csv")

print("\n----- Horas de estudio y Calificacion Final -----")
correlacion = datos["Horas_Estudio"].corr(datos["Calificacion_Final"])
print("correlacion:", correlacion)

plt.scatter(datos["Horas_Estudio"], datos["Calificacion_Final"])
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación final")
plt.title("Horas de estudio vs Calificación final")
plt.show()

print("\n----- Asistencia y Calificacion Final -----")
correlacion = datos["Asistencia"].corr(datos["Calificacion_Final"])
print("correlacion:", correlacion)

plt.scatter(datos["Asistencia"], datos["Calificacion_Final"])
plt.xlabel("Asistencia")
plt.ylabel("Calificación final")
plt.title("Asistencia vs Calificación final")
plt.show()

print("\n----- Tareas y Calificacion Final -----")
correlacion = datos["Tareas"].corr(datos["Calificacion_Final"])
print("correlacion:", correlacion)

plt.scatter(datos["Tareas"], datos["Calificacion_Final"])
plt.xlabel("Tareas")
plt.ylabel("Calificación final")
plt.title("Tareas vs Calificación final")
plt.show()

print("\n----- Examen y Calificacion Final -----")
correlacion = datos["Examen"].corr(datos["Calificacion_Final"])
print("correlacion:", correlacion)

plt.scatter(datos["Examen"], datos["Calificacion_Final"])
plt.xlabel("Examen")
plt.ylabel("Calificación final")
plt.title("Examen vs Calificación final")
plt.show()

print("\n----- Edad y Calificacion Final -----")
correlacion = datos["Edad"].corr(datos["Calificacion_Final"])
print("correlacion:", correlacion)

plt.scatter(datos["Edad"], datos["Calificacion_Final"])
plt.xlabel("Edad")
plt.ylabel("Calificación final")
plt.title("Edad vs Calificación final")
plt.show()