import tkinter
import customtkinter
import time
from customtkinter import *

# Window theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Fonts
comic_sans_ms_font = ("Comic Sans MS", 15, "bold")
sans_serif_font = ("Sans Serif", 15, "bold")
bree_serif_font = ("Bree Serif", 15, "bold")
open_sans_font = ("Open Sans", 15, "bold")
roboto_font = ("Roboto", 15, "bold")
helvetica_font = ("Helvetica", 15, "bold")

# Static Values
sousta = 1  # x - has 5 values
sirma = 2  # y
lamaki = 3  # z
tserki = 4  # k

global_x = 20
global_y = 80

# global orizonties_soustes   # a
# global kathetes_soustes     # b
# global orizontia_diastasi   # c
# global katheti_diastasi     # d


def init_screen(this_screen):
    this_screen.geometry("600x600")
    this_screen.title("Antonopoulos bros")

    heading = CTkLabel(screen, text="Τι header να βάλω;", width=500, height=3,
                       font=comic_sans_ms_font)
    heading.pack(padx=10, pady=10)

    display_input_fields()
    display_calculate_button()
    display_exit_button()


def display_input_fields():

    global orizonties_soustes  # a
    global kathetes_soustes  # b
    global orizontia_diastasi  # c
    global katheti_diastasi  # d
    global check_box

    orizonties_soustes = DoubleVar()
    kathetes_soustes = DoubleVar()  # b
    orizontia_diastasi = DoubleVar()  # c
    katheti_diastasi = DoubleVar()  # d

    CTkLabel(screen, text="Οριζόντιες σούστες", font=comic_sans_ms_font).place(x=global_x, y=global_y)
    CTkEntry(screen, textvariable=orizonties_soustes).place(x=165, y=global_y)

    CTkLabel(screen, text="Κάθετες σούστες", font=comic_sans_ms_font).place(x=global_x, y=global_y+35)
    CTkEntry(screen, textvariable=kathetes_soustes).place(x=165, y=global_y+35)

    CTkLabel(screen, text="Οριζόντια διάσταση", font=comic_sans_ms_font).place(x=global_x, y=global_y+70)
    CTkEntry(screen, textvariable=orizontia_diastasi).place(x=165, y=global_y+70)

    CTkLabel(screen, text="Κάθετη διάσταση", font=comic_sans_ms_font).place(x=global_x, y=global_y+105)
    CTkEntry(screen, textvariable=katheti_diastasi).place(x=165, y=global_y+105)

    check_box = CTkCheckBox(screen, text="Τι να γράψω εδώ;", font=comic_sans_ms_font)
    check_box.place(x=20, y=global_y+140)

    # calculate_button = CTkButton(screen, text='Calculate', text_color="white",
    #                              width=1,
    #                              font=sans_serif_font,
    #                              fg_color="#0ACA7E",
    #                              corner_radius=15,
    #                              hover=True, hover_color="#12D455",
    #                              command=shows_results)
    #
    # calculate_button.pack(padx=5, pady=8, side=BOTTOM, anchor=W)


def validate_values():
    # TODO
    pass


def shows_results():

    CTkProgressBar(screen).place(x=20, y=265)

    CTkLabel(screen, text="retrieved value: " + str(orizonties_soustes.get() * sirma * check_box.get()), font=comic_sans_ms_font).place(x=20, y=285)


def display_calculate_button():
    calculate_button = CTkButton(screen, text='Calculate', text_color="white",
                                 width=1,
                                 font=sans_serif_font,
                                 fg_color="#0ACA7E",
                                 corner_radius=15,
                                 hover=True, hover_color="#12D455",
                                 command=shows_results)

    calculate_button.pack(side=LEFT, anchor=NE, padx=15, pady=0)


def display_exit_button():
    exit_button = CTkButton(screen, text='Exit', text_color="white",
                            width=1,
                            font=sans_serif_font,
                            fg_color="#D53142",
                            corner_radius=15,
                            hover=True, hover_color="#B50938",
                            command=exit)

    exit_button.pack(side=BOTTOM, anchor=SE, padx=15, pady=15)


def close_screen():
    time.sleep(0.2)
    exit()


if __name__ == '__main__':
    screen = CTk()

    init_screen(screen)
    screen.mainloop()
