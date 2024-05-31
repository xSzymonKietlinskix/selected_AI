import random
import variables


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
            B_PROFILE[j].type = 3
            B_ACTIVITY[j].glob_id = glob_ID
            B_ACTIVITY[j].type = 3
        elif x == 2:
            CA_STATES.board[i_ID][j_ID] = 4
            glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
            B_PROFILE[j].glob_id = glob_ID
            B_PROFILE[j].type = 4
            B_ACTIVITY[j].glob_id = glob_ID
            B_ACTIVITY[j].type = 4
        elif x == 3:
            CA_STATES.board[i_ID][j_ID] = 5
            glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
            B_PROFILE[j].glob_id = glob_ID
            B_PROFILE[j].type = 5
            B_ACTIVITY[j].glob_id = glob_ID
            B_ACTIVITY[j].type = 5
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


def move_to_free_ca_state(variables, CA_STATES_TEMP, A_or_B_or_D ,A_PROFILE = None, A_ACTIVITY = None, B_PROFILE = None, B_ACTIVITY = None, D_PROFILE = None, D_ACTIVITY = None):
    CA_free_loc_found = False

    while not CA_free_loc_found:
        free_glob_id = random.randint(1, int(variables.m_rows) * int(variables.n_colls))
        i, j = divmod(free_glob_id -1, int(variables.n_colls))
        if CA_STATES_TEMP.board[i + 1][j + 1] == 0:
            CA_free_loc_found = True
            if A_or_B_or_D == "B":
                if B_PROFILE[j].type == 1:
                    code_B = 3
                elif B_PROFILE[j].type == 2:
                    code_B = 4
                else: code_B = 5
                CA_STATES_TEMP.board[i + 1][j + 1] = code_B
                i_id, j_id = divmod(B_ACTIVITY[j].glob_id -1, int(variables.n_colls))
                CA_STATES_TEMP[i_id + 1][j_id + 1] = 0
                B_ACTIVITY[j].glob_id = free_glob_id
                B_ACTIVITY[j].crB_of_emerg_hops += 1

            elif A_or_B_or_D == "A":
                CA_STATES_TEMP.board[i + 1][j + 1] = 1
                i_id, j_id = divmod(A_ACTIVITY[j].glob_id -1, int(variables.n_colls))
                CA_STATES_TEMP.board[i_id + 1][j_id + 1] = 0
                A_ACTIVITY[j].glob_id = free_glob_id
                A_ACTIVITY[j].crA_of_emerg_hops += 1
                A_ACTIVITY[j].pos_changed = 1

            elif A_or_B_or_D == "D":
                CA_STATES_TEMP.board[i+1][j+1] = 2
                i_id, j_id = divmod(D_ACTIVITY[j].glob_id -1, int(variables.n_colls))
                CA_STATES_TEMP.board[i_id + 1][j_id + 1] = 0
                D_ACTIVITY[j].glob_id = free_glob_id
                D_ACTIVITY[j].crD_of_emerg_hops += 1


def move_rand_neighb_loc(j, cr_free_space, debug_pointer, RAND_NUM, variables, FREE_SPACE_LOC, A_or_B_or_D, CA_STATES_TEMP, A_PROFILE = None, A_ACTIVITY = None, B_PROFILE = None, B_ACTIVITY = None, D_PROFILE = None, D_ACTIVITY = None):
    if variables.debug is True:
        x = RAND_NUM[debug_pointer]
        if debug_pointer == 50:
            debug_pointer = 1
        else:
            debug_pointer += 1
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
        code_B = int(B_PROFILE[j].type) + 2
        i_id, j_id = divmod(new_glob_id - 1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_id + 1][j_id + 1] = code_B
        i_old, j_old = divmod(B_ACTIVITY[j].glob_id - 1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_old + 1][j_old + 1] = 0
        B_ACTIVITY[j].glob_id = new_glob_id

    elif A_or_B_or_D == "D":
        i_id, j_id = divmod(new_glob_id -1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_id + 1][j_id + 1] = 2
        i_old, j_old = divmod(D_ACTIVITY[j].glob_id -1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_old + 1][j_old + 1] = 0
        D_ACTIVITY[j].glob_id = new_glob_id

    elif A_or_B_or_D == "A":
        i_id, j_id = divmod(new_glob_id - 1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_id + 1][j_id + 1] = 1
        i_old, j_old = divmod(A_ACTIVITY[j].glob_id -1, int(variables.n_colls))
        CA_STATES_TEMP.board[i_old + 1][j_old + 1] = 0
        A_ACTIVITY[j].glob_id = new_glob_id


