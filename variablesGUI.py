from tkinter import *

import functions
import program
from variables import Variables
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from program import iter0, ProgramVar
import time
from main import main_fun

class VariablesGUI:
    def __init__(self, master):
        self.master = master
        self.left_frame = Frame(self.master)
        self.left_frame.pack(side=LEFT)
        self.right_frame = Frame(self.master)
        self.right_frame.pack(side=RIGHT)
        self.canvas = None
        self.var_debug = BooleanVar(value=False)
        self.variables = Variables()
        self.entries = {}
        self.create_widgets()
        self.debug_fun()
        self.rectangles = []
        self.root = master

    def debug_fun(self):
        if self.var_debug.get() is True:
            debug_values = []
            with open("Debugging data/debug_data.txt", "r") as file:
                for line in file:
                    debug_values.append(str(line.strip()))

            i = 0
            for var_name, entry in self.entries.items():
                if type(entry) == BooleanVar:
                    entry.set(bool(debug_values[i]))
                else:
                    entry.insert(0,debug_values[i])
                i += 1

            with open("Debugging data/CA_STATES.txt", "r") as file:
                for line in file:
                    row = list(map(int, line.strip().split()))
                    self.variables.board_values.append(row)

        if self.var_debug.get() is False:
            i = 0
            for var_name, entry in self.entries.items():
                if type(entry) == BooleanVar:
                    entry.set(False)
                elif type(entry) == IntVar:
                    entry.set(1)
                else:
                    entry.delete(0,'end')
                i += 1



    def create_entry(self, r, c, v_n):
        if v_n == "power":
            Label(self.left_frame, text="poor").grid(row=r, column=c)
        elif v_n == "fax":
            Label(self.left_frame, text="fair").grid(row=r, column=c)
        else:
            Label(self.left_frame, text=v_n).grid(row=r, column=c)
        if isinstance(self.variables.__dict__[v_n], bool):
            var = BooleanVar()
            Checkbutton(self.left_frame, variable=var).grid(row=r, column=c + 1)
            self.entries[v_n] = var
        else:
            entry = Entry(self.left_frame)
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


        Label(self.left_frame, text="Debug").grid(row=r, column=c)

        Checkbutton(self.left_frame, variable=self.var_debug, command=self.debug_fun).grid(row=r, column=c + 1)

        self.variables.debug = bool(self.var_debug)


        r += 1
        for i, var_name in enumerate(self.variables.__dict__):
            if i >= 8:
                self.create_entry(r, c, var_name)
                r += 1
            if i == 10: break

        test_var = IntVar()
        test_var.set(1)
        Label(self.left_frame, text="test 1", highlightthickness=0).grid(row=r, column=c)
        Radiobutton(self.left_frame, variable=test_var, value=1).grid(row=r, column=c + 1)
        r += 1
        Label(self.left_frame, text="test 2", highlightthickness=0).grid(row=r, column=c)
        Radiobutton(self.left_frame, variable=test_var, value=2).grid(row=r, column=c + 1)
        r += 1
        Label(self.left_frame, text="test 3", highlightthickness=0).grid(row=r, column=c)
        Radiobutton(self.left_frame, variable=test_var, value=3).grid(row=r, column=c + 1)


        if test_var.get() == 1:
            self.variables.test_1 = True
        elif test_var.get() == 2:
            self.variables.test_2 = True
        elif test_var.get() == 3:
            self.variables.test_3 = True

        r = 0
        c += 2
        seed_var = IntVar()
        seed_var.set(1)
        Label(self.left_frame, text="clock_seed", highlightthickness=0).grid(row=r, column=c)
        Radiobutton(self.left_frame, variable=seed_var, value=1).grid(row=r, column=c + 1)
        r += 1
        Label(self.left_frame, text="custom_seed", highlightthickness=0).grid(row=r, column=c)
        Radiobutton(self.left_frame, variable=seed_var, value=2).grid(row=r, column=c + 1)

        if seed_var.get() == 1:
            self.variables.clock_seed = True
        elif seed_var.get() == 2:
            self.variables.custom_seed = True

        r += 1
        self.create_entry(r, c, "seed_value")
        r += 1
        self.create_entry(r, c, "init_capitIC")

        r = 17

        r += 1
        Label(self.left_frame, text="Parameters of A", font=("Helvetica", 12, "bold")).grid(row=r)
        r += 1

        self.create_entry(r, 0, "IQ_range_min")
        self.create_entry(r, 2, "IQ_range_max")

        r += 1
        Label(self.left_frame, text="Health_state", font=("Helvetica", 12, "bold")).grid(row=r)
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
        Label(self.left_frame, text="Risc_accept_level(IQ)", font=("Helvetica", 12, "bold")).grid(row=r)
        r += 1

        r += 1
        self.create_entry(r, 0, "IQ1_lower")
        Label(self.left_frame, text="IQ2").grid(row=r, column=2)
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
        Label(self.left_frame, text="Mobility(IQ)", font=("Helvetica", 12, "bold")).grid(row=r)
        r += 1
        self.create_entry(r, 0, "p_mob_1")
        self.create_entry(r, 2, "p_mob_2")
        self.create_entry(r, 4, "p_mob_3")
        r += 1
        Label(self.left_frame, text="Business_Type", font=("Helvetica", 12, "bold")).grid(row=r)
        r += 1

        c = 0
        for i, var_name in enumerate(self.variables.__dict__):
            if i >= 42:
                self.create_entry(r, c, var_name)
                c += 2
            if i == 44:
                r += 1
                c = 0
            if i == 47:
                r += 1
                c = 0
            if i == 50:
                r += 1
                c = 0
            if i == 52:
                r+=1
                c=0
            if i == 54:
                r+= 1
                c = 0
            if i == 56:
                break

        r += 1
        Label(self.left_frame, text="Wealth_thr", font=("Helvetica", 12, "bold")).grid(row=r)
        r += 1

        c = 0
        for i, var_name in enumerate(self.variables.__dict__):
            if i >= 57:
                self.create_entry(r, c, var_name)
                c += 2
            if i == 59:
                break

        self.save_button = Button(self.left_frame, text="ok", command=self.save_variables)
        self.save_button.grid(row=len(self.variables.__dict__), column=1)

    def generate_board(self, rows, cols):
        if self.canvas is not None:
            self.canvas.delete("all")  # Usuń wszystkie elementy z canvasu

        # Oblicz wymiary canvasu i komórek
        canvas_width = self.left_frame.winfo_width() * 0.7
        canvas_height = self.left_frame.winfo_height()
        color_map = {
            0: "white",
            1: "yellow",
            2: "plum",
            3: "#87ceeb",
            4: "#0000cd",
            5: "#4169e1"
        }
        cell_size = min(canvas_width / cols, canvas_height / rows) * 0.7
        board_width = cols * cell_size
        board_height = rows * cell_size

        # Utwórz nowy canvas, jeśli nie istnieje, lub zresetuj go
        if self.canvas is None:
            self.canvas = Canvas(self.right_frame, width=board_width, height=board_height, bg='white')
            self.canvas.pack()
        else:
            self.canvas.config(width=board_width, height=board_height)
            self.canvas.delete("all")  # Usuń wszystkie elementy z canvasu

        # Zresetuj tablicę prostokątów
        self.rectangles = []

        # Generuj prostokąty na planszy
        for row_idx, row in enumerate(self.variables.board_values):
            row_rectangles = []
            for col_idx, value in enumerate(row):
                x1 = col_idx * cell_size
                y1 = row_idx * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                color = color_map.get(value, "white")
                rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color)
                row_rectangles.append(rectangle)
            self.rectangles.append(row_rectangles)

        # Zaktualizuj wymiary canvasu
        self.canvas.config(width=board_width, height=board_height)
        self.canvas.update_idletasks()

    def update_board(self, pv):
        color_map = {
            0: "white",
            1: "yellow",
            2: "plum",
            3: "#87ceeb",
            4: "#0000cd",
            5: "#4169e1"
        }
        # Update the color of each rectangle
        for row_idx, row in enumerate(self.variables.board_values):
            for col_idx, value in enumerate(row):
                if value == 1:
                    for a in pv.A_ACTIVITY:
                        i_id, j_id = divmod(int(a.glob_id) - 1, int(self.variables.n_colls))
                        if i_id == row_idx and j_id == col_idx:
                            if float(a.curr_cap) >= float(self.variables.rich):
                                color = "red"
                            elif float(a.curr_cap) >= float(self.variables.fax):
                                color = "orange"
                            elif float(a.curr_cap) < float(self.variables.fax):
                                color = "yellow"
                else:
                    color = color_map.get(value, "white")
                self.canvas.itemconfig(self.rectangles[row_idx][col_idx], fill=color)
        self.canvas.update_idletasks()
       # self.right_frame.update()

    def create_plot(self, frame, data_for_plot):
        if not hasattr(self, 'fig'):
            self.fig = Figure(figsize=(4, 3))
            self.ax = self.fig.add_subplot(111)
            self.matplotlib_canvas = FigureCanvasTkAgg(self.fig, master=frame)
            self.matplotlib_canvas.get_tk_widget().pack(side=BOTTOM)
        else:
            self.ax.clear()  # Clear the existing plot

        # Plot some data (this can be updated to reflect new data)
        # self.ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])


        self.ax.plot(data_for_plot['iter'], data_for_plot['av_cap1'], label='poor_av_cap', marker='o', color='b')
        self.ax.plot(data_for_plot['iter'], data_for_plot['av_cap2'], label='fair_av_cap', marker='s', color='g')
        self.ax.plot(data_for_plot['iter'], data_for_plot['av_cap3'], label='rich_av_cap', marker='^', color='r')

        # Dodanie tytułu i etykiet osi
        self.ax.set_xlabel('Iter')
        self.ax.set_ylabel('av_cap')
        self.ax.legend()
        self.matplotlib_canvas.draw()


    def update_gui(self):
        self.root.update_idletasks()
        self.root.update()

    def save_variables(self):
        for var_name, entry in self.entries.items():
            value = entry.get()
            if isinstance(self.variables.__dict__[var_name], float):
                value = float(value)
            elif isinstance(self.variables.__dict__[var_name], float):
                value = float(value)
            elif isinstance(self.variables.__dict__[var_name], bool):
                value = bool(value)
            self.variables.__dict__[var_name] = value

        for var_name, value in self.variables.__dict__.items():
            print(var_name, value)

        if len(self.variables.board_values) != int(self.variables.m_rows) or len(self.variables.board_values[0]) != int(self.variables.n_colls):
            self.variables.board_values = [[0] * int(self.variables.n_colls) for _ in range(int(self.variables.m_rows))]

        for i in range(0, int(self.variables.n_of_iter)):
            #print("Iteracja: ", i)
            if i == 0:
                self.generate_board(int(self.variables.m_rows), int(self.variables.n_colls))
                self.variables.board_values, pv = iter0(self.variables)
                self.update_board(pv)
                with open('results.txt', 'w') as file:
                    file.write("# 1    2        3        4        5        6        7        8        9     10       11     12    13\n")
                    file.write("#      poorest  poorest  poorest  richest  richest  richest  poorest  fair  richest  % of  % of  % of\n")
                    file.write("# iter  CAP      A_ID    GLOB_ID    CAP    A_ID     glob_ID  av cap  av cap  av cap  poor  fair  rich\n")
                with open('debug.txt', 'w') as file:
                    file.write('')
                functions.print_debug(self.variables, pv, i)
                functions.print_results(self.variables, pv, i)
                data_for_plot = functions.get_data_for_plot()
                self.create_plot(self.right_frame, data_for_plot)
            if i > 0:
                self.variables.board_values, self.variables, pv = main_fun(self.variables, pv, i)
                self.update_board(pv)
                functions.print_debug(self.variables, pv, i)
                functions.print_results(self.variables, pv, i)
                data_for_plot = functions.get_data_for_plot()
                self.create_plot(self.right_frame, data_for_plot)
                #print("Plansza: " + str(pv.CA_STATES))
            self.update_gui()
            time.sleep(0.5)

def main():
    root = Tk()
    app = VariablesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


