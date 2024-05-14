import tkinter
import customtkinter
from PIL import ImageTk
from tkinter import filedialog
from linearTransformation import *
from powerTransformation import *
from contrast import *
from histogram import *
from blurFilters import *
from sharpeningFilters import *
from staticFilters import *
from mixingImage import *

# Globbal variables
image = None
image2 = None
history_undo = []
history_redo = []
boolUndo = False

def undo():
    global history_undo, history_redo, boolUndo

    if len(history_undo) != 0:
        history_redo.append(history_undo[-1])
        history_undo.pop()
        image = history_undo[-1]
        boolUndo = True
        image_update(image)
        boolUndo = False

def redo():
    global history_undo

    if len(history_redo) != 0:
        image = history_redo[-1]
        image_update(image)
        history_redo.pop()

def image_update(image):
    global history_undo

    # Getter image_frame size
    frame_width = image_frame.winfo_width()
    frame_height = image_frame.winfo_height()

    # Sizing image to image_frame
    image.thumbnail((frame_width, frame_height))

    photo = ImageTk.PhotoImage(image)
    canvas.config(width=image.width, height=image.height)
    canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
    canvas.image = photo

    if boolUndo == False:
        history_undo.append(image.copy())

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

def linear_brightening():
    global image
    value = slider.get()
    image = rozjasnienie(image, value)
    image_update(image)

def linear_darkening():
    global image
    value = slider.get()
    image = przyciemnienie(image, value)
    image_update(image)

def linear_transformation(option):
    global image, slider, text_var
    # global toolbox_workspace_frame

    for widget in toolbox_workspace_frame.winfo_children():
        widget.destroy()

    if option == "Rozjaśnienie":
        text_label = customtkinter.CTkLabel(toolbox_workspace_frame, text="O ile procent chcesz rozjaśnić:")
        text_label.pack(pady=20)

        slider = customtkinter.CTkSlider(toolbox_workspace_frame, from_=0, to=100, number_of_steps=100,
                                         command=slider_event)
        slider.pack()

        text_var = tkinter.StringVar(value="50.0")

        value_label = customtkinter.CTkLabel(toolbox_workspace_frame, textvariable=text_var, fg_color="#464646",
                                             width=50)
        value_label.pack(pady=10)

        button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=linear_brightening)
        button.pack()

    if option == "Przyciemnienie":
        text_label = customtkinter.CTkLabel(toolbox_workspace_frame, text="O ile procent chcesz przyciemnić:")
        text_label.pack(pady=20)

        slider = customtkinter.CTkSlider(toolbox_workspace_frame, from_=0, to=100, number_of_steps=100,
                                         command=slider_event)
        slider.pack()

        text_var = tkinter.StringVar(value="50.0")

        value_label = customtkinter.CTkLabel(toolbox_workspace_frame, textvariable=text_var, fg_color="#464646",
                                             width=50)
        value_label.pack(pady=10)

        button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=linear_darkening)
        button.pack()

    if option == "Negatyw":
        image = negatyw(image)
        image_update(image)

def power_transformation_fun():
    global image
    value = slider.get()
    image = potegowa(image, value)
    image_update(image)

def power_transformation(option):
    global slider, text_var

    for widget in toolbox_workspace_frame.winfo_children():
        widget.destroy()

    if option == "Rozjaśnienie":
        text_label = customtkinter.CTkLabel(toolbox_workspace_frame, text="Ile chcesz rozjaśnić:")
        text_label.pack(pady=20)

        slider = customtkinter.CTkSlider(toolbox_workspace_frame, from_=0, to=1, number_of_steps=100,
                                         command=slider_event)
        slider.pack()

        text_var = tkinter.StringVar(value="0.5")

        value_label = customtkinter.CTkLabel(toolbox_workspace_frame, textvariable=text_var, fg_color="#464646",
                                             width=50)
        value_label.pack(pady=10)

        text_var.trace_add("write", lambda *args: round_value(2))

        button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=power_transformation_fun)
        button.pack()

    if option == "Przyciemnienie":
        text_label = customtkinter.CTkLabel(toolbox_workspace_frame, text="Ile chcesz przyciemnić:")
        text_label.pack(pady=20)

        slider = customtkinter.CTkSlider(toolbox_workspace_frame, from_=1, to=2, number_of_steps=100,
                                         command=slider_event)
        slider.pack()

        text_var = tkinter.StringVar(value="1.5")

        value_label = customtkinter.CTkLabel(toolbox_workspace_frame, textvariable=text_var, fg_color="#464646",
                                             width=50)
        value_label.pack(pady=10)

        text_var.trace_add("write", lambda *args: round_value(2))

        button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=power_transformation_fun)
        button.pack()

