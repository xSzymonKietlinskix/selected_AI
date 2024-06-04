import random

from program import ProgramVar
import functions

def main_fun(variables, pv, iteration):

    def update_A_pos(a_profile, cap_increased, increase_reason, cap_decreased, decrease_reason, cap_not_changed):
        a_profile.cap_increased = cap_increased
        a_profile.increase_reason = increase_reason
        a_profile.cap_decreased = cap_decreased
        a_profile.decrease_reason = decrease_reason
        a_profile.cap_not_changed = cap_not_changed

    for i in range(int(variables.n_of_A)):
        if pv.A_ACTIVITY[i].crA_of_emerg_hops > 0:
            pv.A_ACTIVITY[i].crA_of_emerg_hops = pv.A_ACTIVITY[i].crA_of_emerg_hops - 1
            # activity 3
            continue
        else:
            glob_ID = int(pv.A_PROFILE[i].glob_id)
            MY_NEIGHB = functions.copy_neighborhood(glob_ID, variables, pv.cells_neighbors, pv.ca_states_temp)
            if_deseas = False
            for n in MY_NEIGHB:
                if n == 2:
                    if_deseas = True
                    break
            if if_deseas is True:
                if variables.debug is True:
                    x = pv.RAND_NUM[iteration]
                else:
                    x = random.random()
                H_state = pv.A_PROFILE[i].Hstate
                Prob_ill = pv.prob_to_be_ill[int(H_state) -1]
                if x <= float(Prob_ill):
                    # activity 1
                    pv.A_ACTIVITY[i].crA_of_emerg_hops = int(variables.iter_susp_B)
                    curr_CAP = pv.A_ACTIVITY[i].curr_cap
                    curr_CAP = curr_CAP - (curr_CAP * float(variables.D_IC_decr_rate))
                    pv.A_ACTIVITY[i].curr_cap = curr_CAP
                    update_A_pos(pv.A_ACTIVITY[i], 0, 0, 1, 4, 0)
                #     business suspended
                    continue

            list_of_businesses_glob_id = []
            counter = 0
            for n in MY_NEIGHB:
                if n == 3 or n == 4 or n == 5:
                    pv.A_ACTIVITY[i].glob_id = int(pv.A_ACTIVITY[i].glob_id)
                    if counter == 0:
                        id = pv.A_ACTIVITY[i].glob_id - int(variables.n_colls)
                    elif counter == 1:
                        id = pv.A_ACTIVITY[i].glob_id - int(variables.n_colls) + 1
                    elif counter == 2:
                        id = pv.A_ACTIVITY[i].glob_id + 1
                    elif counter == 3:
                        id = pv.A_ACTIVITY[i].glob_id + int(variables.n_colls) + 1
                    elif counter == 4:
                        id = pv.A_ACTIVITY[i].glob_id + int(variables.n_colls)
                    elif counter == 5:
                        id = pv.A_ACTIVITY[i].glob_id + int(variables.n_colls) - 1
                    elif counter == 6:
                        id = pv.A_ACTIVITY[i].glob_id - 1
                    elif counter == 7:
                        id = pv.A_ACTIVITY[i].glob_id - int(variables.n_colls) - 1

                    list_of_businesses_glob_id.append(id)
                counter += 1

            if len(list_of_businesses_glob_id) == 0:
                # Activity 6
                continue
            else:
                list_of_bus_id = []
                for b in list_of_businesses_glob_id:
                    for bi in pv.B_ACTIVITY:
                        if bi.glob_id == b:
                            list_of_bus_id.append(bi.id)
                            break

                for b in list_of_bus_id:
                    for bi in pv.B_PROFILE:
                        if bi.id == b:
                            if int(pv.A_PROFILE[i].IQ) <= int(variables.IQ1_lower):
                                my_IQ = 1
                            elif int(pv.A_PROFILE[i].IQ) > int(variables.IQ1_lower) and int(pv.A_PROFILE[i].IQ) <= int(variables.IQ3_greater):
                                my_IQ = 2
                            elif int(pv.A_PROFILE[i].IQ) > int(variables.IQ3_greater):
                                my_IQ = 3
                            if variables.debug is True:
                                x = pv.RAND_NUM[iteration]
                            else:
                                x = random.random()
                            if bi.b_type == 1:
                                if pv.A_ACTIVITY[i].curr_cap >= float(variables.B1_ICthr):
                                    if my_IQ == 1:
                                        B1_risc_accept = float(variables.B1_1)
                                    elif my_IQ == 2:
                                        B1_risc_accept = float(variables.B1_2)
                                    elif my_IQ == 3:
                                        B1_risc_accept = float(variables.B1_3)
                                    if x <= B1_risc_accept:
                                        if variables.debug is True:
                                            x = pv.RAND_NUM[iteration]
                                        else:
                                            x = random.random()
                                        if x <= float(variables.B1_p_risc):
                                            invest_cap = float(pv.A_ACTIVITY[i].curr_cap) * float(variables.B1_inv_a)
                                            new_cap = float(pv.A_ACTIVITY[i].curr_cap) - invest_cap
                                            pv.A_ACTIVITY[i].curr_cap = new_cap
                                            update_A_pos(pv.A_ACTIVITY[i], 0, 0, 1, 1, 0)
                                            break
                                        else:
                                            del_cap = float(pv.A_ACTIVITY[i].curr_cap) * float(variables.B1_ICthr)
                                            invest_cap = float(pv.A_ACTIVITY[i].curr_cap) * float(variables.B1_inv_a)
                                            new_cap = float(pv.A_ACTIVITY[i].curr_cap) + del_cap - invest_cap
                                            pv.A_ACTIVITY[i].curr_cap = new_cap
                                            update_A_pos(pv.A_ACTIVITY[i], 1, 1, 0, 0, 0)
                                    #         list_of_bus_id.remove(b)
                                            break
                                    else:
                                        break

                                else:
                                    break
                            elif bi.b_type == 2:
                                if float(pv.A_ACTIVITY[i].curr_cap) >= float(variables.B2_ICthr):
                                    if my_IQ == 1:
                                        B2_risc_accept = float(variables.B2_1)
                                    elif my_IQ == 2:
                                        B2_risc_accept = float(variables.B2_2)
                                    elif my_IQ == 3:
                                        B2_risc_accept = float(variables.B2_3)
                                    if x <= B2_risc_accept:
                                        if variables.debug is True:
                                            x = pv.RAND_NUM[iteration]
                                        else:
                                            x = random.random()
                                        if x <= float(variables.B2_p_risc):
                                            invest_cap = float(pv.A_ACTIVITY[i].curr_cap) * float(variables.B2_inv_a)
                                            new_cap = float(pv.A_ACTIVITY[i].curr_cap) - invest_cap
                                            pv.A_ACTIVITY[i].curr_cap = new_cap
                                            update_A_pos(pv.A_ACTIVITY[i], 0, 0, 1, 1, 0)
                                            break
                                        else:
                                            del_cap = float(pv.A_ACTIVITY[i].curr_cap) * float(variables.B2_ICthr)
                                            invest_cap = float(pv.A_ACTIVITY[i].curr_cap) * float(variables.B2_inv_a)
                                            new_cap = float(pv.A_ACTIVITY[i].curr_cap) + del_cap - invest_cap
                                            pv.A_ACTIVITY[i].curr_cap = new_cap
                                            update_A_pos(pv.A_ACTIVITY[i], 1, 1, 0, 0, 0)
                                    #         list_of_bus_id.remove(b)
                                            break
                                    else:
                                        break

                                else:
                                    break
                            elif bi.b_type == 3:
                                if float(pv.A_ACTIVITY[i].curr_cap) >= float(variables.B3_ICthr):
                                    if my_IQ == 1:
                                        B3_risc_accept = float(variables.B3_1)
                                    elif my_IQ == 2:
                                        B3_risc_accept = float(variables.B3_2)
                                    elif my_IQ == 3:
                                        B3_risc_accept = float(variables.B3_3)
                                    if x <= B3_risc_accept:
                                        if variables.debug is True:
                                            x = pv.RAND_NUM[iteration]
                                        else:
                                            x = random.random()
                                        if x <= variables.B3_p_risc:
                                            invest_cap = float(pv.A_ACTIVITY[i].curr_cap) * float(variables.B3_inv_a)
                                            new_cap = float(pv.A_ACTIVITY[i].curr_cap) - invest_cap
                                            pv.A_ACTIVITY[i].curr_cap = new_cap
                                            update_A_pos(pv.A_ACTIVITY[i], 0, 0, 1, 1, 0)
                                            break
                                        else:
                                            del_cap = float(pv.A_ACTIVITY[i].curr_cap) * float(variables.B3_ICthr)
                                            invest_cap = float(pv.A_ACTIVITY[i].curr_cap) * float(variables.B3_inv_a)
                                            new_cap = float(pv.A_ACTIVITY[i].curr_cap) + del_cap - invest_cap
                                            pv.A_ACTIVITY[i].curr_cap = new_cap
                                            update_A_pos(pv.A_ACTIVITY[i], 1, 1, 0, 0, 0)
                                            #         list_of_bus_id.remove(b)
                                            break
                                    else:
                                        break

                                else:
                                    break
                        break
        FREE_SPACE_LOC, free_space, cr_free_space = functions.find_free_space_neigh(glob_ID - 1, MY_NEIGHB,
                                                                                pv.cells_neighbors)
        #    if debug then debug.txt print
        if free_space:
            functions.move_rand_neighb_loc(i, cr_free_space, pv.debug_pointer, pv.RAND_NUM, variables, FREE_SPACE_LOC,
                                           "A", pv.ca_states_temp, A_PROFILE=pv.A_PROFILE, A_ACTIVITY=pv.A_ACTIVITY)
            #    if debug then debug.txt print
        else:
            functions.move_to_free_ca_state(variables, pv.ca_states_temp, "A", A_PROFILE=pv.A_PROFILE,
                                            A_ACTIVITY=pv.A_ACTIVITY)

        print("Kapitał: ", pv.A_ACTIVITY[i].curr_cap)
    # end of processing of Ai




    for j in range(int(variables.n_of_B)):
        glob_ID = pv.B_PROFILE[j].glob_id
        i_id, j_id = divmod(glob_ID, int(variables.n_colls))
        MY_NEIGHB = functions.copy_neighborhood(glob_ID, variables, pv.cells_neighbors, pv.ca_states_temp)
        FREE_SPACE_LOC, free_space, cr_free_space = functions.find_free_space_neigh(glob_ID - 1, MY_NEIGHB, pv.cells_neighbors)
        #    if debug then debug.txt print
        if free_space:
            functions.move_rand_neighb_loc(j, cr_free_space, pv.debug_pointer, pv.RAND_NUM, variables, FREE_SPACE_LOC, "B", pv.ca_states_temp, B_PROFILE=pv.B_PROFILE, B_ACTIVITY=pv.B_ACTIVITY)
            #    if debug then debug.txt print
        else:
            functions.move_to_free_ca_state(variables, pv.ca_states_temp, "B", B_PROFILE=pv.B_PROFILE, B_ACTIVITY=pv.B_ACTIVITY)

    for k in range(int(variables.n_of_D)):
        glob_ID = pv.D_PROFILE[k].glob_id
        MY_NEIGHB = functions.copy_neighborhood(glob_ID, variables, pv.cells_neighbors, pv.ca_states_temp)
        FREE_SPACE_LOC, free_space, cr_free_space = functions.find_free_space_neigh(glob_ID - 1, MY_NEIGHB, pv.cells_neighbors)

    #    if debug then debug.txt print

        if free_space:
            functions.move_rand_neighb_loc(k, cr_free_space, pv.debug_pointer, pv.RAND_NUM, variables, FREE_SPACE_LOC, "D", pv.ca_states_temp, D_PROFILE=pv.D_PROFILE, D_ACTIVITY=pv.D_ACTIVITY)
            #    if debug then debug.txt print
        else:
            functions.move_to_free_ca_state(variables, pv.ca_states_temp, "D", D_PROFILE=pv.D_PROFILE, D_ACTIVITY=pv.D_ACTIVITY)

    pv.CA_STATES = pv.ca_states_temp
    CA_STATES_display = [row[1:] for row in pv.CA_STATES.board[1:]]
    return CA_STATES_display, variables, pv