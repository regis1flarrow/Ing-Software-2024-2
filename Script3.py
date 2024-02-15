import matplotlib.pyplot as plt
import numpy as np

# Definir la función escogida : una función cuadrática
def f(x):
    return x ** 2

# Generar datos para la gráfica
x = np.linspace(-10, 10, 100)
y = f(x)

# Graficar la función
plt.plot(x, y)
plt.title('Gráfica de una función cuadrática')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()