def contrast_fun():
    global image
    value = slider.get()
    image = adjust_contrast(image, value)
    image_update(image)

def contrast():
    global slider, text_var

    for widget in toolbox_workspace_frame.winfo_children():
        widget.destroy()

    text_label = customtkinter.CTkLabel(toolbox_workspace_frame, text="Wybierz siłę kontrastu:")
    text_label.pack(pady=20)

    slider = customtkinter.CTkSlider(toolbox_workspace_frame, from_=-128, to=127, number_of_steps=256,
                                     command=slider_event)
    slider.pack()

    text_var = tkinter.StringVar(value="0.0")

    value_label = customtkinter.CTkLabel(toolbox_workspace_frame, textvariable=text_var, fg_color="#464646",
                                         width=50)
    value_label.pack(pady=10)

    text_var.trace_add("write", lambda *args: round_value(0))

    button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=contrast_fun)
    button.pack()

def histogram_fun():
    for widget in toolbox_workspace_frame.winfo_children():
        widget.destroy()

    generate_histogram(image)

def blur_filter_fun():
    global image
    value = slider.get()
    image = box_filter(image, value)
    image_update(image)

def blur_filter():
    global slider, text_var

    for widget in toolbox_workspace_frame.winfo_children():
        widget.destroy()

    text_label = customtkinter.CTkLabel(toolbox_workspace_frame, text="Wybierz rozmiar filtra:")
    text_label.pack(pady=20)

    slider = customtkinter.CTkSlider(toolbox_workspace_frame, from_=-0, to=10, number_of_steps=10,
                                     command=slider_event)
    slider.pack()

    text_var = tkinter.StringVar(value="5.0")

    value_label = customtkinter.CTkLabel(toolbox_workspace_frame, textvariable=text_var, fg_color="#464646",
                                         width=50)
    value_label.pack(pady=10)

    text_var.trace_add("write", lambda *args: round_value(0))

    button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=blur_filter_fun)
    button.pack()

def sharpening_filters(option):
    global image

    for widget in toolbox_workspace_frame.winfo_children():
        widget.destroy()

    filter = None

    robertsHorizontal = [[0, 0, 0], [0, 1, -1], [0, 0, 0]]
    robertsVertical = [[0, 0, 0], [0, 1, 0], [0, -1, 0]]
    prewittHorizontal = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
    prewittVertical = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
    sobelHorizontal = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    sobelVertical = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    laplace = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

    if option == "Filtr Robertsa poziomy":
        filter = robertsHorizontal

    if option == "Filtr Robertsa pionowy":
        filter = robertsVertical

    if option == "Filtr Prewitta poziomy":
        filter = prewittHorizontal

    if option == "Filtr Prewitta pionowy":
        filter = prewittVertical

    if option == "Filtr Sobela poziomy":
        filter = sobelHorizontal

    if option == "Filtr Sobela pionowy":
        filter = sobelVertical

    if option == "Filtr Laplace’a":
        filter = laplace

    image = filterFunction(image, filter)
    image_update(image)

def min_filter_fun():
    global image
    value = slider.get()
    image = min_filter(image, value)
    image_update(image)

def max_filter_fun():
    global image
    value = slider.get()
    image = max_filter(image, value)
    image_update(image)

def median_filter_fun():
    global image
    value = slider.get()
    image = median_filter(image, value)
    image_update(image)

def static_filters(option):
    global slider, text_var

    for widget in toolbox_workspace_frame.winfo_children():
        widget.destroy()

    text_label = customtkinter.CTkLabel(toolbox_workspace_frame, text="Wybierz promień filtra:")
    text_label.pack(pady=20)

    slider = customtkinter.CTkSlider(toolbox_workspace_frame, from_=-0, to=10, number_of_steps=10,
                                     command=slider_event)
    slider.pack()

    text_var = tkinter.StringVar(value="5.0")

    value_label = customtkinter.CTkLabel(toolbox_workspace_frame, textvariable=text_var, fg_color="#464646",
                                         width=50)
    value_label.pack(pady=10)

    text_var.trace_add("write", lambda *args: round_value(0))

    if option == "Minimum":
        button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=min_filter_fun)
        button.pack()

    if option == "Maksimum":
        button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=max_filter_fun)
        button.pack()

    if option == "Średnia":
        button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=median_filter_fun)
        button.pack()

