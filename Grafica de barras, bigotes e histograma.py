import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("estudiantes.csv")

#Barras
plt.bar(datos["Nombre"], datos["Calificacion_Final"])
plt.xlabel("Estudiante")
plt.ylabel("Calificación final")
plt.title("Calificación final por estudiante")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#Bigotes
plt.boxplot(datos["Calificacion_Final"])
plt.ylabel("Calificación final")
plt.title("Boxplot de calificaciones finales")
plt.show()

#Histograma
plt.hist(datos["Calificacion_Final"], bins=10)
plt.title("Histograma de calificaciones finales")
plt.xlabel("Calificación final")
plt.ylabel("Frecuencia")
plt.show()