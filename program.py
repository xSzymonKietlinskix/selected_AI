import random

from variables import Variables
import dataStructures
import pandas as pd


def set_prob_to_be_ill(variables):
    prob_to_be_ill = []
    prob_to_be_ill.append(variables.p_HS1)
    prob_to_be_ill.append(variables.p_HS2)
    prob_to_be_ill.append(variables.p_HS3)
    return prob_to_be_ill

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

    CA_ACTIVE_ABS = [[0] * int(variables.n_colls) for _ in range(int(variables.m_rows))]
    ACTIVE_i_j_ID = [[0] * 2 for _ in range(int(variables.m_rows) * int(variables.n_colls))]

    FREE_SPACE_LOC = [0] * 8

    for i in range(CA_STATES.rows + 1):
        CA_STATES.board[i][0] = -1

    for j in range(CA_STATES.colls + 1):
        CA_STATES.board[0][j] = -1

    A_star = []

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
        print("Tu funkcja")
    #     generete_A_Profile


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
        print("Tu funkcja")
#     generete_CA

#    generete_D_Profile
#    generete_B_Profile

    Prob_to_be_ill = set_prob_to_be_ill(variables)

    # Calculate A_Activity
    # Calculate B_Activity
    # Calculate D_Activity

    A_star.append(A_ACTIVITY)

    debug_pointer = 1
    CA_STATES_display = [row[1:] for row in CA_STATES.board[1:]]
    return CA_STATES_display

