init python:
    import random   


    def dragged_func_let_1(dragged_items, dropped_on):
        global ans_fet_o1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_o1_was_dropped = True
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_o1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_2(dragged_items, dropped_on):
        global ans_fet_two1_was_dropped
        global ans_fet_two2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_two1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_two2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_two2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_two1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_3(dragged_items, dropped_on):
        global ans_fet_thr1_was_dropped
        global ans_fet_thr2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_thr1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_thr2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_thr2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_thr1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_5(dragged_items, dropped_on):
        global ans_fet_fv1_was_dropped
        global ans_fet_fv2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_fv1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_fv2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_fv2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_fv1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_8(dragged_items, dropped_on):
        global ans_fet_et1_was_dropped
        global ans_fet_et2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_et1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_et2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_et2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_et1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_12(dragged_items, dropped_on):
        global ans_fet_twv1_was_dropped
        global ans_fet_twv2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_twv1_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_twv2_was_dropped = True
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_twv1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_twv2_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_13(dragged_items, dropped_on):
        global ans_fet_tht1_was_dropped
        global ans_fet_tht2_was_dropped
        global ans_fet_tht3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_tht1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_tht2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_tht3_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_tht3_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_tht2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fet_tht1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_14(dragged_items, dropped_on):
        global ans_fet_ft1_was_dropped
        global ans_fet_ft2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_ft1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_ft2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_ft2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_ft1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_16(dragged_items, dropped_on):
        global ans_fet_sxt1_was_dropped
        global ans_fet_sxt2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_sxt1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_sxt2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_sxt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_sxt1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_17(dragged_items, dropped_on):
        global ans_fet_svt1_was_dropped
        global ans_fet_svt2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_svt1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_svt2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_svt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_svt1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_19(dragged_items, dropped_on):
        global ans_fet_nt1_was_dropped
        global ans_fet_nt2_was_dropped
        global ans_fet_nt3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_nt1_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_nt2_was_dropped = True
                
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
                    ans_fet_nt3_was_dropped = True
        

        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_nt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_nt1_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fet_nt3_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_let_21(dragged_items, dropped_on):
        global ans_fet_twto1_was_dropped
        global ans_fet_twto2_was_dropped
        global ans_fet_twto3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_twto1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_twto2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fet_twto3_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        

        elif dragged_items[0].drag_name != "1_place":  
                    ans_fet_twto3_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fet_twto2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fet_twto1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################