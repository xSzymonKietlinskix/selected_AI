from tkinter import *
from variables import Variables

class VariablesGUI:
    def __init__(self, master):
        self.master = master
        self.variables = Variables()
        self.entries = {}
        self.create_widgets()

    def create_entry(self, r, c, v_n):
        Label(self.master, text=v_n).grid(row=r, column=c)
        if isinstance(self.variables.__dict__[v_n], bool):
            var = BooleanVar()
            Checkbutton(self.master, variable=var).grid(row=r, column=c + 1)
            self.entries[v_n] = var
        else:
            entry = Entry(self.master)
            entry.grid(row=r, column=c + 1)
            self.entries[v_n] = entry

    def create_widgets(self):
        r = 0
        c = 0
        for i, var_name in enumerate(self.variables.__dict__):
            if i < 7:
                self.create_entry(r, c, var_name)
                r += 1
            else:
                break

        r = 0
        c = 2
        for i, var_name in enumerate(self.variables.__dict__):
            if i >= 7:
                self.create_entry(r, c, var_name)
                r += 1
            if i == 17:
                break

        Label(self.master, text="").grid(row=r)
        r += 1
        self.create_entry(r, 0, "IQ_range_min")
        self.create_entry(r, 2, "IQ_range_max")

        r += 1
        Label(self.master, text="Health_state").grid(row=r)
        r += 1

        c = 0
        for i, var_name in enumerate(self.variables.__dict__):
            if i >= 20:
                self.create_entry(r, c, var_name)
                c += 2
            if i == 22:
                r += 1
                c = 0
            if i == 25:
                break

        r += 1
        self.create_entry(r, 0, "iter_susp_B")
        self.create_entry(r, 2, "D_IC_decr_rate")
        r += 1
        Label(self.master, text="Risc_accept_level(IQ)").grid(row=r)
        r += 1

        r += 1
        self.create_entry(r, 0, "IQ1_lower")
        Label(self.master, text="IQ2").grid(row=r, column=2)
        self.create_entry(r, 3, "IQ3_greater")
        r += 1

        c = 0
        for i, var_name in enumerate(self.variables.__dict__):
            if i >= 30:
                self.create_entry(r, c, var_name)
                c += 2
            if i == 32:
                r += 1
                c = 0
            if i == 35:
                r += 1
                c = 0
            if i == 38:
                break

        r += 1
        Label(self.master, text="Mobility(IQ)").grid(row=r)
        r += 1
        self.create_entry(r, 0, "p_mob_1")
        self.create_entry(r, 2, "p_mob_2")
        self.create_entry(r, 4, "p_mob_3")
        r += 1
        Label(self.master, text="Business_Type").grid(row=r)
        r += 1

        c = 0
        for i, var_name in enumerate(self.variables.__dict__):
            if i >= 42:
                self.create_entry(r, c, var_name)
                c += 2
            if i == 46:
                r += 1
                c = 0
            if i == 51:
                r += 1
                c = 0
            if i == 56:
                break

        r += 1
        Label(self.master, text="Wealth_thr").grid(row=r)
        r += 1

        c = 0
        for i, var_name in enumerate(self.variables.__dict__):
            if i >= 57:
                self.create_entry(r, c, var_name)
                c += 2
            if i == 59:
                break



        self.save_button = Button(self.master, text="Save", command=self.save_variables)
        self.save_button.grid(row=len(self.variables.__dict__), column=1)

    def save_variables(self):
        for var_name, entry in self.entries.items():
            value = entry.get()
            if isinstance(self.variables.__dict__[var_name], int):
                value = int(value)
            elif isinstance(self.variables.__dict__[var_name], float):
                value = float(value)
            elif isinstance(self.variables.__dict__[var_name], bool):
                value = value.lower() == 'true'
            self.variables.__dict__[var_name] = value

        for var_name, value in self.variables.__dict__.items():
            print(var_name, value)

root = Tk()
app = VariablesGUI(root)
root.mainloop()