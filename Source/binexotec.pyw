from tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master, bg="#4B4B4B")
        self.master = master
        self.pack(expand=True, fill="both")
        self.is_space2_visible = False  
        self.create_layout()

    def create_layout(self):
        # Configuración del layout principal
        space0 = Frame(self, bg="#3E3E3E")
        space0.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        space0.grid_rowconfigure(0, weight=1)
        space0.grid_columnconfigure(0, weight=1)

        # Frame plegable (space2)
        space1 = Frame(space0, bg="grey")
        space1.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')
        self.space2 = Frame(space0, bg="grey")
        self.space2.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')
        self.space2.grid_remove()  # Oculta space2 al inicio
        space3 = Frame(space0, bg="lightgray")
        space3.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

        # Botón para colapsar/expandir space2 con flecha hacia arriba o abajo
        self.toggle_button = Button(space3, text="LOGIC OPERATION ↓", command=self.toggle_space2, bg="silver")
        self.toggle_button.pack(pady=5)

        # Configurar grid para que las filas y columnas se expandan
        self.configure_grid2(self.space2)
        self.configure_grid(space1)

        # Crear cada sección directamente
        self.create_entry_section(space1, row=0, label_text="HEX", var_name="hex_var")
        self.create_entry_section(space1, row=1, label_text="DEC", var_name="dec_var")
        self.create_entry_section(space1, row=2, label_text="OCT", var_name="oct_var")
        self.create_entry_section(space1, row=3, label_text="BIN", var_name="bin_var")

        # Crear secciones lógicas
        operations = ["AND", "OR", "XOR", "NAND", "NOR", "NOT"]
        for idx, label in enumerate(operations):
            self.create_entry_section1(self.space2, row=idx, column=0, label_text=label, var_name=f"{label.lower()}_var")

    def toggle_space2(self):
        """Oculta o muestra el frame space2 y actualiza el texto del botón."""
        if self.is_space2_visible:
            self.space2.grid_remove()  # Oculta space2
            self.toggle_button.config(text="LOGIC OPERATION ↓")  # Cambia el texto a flecha hacia abajo
        else:
            self.space2.grid()  # Muestra space2
            self.toggle_button.config(text="LOGIC OPERATION ↑")  # Cambia el texto a flecha hacia arriba
        self.is_space2_visible = not self.is_space2_visible

    def configure_grid(self, frame):
        """Configura las filas y columnas de un frame para que se expandan."""
        for i in range(4):  # Filas
            frame.grid_rowconfigure(i, weight=1)
        for j in range(2):  # Columnas
            frame.grid_columnconfigure(j, weight=1)

    def configure_grid2(self, frame):
        """Configura las filas y columnas de un frame para que se expandan."""
        for i in range(6):  # Filas
            frame.grid_rowconfigure(i, weight=1)
        for j in range(4):  # Columnas
            frame.grid_columnconfigure(j, weight=1)

    def create_entry_section(self, parent, row, label_text, var_name):
        """Crea un conjunto de button y entry para una fila."""

        button = Button(parent, width=8, text=label_text, bg="silver", command=lambda: self.on_button_click(label_text))
        button.grid(row=row, column=0, padx=2, pady=2, sticky='wnse')

        entry_var = StringVar()
        entry = Entry(parent, width=47, textvariable=entry_var, font=("Consolas", 9), fg="white", bg="#3E3E3E", insertbackground="white")
        entry.grid(row=row, column=1, padx=2, pady=2, sticky='wnse')

        # Asignar los valores a atributos dinámicamente
        setattr(self, var_name, entry_var)

    def create_entry_section1(self, parent, row, column, label_text, var_name):
        """Crea un conjunto de label y entry para una fila."""
        
        label = Label(parent, text=label_text, bg="silver")
        label.grid(row=row, column=column+1, padx=2, pady=2, sticky='wnse')

        # Entrada principal en la columna 0
        entry_var1 = StringVar()
        entry = Entry(parent, width=16, textvariable=entry_var1, font=("Consolas", 9), fg="white", bg="#3E3E3E", insertbackground="white")
        entry.grid(row=row, column=column, padx=2, pady=2, sticky='wnse')

        # Si la operación NO es "NOT", crear la segunda entrada en la columna 2
        if label_text != "NOT":
            entry_var2 = StringVar()
            entry = Entry(parent, width=16, textvariable=entry_var2, font=("Consolas", 9), fg="white", bg="#3E3E3E", insertbackground="white")
            entry.grid(row=row, column=column+2, padx=2, pady=2, sticky='wnse')

        # Crear la entrada de resultado en la columna 3 (para todas las operaciones)
        entry_var3 = StringVar()
        entry = Entry(parent, width=16, textvariable=entry_var3, font=("Consolas", 9), fg="white", bg="#3E3E3E", insertbackground="white")
        entry.grid(row=row, column=column+3, padx=2, pady=2, sticky='wnse')

        # Asignar los valores a atributos dinámicamente
        setattr(self, var_name, entry_var1)

    def on_button_click(self, label_text):
        """Función que se ejecuta al hacer clic en un botón."""
        print(f"Button {label_text} clicked!")


root = Tk()
root.wm_title("Binexoctec")
app = Application(root)
app.mainloop()
