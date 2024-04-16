import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, IntVar, Radiobutton, Label, END
from variables import Variables
import numpy as np

# Tworzy planszę
def create_board(var):
    size = 500
    m = var.m_rows + 1
    n = var.n_colls + 1
    canvas = Canvas(window, width=size, height=size)
    canvas.place(x=645, y=25)

    # Szerokość i wysokość każdego prostokąta
    square_width = size // n
    square_height = size // m

    # Rysowanie siatki planszy
    for i in range(0, size, square_height):
        canvas.create_line(0, i, size, i, fill="black")
    for j in range(0, size, square_width):
        canvas.create_line(j, 0, j, size, fill="black")

    # Wypisanie numerów kolumn
    for i in range(n):
        x = (i + 0.5) * square_width
        y = square_height / 2
        canvas.create_text(x, y, text=str(i))

    # Wypisanie numerów wierszy
    for j in range(m):
        x = square_width / 2
        y = (j + 0.5) * square_height
        canvas.create_text(x, y, text=str(j))



    # to pewnie trzeba będzie wyrzucić do osobnej funkcji
    # Wstawienie wartości do konkretnych pól planszy
    for row in range(n - 1):
        for col in range(m - 1):
            if var.board_values[row + 1][col + 1] != "":
                x = (col + 1) * square_width + square_width / 2
                y = (row + 1) * square_height + square_height / 2
                canvas.create_text(x, y, text=var.board_values[row + 1][col + 1], font=("Helvetica", 12, "bold"))


# tworzy wykres
def draw_plot(window):
    # Dane do wykresu
    x = [1, 2, 3, 4, 5]
    y1 = [2, 3, 5, 7, 11]
    y2 = [1, 4, 6, 8, 10]
    y3 = [3, 2, 4, 6, 8]

    # Tworzenie wykresu
    fig = plt.figure(figsize=(5.5, 2.6))
    ax = fig.add_subplot(111)
    ax.plot(x, y1, color='red' ,label='reach')
    ax.plot(x, y2, color='green' , label='fair')
    ax.plot(x, y3, color='blue' , label='power')
    ax.set_xlabel('iteration')
    ax.set_ylabel('av_capitol')
    ax.legend()
    # ax.set_title('Wykres liniowy')

    # Umieszczenie wykresu w widżecie Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x = 620, y = 550)

# pokazuje wartości debugowania po zaznaczeniu checboxa
def debug_action():
    if debug.get() == 1:
        # m_rows
        entry_1.insert(0, 6)
        # n_colls
        entry_59.insert(0, 6)
        # n_of_A
        entry_56.insert(0, 2)
        # n_of_D
        entry_57.insert(0, 2)
        # n_of_B
        entry_58.insert(0, 4)
        # n_of_iter
        entry_43.insert(0, 5)
        # n_of_exper
        entry_44.insert(0, 1)
        # init_capitIC
        entry_45.insert(0, 10)
        # IQ_range_min
        entry_2.insert(0, 70)
        # IQ_range_max
        entry_40.insert(0, 140)

        #wczytanie tablicy stanów
        board = load_board("Debugging data/CA_STATES.txt")

        #AGENTS A
        var.board_values = board
        #dopisać reszte na podstawie moodla

def load_board(file):
    loaded_board = np.loadtxt(file)
    new_row = np.full(loaded_board.shape[1], 0)
    loaded_board = np.insert(loaded_board, 0, new_row, axis=0)
    new_coll = np.full(loaded_board.shape[0], 0)
    loaded_board = np.insert(loaded_board, 0, new_coll, axis=1)
    map_num_to_letters = {
        0: "",
        3: "B1",
        1: "A",
        2: "D",
        4: "B2",
        5: "B3"
    }
    board = np.vectorize(map_num_to_letters.get)(loaded_board)

    return board

def clear():
    # m_rows
    entry_1.delete(0, END)
    # n_colls
    entry_59.delete(0, END)
    # n_of_A
    entry_56.delete(0, END)
    # n_of_D
    entry_57.delete(0, END)
    # n_of_B
    entry_58.delete(0, END)
    # n_of_iter
    entry_43.delete(0, END)
    # n_of_exper
    entry_44.delete(0, END)
    # init_capitIC
    entry_45.delete(0, END)
    # IQ_range_min
    entry_2.delete(0, END)
    # IQ_range_max
    entry_40.delete(0, END)


