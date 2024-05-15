import random
import pandas as pd
from variables import Variables
import dataStructures


# NIE GOTOWE
def copy_neighborhood(glob_id, CELLS_NEIGHBORS):
    for m in range(1,8):
        m_neighb_ID = CELLS_NEIGHBORS[glob_id][m]

# NIE GOTOWE, powinno byc jak w folderze CA structs w pdf img001.pdf w prawym dolnym no i prawie jest tlyko gdzieś coś źle sprawdzam xD
def create_cells_neighbors(m, n):
    # Tworzymy pustą macierz o wymiarach m x n
    matrix = [[-1] * 8 for _ in range(m * n)]

    # Funkcja zwracająca sąsiadów danego punktu
    def get_neighbors(point, m, n):
        neighbors = []
        i, j = divmod(point, n)  # Obliczamy indeksy wiersza i kolumny dla danego punktu
        # Sprawdzamy sąsiadów wokół danego punktu, zaczynając od sąsiada powyżej i z lewej strony
        if i-1 > 0:
            neighbors.append((i-1) * n + j)
        else:
            neighbors.append(-2)
        if i-1 > 0 and j + 1 <= n:
            neighbors.append((i - 1) * n + j + 1)
        else:
            neighbors.append(-2)
        if j + 1 <= n:
            neighbors.append((i) * n + j + 1)
        else:
            neighbors.append(-2)
        if i+1 <= m and j+1 <= n:
            neighbors.append((i+1) * n + j + 1)
        else:
            neighbors.append(-2)
        if i+1 <= m:
            neighbors.append((i+1) * n + j)
        else:
            neighbors.append(-2)
        if i+1 <= m and j-1 >= 0:
            neighbors.append((i + 1) * n + j - 1)
        else:
            neighbors.append(-2)
        if j-1 >= 0:
            neighbors.append((i) * n + j - 1)
        else:
            neighbors.append(-2)
        if i+1 <= m and j-1 >= 0:
            neighbors.append((i - 1) * n + j - 1)
        else:
            neighbors.append(-2)
        return neighbors


    # Wypełniamy macierz sąsiadami dla każdego punktu
    for point in range(m * n):
        neighbors = get_neighbors(point, m, n)
        for idx, neighbor in enumerate(neighbors):
            matrix[point][idx] = neighbor + 1

    return matrix
# losowanie z gaussa
def gauss_int(min_value, max_value):
    mean = (max_value + min_value) / 2.0
    std_dev = (max_value - min_value) / 4.0  # Adjust this value as needed
    while True:
        value = int(random.gauss(mean, std_dev))
        if min_value <= value <= max_value:
            return value

# inicjacja A PROFILE
def create_A_profile(variables, A_PROFILE):
    for i in range(0, int(variables.n_of_A)):
        aprof = dataStructures.AProfile(i,0,0,0,0,0,0,0)
        A_PROFILE.append(aprof)
        A_PROFILE[i].IQ = gauss_int(int(variables.IQ_range_min), int(variables.IQ_range_max))
        numbers = [1, 2, 3]
        probabilities = [float(variables.p_HS1), float(variables.p_HS2), float(variables.p_HS3)]
        x = random.choices(numbers, weights=probabilities, k=1)[0]
        if x == 1:
            A_PROFILE[i].Hstate = 1
        elif x == 2:
            A_PROFILE[i].Hstate = 2
        elif x == 3:
            A_PROFILE[i].Hstate = 3
    # accepting business risc probability and mobility probability
    my_id = A_PROFILE[i].IQ
    if my_id <= int(variables.IQ1_lower):
        A_PROFILE[i].r_acc_B1 = float(variables.B1_1)
        A_PROFILE[i].r_acc_B2 = float(variables.B2_1)
        A_PROFILE[i].r_acc_B3 = float(variables.B3_1)
        A_PROFILE[i].Mobility = float(variables.p_mob_1)
    elif my_id >= int(variables.IQ3_greater):
        A_PROFILE[i].r_acc_B1 = float(variables.B1_3)
        A_PROFILE[i].r_acc_B2 = float(variables.B2_3)
        A_PROFILE[i].r_acc_B3 = float(variables.B3_3)
        A_PROFILE[i].Mobility = float(variables.p_mob_3)
    else:
        A_PROFILE[i].r_acc_B1 = float(variables.B1_2)
        A_PROFILE[i].r_acc_B2 = float(variables.B2_2)
        A_PROFILE[i].r_acc_B3 = float(variables.B3_2)
        A_PROFILE[i].Mobility = float(variables.p_mob_2)

# inicjacja B PROFILE
def create_B_profile(variables, B_PROFILE):
    for i in range(0, int(variables.n_of_B)):
        buis = dataStructures.BProfile(i,0,0,0,0,0,0)
        B_PROFILE.append(buis)

