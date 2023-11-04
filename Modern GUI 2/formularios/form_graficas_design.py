import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FormularioGraficasDesign():

    def __init__(self, panel_principal):           
        # Crear dos subgráficos usando Matplotlib
        figura = Figure(figsize=(8, 6), dpi=100)
        ax1 = figura.add_subplot(211)
        ax2 = figura.add_subplot(212)                
        
        # Ajustar la distribución para agregar espacio de separación en el eje Y
        figura.subplots_adjust(hspace=0.4)

        # Graficar en los subgráficos
        self.grafico1(ax1)
        self.grafico2(ax2)

        # Agregar los gráficos a la ventana de Tkinter
        canvas = FigureCanvasTkAgg(figura, master=panel_principal)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    def grafico1(self, ax):
        # Función para graficar el primer conjunto de datos como un gráfico de barras
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

        # Cambiar a un gráfico de barras
        ax.bar(x, y, label='Gráfico 1', color='blue', alpha=0.7)

        # Personalizar el aspecto del gráfico
        ax.set_title('Gráfico 1 - Gráfico de Barras')
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.legend()

        # Añadir etiquetas a cada barra
        for i, v in enumerate(y):
            ax.text(x[i] - 0.1, v + 0.1, str(v), color='black')

        # Añadir cuadrícula
        ax.grid(axis='y', linestyle='--', alpha=0.7)

    def grafico2(self, ax):
        # Función para graficar el segundo conjunto de datos
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 1, 2, 1]
        ax.plot(x, y, label='Gráfico 2', color='red')
        ax.set_title('Gráfico 2',)
        ax.set_xlabel('Eje X', fontsize=12)
        ax.set_ylabel('Eje Y', fontsize=12)
        ax.plot(x, y, label='Gráfico 2', color='red', linestyle='--', marker='o')
        ax.annotate('Punto importante', xy=(3, 1), xytext=(3.5, 1.5),
                    arrowprops=dict(facecolor='black', shrink=0.05))        
        ax.set_xlim(0, 6)  # Establece los límites del eje x
        ax.set_ylim(0, 3)  # Establece los límites del eje y
        ax.grid(True, linestyle='--', alpha=0.6)        
        ax.legend()   