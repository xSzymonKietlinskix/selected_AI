from program import ProgramVar
import functions

def main_fun(variables, pv):
    for iter in range(int(variables.n_of_iter)):
        for i in range(int(variables.n_of_A)):
            print("To be done!")
        # end of processing of Ai

        for i in range(int(variables.n_of_B)):
            print("To be done!")

        pv = ProgramVar(pv)
        for k in range(int(variables.n_of_D)):
            glob_ID = pv.D_PROFILE[k].glob_id
            MY_NEIGHB = functions.copy_neighborhood(glob_ID, pv.cells_neighbors, pv.ca_states_temp)
            FREE_SPACE_LOC, free_space, cr_free_space = functions.find_free_space_neigh(k, MY_NEIGHB, pv.cells_neighbors)

        #    if debug then debug.txt print

            if free_space:
                functions.move_rand_neighb_loc(k, cr_free_space, pv.debug_pointer, pv.RAND_NUM, variables, FREE_SPACE_LOC, "D", pv.ca_states_temp, D_PROFILE=pv.D_PROFILE, D_ACTIVITY=pv.D_ACTIVITY)
                #    if debug then debug.txt print
            else:
                functions.move_to_free_ca_state(variables, pv.ca_states_temp, "D", D_PROFILE=pv.D_PROFILE, D_ACTIVITY=pv.D_ACTIVITY)
        