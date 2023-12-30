import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from PyQt5.QtWidgets import QApplication
import sys

# Variable para rastrear la ventana activa (Resistencia o Capacitor)
active_window = "Resistencia"

# Crear una instancia de QApplication para mejorar la apariencia
app = QApplication(sys.argv)

def show_resistencia_serie():
    label_resistencia.config(image=image_resistencia_serie)
    label_tipo_resistencia.config(text="Resistencia en Serie")
    global active_window
    active_window = "Resistencia"

def show_resistencia_paralelo():
    label_resistencia.config(image=image_resistencia_paralelo)
    label_tipo_resistencia.config(text="Resistencia en Paralelo")
    global active_window
    active_window = "Resistencia"

def show_capacitor_serie():
    label_capacitor.config(image=image_capacitor_serie)
    label_tipo_capacitor.config(text="Capacitor en Serie")
    global active_window
    active_window = "Capacitor"

def show_capacitor_paralelo():
    label_capacitor.config(image=image_capacitor_paralelo)
    label_tipo_capacitor.config(text="Capacitor en Paralelo")
    global active_window
    active_window = "Capacitor"

def add_resistor_entry():
    # Borra los campos anteriores eliminando las referencias en la lista
    for entry in resistors_entries:
        entry.destroy()
    for label in resistors_labels:
        label.destroy()
    resistors_entries.clear()
    resistors_labels.clear()

    resistor_count = int(resistor_count_entry.get())
    for i in range(1, resistor_count + 1):
        column = (i - 1) // 10  # Distribuir en columnas de 10
        row = (i - 1) % 10
        label = tk.Label(resistencia_canvas, text=f"R{i}:", font=("Arial", 10))
        entry = tk.Entry(resistencia_canvas, font=("Arial", 10))
        label.grid(row=row, column=2 * column, sticky="w")
        entry.grid(row=row, column=2 * column + 1)
        resistors_labels.append(label)
        resistors_entries.append(entry)  # Agrega los nuevos campos a la lista

def add_capacitor_entry():
    # Borra los campos anteriores eliminando las referencias en la lista
    for entry in capacitors_entries:
        entry.destroy()
    for label in capacitors_labels:
        label.destroy()
    capacitors_entries.clear()
    capacitors_labels.clear()

    capacitor_count = int(capacitor_count_entry.get())
    for i in range(1, capacitor_count + 1):
        column = (i - 1) // 10  # Distribuir en columnas de 10
        row = (i - 1) % 10
        label = tk.Label(capacitor_canvas, text=f"C{i}:", font=("Arial", 10))
        entry = tk.Entry(capacitor_canvas, font=("Arial", 10))
        label.grid(row=row, column=2 * column, sticky="w")
        entry.grid(row=row, column=2 * column + 1)
        capacitors_labels.append(label)
        capacitors_entries.append(entry)  # Agrega los nuevos campos a la lista

def calc_resistencia():
    if active_window == "Resistencia":
        # Verificar si se ha seleccionado el tipo de resistencia
        if label_tipo_resistencia.cget("text") not in ["Resistencia en Serie", "Resistencia en Paralelo"]:
            tk.messagebox.showinfo("Advertencia", "Por favor, selecciona el tipo de resistencia antes de calcular.")
            return

        resistors = [float(entry.get()) for entry in resistors_entries]
        if label_tipo_resistencia.cget("text") == "Resistencia en Serie":
            resistance_equiv = sum(resistors)
            resultado_resistencia.set(f"Resistencia Equivalente en Serie: {resistance_equiv} ohmios")
        elif label_tipo_resistencia.cget("text") == "Resistencia en Paralelo":
            resistance_equiv = 1 / sum(1 / (resistor or 1) for resistor in resistors)
            resultado_resistencia.set(f"Resistencia Equivalente en Paralelo: {resistance_equiv} ohmios")
    else:
        tk.messagebox.showinfo("Advertencia", "Por favor, selecciona el tipo de resistencia antes de calcular.")


def calc_capacitor():
    if active_window == "Capacitor":
        # Verificar si se ha seleccionado el tipo de capacitor
        if label_tipo_capacitor.cget("text") not in ["Capacitor en Serie", "Capacitor en Paralelo"]:
            tk.messagebox.showinfo("Advertencia", "Por favor, selecciona el tipo de capacitor antes de calcular.")
            return

        capacitors = [float(entry.get()) for entry in capacitors_entries]
        if label_tipo_capacitor.cget("text") == "Capacitor en Serie":
            capacitance_equiv = 1 / sum(1 / (capacitor or 1) for capacitor in capacitors)
            resultado_capacitor.set(f"Capacitor Equivalente en Serie: {capacitance_equiv} faradios")
        elif label_tipo_capacitor.cget("text") == "Capacitor en Paralelo":
            capacitance_equiv = sum(capacitors)
            resultado_capacitor.set(f"Capacitor Equivalente en Paralelo: {capacitance_equiv} faradios")
    else:
        tk.messagebox.showinfo("Advertencia", "Por favor, selecciona el tipo de capacitor antes de calcular.")