def slider_event(value):
    text_var.set(f"{slider.get()}")

def round_value(round_value):
    try:
        rounded_value = round(float(text_var.get()), round_value)
        text_var.set(str(rounded_value))
    except ValueError:
        pass

def one_image_mode():
    global canvas, image_frame, toolbox_workspace_frame

    # Usunięcie poprzednich elementów
    for widget in main_area.winfo_children():
        widget.destroy()

    # Grid
    main_area.columnconfigure(0, weight=10)
    main_area.columnconfigure(1, weight=0)
    main_area.grid_rowconfigure(0, weight=10)
    main_area.grid_rowconfigure(1, weight=1)

    # Image frame
    image_frame = customtkinter.CTkFrame(main_area, fg_color="#262626")
    image_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    image_frame.propagate(False)

    # Toolbox frame
    toolbox_frame = customtkinter.CTkFrame(main_area, fg_color="#464646")
    toolbox_frame.grid(row=0, column=1, rowspan=2, sticky='nsew')
    toolbox_label = customtkinter.CTkLabel(toolbox_frame, text="Przybornik")
    toolbox_label.grid(row=0, column=0, sticky='ew')

    toolbox_workspace_frame = customtkinter.CTkFrame(toolbox_frame, fg_color="#262626")
    toolbox_workspace_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
    toolbox_frame.columnconfigure(0, weight=1)

    toolbox_frame.rowconfigure(0, weight=0)
    toolbox_frame.rowconfigure(1, weight=1)

    # Button frame
    button_frame = customtkinter.CTkFrame(main_area, fg_color="#535353")
    button_frame.grid(row=1, column=0)

    # Add image button
    button = customtkinter.CTkButton(button_frame, text="Otwórz zdjęcie", command=open_file)
    button.pack(expand=True)

    # Image canvas
    canvas = customtkinter.CTkCanvas(image_frame, bg="#262626", highlightthickness=0)
    canvas.pack(expand=True)

    # Disable effects for two images
    effects_menu.entryconfig("Transformacja liniowa", state="active")
    effects_menu.entryconfig("Transformacja potęgowa", state="active")
    effects_menu.entryconfig("Kontrast", state="active")
    effects_menu.entryconfig("Histogram", state="active")
    effects_menu.entryconfig("Filtr rozmywający", state="active")
    effects_menu.entryconfig("Filtr wyostrzający", state="active")
    effects_menu.entryconfig("Filtry statyczne", state="active")
    effects_menu.entryconfig("Mieszanie obrazów", state="disable")

    # Set the image_frame size based on the current window dimensions (bug fix)
    app.update()
    width = main_area.winfo_width()
    height = main_area.winfo_height()
    image_frame.configure(width=width - 200, height=height - 200)

def image_update_two_mode_1(image):
    # Getter image_frame size
    frame_width = image1_frame.winfo_width()
    frame_height = image1_frame.winfo_height()

    # Sizing image to image_frame
    image.thumbnail((frame_width, frame_height))

    photo = ImageTk.PhotoImage(image)
    canvas1.config(width=image.width, height=image.height)
    canvas1.create_image(0, 0, anchor=tkinter.NW, image=photo)
    canvas1.image = photo

def image_update_two_mode_2(image):
    # Getter image_frame size
    frame_width = image2_frame.winfo_width()
    frame_height = image2_frame.winfo_height()

    # Sizing image to image_frame
    image.thumbnail((frame_width, frame_height))

    photo = ImageTk.PhotoImage(image)
    canvas2.config(width=image.width, height=image.height)
    canvas2.create_image(0, 0, anchor=tkinter.NW, image=photo)
    canvas2.image = photo

def open_file_two_mode_1():
    global image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image_update_two_mode_1(image)

def open_file_two_mode_2():
    global image2
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        image2 = Image.open(file_path)
        image_update_two_mode_2(image2)

def transparency_fun():
    global image
    value = slider.get()
    image = transparency(image, image2, value)
    image_update_two_mode_1(image)

