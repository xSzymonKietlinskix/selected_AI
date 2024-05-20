from tkinter import *

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
            if i == 46:
                r += 1
                c = 0
            if i == 51:
                r += 1
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
            self.canvas.delete("all")

        canvas_width = self.master.winfo_width() / 2
        canvas_height = self.master.winfo_height()

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
        self.canvas = Canvas(self.right_frame, width=board_width, height=board_height, bg='white')
        self.canvas.pack()

        self.rectangles = []
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
                # self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color)
            self.rectangles.append(row_rectangles)

        self.canvas.config(width=board_width, height=board_height)
        self.canvas.update_idletasks()

    def update_board(self):
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
                color = color_map.get(value, "white")
                self.canvas.itemconfig(self.rectangles[row_idx][col_idx], fill=color)
        self.canvas.update_idletasks()

    def create_plot(self, frame):
        if not hasattr(self, 'fig'):
            self.fig = Figure(figsize=(4, 2))
            self.ax = self.fig.add_subplot(111)
            self.matplotlib_canvas = FigureCanvasTkAgg(self.fig, master=frame)
            self.matplotlib_canvas.get_tk_widget().pack(side=BOTTOM)
        else:
            self.ax.clear()  # Clear the existing plot

        # Plot some data (this can be updated to reflect new data)
        self.ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
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

        if not hasattr(self, 'matplotlib_canvas'):
            self.create_plot(self.right_frame)
        if self.canvas is None:
            self.generate_board(int(self.variables.m_rows), int(self.variables.n_colls))
        else:
            self.canvas.delete("all")
            self.canvas.destroy()
            self.canvas = None

        for i in range(0, int(self.variables.n_of_iter)):
            print("Iteracja: ", i)
            if i == 0:
                if self.canvas is None:
                    self.generate_board(int(self.variables.m_rows), int(self.variables.n_colls))
                self.variables.board_values, pv = iter0(self.variables)
                self.update_board()
            if i > 0:
                self.variables.board_values[0][2] = 0
                main_fun(self.variables, pv)
                self.update_board()
            self.update_gui()
            time.sleep(1)




def main():
    root = Tk()
    app = VariablesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


