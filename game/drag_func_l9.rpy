init python:
    import random   


    def dragged_func_lnn_1(dragged_items, dropped_on):
        global ans_fnn_o1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fnn_o1_was_dropped = True
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fnn_o1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################


    def dragged_func_lnn_12(dragged_items, dropped_on):
        global ans_fnn_twv1_was_dropped
        global ans_fnn_twv2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fnn_twv1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fnn_twv2_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_fnn_twv2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_fnn_twv1_was_dropped = False
        renpy.restart_interaction()       


###########################################################################################################################