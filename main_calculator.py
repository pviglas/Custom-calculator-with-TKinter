import customtkinter
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

fields = ('Οριζόντιες σούστες', 'Κάθετες σούστες', 'Οριζόντια διάσταση', 'Κάθετη διάσταση')
check_boxes = 'Tick box'
result = 'Αποτέλεσμα'
radio_buttons = [("επιλογή 1", 10), ("επιλογή 2", 100), ("επιλογή 3", 1000), ("επιλογή 4", 0), ("επιλογή 5", 1)]

# Constants
sirma = 10      # y
lamaki = 100    # z
tserki = 1000   # k


def clean(entries):
    for field in fields:
        entries[field].delete(0, END)
        entries[field].insert(0, ".!.")

    entries[result].delete(0, END)
    entries[result].insert(0, ".!.")


def calculate_price(entries):
    orizonties_soustes = float(entries['Οριζόντιες σούστες'].get())     # a
    kathetes_soustes = float(float(entries['Κάθετες σούστες'].get()))   # b
    orizontia_diastasti = float(entries['Οριζόντια διάσταση'].get())    # c
    katheti_diastasi = float(entries['Κάθετη διάσταση'].get())          # d
    check_box_value = 1 - entries[check_boxes].get()    # if check box is enabled, then multiply by 0 should be applied
    # check_box_value = 1 - check_box_value

    # calculation formula: a*b*x  + 2*(b-1)*c*y + (1 || 0)* [4*(c+d)*z + 4*(a+b)*k]
    calculation_1 = orizonties_soustes * kathetes_soustes * sousta_radio_button.get()
    calculation_2 = 2 * (kathetes_soustes - 1) * orizontia_diastasti * sirma
    calculation_3 = 4 * (orizontia_diastasti + katheti_diastasi) * lamaki
    calculation_4 = 4 * (orizonties_soustes + kathetes_soustes) * tserki

    final_result = calculation_1 + calculation_2 + (check_box_value * (calculation_3 + calculation_4))
    entries[result].delete(0, END)
    entries[result].insert(0, final_result)


def create_form(root, fields):
    screen.geometry("600x600")
    screen.title("Antonopoulos bros")

    entries = {}

    row = CTkFrame(root)
    label = CTkLabel(row, width=42, text="Βρες μου έναν τίτλο", anchor='w', font=comic_sans_ms_font)
    row.pack(side=TOP, fill=X, padx=10, pady=10)
    label.pack()

    # Display static input fields
    for field in fields:
        row = CTkFrame(root, fg_color="#1A1A1A")
        label = CTkLabel(row, width=22, text=field, anchor='w', font=comic_sans_ms_font)
        entry = CTkEntry(row)
        entry.insert(0, "0")

        row.pack(side=TOP, fill=X, padx=10, pady=5)
        label.pack(side=LEFT)
        entry.place(x=16)
        entry.pack(side=LEFT, expand=NO, fill=X, padx=15)

        entries[field] = entry

    # Display check box
    row = CTkFrame(root, fg_color="#1A1A1A")
    check_box_field = CTkCheckBox(row, text=check_boxes, font=comic_sans_ms_font)

    entries[check_boxes] = check_box_field

    row.pack(side=TOP, fill=X, padx=10, pady=25)
    label.pack(side=LEFT)
    check_box_field.place(x=16)
    check_box_field.pack(side=LEFT, expand=NO, fill=X, padx=5)

    # Display radio buttons
    for radio_button, val in radio_buttons:
        row = CTkFrame(root, fg_color="#1A1A1A")
        radio_button_field = CTkRadioButton(row, text=radio_button, variable=sousta_radio_button, value=val, font=comic_sans_ms_font)

        entries[radio_button] = val

        row.pack(side=TOP, fill=X, padx=10, pady=5)
        label.pack(side=LEFT)

        radio_button_field.place(x=16)
        radio_button_field.pack(side=LEFT, expand=NO, fill=X, padx=5)

    # Display result field
    row = CTkFrame(root, fg_color="#1A1A1A")
    label = CTkLabel(row, width=22, text=result, anchor='w', font=comic_sans_ms_font)

    entry = CTkEntry(row)
    entry.insert(0, " ")

    row.pack(side=TOP, fill=X, padx=10, pady=15)
    label.pack(side=LEFT)
    entry.place(x=16)
    entry.pack(side=LEFT, expand=NO, fill=X, padx=15)

    entries[result] = entry

    return entries


def init_screen():
    inputs = create_form(screen, fields)

    # Buttons
    calculate_button = CTkButton(screen, text='Υπολογισμός', text_color="white",
                                 width=1,
                                 font=sans_serif_font,
                                 fg_color="#0ACA7E",
                                 corner_radius=15,
                                 hover=True, hover_color="#12D455",
                                 command=(lambda e=inputs: calculate_price(e)))
    calculate_button.pack(side=LEFT, padx=15, pady=0)

    clean_button = CTkButton(screen, text='Εκκαθαρισμός', text_color="white",
                             width=1,
                             font=sans_serif_font,
                             fg_color="#0ACA7E",
                             corner_radius=15,
                             hover=True, hover_color="#12D455",
                             command=(lambda e=inputs: clean(e)))
    clean_button.pack(side=LEFT, padx=15, pady=0)

    exit_button = CTkButton(screen, text='Έξοδος', text_color="white",
                            width=1,
                            font=sans_serif_font,
                            fg_color="#D53142",
                            corner_radius=15,
                            hover=True, hover_color="#B50938",
                            command=screen.quit)
    exit_button.pack(side=RIGHT, padx=15, pady=0)


if __name__ == '__main__':
    screen = CTk()
    sousta_radio_button = IntVar()  # x
    init_screen()

    screen.mainloop()