def map_values():
    # Pobierz wartości wpisane do pól Entry i wpisz je do obiektu zawierającego zmienne
    #Top
    var.m_rows = int(entry_1.get())
    var.n_colls = int(entry_59.get())
    var.n_of_A = int(entry_56.get())
    var.n_of_D = int(entry_57.get())
    var.n_of_B = int(entry_58.get())
    var.n_of_iter = int(entry_43.get())
    var.n_of_exper = int(entry_44.get())
    var.init_capitIC = int(entry_45.get())

    # Parameters of A
    var.IQ_range_min = int(entry_2.get())
    var.IQ_range_max = int(entry_40.get())
    # Health_State
    var.p_HS1 = float(entry_4.get())
    var.p_HS2 = float(entry_5.get())
    var.p_HS3 = float(entry_6.get())
    var.p_itl1 = float(entry_37.get())
    var.p_itl2 = float(entry_38.get())
    var.p_itl3 = float(entry_39.get())
    var.iter_susp_B = int(entry_3.get())
    # Risc_accept_level (IQ)
    var.IQ_smaller_than = int(entry_41.get())
    var.IQ_greater_than = int(entry_42.get())
    var.B1_1 = float(entry_7.get())
    var.B1_2 = float(entry_8.get())
    var.B1_3 = float(entry_9.get())
    var.B2_1 = float(entry_13.get())
    var.B2_2 = float(entry_14.get())
    var.B2_3 = float(entry_15.get())
    var.B3_1 = float(entry_16.get())
    var.B3_2 = float(entry_17.get())
    var.B3_3 = float(entry_18.get())
    # Mobility
    var.p_mob_1 = float(entry_19.get())
    var.p_mob_2 = float(entry_20.get())
    var.p_mob_3 = float(entry_21.get())

    # Business type
    var.B1_ICthr = float(entry_22.get())
    var.B2_ICthr = float(entry_23.get())
    var.B3_ICthr = float(entry_24.get())
    var.B1_inv_a = float(entry_25.get())
    var.B2_inv_a = float(entry_27.get())
    var.B3_inv_a = float(entry_26.get())
    var.B1_gap = float(entry_28.get())
    var.B2_gap = float(entry_30.get())
    var.B3_gap = float(entry_29.get())
    var.B1_p_risc = float(entry_31.get())
    var.B2_p_risc = float(entry_33.get())
    var.B3_p_risc = float(entry_32.get())
    var.B1_p_avoid = float(entry_34.get())
    var.B2_p_avoid = float(entry_36.get())
    var.B3_p_avoid = float(entry_35.get())

    # Wealth thr
    var.power = int(entry_10.get())
    var.fax = int(entry_11.get())
    var.rich = int(entry_12.get())

    # generowanie losowej planszy, gdy nie używamy pola debug. Będzie trzeba zmienić ale na razie nie wiem jak
    if var.board_values == None:
        var.board_values = [[random.choice(["", "X"]) for _ in range(var.m_rows + 1)] for _ in range(var.n_colls + 1)]

    if debug.get() == 1:
        var.debug = True
    elif debug.get() == 0:
        var.debug = False

    if read_selection.get() == 1:
        var.read_CA_states = True
    elif read_selection.get() == 2:
        var.read_A_PROFILE = True
    elif read_selection.get() == 3:
        var.read_RAND_NUM = True

    if read_test.get() == 1:
        var.test_1 = True
    elif read_test.get() == 2:
        var.test_2 = True
    elif read_test.get() == 3:
        var.test_3 = True

    if seed.get() == 1:
        var.clock_seed = True
    elif seed.get() == 2:
        var.custom_seed = True
        var.seed_value = int(entry_55.get())


    create_board(var)
    draw_plot(window)
    print_values(var)

# wypisuje zmienne w konsoli
def print_values(var):
    for v in vars(var):
        value = getattr(var, v)
        print(f"{v}: {value}")


# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\xiii5\Desktop\Notatki_stacja\UKSW\selected AI\test\build\assets\frame0")
# teraz jest uniweralna i działa na każdym urządzeniu
SOURCE_PATH = Path(__file__).parent
ASSETS_PATH = SOURCE_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("GUI v1")
window.geometry("1200x850")
window.configure(bg = "#F5D6CF")

var = Variables() #obiekt ze zmiennymi

