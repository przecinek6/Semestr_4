import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import ImageTk
from linearTransformation import *
from powerTransformation import *
from contrast import *
from histogram import *

customtkinter.set_appearance_mode("#1e1e1e")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Edytor obrazów")

# Zmienna przechowująca obraz
image = None

def image_update(image):
    # Przeskalowanie obrazka do maksymalnej szerokości 1000 px
    image.thumbnail((1000, 1000))
    photo = ImageTk.PhotoImage(image)
    canvas.config(width=image.width, height=image.height)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo  # to avoid garbage collection

# Funkcja do otwierania obrazka
def open_file():
    global image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image_update(image)

def save_file():
    if image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                  filetypes=[("PNG files", "*.png"),
                                                             ("JPEG files", "*.jpg"),
                                                             ("All files", "*.*")])
        if file_path:
            image.save(file_path)

def bool_reset():
    global rozjasnienieBool
    global przyciemnienieBool
    global powerTransformationBool
    global contrastBool

    rozjasnienieBool = False
    przyciemnienieBool = False
    powerTransformationBool = False
    contrastBool = False

    slider_unpack()

def linear_transformation(option):
    bool_reset()
    global image
    global rozjasnienieBool
    global przyciemnienieBool

    if option == "Rozjaśnienie":
        rozjasnienieBool = True
        slider_pack()

    if option == "Przyciemnienie":
        przyciemnienieBool = True
        slider_pack()

    if option == "Negatyw":
        image = negatyw(image)
        image_update(image)

def power_transformation(option):
    bool_reset()
    global powerTransformationBool
    powerTransformationBool = True

    if option == "Rozjaśnienie":
        slider_pack(0, 1)

    if option == "Przyciemnienie":
        slider_pack(1, 2)

def contrast_fun():
    bool_reset()
    global contrastBool
    contrastBool = True

    slider_pack(-128, 126, 255)

def histogram_fun():
    bool_reset()
    generate_histogram(image)

# Funkcja do utworzenia menu rozwijanego z opcjami
def create_dropdown_menu(menu, options, command):
    for option in options:
        menu.add_command(label=option, command=lambda opt=option: command(opt))

def slider_event(value):
    if powerTransformationBool:
        label.configure(text=round(value, 2))

    elif contrastBool:
        label.configure(text=round(value))

    else:
        label.configure(text=value)

def slider_pack(config_from=0, config_to=100, config_steps=100):
    label.pack()
    slider.configure()
    slider.configure(from_=config_from, to=config_to, number_of_steps=config_steps)
    slider.pack()
    apply_button.pack(pady=10)

def slider_unpack():
    label.pack_forget()
    slider.pack_forget()
    apply_button.pack_forget()

def get_Value():
    value = slider.get()

    if rozjasnienieBool:
        image_update(rozjasnienie(image, value))

    if przyciemnienieBool:
        image_update(przyciemnienie(image, value))

    if powerTransformationBool:
        image_update(potegowa(image, value))

    if contrastBool:
        image_update(adjust_contrast(image, value))


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
effects_menu.add_command(label="Kontrast", command=contrast_fun)

# Histogram
effects_menu.add_command(label="Histogram", command=histogram_fun)

app.config(menu=menu)

image_frame = tk.Frame(app, width=1000, height=720)
image_frame.pack(side=tk.LEFT)

canvas = tk.Canvas(image_frame, width=1000, height=720, bg="#1e1e1e", highlightthickness=0)
canvas.pack()

# Obszar po prawej stronie
right_frame = customtkinter.CTkFrame(app, width=280, height=720)
right_frame.pack(side=tk.RIGHT)

# Label suwaka
label = customtkinter.CTkLabel(right_frame, text="")

# Suwak
slider = customtkinter.CTkSlider(right_frame, command=slider_event)
slider.set(0)

# Przycisk zastosuj
apply_button = customtkinter.CTkButton(right_frame, text="Zastosuj", command=get_Value)


app.mainloop()