# Función para mostrar la portada de la empresa
def mostrar_portada_empresa():
    ventana_portada = tk.Toplevel(root)
    ventana_portada.title("Portada de la Empresa")

    # Carga la imagen de la portada de la empresa
    imagen_portada = Image.open("C:\\Users\chris\OneDrive\Escritorio\Proyecto_ElectricidadyMagnetismo\Tuuxt.png")  # Reemplaza con la ubicación de tu imagen
    imagen_portada = ImageTk.PhotoImage(imagen_portada)

    # Crea una etiqueta para mostrar la imagen de la portada
    label_portada = tk.Label(ventana_portada, image=imagen_portada)
    label_portada.pack()

    # Crea un marco para los logotipos en la parte superior
    frame_logos = tk.Frame(ventana_portada)
    frame_logos.pack(side="top", fill="x")

    # Crea etiquetas para los logotipos en los extremos
    imagen_logo_izquierdo = Image.open(r"C:\Users\chris\OneDrive\Escritorio\Proyecto_ElectricidadyMagnetismo\unam.png")  # Reemplaza con la ubicación de tu imagen
    imagen_logo_izquierdo = ImageTk.PhotoImage(imagen_logo_izquierdo)
    label_logo_izquierdo = tk.Label(frame_logos, image=imagen_logo_izquierdo)
    label_logo_izquierdo.pack(side="left")

    imagen_logo_derecho = Image.open(r"C:\Users\chris\OneDrive\Escritorio\Proyecto_ElectricidadyMagnetismo\Aragon.png")  # Reemplaza con la ubicación de tu imagen
    imagen_logo_derecho = ImageTk.PhotoImage(imagen_logo_derecho)
    label_logo_derecho = tk.Label(frame_logos, image=imagen_logo_derecho)
    label_logo_derecho.pack(side="right")

    # Agrega un texto centrado
    texto_empresa = "TUUXT"
    label_texto_empresa = tk.Label(ventana_portada, text=texto_empresa, font=("Arial", 60))
    label_texto_empresa.pack(pady=1)  # Espaciado vertical
    
    texto_empresa = "Integrantes"
    label_texto_empresa = tk.Label(ventana_portada, text=texto_empresa, font=("Arial", 18))
    label_texto_empresa.pack(pady=1)  # Espaciado vertical
    
    texto_empresa = "Soancatl Zacamitzin Miguel Angel"
    label_texto_empresa = tk.Label(ventana_portada, text=texto_empresa, font=("Arial", 20))
    label_texto_empresa.pack(pady=1)  # Espaciado vertical
    
    texto_empresa = "Lara Martinez Christian Gael"
    label_texto_empresa = tk.Label(ventana_portada, text=texto_empresa, font=("Arial", 20))
    label_texto_empresa.pack(pady=1)  # Espaciado vertical
    
    # Agrega un texto centrado
    texto_empresa = "Hernandez Miranda Jorge"
    label_texto_empresa = tk.Label(ventana_portada, text=texto_empresa, font=("Arial", 20))
    label_texto_empresa.pack(pady=1)  # Espaciado vertical
    
    texto_empresa = "Contreras Mateo"
    label_texto_empresa = tk.Label(ventana_portada, text=texto_empresa, font=("Arial", 20))
    label_texto_empresa.pack(pady=1)  # Espaciado vertical

    ventana_portada.mainloop()

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Resistencias y Capacitores")



# Crear pestañas con estilos personalizados
tab_control = ttk.Notebook(root)

# Personalizar el estilo de las pestañas
style = ttk.Style()
style.configure("TNotebook.Tab", padding=(10, 8, 10, 0), font=('Arial', 23), background='white', foreground='red')  # Establece el color de fondo y el color del texto

tab_resistencia = ttk.Frame(tab_control)
tab_capacitor = ttk.Frame(tab_control)
tab_control.add(tab_resistencia, text="Resistencias")
tab_control.add(tab_capacitor, text="Capacitores")
tab_control.pack(expand=1, fill="both")



# Resistencias
resistors_entries = []
resistors_labels = []  # Lista para las etiquetas de las resistencias
resultado_resistencia = tk.StringVar()
resistencia_frame = tk.Frame(tab_resistencia)
resistencia_frame.pack()

# Frame para las imágenes de resistencias
image_frame_resistencia = tk.Frame(resistencia_frame)
image_frame_resistencia.pack()

image_resistencia_serie = Image.open(r"C:\Users\chris\OneDrive\Escritorio\Proyecto_ElectricidadyMagnetismo\ResistenciaSerie.gif")
image_resistencia_serie = ImageTk.PhotoImage(image_resistencia_serie)

