init python:
    import random   


    def dragged_func_lten_1(dragged_items, dropped_on):
        global ans_ften_o1_was_dropped
        global ans_ften_o2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_o1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_o2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_ften_o2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ften_o1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lten_3(dragged_items, dropped_on):
        global ans_ften_thr1_was_dropped
        global ans_ften_thr2_was_dropped
        global ans_ften_thr3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_thr1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_thr2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_thr3_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_ften_thr3_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ften_thr2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_ften_thr1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lten_4(dragged_items, dropped_on):
        global ans_ften_fr1_was_dropped
        global ans_ften_fr2_was_dropped
        global ans_ften_fr3_was_dropped
        global ans_ften_fr4_was_dropped

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
                    ans_ften_fr1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_fr2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_fr3_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_4":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_fr4_was_dropped = True
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ften_fr3_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ften_fr2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_ften_fr4_was_dropped = False
        elif dragged_items[0].drag_name != "4_place":  
                    ans_ften_fr1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lten_8(dragged_items, dropped_on):
        global ans_ften_et1_was_dropped
        global ans_ften_et2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_et1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_et2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_ften_et2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ften_et1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lten_10(dragged_items, dropped_on):
        global ans_ften_t1_was_dropped
        global ans_ften_t2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_t1_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_t2_was_dropped = True
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_ften_t1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ften_t2_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lten_11(dragged_items, dropped_on):
        global ans_ften_el1_was_dropped
        global ans_ften_el2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_el1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_el2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_ften_el2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ften_el1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lten_13(dragged_items, dropped_on):
        global ans_ften_thtt1_was_dropped
        global ans_ften_thtt2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_thtt1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ften_thtt2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_ften_thtt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ften_thtt1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################