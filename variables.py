import random


class Variables:
    def __init__(self):
        self.m_rows = 0
        self.n_colls = 0
        self.n_of_A = 0
        self.n_of_D = 0
        self.n_of_B = 0
        self.n_of_iter = 0
        self.n_of_exper = 0
        self.debug = False
        self.read_CA_states = False
        self.read_A_PROFILE = False
        self.read_RAND_NUM = False
        self.test_1 = False
        self.test_2 = False
        self.test_3 = False
        self.clock_seed = False
        self.custom_seed = False
        self.seed_value = 0
        self.init_capitIC = 0
        # Parameters of A
        self.IQ_range_min = 0
        self.IQ_range_max = 0
        self.p_HS1 = 0
        self.p_HS2 = 0
        self.p_HS3 = 0
        self.p_itl1 = 0
        self.p_itl2 = 0
        self.p_itl3 = 0
        self.iter_susp_B = 0
        self.D_IC_decr_rate = 0
        # RISC ACCEPT LEVEL
        self.IQ1_lower = 0
        self.IQ3_greater = 0
        self.B1_1 = 0
        self.B1_2 = 0
        self.B1_3 = 0
        self.B2_1 = 0
        self.B2_2 = 0
        self.B2_3 = 0
        self.B3_1 = 0
        self.B3_2 = 0
        self.B3_3 = 0
        # MOBILITY
        self.p_mob_1 = 0
        self.p_mob_2 = 0
        self.p_mob_3 = 0
        # BUISNESS TYPE
        self.B1_ICthr = 0
        self.B1_inv_a = 0
        self.B1_gap = 0
        self.B1_p_risc = 0
        self.B1_p_avoid = 0
        self.B2_ICthr = 0
        self.B2_inv_a = 0
        self.B2_gap = 0
        self.B2_p_risc = 0
        self.B2_p_avoid = 0
        self.B3_ICthr = 0
        self.B3_inv_a = 0
        self.B3_gap = 0
        self.B3_p_risc = 0
        self.B3_p_avoid = 0
        # WEALTH THR
        self.power = 0
        self.fax = 0
        self.rich = 0
        # na razie losowe wartości, później trzeba to ulepszyć i generować odpowiednio
        self.board_values = None
