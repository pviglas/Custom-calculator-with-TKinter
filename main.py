from tkinter import *

import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


fields = (
    'ELATIRIO MIKRO', 'SOUSTAKI MIKRO', 'SOUSTAKI MEGALO', 'ELATIRIO MEGALO',
    'MALAKAS')

def monthly_payment(entries):
    # period rate:
    r = (float(entries['Annual Rate'].get()) / 100) / 12
    print("r", r)
    # principal loan:
    loan = float(entries['Loan Principle'].get())
    n = float(entries['Number of Payments'].get())
    remaining_loan = float(entries['Remaining Loan'].get())
    q = (1 + r) ** n
    monthly = r * ((q * loan - remaining_loan) / (q - 1))
    monthly = ("%8.2f" % monthly).strip()
    entries['Monthly Payment'].delete(0, tk.END)
    entries['Monthly Payment'].insert(0, monthly)
    print("Monthly Payment: %f" % float(monthly))


def final_balance(entries):
    # period rate:
    r = (float(entries['Annual Rate'].get()) / 100) / 12
    print("r", r)
    # principal loan:
    loan = float(entries['Loan Principle'].get())
    n = float(entries['Number of Payments'].get())
    monthly = float(entries['Monthly Payment'].get())
    q = (1 + r) ** n
    remaining = q * loan - ((q - 1) / r) * monthly
    remaining = ("%8.2f" % remaining).strip()
    entries['Remaining Loan'].delete(0, END)
    entries['Remaining Loan'].insert(0, remaining)
    print("Remaining Loan: %f" % float(remaining))


def makeform(root, fields):
    entries = {}

    for field in fields:

        print(field)
        row = Frame(root)

        lab = Label(row, width=22, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")

        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)

        entries[field] = ent
    return entries


def custom_form_found():
    ents = makeform(screen, fields)

    b1 = Button(screen, text='Final Balance',
                command=(lambda e=ents: final_balance(e)))
    b1.pack(side=LEFT, padx=5, pady=5)

    b2 = Button(screen, text='Monthly Payment',
                   command=(lambda e=ents: monthly_payment(e)))
    b2.pack(side=LEFT, padx=5, pady=5)

    b3 = Button(screen, text='Quit', command=screen.quit)
    b3.pack(side=LEFT, padx=5, pady=5)



if __name__ == '__main__':

    #screen = Tk()
    screen = CTk()

    custom_form_found()


    screen.mainloop()