def mixing_images(option):
    global image, image2, slider, text_var

    for widget in toolbox_workspace_frame.winfo_children():
        widget.destroy()

    if option == "Suma":
        image = additiveMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Odejmowanie":
        image = subtractiveMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Różnica":
        image = subtractiveMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Mnożenie":
        image = multiplyMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Mnożenie odwrotności":
        image = screenMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Negacja":
        image = negationMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Ciemniejsze":
        image = darkenMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Jaśniejsze":
        image = lightenMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Wyłączenie":
        image = exclusionMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Nakładka":
        image = overlayMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Ostre światło":
        image = hardLightMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Łagodne światło":
        image = softLightMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Rozcieńczenie":
        image = colorDodgeMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Wypalanie":
        image = colorBurnMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Reflect mode":
        image = reflectMode(image, image2)
        image_update_two_mode_1(image)

    if option == "Przezroczystość":
        text_label = customtkinter.CTkLabel(toolbox_workspace_frame, text="Wybierz stopień przenikania:")
        text_label.pack(pady=20)

        slider = customtkinter.CTkSlider(toolbox_workspace_frame, from_=-0, to=1, number_of_steps=10,
                                         command=slider_event)
        slider.pack()

        text_var = tkinter.StringVar(value="0.5")

        value_label = customtkinter.CTkLabel(toolbox_workspace_frame, textvariable=text_var, fg_color="#464646",
                                             width=50)
        value_label.pack(pady=10)

        text_var.trace_add("write", lambda *args: round_value(1))

        button = customtkinter.CTkButton(toolbox_workspace_frame, text="Zastosuj", command=transparency_fun)
        button.pack()

def two_image_mode():
    global canvas1, canvas2, image1_frame, image2_frame, toolbox_workspace_frame

    # Usunięcie poprzednich elementów
    for widget in main_area.winfo_children():
        widget.destroy()

    # Grid
    main_area.columnconfigure(0, weight=4)
    main_area.columnconfigure(1, weight=4)
    main_area.columnconfigure(2, weight=1)
    main_area.grid_rowconfigure(0, weight=10)
    main_area.grid_rowconfigure(1, weight=1)

    # First image frame
    image1_frame = customtkinter.CTkFrame(main_area, fg_color="#262626")
    image1_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    image1_frame.propagate(False)

    # Second image frame
    image2_frame = customtkinter.CTkFrame(main_area, fg_color="#262626")
    image2_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
    image2_frame.propagate(False)

    # Toolbox frame
    toolbox_frame = customtkinter.CTkFrame(main_area, fg_color="#464646")
    toolbox_frame.grid(row=0, column=2, rowspan=2, sticky='nsew')
    toolbox_label = customtkinter.CTkLabel(toolbox_frame, text="Przybornik")
    toolbox_label.grid(row=0, column=0, sticky='ew')

    toolbox_workspace_frame = customtkinter.CTkFrame(toolbox_frame, fg_color="#262626")
    toolbox_workspace_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
    toolbox_frame.columnconfigure(0, weight=1)

    toolbox_frame.rowconfigure(0, weight=0)
    toolbox_frame.rowconfigure(1, weight=1)

    # First button frame
    button1_frame = customtkinter.CTkFrame(main_area, fg_color="#535353")
    button1_frame.grid(row=1, column=0)

    # Second button frame
    button2_frame = customtkinter.CTkFrame(main_area, fg_color="#535353")
    button2_frame.grid(row=1, column=1)

    # Add first image button
    button1 = customtkinter.CTkButton(button1_frame, text="Otwórz zdjęcie", command=open_file_two_mode_1)
    button1.pack(expand=True)

    # Add second image button
    button2 = customtkinter.CTkButton(button2_frame, text="Otwórz zdjęcie", command=open_file_two_mode_2)
    button2.pack(expand=True)

    # First image canvas
    canvas1 = customtkinter.CTkCanvas(image1_frame, bg="#262626", highlightthickness=0)
    canvas1.pack(expand=True)

    # Second image canvas
    canvas2 = customtkinter.CTkCanvas(image2_frame, bg="#262626", highlightthickness=0)
    canvas2.pack(expand=True)

    # Disable effects for one image
    effects_menu.entryconfig("Transformacja liniowa", state="active")
    effects_menu.entryconfig("Transformacja potęgowa", state="active")
    effects_menu.entryconfig("Kontrast", state="active")
    effects_menu.entryconfig("Histogram", state="active")
    effects_menu.entryconfig("Filtr rozmywający", state="active")
    effects_menu.entryconfig("Filtr wyostrzający", state="active")
    effects_menu.entryconfig("Filtry statyczne", state="active")
    effects_menu.entryconfig("Mieszanie obrazów", state="active")

