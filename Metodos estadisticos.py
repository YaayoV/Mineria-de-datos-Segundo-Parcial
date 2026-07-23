import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier, plot_tree

archivo_csv = Path(__file__).with_name("dataset_sucursales_mensual.csv")
df = pd.read_csv(archivo_csv)
df = df.rename(columns={
    "Gasto_Publicidad": "Publicidad",
    "Clientes_Atendidos": "Clientes",
    "Satisfaccion_Cliente": "Satisfaccion",
    "Descuento_Promedio": "Descuento",
})
features = ["Publicidad", "Clientes", "Satisfaccion", "Descuento"]
variables = features + ["Ventas_Totales"]

print("Medidas descriptivas:")
print(df.describe(include="all"))
print("\nCorrelaciones con Ventas_Totales:")
print(df[variables].corr()["Ventas_Totales"].drop("Ventas_Totales").round(3))

corr = df[variables].corr()
fig, ax = plt.subplots(figsize=(8, 6))
image = ax.matshow(corr, cmap="coolwarm")
ax.set_xticks(range(len(variables)), variables, rotation=90)
ax.set_yticks(range(len(variables)), variables)
fig.colorbar(image)
ax.set_title("Matriz de correlación", pad=20)
plt.show()

X = df[features]
y = df["Cumplio_Meta"].map({"Si": 1, "Sí": 1, "No": 0})
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

models = {
    "Árbol de decisión": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Naive Bayes": GaussianNB(),
    "Regresión Logística": LogisticRegression(max_iter=200),
}
for name, model in models.items():
    model.fit(X_train, y_train)
    print(f"\n{name}:\n{classification_report(y_test, model.predict(X_test))}")

plt.figure(figsize=(12, 8))
plot_tree(
    models["Árbol de decisión"],
    feature_names=features,
    class_names=["No", "Sí"],
    filled=True,
)
plt.show()

y_sales = df["Ventas_Totales"]
for title, cols in [
    ("Regresión Lineal Simple (Publicidad → Ventas_Totales)", ["Publicidad"]),
    ("Regresión Múltiple (Todas las variables → Ventas_Totales)", features),
]:
    model = LinearRegression().fit(df[cols], y_sales)
    print(f"\n{title}")
    print("Coeficiente:" if len(cols) == 1 else "Coeficientes:", model.coef_[0] if len(cols) == 1 else model.coef_)
    print("Intercepto:", model.intercept_)
    if len(cols) == 1:
        plt.scatter(df[cols[0]], y_sales, color="blue")
        plt.plot(df[cols[0]], model.predict(df[cols]), color="red")
        plt.xlabel("Publicidad")
        plt.ylabel("Ventas Totales")
        plt.title("Regresión Lineal Simple")
        plt.show()