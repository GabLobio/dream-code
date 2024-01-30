init python:
    import random   


    def dragged_func_lsv_1(dragged_items, dropped_on):
        global ans_fsv_o1_was_dropped
        global ans_fsv_o2_was_dropped
        global ans_fsv_o3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_o1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_o2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_o3_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_o3_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsv_o2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fsv_o1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_2(dragged_items, dropped_on):
        global ans_fsv_t1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_t1_was_dropped = True
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_t1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_3(dragged_items, dropped_on):
        global ans_fsv_thr1_was_dropped
        global ans_fsv_thr2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_thr1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_thr2_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_thr2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsv_thr1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_4(dragged_items, dropped_on):
        global ans_fsv_fr1_was_dropped
        global ans_fsv_fr2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_thr1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_thr2_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_fr1_was_dropped = True
            

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_fr2_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_fr2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsv_fr1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_5(dragged_items, dropped_on):
        global ans_fsv_fv1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_fv1_was_dropped = True

                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_fv1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_10(dragged_items, dropped_on):
        global ans_fsv_ten1_was_dropped
        global ans_fsv_ten2_was_dropped
        global ans_fsv_ten3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_ten1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_ten2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_ten3_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_ten3_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsv_ten2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fsv_ten1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_14(dragged_items, dropped_on):
        global ans_fsv_ft1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_ft1_was_dropped = True
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_ft1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_15(dragged_items, dropped_on):
        global ans_fsv_fft1_was_dropped
        global ans_fsv_fft2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_fft1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_fft2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_fft2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsv_fft1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_18(dragged_items, dropped_on):
        global ans_fsv_et1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_et1_was_dropped = True
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_et1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_19(dragged_items, dropped_on):
        global ans_fsv_nt1_was_dropped
        global ans_fsv_nt2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_nt1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_nt2_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        

        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_nt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsv_nt1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_22(dragged_items, dropped_on):
        global ans_fsv_twtt1_was_dropped
        global ans_fsv_twtt2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_nt1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_twtt1_was_dropped = True
            

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_twtt2_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        

        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_twtt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsv_twtt1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lsv_27(dragged_items, dropped_on):
        global ans_fsv_twts1_was_dropped
        global ans_fsv_twts2_was_dropped
        global ans_fsv_twts3_was_dropped


        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_twts1_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fsv_twts2_was_dropped = True

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
                    ans_fsv_twts3_was_dropped = True



        elif dragged_items[0].drag_name != "1_place":  
                    ans_fsv_twts2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fsv_twts1_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_fsv_twts3_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################