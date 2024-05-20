import random
import variables

def copy_neighborhood(glob_id, CELLS_NEIGHBORS, CA_STATES_TEMP):
    MY_NEIGHB = [0] * 8
    for m in range(0, 7):
        m_neighb_ID = CELLS_NEIGHBORS[glob_id][m]
        if m_neighb_ID == -1:
            MY_NEIGHB[m] = -1
        else:
            i,j = divmod(m_neighb_ID, int(variables.n_colls))
            MY_NEIGHB[m] = CA_STATES_TEMP.board[i][j]
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


# def find_free_space_neigh(j, free_space, cr_free_space, FREE_SPACE_LOC):
