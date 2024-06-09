import random
import variables
import pandas as pd

def copy_neighborhood(glob_id, variables, CELLS_NEIGHBORS, CA_STATES_TEMP):
    MY_NEIGHB = [0] * 8
    for m in range(0, 8):
        m_neighb_ID = CELLS_NEIGHBORS[glob_id-1][m]
        if m_neighb_ID == -1:
            MY_NEIGHB[m] = -1
        else:
            i,j = divmod(m_neighb_ID -1, int(variables.n_colls))
            CA_states_tempp = [row[1:] for row in CA_STATES_TEMP.board[1:]]
            MY_NEIGHB[m] = CA_states_tempp[i][j]
    return MY_NEIGHB

def create_cells_neighbors(m, n):
    # Tworzymy pustą macierz o wymiarach m x n
    matrix = [[-1] * 8 for _ in range(m * n)]

    VALEUS = [[-1] * (int(n) + 2) for _ in range((int(m) + 2))]
    value = 1
    for i in range(1, len(VALEUS) - 1):
        for j in range(1, len(VALEUS[0]) - 1):
            VALEUS[i][j] = value
            value += 1

    # Funkcja zwracająca sąsiadów danego punktu
    def get_neighbors(point, n, VALEUS):
        neighbors = []
        i, j = divmod(point, n)  # Obliczamy indeksy wiersza i kolumny dla danego punktu
        i += 1
        j += 1
        neighbors.append(VALEUS[i-1][j])
        neighbors.append(VALEUS[i-1][j+1])
        neighbors.append(VALEUS[i][j + 1])
        neighbors.append(VALEUS[i+1][j + 1])
        neighbors.append(VALEUS[i+1][j])
        neighbors.append(VALEUS[i + 1][j - 1])
        neighbors.append(VALEUS[i][j - 1])
        neighbors.append(VALEUS[i - 1][j - 1])
        return neighbors



    # Wypełniamy macierz sąsiadami dla każdego punktu
    for point in range(m * n):
        neighbors = get_neighbors(point, n, VALEUS)
        for idx, neighbor in enumerate(neighbors):
            matrix[point][idx] = neighbor

    return matrix

def create_rand_CA_STATES(variables, CA_STATES,
                          CA_ACTIVE_ABS, A_PROFILE, A_ACTIVITY,
                          B_PROFILE, B_ACTIVITY, D_PROFILE, D_ACTIVITY):
    # create agents Ai in CA_STATES
    for i in range(0, int(variables.n_of_A)):
        i_ID = random.randint(1, int(variables.m_rows))
        j_ID = random.randint(1, int(variables.n_colls))
        while CA_STATES.board[i_ID][j_ID] != 0:
            i_ID = random.randint(1, int(variables.m_rows))
            j_ID = random.randint(1, int(variables.n_colls))

        CA_STATES.board[i_ID][j_ID] = 1
        glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
        A_PROFILE[i].glob_id = glob_ID
        A_ACTIVITY[i].glob_id = glob_ID

    # create business Aj
    for j in range(0, int(variables.n_of_B)):
        i_ID = random.randint(1, int(variables.m_rows))
        j_ID = random.randint(1, int(variables.n_colls))
        while CA_STATES.board[i_ID][j_ID] != 0:
            i_ID = random.randint(1, int(variables.m_rows))
            j_ID = random.randint(1, int(variables.n_colls))

        numbers = [1, 2, 3]
        probabilities = [float(variables.B1_p_avoid), float(variables.B2_p_avoid), float(variables.B3_p_avoid)]
        x = random.choices(numbers, weights=probabilities, k=1)[0]
        if x == 1:
            CA_STATES.board[i_ID][j_ID] = 3
            glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
            B_PROFILE[j].glob_id = glob_ID
            B_PROFILE[j].b_type = 1
            B_ACTIVITY[j].glob_id = glob_ID
            B_ACTIVITY[j].type = 1
        elif x == 2:
            CA_STATES.board[i_ID][j_ID] = 4
            glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
            B_PROFILE[j].glob_id = glob_ID
            B_PROFILE[j].b_type = 2
            B_ACTIVITY[j].glob_id = glob_ID
            B_ACTIVITY[j].type = 2
        elif x == 3:
            CA_STATES.board[i_ID][j_ID] = 5
            glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
            B_PROFILE[j].glob_id = glob_ID
            B_PROFILE[j].b_type = 3
            B_ACTIVITY[j].glob_id = glob_ID
            B_ACTIVITY[j].type = 3
    # create decrease Dk
    for k in range(0, int(variables.n_of_D)):
        i_ID = random.randint(1, int(variables.m_rows))
        j_ID = random.randint(1, int(variables.n_colls))
        while CA_STATES.board[i_ID][j_ID] != 0:
            i_ID = random.randint(1, int(variables.m_rows))
            j_ID = random.randint(1, int(variables.n_colls))

        CA_STATES.board[i_ID][j_ID] = 2
        glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
        D_PROFILE[k].glob_id = glob_ID
        D_ACTIVITY[k].glob_id = glob_ID