# Drop down menu function
def create_dropdown_menu(menu, options, command):
    for option in options:
        menu.add_command(label=option, command=lambda opt=option: command(opt))

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Edytor obrazów")

menu = tkinter.Menu(app)

# Plik menu
file_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label="Plik", menu=file_menu)
# file_menu.add_command(label="Otwórz plik")
file_menu.add_command(label="Zapisz plik", command=save_file)

# Edycja menu
edit_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label="Edycja", menu=edit_menu)
edit_menu.add_command(label="Cofnij zmiany", command=undo)
edit_menu.add_command(label="Przywróć zmiany", command=redo)

# Tryby menu
modes_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label="Tryby", menu=modes_menu)
modes_menu.add_command(label="Tryb jednego obrazka", command=one_image_mode)
modes_menu.add_command(label="Tryb mieszania dwóch obrazków", command=two_image_mode)

# Efekty menu
effects_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label="Efekty", menu=effects_menu)

# Transformacja liniowa
mixing_options_menu = tkinter.Menu(effects_menu, tearoff=0)
effects_menu.add_cascade(label="Transformacja liniowa", menu=mixing_options_menu)
mixing_options = ["Rozjaśnienie", "Przyciemnienie", "Negatyw"]
create_dropdown_menu(mixing_options_menu, mixing_options, linear_transformation)

# Transformacja potęgowa
sharpening_options_menu = tkinter.Menu(effects_menu, tearoff=0)
effects_menu.add_cascade(label="Transformacja potęgowa", menu=sharpening_options_menu)
power_options = ["Rozjaśnienie", "Przyciemnienie"]
create_dropdown_menu(sharpening_options_menu, power_options, power_transformation)

# Kontrast
effects_menu.add_command(label="Kontrast", command=contrast)

# Histogram
effects_menu.add_command(label="Histogram", command=histogram_fun)

# Filtr rozmywający
effects_menu.add_command(label="Filtr rozmywający", command=blur_filter)

# Filtr wyostrzający
sharpening_options_menu = tkinter.Menu(effects_menu, tearoff=0)
effects_menu.add_cascade(label="Filtr wyostrzający", menu=sharpening_options_menu)
sharpening_options = ["Filtr Robertsa poziomy", "Filtr Robertsa pionowy",
                    "Filtr Prewitta poziomy", "Filtr Prewitta pionowy",
                    "Filtr Sobela poziomy", "Filtr Sobela pionowy",
                    "Filtr Laplace’a"]
create_dropdown_menu(sharpening_options_menu, sharpening_options, sharpening_filters)

# Transformacja liniowa
mixing_options_menu = tkinter.Menu(effects_menu, tearoff=0)
effects_menu.add_cascade(label="Filtry statyczne", menu=mixing_options_menu)
mixing_options = ["Minimum", "Maksimum", "Średnia"]
create_dropdown_menu(mixing_options_menu, mixing_options, static_filters)

# Mieszanie dwóch obrazów
mixing_options_menu = tkinter.Menu(effects_menu, tearoff=0)
effects_menu.add_cascade(label="Mieszanie obrazów", menu=mixing_options_menu)
mixing_options = ["Suma", "Odejmowanie", "Różnica", "Mnożenie", "Mnożenie odwrotności", "Negacja", "Ciemniejsze",
                  "Jaśniejsze", "Wyłączenie", "Nakładka", "Ostre światło", "Łagodne światło", "Rozcieńczenie",
                  "Wypalanie", "Reflect mode", "Przezroczystość"]
create_dropdown_menu(mixing_options_menu, mixing_options, mixing_images)

app.config(menu=menu)

# Ramka dla głównego obszaru aplikacji
main_area = customtkinter.CTkFrame(app, fg_color="#535353")
main_area.pack(fill=tkinter.BOTH, expand=True)

one_image_mode()

app.mainloop()