image_resistencia_paralelo = Image.open(r"C:\Users\chris\OneDrive\Escritorio\Proyecto_ElectricidadyMagnetismo\ResistenciaParalelo.gif")
image_resistencia_paralelo = ImageTk.PhotoImage(image_resistencia_paralelo)

show_resistencia_serie_button = tk.Button(image_frame_resistencia, text="Resistencia en Serie", command=show_resistencia_serie, font=("Arial", 12), bg="blue", fg="white")
show_resistencia_serie_button.pack()

show_resistencia_paralelo_button = tk.Button(image_frame_resistencia, text="Resistencia en Paralelo", command=show_resistencia_paralelo, font=("Arial", 12), bg="green", fg="white")
show_resistencia_paralelo_button.pack()

label_resistencia = tk.Label(image_frame_resistencia, image=image_resistencia_serie)
label_resistencia.pack()

label_tipo_resistencia = tk.Label(image_frame_resistencia, text="Seleccione el tipo de resistencia:", font=("Arial", 12))
label_tipo_resistencia.pack()



tk.Label(resistencia_frame, text="Número de resistencias:").pack()
resistor_count_entry = tk.Entry(resistencia_frame, font=("Arial", 12))
resistor_count_entry.pack()


add_resistor_button = tk.Button(resistencia_frame, text="Agregar Campos de Resistencias", command=add_resistor_entry, font=("Arial", 12), bg="blue", fg="white")
add_resistor_button.pack(pady=(5, 10))




calc_button = tk.Button(resistencia_frame, text="Calcular en Ω", command=calc_resistencia, font=("Arial", 12), bg="green", fg="white")
calc_button.pack()

tk.Label(resistencia_frame, textvariable=resultado_resistencia, font=("Arial", 12)).pack()





# Canvas para resistencias
resistencia_canvas = tk.Frame(tab_resistencia)
resistencia_canvas.pack()

# Capacitores
capacitors_entries = []
capacitors_labels = []  # Lista para las etiquetas de los capacitores
resultado_capacitor = tk.StringVar()
capacitor_frame = tk.Frame(tab_capacitor)
capacitor_frame.pack()



# Frame para las imágenes de capacitores
image_frame_capacitor = tk.Frame(capacitor_frame)
image_frame_capacitor.pack()

image_capacitor_serie = Image.open(r"C:\Users\chris\OneDrive\Escritorio\Proyecto_ElectricidadyMagnetismo\CapacitorSerie.jpg")
image_capacitor_serie = ImageTk.PhotoImage(image_capacitor_serie)

image_capacitor_paralelo = Image.open(r"C:\Users\chris\OneDrive\Escritorio\Proyecto_ElectricidadyMagnetismo\CapacitorParalelo.jpg")
image_capacitor_paralelo = ImageTk.PhotoImage(image_capacitor_paralelo)

show_capacitor_serie_button = tk.Button(image_frame_capacitor, text="Capacitor en Serie", command=show_capacitor_serie, font=("Arial", 12), bg="blue", fg="white")
show_capacitor_serie_button.pack()

show_capacitor_paralelo_button = tk.Button(image_frame_capacitor, text="Capacitor en Paralelo", command=show_capacitor_paralelo, font=("Arial", 12), bg="green", fg="white")
show_capacitor_paralelo_button.pack()

label_capacitor = tk.Label(image_frame_capacitor, image=image_capacitor_serie)
label_capacitor.pack()

label_tipo_capacitor = tk.Label(image_frame_capacitor, text="Seleccione el tipo de capacitor:", font=("Arial", 12))
label_tipo_capacitor.pack()




tk.Label(capacitor_frame, text="Número de capacitores:").pack()
capacitor_count_entry = tk.Entry(capacitor_frame, font=("Arial", 12))
capacitor_count_entry.pack()

add_capacitor_button = tk.Button(capacitor_frame, text="Agregar Campos de Capacitores", command=add_capacitor_entry, font=("Arial", 12), bg="blue", fg="white")
add_capacitor_button.pack(pady=(5, 10))  # Ajuste el valor de pady según sea necesario

calc_capacitor_button = tk.Button(capacitor_frame, text="Calcular en: Faradios", command=calc_capacitor, font=("Arial", 12), bg="green", fg="white")
calc_capacitor_button.pack()

tk.Label(capacitor_frame, textvariable=resultado_capacitor, font=("Arial", 12)).pack()



# Canvas para capacitores
capacitor_canvas = tk.Frame(tab_capacitor)
capacitor_canvas.pack()


# Botón para mostrar la portada de la empresa
mostrar_portada_button = tk.Button(root, text="Mostrar los datos de la Empresa", command=mostrar_portada_empresa, width=45, bg="red", fg="white", font=("Arial", 11))
mostrar_portada_button.pack(side="bottom", pady=22)


# Mueve el botón al final de la pestaña "Capacitores"
mostrar_portada_button.pack(side="bottom", pady=22)

root.mainloop()

# Cerrar la aplicación PyQt5
app.quit() 

