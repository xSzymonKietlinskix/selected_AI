from program import ProgramVar
import functions

def main_fun(variables, pv):
    for i in range(int(variables.n_of_A)):
        print("To be done!")
    # end of processing of Ai
    for j in range(int(variables.n_of_B)):
        glob_ID = pv.B_PROFILE[j].glob_id
        i_id, j_id = divmod(glob_ID, int(variables.n_colls))
        MY_NEIGHB = functions.copy_neighborhood(glob_ID, variables, pv.cells_neighbors, pv.ca_states_temp)
        FREE_SPACE_LOC, free_space, cr_free_space = functions.find_free_space_neigh(j, MY_NEIGHB, pv.cells_neighbors)
        #    if debug then debug.txt print
        if free_space:
            functions.move_rand_neighb_loc(j, cr_free_space, pv.debug_pointer, pv.RAND_NUM, variables, FREE_SPACE_LOC, "B", pv.ca_states_temp, B_PROFILE=pv.B_PROFILE, B_ACTIVITY=pv.B_ACTIVITY)
            #    if debug then debug.txt print
        else:
            functions.move_to_free_ca_state(variables, pv.ca_states_temp, "B", B_PROFILE=pv.B_PROFILE, B_ACTIVITY=pv.B_ACTIVITY)

    for k in range(int(variables.n_of_D)):
        glob_ID = pv.D_PROFILE[k].glob_id
        MY_NEIGHB = functions.copy_neighborhood(glob_ID, variables, pv.cells_neighbors, pv.ca_states_temp)
        FREE_SPACE_LOC, free_space, cr_free_space = functions.find_free_space_neigh(k, MY_NEIGHB, pv.cells_neighbors)

    #    if debug then debug.txt print

        if free_space:
            functions.move_rand_neighb_loc(k, cr_free_space, pv.debug_pointer, pv.RAND_NUM, variables, FREE_SPACE_LOC, "D", pv.ca_states_temp, D_PROFILE=pv.D_PROFILE, D_ACTIVITY=pv.D_ACTIVITY)
            #    if debug then debug.txt print
        else:
            functions.move_to_free_ca_state(variables, pv.ca_states_temp, "D", D_PROFILE=pv.D_PROFILE, D_ACTIVITY=pv.D_ACTIVITY)

    pv.CA_STATES = pv.ca_states_temp
    CA_STATES_display = [row[1:] for row in pv.CA_STATES.board[1:]]
    return CA_STATES_display