import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("#1e1e1e")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Edytor obrazów")

# Zmienna przechowująca obraz
image = None

# Funkcja do otwierania obrazka
def open_file():
    global image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        image = Image.open(file_path)
        # Przeskalowanie obrazka do maksymalnej szerokości 1000 px
        image.thumbnail((1000, 1000))
        photo = ImageTk.PhotoImage(image)
        canvas.config(width=image.width, height=image.height)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo  # to avoid garbage collection

def save_file():
    if image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                  filetypes=[("PNG files", "*.png"),
                                                             ("JPEG files", "*.jpg"),
                                                             ("All files", "*.*")])
        if file_path:
            image.save(file_path)

def linear_transformation(option):
    print("Transformacja liniowa:", option)

def power_transformation(option):
    print("Transformacja potęgowa:", option)

# Funkcja do utworzenia menu rozwijanego z opcjami
def create_dropdown_menu(menu, options, command):
    for option in options:
        menu.add_command(label=option, command=lambda opt=option: command(opt))

# Główne menu
menu = tk.Menu(app)

# Menu "Plik"
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Plik", menu=file_menu)
file_menu.add_command(label="Otwórz plik", command=open_file)
file_menu.add_command(label="Zapisz plik", command=save_file)

# Menu "Efekty"
effects_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Efekty", menu=effects_menu)

# Menu rozwijane "Transformacja liniowa"
linear_options_menu = tk.Menu(effects_menu, tearoff=0)
effects_menu.add_cascade(label="Transformacja liniowa", menu=linear_options_menu)
linear_options = ["Rozjaśnienie", "Przyciemnienie", "Negatyw"]
create_dropdown_menu(linear_options_menu, linear_options, linear_transformation)

# Menu rozwijane "Transformacja potęgowa"
power_options_menu = tk.Menu(effects_menu, tearoff=0)
effects_menu.add_cascade(label="Transformacja potęgowa", menu=power_options_menu)
power_options = ["Rozjaśnienie", "Przyciemnienie"]
create_dropdown_menu(power_options_menu, power_options, power_transformation)

# Menu rozwijane "Mieszanie dwóch obrazów"
mixing_options_menu = tk.Menu(effects_menu, tearoff=0)
effects_menu.add_cascade(label="Mieszanie dwóch obrazów", menu=mixing_options_menu)
power_options = ["Suma", "Odejmowanie", "Odejmowanie", "Różnica", "Mnożenie", "Mnożenie odwrotności", "Negacja", "Ciemniejsze"
                 , "Jaśniejsze", "Wyłączenie", "Nakładka", "Ostre światło", "Łagodne światło", "Wypalanie", "Reflect mode", "Przezroczystość"]
create_dropdown_menu(mixing_options_menu, power_options, power_transformation)

# Kontrast
effects_menu.add_command(label="Kontrast", command=open_file)

# Histogram
effects_menu.add_command(label="Histogram", command=open_file)





app.config(menu=menu)

image_frame = tk.Frame(app, width=1000, height=720)
image_frame.pack(side=tk.LEFT)

canvas = tk.Canvas(image_frame, width=1000, height=720, bg="#1e1e1e", highlightthickness=0)
canvas.pack()



app.mainloop()