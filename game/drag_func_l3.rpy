init python:
    import random
###########################################################################################################################


    def dragged_func_lth_1(dragged_items, dropped_on):
        global ans_f3o01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3o01_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3o01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_2(dragged_items, dropped_on):
        global ans_f3t01_was_dropped
        global ans_f3t02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":
                
                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3t01_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3t02_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3t01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3t02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_4(dragged_items, dropped_on):
        global ans_f3f01_was_dropped
        global ans_f3f02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":
                
                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3f01_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3f02_was_dropped = True

                
        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3f01_was_dropped = False

        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3f02_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_7(dragged_items, dropped_on):
        global ans_f3s01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3s01_was_dropped = True


                
        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3s01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_8(dragged_items, dropped_on):
        global ans_f3e01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3e01_was_dropped = True


                
        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3e01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_10(dragged_items, dropped_on):
        global ans_f3te01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3te01_was_dropped = True

            if dragged_items[0].drag_name == "answer_3":
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3te01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_12(dragged_items, dropped_on):
        global ans_f3tw01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3tw01_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3tw01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_13(dragged_items, dropped_on):
        global ans_f3th01_was_dropped
        global ans_f3th02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3th01_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3th02_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3th02_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3th01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_14(dragged_items, dropped_on):
        global ans_f3ft01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3ft01_was_dropped = True

        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3ft01_was_dropped = False
                    
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_15(dragged_items, dropped_on):
        global ans_f3fit01_was_dropped
        global ans_f3fit02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3fit01_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3fit02_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3fit02_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3fit01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_16(dragged_items, dropped_on):
        global ans_f3sit01_was_dropped
        global ans_f3sit02_was_dropped
        global ans_f3sit03_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3sit01_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3sit02_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3sit03_was_dropped = True

                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                    

        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3sit02_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3sit03_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  # Added check to see if dragged away
                    ans_f3sit01_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_17(dragged_items, dropped_on):
        global ans_f3set01_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3set01_was_dropped = True

        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3set01_was_dropped = False
                    
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_18(dragged_items, dropped_on):
        global ans_f3egt01_was_dropped

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
                    ans_f3egt01_was_dropped = True
        

        
        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3egt01_was_dropped = False
                    
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_19(dragged_items, dropped_on):
        global ans_f3nit01_was_dropped
        global ans_f3nit02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3nit01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3nit02_was_dropped = True
        

        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3nit01_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3nit02_was_dropped = False
                    
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_20(dragged_items, dropped_on):
        global ans_f3twt01_was_dropped
        global ans_f3twt02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3twt01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3twt02_was_dropped = True
        

        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3twt01_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3twt02_was_dropped = False
                    
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_21(dragged_items, dropped_on):
        global ans_f3twet01_was_dropped
        global ans_f3twet02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3twet01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3twet02_was_dropped = True
        

        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3twet01_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3twet02_was_dropped = False
                    
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lth_24(dragged_items, dropped_on):
        global ans_f3twef01_was_dropped
        global ans_f3twef02_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3twef01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3twef02_was_dropped = True
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3twef01_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_f3twef02_was_dropped = True

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        

        ########### Check if drop place is empty ############
        elif dragged_items[0].drag_name != "1_place":  # Added check to see if dragged away
                    ans_f3twef01_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  # Added check to see if dragged away
                    ans_f3twef02_was_dropped = False
                    
        renpy.restart_interaction()


###########################################################################################################################