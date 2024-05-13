import random

from variables import Variables
import dataStructures
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

