init python:
    import random   


    def dragged_func_lf_2(dragged_items, dropped_on):
        global ans_ff_o1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_o1_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_o1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_3(dragged_items, dropped_on):
        global ans_ff_th01_was_dropped
        global ans_ff_th02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_th01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_th02_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_th01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_th02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_4(dragged_items, dropped_on):
        global ans_ff_fr01_was_dropped
        global ans_ff_fr02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_fr01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_fr02_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_fr01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_fr02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_5(dragged_items, dropped_on):
        global ans_ff_fv01_was_dropped
        global ans_ff_fv02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_fv01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_fv02_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_fv01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_fv02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_6(dragged_items, dropped_on):
        global ans_ff_sx01_was_dropped
        global ans_ff_sx02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_sx01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_sx02_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_sx01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_sx02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_9(dragged_items, dropped_on):
        global ans_ff_nn01_was_dropped
        global ans_ff_nn02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_nn01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_nn02_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_nn01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_nn02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_11(dragged_items, dropped_on):
        global ans_ff_el01_was_dropped
        global ans_ff_el02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_el01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_el02_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_el01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_el02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_13(dragged_items, dropped_on):
        global ans_ff_tt01_was_dropped
        global ans_ff_tt02_was_dropped
        global ans_ff_tt03_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tt01_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tt02_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tt03_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_tt01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_tt02_was_dropped = False
        
        elif dragged_items[0].drag_name != "3_place":  # Added check to see if dragged away
                    ans_ff_tt03_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_14(dragged_items, dropped_on):
        global ans_ff_ft01_was_dropped
        global ans_ff_ft02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_ft01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_ft02_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_ft01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_ft02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################

    def dragged_func_lf_16(dragged_items, dropped_on):
        global ans_ff_st01_was_dropped
        global ans_ff_st02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_st01_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_st02_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_st02_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_st01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_17(dragged_items, dropped_on):
        global ans_ff_svt01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_svt01_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_svt01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_18(dragged_items, dropped_on):
        global ans_ff_egt01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_egt01_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_egt01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_19(dragged_items, dropped_on):
        global ans_ff_nt01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_nt01_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_nt01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_20(dragged_items, dropped_on):
        global ans_ff_tw01_was_dropped
        global ans_ff_tw02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tw02_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tw01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_tw01_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_tw02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_21(dragged_items, dropped_on):
        global ans_ff_two01_was_dropped
        global ans_ff_two02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_two02_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_two01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_two01_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_two02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_22(dragged_items, dropped_on):
        global ans_ff_twt01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_twt01_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_twt01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_25(dragged_items, dropped_on):
        global ans_ff_tf01_was_dropped
        global ans_ff_tf02_was_dropped
        global ans_ff_tf03_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tf01_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tf02_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tf03_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_tf02_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_tf01_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  # Added check to see if dragged away
                    ans_ff_tf03_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_26(dragged_items, dropped_on):
        global ans_ff_ts01_was_dropped
        global ans_ff_ts02_was_dropped
        global ans_ff_ts03_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_ts01_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_ts02_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_ts03_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_ts01_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_ts02_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  # Added check to see if dragged away
                    ans_ff_ts03_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_27(dragged_items, dropped_on):
        global ans_ff_twts01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_twts01_was_dropped = True
                    

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_twts01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_28(dragged_items, dropped_on):
        global ans_ff_twte01_was_dropped
        global ans_ff_twte02_was_dropped
        global ans_ff_twte03_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_twte01_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_twte02_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_twte03_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_twte01_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_twte02_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  # Added check to see if dragged away
                    ans_ff_twte03_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_29(dragged_items, dropped_on):
        global ans_ff_twtn01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_twtn01_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_twtn01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_30(dragged_items, dropped_on):
        global ans_ff_tht01_was_dropped 
        global ans_ff_tht02_was_dropped
        global ans_ff_tht03_was_dropped
        global ans_ff_tht04_was_dropped 

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tht01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "5_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tht02_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "5_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tht03_was_dropped = True
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "5_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_4":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_tht04_was_dropped = True
                
                if dropped_on.drag_name == "5_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_tht01_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_tht02_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  # Added check to see if dragged away
                    ans_ff_tht03_was_dropped = False
        elif dragged_items[0].drag_name != "4_place":  # Added check to see if dragged away
                    ans_ff_tht04_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_31(dragged_items, dropped_on):
        global ans_ff_thto01_was_dropped 
        global ans_ff_thto02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thto01_was_dropped = True

            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thto02_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_thto02_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_thto01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_33(dragged_items, dropped_on):
        global ans_ff_thtt01_was_dropped 
        global ans_ff_thtt02_was_dropped
        global ans_ff_thtt03_was_dropped 
        global ans_ff_thtt04_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtt01_was_dropped = True

            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtt02_was_dropped = True
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtt03_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_4":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtt04_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_thtt04_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_thtt03_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  # Added check to see if dragged away
                    ans_ff_thtt02_was_dropped = False
        elif dragged_items[0].drag_name != "4_place":  # Added check to see if dragged away
                    ans_ff_thtt01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_34(dragged_items, dropped_on):
        global ans_ff_thtf01_was_dropped 
        global ans_ff_thtf02_was_dropped
        global ans_ff_thtf03_was_dropped 
        global ans_ff_thtf04_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtf01_was_dropped = True

            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtf02_was_dropped = True
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtf03_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_4":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtf04_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_thtf04_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ff_thtf03_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  # Added check to see if dragged away
                    ans_ff_thtf02_was_dropped = False
        elif dragged_items[0].drag_name != "4_place":  # Added check to see if dragged away
                    ans_ff_thtf01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_35(dragged_items, dropped_on):
        global ans_ff_thtfv01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtfv01_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_thtfv01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_36(dragged_items, dropped_on):
        global ans_ff_thtsx01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtsx01_was_dropped = True
            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_thtsx01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_37(dragged_items, dropped_on):
        global ans_ff_thtsv01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thtsv01_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_thtsv01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lf_38(dragged_items, dropped_on):
        global ans_ff_thte01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ff_thte01_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_ff_thte01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################