canvas = Canvas(
    window,
    bg = "#F4F3F2",
    height = 850,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    4.0,
    4.0,
    5.0,
    845.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    4.0,
    4.0,
    600.0,
    5.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    4.0,
    843.9999999999998,
    600.0,
    845.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    599.0,
    843.9999999999998,
    1194.0,
    845.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    599.0,
    3.9999999999998295,
    1194.0,
    5.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    599.0,
    4.0,
    600.0,
    845.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1193.0,
    4.0,
    1194.0,
    845.0,
    fill="#000000",
    outline="")

canvas.create_text(
    20.0,
    50.0,
    anchor="nw",
    text="N_colls",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    20.0,
    88.0,
    anchor="nw",
    text="n_of_A",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    20.0,
    108.0,
    anchor="nw",
    text="n_of_D",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    20.0,
    128.0,
    anchor="nw",
    text="n_of_B",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    20.0,
    166.0,
    anchor="nw",
    text="n_of_iter",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    20.0,
    186.0,
    anchor="nw",
    text="n_of_exper",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    20.0,
    30.0,
    anchor="nw",
    text="M_row",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    135.0,
    245.0,
    anchor="nw",
    text="min",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    268.0,
    245.0,
    anchor="nw",
    text="max",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    20.0,
    225.0,
    anchor="nw",
    text="Parameters of A",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    20.0,
    412.0,
    anchor="nw",
    text="Risc_accept_level (IQ)",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    21.0,
    579.0,
    anchor="nw",
    text="Mobility (IQ)",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    147.5,
    39.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=120.0,
    y=30.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    20.0,
    264.0,
    anchor="nw",
    text="IQ_range",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    20.0,
    294.0,
    anchor="nw",
    text="Health_state",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    147.5,
    273.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=120.0,
    y=264.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    20.0,
    380.0,
    anchor="nw",
    text="n_iter_susp_B",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    147.5,
    389.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=120.0,
    y=380.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    43.0,
    325.0,
    anchor="nw",
    text="p_HS1",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    147.5,
    335.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=120.0,
    y=326.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    217.0,
    325.0,
    anchor="nw",
    text="p_HS2",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    321.5,
    335.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=294.0,
    y=326.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    408.0,
    325.0,
    anchor="nw",
    text="p_HS3",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    512.5,
    335.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=485.0,
    y=326.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    47.0,
    490.0,
    anchor="nw",
    text="B1",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    130.0,
    470.0,
    anchor="nw",
    text="p_acc",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    140.0,
    599.0,
    anchor="nw",
    text="p_mob",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    26.0,
    786.0,
    anchor="nw",
    text="power",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    210.0,
    786.0,
    anchor="nw",
    text="fax",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    401.0,
    787.0,
    anchor="nw",
    text = "rich",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    156.0,
    583.0,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    329.0,
    583.0,
    anchor="nw",
    text="2",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    501.0,
    583.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    145.0,
    304.0,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    318.0,
    304.0,
    anchor="nw",
    text="2",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    506.0,
    304.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    309.0,
    599.0,
    anchor="nw",
    text="p_mob",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    481.0,
    599.0,
    anchor="nw",
    text="p_mob",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    498.0,
    470.0,
    anchor="nw",
    text="p_acc",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    306.0,
    470.0,
    anchor="nw",
    text="p_acc",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    151.5,
    500.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=124.0,
    y=491.0,
    width=55.0,
    height=16.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    325.5,
    500.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=298.0,
    y=491.0,
    width=55.0,
    height=16.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    516.5,
    500.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=489.0,
    y=491.0,
    width=55.0,
    height=16.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    48.5,
    816.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=21.0,
    y=807.0,
    width=55.0,
    height=16.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    222.5,
    816.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=195.0,
    y=807.0,
    width=55.0,
    height=16.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    413.5,
    816.0,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=386.0,
    y=807.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    47.0,
    518.0,
    anchor="nw",
    text="B2",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    151.5,
    528.0,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=124.0,
    y=519.0,
    width=55.0,
    height=16.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    325.5,
    528.0,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=298.0,
    y=519.0,
    width=55.0,
    height=16.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    516.5,
    528.0,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=489.0,
    y=519.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    47.0,
    545.0,
    anchor="nw",
    text="B3",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    151.5,
    555.0,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=124.0,
    y=546.0,
    width=55.0,
    height=16.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    325.5,
    555.0,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=298.0,
    y=546.0,
    width=55.0,
    height=16.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    516.5,
    555.0,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=489.0,
    y=546.0,
    width=55.0,
    height=16.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    163.5,
    629.0,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_19.place(
    x=136.0,
    y=620.0,
    width=55.0,
    height=16.0
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    333.5,
    629.0,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_20.place(
    x=306.0,
    y=620.0,
    width=55.0,
    height=16.0
)

entry_image_21 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(
    503.5,
    629.0,
    image=entry_image_21
)
entry_21 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_21.place(
    x=476.0,
    y=620.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    21.0,
    648.0,
    anchor="nw",
    text="Business type",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    20.0,
    760.0,
    anchor="nw",
    text="Wealth thr",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    21.0,
    689.0,
    anchor="nw",
    text="p_HS1",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    95.0,
    806.0,
    anchor="nw",
    text="of IC",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    269.0,
    806.0,
    anchor="nw",
    text="of IC",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    460.0,
    806.0,
    anchor="nw",
    text="of IC",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_22 = PhotoImage(
    file=relative_to_assets("entry_22.png"))
entry_bg_22 = canvas.create_image(
    106.5,
    699.0,
    image=entry_image_22
)
entry_22 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_22.place(
    x=79.0,
    y=690.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    21.0,
    710.0,
    anchor="nw",
    text="p_HS1",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_23 = PhotoImage(
    file=relative_to_assets("entry_23.png"))
entry_bg_23 = canvas.create_image(
    106.5,
    720.0,
    image=entry_image_23
)
entry_23 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_23.place(
    x=79.0,
    y=711.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    21.0,
    731.0,
    anchor="nw",
    text="p_HS1",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_24 = PhotoImage(
    file=relative_to_assets("entry_24.png"))
entry_bg_24 = canvas.create_image(
    106.5,
    741.0,
    image=entry_image_24
)
entry_24 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_24.place(
    x=79.0,
    y=732.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    200.0,
    670.0,
    anchor="nw",
    text="inv a",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    136.0,
    689.0,
    anchor="nw",
    text="of IC",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    136.0,
    710.0,
    anchor="nw",
    text="of IC",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    495.0,
    688.0,
    anchor="nw",
    text="of IC",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    495.0,
    709.0,
    anchor="nw",
    text="of IC",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    136.0,
    731.0,
    anchor="nw",
    text="of IC",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_25 = PhotoImage(
    file=relative_to_assets("entry_25.png"))
entry_bg_25 = canvas.create_image(
    216.5,
    699.0,
    image=entry_image_25
)
entry_25 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_25.place(
    x=189.0,
    y=690.0,
    width=55.0,
    height=16.0
)

entry_image_26 = PhotoImage(
    file=relative_to_assets("entry_26.png"))
entry_bg_26 = canvas.create_image(
    216.5,
    741.0,
    image=entry_image_26
)
entry_26 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_26.place(
    x=189.0,
    y=732.0,
    width=55.0,
    height=16.0
)

entry_image_27 = PhotoImage(
    file=relative_to_assets("entry_27.png"))
entry_bg_27 = canvas.create_image(
    216.5,
    720.0,
    image=entry_image_27
)
entry_27 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_27.place(
    x=189.0,
    y=711.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    263.0,
    656.0,
    anchor="nw",
    text="increase of GAP",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_28 = PhotoImage(
    file=relative_to_assets("entry_28.png"))
entry_bg_28 = canvas.create_image(
    287.5,
    699.0,
    image=entry_image_28
)
entry_28 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_28.place(
    x=260.0,
    y=690.0,
    width=55.0,
    height=16.0
)

entry_image_29 = PhotoImage(
    file=relative_to_assets("entry_29.png"))
entry_bg_29 = canvas.create_image(
    287.5,
    741.0,
    image=entry_image_29
)
entry_29 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_29.place(
    x=260.0,
    y=732.0,
    width=55.0,
    height=16.0
)

entry_image_30 = PhotoImage(
    file=relative_to_assets("entry_30.png"))
entry_bg_30 = canvas.create_image(
    287.5,
    720.0,
    image=entry_image_30
)
entry_30 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_30.place(
    x=260.0,
    y=711.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    361.0,
    670.0,
    anchor="nw",
    text="p_risc",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_31 = PhotoImage(
    file=relative_to_assets("entry_31.png"))
entry_bg_31 = canvas.create_image(
    380.5,
    699.0,
    image=entry_image_31
)
entry_31 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_31.place(
    x=353.0,
    y=690.0,
    width=55.0,
    height=16.0
)

entry_image_32 = PhotoImage(
    file=relative_to_assets("entry_32.png"))
entry_bg_32 = canvas.create_image(
    380.5,
    741.0,
    image=entry_image_32
)
entry_32 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_32.place(
    x=353.0,
    y=732.0,
    width=55.0,
    height=16.0
)

entry_image_33 = PhotoImage(
    file=relative_to_assets("entry_33.png"))
entry_bg_33 = canvas.create_image(
    380.5,
    720.0,
    image=entry_image_33
)
entry_33 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_33.place(
    x=353.0,
    y=711.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    435.0,
    670.0,
    anchor="nw",
    text="p_avoid_B",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_34 = PhotoImage(
    file=relative_to_assets("entry_34.png"))
entry_bg_34 = canvas.create_image(
    462.5,
    699.0,
    image=entry_image_34
)
entry_34 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_34.place(
    x=435.0,
    y=690.0,
    width=55.0,
    height=16.0
)

entry_image_35 = PhotoImage(
    file=relative_to_assets("entry_35.png"))
entry_bg_35 = canvas.create_image(
    462.5,
    741.0,
    image=entry_image_35
)
entry_35 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_35.place(
    x=435.0,
    y=732.0,
    width=55.0,
    height=16.0
)

entry_image_36 = PhotoImage(
    file=relative_to_assets("entry_36.png"))
entry_bg_36 = canvas.create_image(
    462.5,
    720.0,
    image=entry_image_36
)
entry_36 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_36.place(
    x=435.0,
    y=711.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    43.0,
    350.0,
    anchor="nw",
    text="p_ill1",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_37 = PhotoImage(
    file=relative_to_assets("entry_37.png"))
entry_bg_37 = canvas.create_image(
    147.5,
    360.0,
    image=entry_image_37
)
entry_37 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_37.place(
    x=120.0,
    y=351.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    217.0,
    350.0,
    anchor="nw",
    text="p_ill2",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_38 = PhotoImage(
    file=relative_to_assets("entry_38.png"))
entry_bg_38 = canvas.create_image(
    321.5,
    360.0,
    image=entry_image_38
)
entry_38 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_38.place(
    x=294.0,
    y=351.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    408.0,
    350.0,
    anchor="nw",
    text="p_ill3",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_39 = PhotoImage(
    file=relative_to_assets("entry_39.png"))
entry_bg_39 = canvas.create_image(
    512.5,
    360.0,
    image=entry_image_39
)
entry_39 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_39.place(
    x=485.0,
    y=351.0,
    width=55.0,
    height=16.0
)

entry_image_40 = PhotoImage(
    file=relative_to_assets("entry_40.png"))
entry_bg_40 = canvas.create_image(
    283.5,
    274.0,
    image=entry_image_40
)
entry_40 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_40.place(
    x=256.0,
    y=265.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    47.0,
    444.0,
    anchor="nw",
    text="IQ <",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    266.0,
    443.0,
    anchor="nw",
    text="IQ >",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    204.0,
    444.0,
    anchor="nw",
    text="IQ",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_41 = PhotoImage(
    file=relative_to_assets("entry_41.png"))
entry_bg_41 = canvas.create_image(
    114.5,
    453.0,
    image=entry_image_41
)
entry_41 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_41.place(
    x=87.0,
    y=444.0,
    width=55.0,
    height=16.0
)

entry_image_42 = PhotoImage(
    file=relative_to_assets("entry_42.png"))
entry_bg_42 = canvas.create_image(
    325.5,
    453.0,
    image=entry_image_42
)
entry_42 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_42.place(
    x=298.0,
    y=444.0,
    width=55.0,
    height=16.0
)

entry_image_43 = PhotoImage(
    file=relative_to_assets("entry_43.png"))
entry_bg_43 = canvas.create_image(
    147.5,
    176.0,
    image=entry_image_43
)
entry_43 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_43.place(
    x=120.0,
    y=167.0,
    width=55.0,
    height=16.0
)

entry_image_44 = PhotoImage(
    file=relative_to_assets("entry_44.png"))
entry_bg_44 = canvas.create_image(
    147.5,
    196.0,
    image=entry_image_44
)
entry_44 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_44.place(
    x=120.0,
    y=187.0,
    width=55.0,
    height=16.0
)

canvas.create_text(
    256.0,
    186.0,
    anchor="nw",
    text="Init_capit IC",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_45 = PhotoImage(
    file=relative_to_assets("entry_45.png"))
entry_bg_45 = canvas.create_image(
    383.5,
    196.0,
    image=entry_image_45
)
entry_45 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_45.place(
    x=356.0,
    y=187.0,
    width=55.0,
    height=16.0
)

seed = IntVar()
seed.set(1)

radiobutton_1 = Radiobutton(window, text="clock_seed", variable=seed, value=1, highlightthickness=0)
radiobutton_1.place(x=440, y=145)

radiobutton_2 = Radiobutton(window, text="custom_seed", variable=seed, value=2, highlightthickness=0)
radiobutton_2.place(x=440, y=163)


read_selection = IntVar()
read_selection.set(1)

radiobutton_1 = Radiobutton(window, text="read CA_STATES", variable=read_selection, value=1, highlightthickness=0)
radiobutton_1.place(x=256, y=60)

radiobutton_2 = Radiobutton(window, text="read A_PROFILE", variable=read_selection, value=2, highlightthickness=0)
radiobutton_2.place(x=256, y=78)

radiobutton_3 = Radiobutton(window, text="read RAND_NUM", variable=read_selection, value=3, highlightthickness=0)
radiobutton_3.place(x=256, y=96)

read_test = IntVar()
read_test.set(1)

radiobutton_4 = Radiobutton(window, text="test 1", variable=read_test, value=1, highlightthickness=0)
radiobutton_4.place(x=256, y=121)

radiobutton_5 = Radiobutton(window, text="test 2", variable=read_test, value=2, highlightthickness=0)
radiobutton_5.place(x=256, y=139)

radiobutton_6 = Radiobutton(window, text="test 3", variable=read_test, value=3, highlightthickness=0)
radiobutton_6.place(x=256, y=157)

debug = IntVar()

C2 = Checkbutton(window, text = "Debug", variable = debug,
   onvalue = 1, offvalue = 0, height=0,
   width = 5, command=debug_action)
C2.place(x=256.0, y=32.0)






entry_image_55 = PhotoImage(
    file=relative_to_assets("entry_55.png"))
entry_bg_55 = canvas.create_image(
    492.5,
    196.0,
    image=entry_image_55
)
entry_55 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_55.place(
    x=440.0,
    y=187.0,
    width=105.0,
    height=16.0
)

entry_image_56 = PhotoImage(
    file=relative_to_assets("entry_56.png"))
entry_bg_56 = canvas.create_image(
    147.5,
    98.0,
    image=entry_image_56
)
entry_56 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_56.place(
    x=120.0,
    y=89.0,
    width=55.0,
    height=16.0
)

entry_image_57 = PhotoImage(
    file=relative_to_assets("entry_57.png"))
entry_bg_57 = canvas.create_image(
    147.5,
    118.0,
    image=entry_image_57
)
entry_57 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_57.place(
    x=120.0,
    y=109.0,
    width=55.0,
    height=16.0
)

entry_image_58 = PhotoImage(
    file=relative_to_assets("entry_58.png"))
entry_bg_58 = canvas.create_image(
    147.5,
    138.0,
    image=entry_image_58
)
entry_58 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_58.place(
    x=120.0,
    y=129.0,
    width=55.0,
    height=16.0
)

entry_image_59 = PhotoImage(
    file=relative_to_assets("entry_59.png"))
entry_bg_59 = canvas.create_image(
    147.5,
    60.0,
    image=entry_image_59
)
entry_59 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_59.place(
    x=120.0,
    y=50.0,
    width=55.0,
    height=18.0
)

canvas.create_rectangle(
    9.989501953125,
    243.0,
    593.989501953125,
    244.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    10.0,
    647.0,
    594.0,
    648.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    613.0,
    818.9999999999999,
    1179.0,
    820.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    613.0,
    544.9999999999999,
    1179.0,
    546.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    612.754150390625,
    543.9989013671875,
    613.754150390625,
    820.0001831054688,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1177.24169921875,
    543.9998168945312,
    1178.24169921875,
    819.0002746582031,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    10.0,
    754.0,
    594.0,
    755.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    593.0,
    242.0,
    594.0,
    648.0111083984375,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    593.0,
    647.0,
    594.0,
    755.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    10.0,
    242.0,
    11.0,
    648.0111083984375,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    10.0,
    647.0,
    11.0,
    755.0,
    fill="#000000",
    outline="")




display_button = Button(window, text="Start", command=map_values)
display_button.place(x=500, y=800)
display_button = Button(window, text="Clear", command=clear)
display_button.place(x=540, y=800)
window.resizable(False, False)
window.mainloop()
