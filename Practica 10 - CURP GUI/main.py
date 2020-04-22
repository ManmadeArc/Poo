import tkinter as tk
from clases import Usuario


class EntryPlaceholder(tk.Entry):
    def __init__(self, master, placeholder, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.insert("1", placeholder)


window = tk.Tk()
window.minsize(400, 250)
window.title("Generación y guardado de CURP")
input_widgets = {}

instructions = tk.Label(
    master=window,
    text="Ingrese sus datos"
)
instructions.pack()

input_info = {
    "nombre": "Primer Nombre",
    "apellido_paterno": "Apellido paterno",
    "apellido_materno": "Apellido materno",
    "sexo": "Sexo (H/M)",
    "dd_nacimiento": "Dia de nacimiento(dd)",
    "mm_nacimiento": "Mes de nacimiento(mm)",
    "yyyy_nacimiento": "Año de nacimiento(aaaa)",
    "estado": "Estado de nacimiento ej. Baja california",
}



for key, placeholder in input_info.items():
    input_widgets[key] = EntryPlaceholder(
        window,
        placeholder,
        width=50
    )
    input_widgets[key].pack()

def Save():
    Client=Usuario(input_widgets["dd_nacimiento"].get(),input_widgets["mm_nacimiento"].get(),
            input_widgets["yyyy_nacimiento"].get(),input_widgets["nombre"].get(),
            input_widgets["apellido_paterno"].get(), input_widgets["apellido_materno"].get(),
            input_widgets["sexo"].get(), input_widgets["estado"].get())
    Client.Save_User()
    for key, placeholder in input_info.items():
        input_widgets[key].delete(0,tk.END)
        input_widgets[key].insert(0,placeholder)
    




submit_btn = tk.Button(
    window,
    text="Guardar datos y CURP",
    command=Save,
    borderwidth=2
)
submit_btn.pack()

window.mainloop()