# inicjacja niewiadomej listy


def find_free_space_neigh(j, MY_NEIGHB, CELLS_NEIGHBORS):
    real_free_space = False
    FREE_SPACE_LOC = [0] * 8
    cr_free_space = 0
    for m in range(0, 8):
        if MY_NEIGHB[m] == 0:
            real_free_space = True
            FREE_SPACE_LOC[cr_free_space] = CELLS_NEIGHBORS[j][m]
            cr_free_space += 1
    free_space = real_free_space
    return FREE_SPACE_LOC, free_space, cr_free_space


def move_to_free_ca_state(k,variables, CA_STATES_TEMP, A_or_B_or_D ,A_PROFILE = None, A_ACTIVITY = None, B_PROFILE = None, B_ACTIVITY = None, D_PROFILE = None, D_ACTIVITY = None):
    CA_free_loc_found = False

    while not CA_free_loc_found:
        free_glob_id = random.randint(1, int(variables.m_rows) * int(variables.n_colls))
        i, j = divmod(free_glob_id -1, int(variables.n_colls))
        if CA_STATES_TEMP.board[i + 1][j + 1] == 0:
            CA_free_loc_found = True
            if A_or_B_or_D == "B":
                if B_PROFILE[k].b_type == 1:
                    code_B = 3
                elif B_PROFILE[k].b_type == 2:
                    code_B = 4
                else: code_B = 5
                CA_STATES_TEMP.board[i + 1][j + 1] = code_B
                i_id, j_id = divmod(B_ACTIVITY[k].glob_id -1, int(variables.n_colls))
                CA_STATES_TEMP.board[i_id + 1][j_id + 1] = 0
                B_ACTIVITY[k].glob_id = free_glob_id
                B_ACTIVITY[k].crB_of_emerg_hops += 1

            elif A_or_B_or_D == "A":
                CA_STATES_TEMP.board[i + 1][j + 1] = 1
                i_id, j_id = divmod(A_ACTIVITY[k].glob_id -1, int(variables.n_colls))
                CA_STATES_TEMP.board[i_id + 1][j_id + 1] = 0
                A_ACTIVITY[k].glob_id = free_glob_id
                A_ACTIVITY[k].crA_of_emerg_hops += 1
                A_ACTIVITY[k].pos_changed = 1

            elif A_or_B_or_D == "D":
                CA_STATES_TEMP.board[i+1][j+1] = 2
                i_id, j_id = divmod(D_ACTIVITY[k].glob_id -1, int(variables.n_colls))
                CA_STATES_TEMP.board[i_id + 1][j_id + 1] = 0
                D_ACTIVITY[k].glob_id = free_glob_id
                D_ACTIVITY[k].crD_of_emerg_hops += 1


def move_rand_neighb_loc(j, cr_free_space, debug_pointer, RAND_NUM, variables, FREE_SPACE_LOC, A_or_B_or_D, CA_STATES_TEMP, A_PROFILE = None, A_ACTIVITY = None, B_PROFILE = None, B_ACTIVITY = None, D_PROFILE = None, D_ACTIVITY = None):
    if variables.read_RAND_NUM is True:
        if debug_pointer == 50:
            debug_pointer = 0
        else:
            debug_pointer += 1
        x = RAND_NUM[debug_pointer]
    else:
        x = random.random()

    del_x = 1.0/cr_free_space

    if x <= del_x:
        new_glob_id = FREE_SPACE_LOC[0]

    elif x <= 2*del_x:
        new_glob_id = FREE_SPACE_LOC[1]

    elif x <= 3*del_x:
        new_glob_id = FREE_SPACE_LOC[2]

    elif x <= 4*del_x:
        new_glob_id = FREE_SPACE_LOC[3]

    elif x <= 5*del_x:
        new_glob_id = FREE_SPACE_LOC[4]

    elif x <= 6*del_x:
        new_glob_id = FREE_SPACE_LOC[5]

    elif x <= 7*del_x:
        new_glob_id = FREE_SPACE_LOC[6]

    else:
        new_glob_id = FREE_SPACE_LOC[7]

    if A_or_B_or_D == "B":
        code_B = int(B_PROFILE[j].b_type) + 2
        i_id, j_id = divmod(new_glob_id - 1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_id + 1][j_id + 1] = code_B
        i_old, j_old = divmod(int(B_ACTIVITY[j].glob_id) - 1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_old + 1][j_old + 1] = 0
        B_ACTIVITY[j].glob_id = new_glob_id

    elif A_or_B_or_D == "D":
        i_id, j_id = divmod(new_glob_id -1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_id + 1][j_id + 1] = 2
        i_old, j_old = divmod(int(D_ACTIVITY[j].glob_id) -1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_old + 1][j_old + 1] = 0
        D_ACTIVITY[j].glob_id = new_glob_id

    elif A_or_B_or_D == "A":
        i_id, j_id = divmod(new_glob_id - 1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_id + 1][j_id + 1] = 1
        i_old, j_old = divmod(int(A_ACTIVITY[j].glob_id) -1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_old + 1][j_old + 1] = 0
        A_ACTIVITY[j].glob_id = new_glob_id


