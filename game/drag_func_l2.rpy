init python:
    import random   

    def dragged_func_lt_1(dragged_items, dropped_on):
        global ans_f0_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_h1":

                if dropped_on.drag_name == "h1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f0_was_dropped = True

            if dragged_items[0].drag_name == "answer_p":

                if dropped_on.drag_name == "h1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "h1_place":  # Added check to see if dragged away
                    ans_f0_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lt_2(dragged_items, dropped_on):
        global ans_ft_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_h2":

                if dropped_on.drag_name == "h2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ft_was_dropped = True

            if dragged_items[0].drag_name == "answer_/h2":

                if dropped_on.drag_name == "h2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "h2_place":  # Added check to see if dragged away
                    ans_ft_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lt_7(dragged_items, dropped_on):
        global ans_fs1_was_dropped
        global ans_fs2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_h2":

                if dropped_on.drag_name == "h2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fs1_was_dropped = True

                if dropped_on.drag_name == "/h2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_/h2":

                if dropped_on.drag_name == "h2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "/h2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fs2_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "h2_place":  # Added check to see if dragged away
                    ans_fs1_was_dropped = False
        elif dragged_items[0].drag_name != "/h2_place":  # Added check to see if dragged away
                    ans_fs2_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lt_8(dragged_items, dropped_on):
        global ans_fe1_was_dropped
        global ans_fe2_was_dropped
        global ans_fe3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fe1_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fe2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fe3_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_fe1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_fe2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  # Added check to see if dragged away
                    ans_fe3_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lt_9(dragged_items, dropped_on):
        global ans_fn1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fn1_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_fn1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lt_10(dragged_items, dropped_on):
        global ans_ft01_was_dropped
        global ans_ft02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_01":

                if dropped_on.drag_name == "01_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ft01_was_dropped = True

                if dropped_on.drag_name == "02_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_02":

                if dropped_on.drag_name == "01_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "02_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ft02_was_dropped = True
                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "01_place":  # Added check to see if dragged away
                    ans_ft01_was_dropped = False
        elif dragged_items[0].drag_name != "02_place":  # Added check to see if dragged away
                    ans_ft02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lt_11(dragged_items, dropped_on):
        global ans_fe01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fe01_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_fe01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lt_12(dragged_items, dropped_on):
        global ans_ftw01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ftw01_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ftw01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lt_13(dragged_items, dropped_on):
        global ans_fth01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fth01_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_fth01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lt_15(dragged_items, dropped_on):
        global ans_ffit01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffit01_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_ffit01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################