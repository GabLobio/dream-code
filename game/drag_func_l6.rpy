init python:
    import random   


    def dragged_func_lsx_0(dragged_items, dropped_on):
        global ans_fsx_o1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_o1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_o1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_1(dragged_items, dropped_on):
        global ans_fsx_on1_was_dropped
        global ans_fsx_on2_was_dropped
        global ans_fsx_on3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_on1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_on2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_on3_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_on3_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_on2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fsx_on1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_2(dragged_items, dropped_on):
        global ans_fsx_two1_was_dropped
        global ans_fsx_two2_was_dropped
        global ans_fsx_two3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_two1_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_two2_was_dropped = True
                    

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_two3_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_on3_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_on2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fsx_on1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_3(dragged_items, dropped_on):
        global ans_fsx_thr1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_thr1_was_dropped = True
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_thr1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_8(dragged_items, dropped_on):
        global ans_fsx_et1_was_dropped
        global ans_fsx_et2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_et1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_et2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_et2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_et1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_9(dragged_items, dropped_on):
        global ans_fsx_nn1_was_dropped
        global ans_fsx_nn2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_nn1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_nn2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_nn2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_nn1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_12(dragged_items, dropped_on):
        global ans_fsx_twl1_was_dropped
        global ans_fsx_twl2_was_dropped
        global ans_fsx_twl3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twl1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twl2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twl3_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            
                    
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_twl3_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_twl2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fsx_twl1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_13(dragged_items, dropped_on):
        global ans_fsx_tht1_was_dropped
        global ans_fsx_tht2_was_dropped
        global ans_fsx_tht3_was_dropped
        global ans_fsx_tht4_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_tht1_was_dropped = True
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_tht2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_tht3_was_dropped = True
            
            
            if dragged_items[0].drag_name == "answer_4":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_tht4_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)                  
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_tht4_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_tht2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fsx_tht1_was_dropped = False
        elif dragged_items[0].drag_name != "4_place":  
                    ans_fsx_tht3_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_16(dragged_items, dropped_on):
        global ans_fsx_st1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_st1_was_dropped = True
            

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_st1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_18(dragged_items, dropped_on):
        global ans_fsx_egt1_was_dropped
        global ans_fsx_egt2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_egt1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_egt2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_egt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_egt1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_19(dragged_items, dropped_on):
        global ans_fsx_nt1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_nt1_was_dropped = True
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_nt1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_20(dragged_items, dropped_on):
        global ans_fsx_twt1_was_dropped
        global ans_fsx_twt2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twt1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twt2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_twt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_twt1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_21(dragged_items, dropped_on):
        global ans_fsx_twto1_was_dropped
        global ans_fsx_twto2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twto1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twto2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_twto2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_twto1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_22(dragged_items, dropped_on):
        global ans_fsx_twtt1_was_dropped

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
                    ans_fsx_twtt1_was_dropped = True
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_twtt1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_23(dragged_items, dropped_on):
        global ans_fsx_twth1_was_dropped
        global ans_fsx_twth2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twth2_was_dropped = True
                

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
            

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twth1_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_twth1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_twth2_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_26(dragged_items, dropped_on):
        global ans_fsx_twts1_was_dropped
        global ans_fsx_twts2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twts1_was_dropped = True
                

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twts2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_twts2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_twts1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_27(dragged_items, dropped_on):
        global ans_fsx_twtsv1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_twtsv1_was_dropped = True
            

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_twtsv1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_30(dragged_items, dropped_on):
        global ans_fsx_tty1_was_dropped
        global ans_fsx_tty2_was_dropped
        global ans_fsx_tty3_was_dropped
        global ans_fsx_tty4_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_tty1_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_tty2_was_dropped = True
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_tty3_was_dropped = True
            


            if dragged_items[0].drag_name == "answer_4":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_tty4_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                

                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_tty4_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_tty1_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fsx_tty2_was_dropped = False
        elif dragged_items[0].drag_name != "4_place":  
                    ans_fsx_tty3_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_31(dragged_items, dropped_on):
        global ans_fsx_ttyo1_was_dropped
        global ans_fsx_ttyo2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_ttyo2_was_dropped = True


            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_ttyo1_was_dropped =True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                

                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_ttyo1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_ttyo2_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_32(dragged_items, dropped_on):
        global ans_fsx_ttytw1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_ttytw1_was_dropped = True
                

                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_ttytw1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_34(dragged_items, dropped_on):
        global ans_fsx_ttyfr1_was_dropped
        global ans_fsx_ttyfr2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_ttyfr1_was_dropped = True
            


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_ttyfr2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    


        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_ttyfr2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_ttyfr1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_35(dragged_items, dropped_on):
        global ans_fsx_ttyfv1_was_dropped
        global ans_fsx_ttyfv2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_ttyfv1_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_ttyfv2_was_dropped = True
                

                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_ttyfv1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_ttyfv2_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsx_42(dragged_items, dropped_on):
        global ans_fsx_fttw1_was_dropped
        global ans_fsx_fttw2_was_dropped
        global ans_fsx_fttw3_was_dropped
        global ans_fsx_fttw4_was_dropped

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
                    ans_fsx_fttw1_was_dropped = True

            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_fttw2_was_dropped = True
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_fttw3_was_dropped = True

                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

            if dragged_items[0].drag_name == "answer_4":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsx_fttw4_was_dropped = True
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsx_fttw4_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsx_fttw3_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fsx_fttw2_was_dropped = False
        elif dragged_items[0].drag_name != "4_place":  
                    ans_fsx_fttw1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################