def print_results(variables, pv, iteration):

    poorest_cap = 0
    poorest_A_id = 0
    poorest_glob_id = 0
    richest_cap = 0
    richest_A_id = 0
    richest_glob_id = 0
    poorest_av_cap = 0
    fair_av_cap = 0
    richest_av_cap = 0
    procent_poorest = 0
    procent_fair = 0
    procent_richest = 0

    poor = []
    fax = []
    rich = []

    for a in pv.A_ACTIVITY:
        if a.curr_cap >= float(variables.rich):
            rich.append(a)
        elif a.curr_cap >= float(variables.fax):
            fax.append(a)
        elif a.curr_cap < float(variables.fax):
            poor.append(a)

    if len(fax) != 0:
        sorted_fax = sorted(fax, key=lambda a: a.curr_cap)
        fair_av_cap = sum(map(lambda x: x.curr_cap, fax)) / len(fax)
        procent_fair = len(fax) / len(pv.A_ACTIVITY)

    if len(poor) != 0:
        sorted_poor = sorted(poor, key=lambda a: a.curr_cap)
        poorest_cap = sorted_poor[0].curr_cap
        poorest_A_id = sorted_poor[0].id
        poorest_glob_id = sorted_poor[0].glob_id
        poorest_av_cap = sum(map(lambda x: x.curr_cap, poor)) / len(poor)
        procent_poorest = len(poor) / len(pv.A_ACTIVITY)

    if len(rich) != 0:
        sorted_rich = sorted(rich, key=lambda a: a.curr_cap, reverse=True)
        richest_cap = sorted_rich[0].curr_cap
        richest_A_id = sorted_rich[0].id
        richest_glob_id = sorted_rich[0].glob_id
        richest_av_cap = sum(map(lambda x: x.curr_cap, rich)) / len(rich)
        procent_richest = len(rich) / len(pv.A_ACTIVITY)


    with open('results.txt', 'a') as f:
        print("   "+str(iteration) + "   " + str(poorest_cap) + "        " + str(poorest_A_id) + "        " + str(poorest_glob_id) +
              "       " + str(richest_cap) + "      " + str(richest_A_id) + "       " + str(richest_glob_id) + "       " +
              str(poorest_av_cap) + "     " +  str(fair_av_cap) + "  " + str(richest_av_cap) + "     " + str(procent_poorest) + "    " + str(procent_fair) + "    " + str(procent_richest), file=f)


def print_debug(variables, pv, iteration):
    with open('debug.txt', 'a') as f:
        print("Iteration: " + str(iteration), file=f)
        print("CA_STATES: " + str(pv.CA_STATES), file=f)
        print("CA_ACTIVE_ABS: " + str(pv.CA_ACTIVE_ABS), file=f)
        print("CELLS_NEIGHBOURS: " + str(pv.cells_neighbors), file=f)
        print("A_PROFILE: ", file=f)
        for a in pv.A_PROFILE:
            print(a, file=f)
        print("B_PROFILE: ", file=f)
        for b in pv.B_PROFILE:
            print(b, file=f)
        print("D_PROFILE: ", file=f)
        for d in pv.D_PROFILE:
            print(d, file=f)
        print("A_ACTIVITY: ", file=f)
        for aa in pv.A_ACTIVITY:
            print(aa, file=f)
        print("B_ACTIVITY: ", file=f)
        for bb in pv.B_ACTIVITY:
            print(bb, file=f)
        print("D_ACTIVITY: ", file=f)
        for dd in pv.D_ACTIVITY:
            print(dd, file=f)
        print("Prob_to_be_ill: " + str(pv.prob_to_be_ill), file=f)

def get_data_for_plot():
    # Definicja ścieżki do pliku
    file_path = 'results.txt'

    # Wczytanie danych z pliku tekstowego, pomijając komentarze i nagłówki
    # df = pd.read_csv(file_path, delim_whitespace=True, comment='#', skiprows=2, header=None)
    df = pd.read_csv(file_path, sep='\s+', comment='#', skiprows=2, header=None)
    # Nazwanie kolumn zgodnie z podanym formatem
    columns = ['iter', 'poorest_CAP', 'A_ID', 'GLOB_ID', 'richest_CAP', 'A_ID2', 'glob_ID2', 'av_cap1', 'av_cap2',
               'av_cap3', '%_of_poor', '%_of_fair', '%_of_rich']
    df.columns = columns

    # Wyciągnięcie kolumn 'av_cap1', 'av_cap2', 'av_cap3'
    av_caps = df[['iter', 'av_cap1', 'av_cap2', 'av_cap3']]

    # Wyświetlenie wyników
    return av_caps





