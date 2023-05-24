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

# Field names
orizonties_soustes_name = 'Οριζόντιες σούστες'
kathetes_soustes_name = 'Κάθετες σούστες'
orizontia_diastasti_name = 'Οριζόντια διάσταση (cm)'
katheti_diastasi_name = 'Κάθετη διάσταση (cm)'
fields = (orizonties_soustes_name, kathetes_soustes_name, orizontia_diastasti_name, katheti_diastasi_name)
check_boxes = 'Με λαμάκι'
result = 'Αποτέλεσμα'

# Radio buttons name and values
radio_buttons = [("2.30", 0.0375), ("2.40", 0.0402), ("2.30 χαμηλό", 0.0325), ("2.40 χαμηλό", 0.036), ("Σουστάκι", 0.0235)]

# Constants
sirma = 0.023718
lamaki = 0.13382
tserki = 0.0011494


def clear(entries):
    for field in fields:
        entries[field].delete(0, END)
        entries[field].insert(0, "")

    entries[result].delete(0, END)
    entries[result].insert(0, "")


def calculate(entries):
    orizonties_soustes = float(entries[orizonties_soustes_name].get())
    kathetes_soustes = float(entries[kathetes_soustes_name].get())
    orizontia_diastasti = float(entries[orizontia_diastasti_name].get())
    katheti_diastasi = float(entries[katheti_diastasi_name].get())

    # if check box is enabled, then multiply by 1 should be applied
    check_box_value = entries[check_boxes].get()

    # calculation formula: a*b*x  + 2*(b-1)*c*y + (1 || 0)* [4*(c+d)*z + 4*(a+b)*k]
    calculation_1 = orizonties_soustes * kathetes_soustes * sousta_radio_button.get()
    calculation_2 = 2 * (kathetes_soustes - 1) * orizontia_diastasti * sirma
    calculation_3 = 4 * (orizontia_diastasti + katheti_diastasi) * lamaki
    calculation_4 = 4 * (orizonties_soustes + kathetes_soustes) * tserki

    final_result = calculation_1 + calculation_2 + (check_box_value * (calculation_3 + calculation_4))
    entries[result].delete(0, END)
    entries[result].insert(0, final_result)

    # Print calculation in console
    print("Calculation:"
          " ({} * {} * {})"
          " + [2 * ({} - 1) * {} * {}]"
          " + [ {} * "
          " [4 * ({} + {}) * {}]"
          " + [4 * ({} + {}) * {}] ]"
          .format(orizonties_soustes, kathetes_soustes, sousta_radio_button.get(),
                  kathetes_soustes, orizontia_diastasti, sirma,
                  check_box_value,
                  orizontia_diastasti, katheti_diastasi, lamaki,
                  orizonties_soustes, kathetes_soustes, tserki
                  )
          )


def create_form(root):
    screen.geometry("600x600")
    screen.title("Antonopoulos bros")

    entries = {}

    row = CTkFrame(root)
    label = CTkLabel(row, width=42, text="Υπολογισμός τελάρων", anchor='w', font=comic_sans_ms_font)
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
    check_box_field.select()    # enable check box by default

    entries[check_boxes] = check_box_field

    row.pack(side=TOP, fill=X, padx=10, pady=25)
    label.pack(side=LEFT)
    check_box_field.place(x=16)
    check_box_field.pack(side=LEFT, expand=NO, fill=X, padx=5)

    # Display radio buttons
    for radio_button, val in radio_buttons:
        row = CTkFrame(root, fg_color="#1A1A1A")
        radio_button_field = CTkRadioButton(row, text=radio_button, variable=sousta_radio_button, value=val,
                                            font=comic_sans_ms_font)

        entries[radio_button] = val

        row.pack(side=TOP, fill=X, padx=10, pady=5)
        label.pack(side=LEFT)

        radio_button_field.place(x=16)
        radio_button_field.pack(side=LEFT, expand=NO, fill=X, padx=5)

    # Display result field
    row = CTkFrame(root, fg_color="#1A1A1A")
    label = CTkLabel(row, width=22, text=result, anchor='w', font=comic_sans_ms_font)

    entry = CTkEntry(row, width=220)
    entry.insert(0, " ")

    row.pack(side=TOP, fill=X, padx=10, pady=15)
    label.pack(side=LEFT)
    entry.place(x=16)
    entry.pack(side=LEFT, expand=NO, fill=X, padx=15)

    entries[result] = entry

    return entries


def show_constants():
    top = CTkToplevel()
    top.geometry("350x280")
    top.title("Σταθερές")

    sirma_str = 'Σύρμα: {} κιλά'.format(sirma)
    lamaki_str = '  Λαμάκι: {} κιλά'.format(lamaki)
    tserki_str = '   Τσέρκι: {} κιλά'.format(tserki)

    CTkLabel(top, width=22, text=sirma_str, font=comic_sans_ms_font).pack(pady=5)
    CTkLabel(top, width=22, text=lamaki_str, font=comic_sans_ms_font).pack(pady=2)
    CTkLabel(top, width=22, text=tserki_str, font=comic_sans_ms_font).pack(pady=2)

    # Display radio buttons values
    for radio_button, value in radio_buttons:
        label_text = '> {}: {}'.format(radio_button, value)
        CTkLabel(top, width=22, text=label_text, font=comic_sans_ms_font).pack(pady=1)


def init_screen():
    inputs = create_form(screen)

    # Buttons
    calculate_button = CTkButton(screen, text='Υπολογισμός', text_color="white",
                                 width=1,
                                 font=sans_serif_font,
                                 fg_color="#0ACA7E",
                                 corner_radius=15,
                                 hover=True, hover_color="#12D455",
                                 command=(lambda e=inputs: calculate(e)))
    calculate_button.pack(side=LEFT, padx=15, pady=0)

    clean_button = CTkButton(screen, text='Καθαρισμός', text_color="white",
                             width=1,
                             font=sans_serif_font,
                             fg_color="#0ACA7E",
                             corner_radius=15,
                             hover=True, hover_color="#12D455",
                             command=(lambda e=inputs: clear(e)))
    clean_button.pack(side=LEFT, padx=15, pady=0)

    constant_button = CTkButton(screen, text='Σταθερές', text_color="white",
                                width=1,
                                font=sans_serif_font,
                                fg_color="#0ACA7E",
                                corner_radius=15,
                                hover=True, hover_color="#12D455",
                                command=show_constants)
    constant_button.pack(side=LEFT, padx=15, pady=0)

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
    sousta_radio_button = DoubleVar()
    init_screen()

    screen.mainloop()