# inicjacja D PROFILE
def create_D_profile(variables, D_PROFILE):
    for i in range(0, int(variables.n_of_D)):
        dis = dataStructures.DProfile(i,0)
        D_PROFILE.append(dis)

# Tworzenie tablicy CA
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
def set_prob_to_be_ill(variables):
    prob_to_be_ill = []
    prob_to_be_ill.append(variables.p_HS1)
    prob_to_be_ill.append(variables.p_HS2)
    prob_to_be_ill.append(variables.p_HS3)
    return prob_to_be_ill

def iter0(variables):
    # inicjacja pustych list
    CA_STATES = dataStructures.CaStates(variables.m_rows, variables.n_colls)
    A_PROFILE = []
    B_PROFILE = []
    D_PROFILE = []
    A_ACTIVITY = []
    B_ACTIVITY = []
    D_ACTIVITY = []

    MY_NEIGHB = [0] * 8
    # CELLS_NEIGHBORS = [[0] * 8 for _ in range(int(variables.m_rows) * int(variables.n_colls))]
    CA_STATES_TEMP = CA_STATES 
    Prob_to_be_ill = [0] * 3

    # Inicjacja pustej listy historii
    A_star = []

    # Inicjacja pustej listy liczb losowych
    RAND_NUM = []

    # inicjacja macierzy z globalnymi id
    CA_ACTIVE_ABS = [[-1] * (int(variables.n_colls) + 1) for _ in range((int(variables.m_rows)+1))]
    value = 1
    for i in range(1, len(CA_ACTIVE_ABS)):
        for j in range(1, len(CA_ACTIVE_ABS[0])):
            CA_ACTIVE_ABS[i][j] = value
            value += 1

    # jeszcze nie wiem co to
    ACTIVE_i_j_ID = [[0] * 2 for _ in range(int(variables.m_rows) * int(variables.n_colls))]

    FREE_SPACE_LOC = [0] * 8

    # pierwszy wiersz i pierwsza kolumna planszy równa -1
    for i in range(CA_STATES.rows + 1):
        CA_STATES.board[i][0] = -1

    for j in range(CA_STATES.colls + 1):
        CA_STATES.board[0][j] = -1


    #obsługa zachowań przy opcji debug i bez niej
    if variables.debug is True and variables.read_RAND_NUM is True:
        with open("Debugging data/RAND_NUM.txt", "r") as file:
            for line in file:
                RAND_NUM.append(float(line.strip()))
    else:
        RAND_NUM = [random.random() for _ in range(50)]

    if variables.debug is True and variables.read_A_PROFILE is True:
        df = pd.read_csv('Debugging data/A_PROFILE.txt', delimiter='\s+')
        row = df.iloc[-int(variables.n_of_A):]
        for i in range(1, int(variables.n_of_A) + 1):
            agent = dataStructures.AProfile(row["#1"][i], row["2"][i], row["3"][i], row["4"][i], row["5"][i], row["6"][i], row["7"][i], row["8"][i])
            A_PROFILE.append(agent)
    else:
        create_A_profile(variables, A_PROFILE)

    # tworzenie B i D profile
    create_B_profile(variables, B_PROFILE)
    create_D_profile(variables, D_PROFILE)

    # inicjacja pustych A,B,D activity
    for i in range(len(A_PROFILE)):
        activity = dataStructures.AActivity(i, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        A_ACTIVITY.append(activity)

    for i in range(len(B_PROFILE)):
        activity = dataStructures.BActivity(i, 0, 0, 0)
        B_ACTIVITY.append(activity)

    for i in range(len(D_PROFILE)):
        activity = dataStructures.DActivity(i, 0, 0)
        D_ACTIVITY.append(activity)

    if variables.debug is True and variables.read_CA_states is True:
        board = []
        with open("Debugging data/CA_STATES.txt", "r") as file:
            for line in file:
                row = list(map(int, line.strip().split()))
                board.append(row)
        for i in range(len(board)):
            for j in range(len(board[i])):
                CA_STATES.board[i + 1][j + 1] = board[i][j]
    else:
        create_rand_CA_STATES(variables, CA_STATES, CA_ACTIVE_ABS, A_PROFILE, A_ACTIVITY, B_PROFILE, B_ACTIVITY, D_PROFILE,
                          D_ACTIVITY)


    CELLS_NEIGHBORS = create_cells_neighbors(int(variables.m_rows), int(variables.n_colls))
    print(CELLS_NEIGHBORS)
    Prob_to_be_ill = set_prob_to_be_ill(variables)

    A_star.append(A_ACTIVITY)

    debug_pointer = 1
    # plansza bez pierwszego wiersza i pierwszej kolumny, do wyświetlania w GUI
    CA_STATES_display = [row[1:] for row in CA_STATES.board[1:]]
    return CA_STATES_display

