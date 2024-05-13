class CaStates:
    def __init__(self, rows, colls):
        self.rows = int(rows)
        self.colls = int(colls)
        self.board = [[0] * (int(self.colls) + 1)for _ in range((int(self.rows) + 1))]

class AProfile:
    def __init__(self, id, glob_id, IQ, Hstate, r_acc_B1, r_acc_B2, r_acc_B3, Mobility):
        self.Mobility = Mobility
        self.r_acc_B3 = r_acc_B3
        self.r_acc_B2 = r_acc_B2
        self.r_acc_B1 = r_acc_B1
        self.Hstate = Hstate
        self.IQ = IQ
        self.glob_id = glob_id
        self.id = id

class BProfile:
    def __init__(self, id, glob_id, b_type, IC_thr, inv_a, CAP_incr, p_risc):
        self.type = b_type
        self.IC_thr = IC_thr
        self.inv_a = inv_a
        self.CAP_incr = CAP_incr
        self.p_risc = p_risc
        self.glob_id = glob_id
        self.id = id

class DProfile:
    def __init__(self, id, glob_id):
        self.id = id
        self.glob_id = glob_id

class AActivity:
    def __init__(self, id, glob_id, pos_changed, curr_cap, cap_increased, increase_reason, cap_decreased, decrease_reason, d_susp_buisness, crA_of_emerg_hops):
        self.pos_changed = pos_changed
        self.curr_cap = curr_cap
        self.cap_increased = cap_increased
        self.increase_reason = increase_reason
        self.cap_decreased = cap_decreased
        self.decrease_reason = decrease_reason
        self.glob_id = glob_id
        self.id = id
        self.decrease_reason = decrease_reason
        self.d_susp_buisness = d_susp_buisness
        self.crA_of_emerg_hops = crA_of_emerg_hops

class BActivity:
    def __init__(self, id, glob_id, b_type, crB_of_emerg_hops):
        self.type = b_type
        self.crB_of_emerg_hops = crB_of_emerg_hops
        self.glob_id = glob_id
        self.id = id

class DActivity:
    def __init__(self, id, glob_id, crD_of_emerg_hops):
        self.crD_of_emerg_hops = crD_of_emerg_hops
        self.glob_id = glob_id
        self.id = id


