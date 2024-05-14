import random
from variables import Variables
import dataStructures


def gauss_int(min_value, max_value):
    mean = (max_value + min_value) / 2.0
    std_dev = (max_value - min_value) / 4.0  # Adjust this value as needed
    while True:
        value = int(random.gauss(mean, std_dev))
        if min_value <= value <= max_value:
            return value

def create_rand_CA_STATES(variables, CA_STATES,
                          CA_ACTIVE_ABS, A_PROFILE, A_ACTIVITY,
                          B_PROFILE, B_ACTIVITY, D_PROFILE, D_ACTIVITY):
    # create agents Ai in CA_STATES
    for i in range(1, int(variables.n_of_A)+1):
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
    for j in range(1, int(variables.n_of_B)+1):
        i_ID = random.randint(1, int(variables.m_rows))
        j_ID = random.randint(1, int(variables.n_colls))
        while CA_STATES.board[i_ID][j_ID] != 0:
            i_ID = random.randint(1, int(variables.m_rows))
            j_ID = random.randint(1, int(variables.n_colls))

        numbers = [1, 2, 3]
        probabilities = [variables.B1_p_avoid, variables.B2_p_avoid, variables.B3_p_avoid]
        x = random.choices(numbers, weights=probabilities, k=1)[0]
        if x <= variables.B1_p_avoid:
            CA_STATES.board[i_ID][j_ID] = 3
            glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
            B_PROFILE[j].glob_id = glob_ID
            B_PROFILE[j].type = 3
            B_ACTIVITY[j].glob_id = glob_ID
            B_ACTIVITY[j].type = 3
        elif x <= variables.B1_p_avoid + variables.B2_p_avoid:
            CA_STATES.board[i_ID][j_ID] = 4
            glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
            B_PROFILE[j].glob_id = glob_ID
            B_PROFILE[j].type = 4
            B_ACTIVITY[j].glob_id = glob_ID
            B_ACTIVITY[j].type = 4
        else:
            CA_STATES.board[i_ID][j_ID] = 5
            glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
            B_PROFILE[j].glob_id = glob_ID
            B_PROFILE[j].type = 5
            B_ACTIVITY[j].glob_id = glob_ID
            B_ACTIVITY[j].type = 5
    # create decrease Dk
    for k in range(1, int(variables.n_of_D)+1):
        i_ID = random.randint(1, int(variables.m_rows))
        j_ID = random.randint(1, int(variables.n_colls))
        while CA_STATES.board[i_ID][j_ID] != 0:
            i_ID = random.randint(1, int(variables.m_rows))
            j_ID = random.randint(1, int(variables.n_colls))

        CA_STATES.board[i_ID][j_ID] = 2
        glob_ID = CA_ACTIVE_ABS[i_ID][j_ID]
        D_PROFILE[k].glob_id = glob_ID
        D_ACTIVITY[k].glob_id = glob_ID
    # create profile of agents Ai
    for i in range(1, int(variables.n_of_A)+1):
        A_PROFILE[i].IQ = gauss_int(variables.IQ_range_min, variables.IQ_range_max)
        numbers = [1, 2, 3]
        probabilities = [variables.p_HS1, variables.p_HS2, variables.p_HS3]
        x = random.choices(numbers, weights=probabilities, k=1)[0]
        if x <= variables.p_HS1:
            A_PROFILE[i].Hstate = 1
        elif x <= variables.p_HS1 + variables.p_HS2:
            A_PROFILE[i].Hstate = 2
        else:
            A_PROFILE[i].Hstate = 3
    # accepting business risc probability and mobility probability
    my_id = A_PROFILE[i].IQ
    if my_id <= variables.IQ1_lower:
        A_PROFILE[i].r_acc_B1 = variables.B1_1
        A_PROFILE[i].r_acc_B2 = variables.B2_1
        A_PROFILE[i].r_acc_B3 = variables.B3_1
        A_PROFILE[i].Mobility = variables.p_mob_1
    elif my_id >= variables.IQ3_greater:
        A_PROFILE[i].r_acc_B1 = variables.B1_3
        A_PROFILE[i].r_acc_B2 = variables.B2_3
        A_PROFILE[i].r_acc_B3 = variables.B3_3
        A_PROFILE[i].Mobility = variables.p_mob_3
    else:
        A_PROFILE[i].r_acc_B1 = variables.B1_2
        A_PROFILE[i].r_acc_B2 = variables.B2_2
        A_PROFILE[i].r_acc_B3 = variables.B3_2
        A_PROFILE[i].Mobility = variables.p_mob_2


def iter0(variables):
    CA_STATES = dataStructures.CaStates(variables.m_rows, variables.n_colls)
    A_PROFILE = []
    B_PROFILE = []
    D_PROFILE = []
    A_ACTIVITY = []
    B_ACTIVITY = []
    D_ACTIVITY = []

    MY_NEIGHB = [0] * 8
    CELLS_NEIGHBORS = [[0] * 8 for _ in range(int(variables.m_rows) * int(variables.n_colls))]
    CA_STATES_TEMP = CA_STATES 
    Prob_to_be_ill = [0] * 3

    RAND_NUM = []
    if variables.debug is False:
        RAND_NUM = [random.random() for _ in range(50)]
    elif variables.debug is True:
        with open("Debugging data/RAND_NUM.txt", "r") as file:
            for line in file:
                RAND_NUM.append(float(line.strip()))


    CA_ACTIVE_ABS = [[0] * int(variables.n_colls) for _ in range(int(variables.m_rows))]
    ACTIVE_i_j_ID = [[0] * 2 for _ in range(int(variables.m_rows) * int(variables.n_colls))]

    FREE_SPACE_LOC = [0] * 8

    for i in range(CA_STATES.rows + 1):
        CA_STATES.board[i][0] = -1

    for j in range(CA_STATES.colls + 1):
        CA_STATES.board[0][j] = -1

    A_star = []

    create_rand_CA_STATES(variables, CA_STATES, CA_ACTIVE_ABS, A_PROFILE, A_ACTIVITY, B_PROFILE, B_ACTIVITY, D_PROFILE, D_ACTIVITY)
