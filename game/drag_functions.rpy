init python:
    import random   

    ######## Ito yung unang gawa ######################

    def dragged_func(dragged_items, dropped_on):
        global p_tag_was_dropped
        global html_tag_was_dropped

        if dropped_on is not None:
            if dragged_items[0].drag_name == "pTag" and dropped_on.drag_name == "pTagPlace":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                dragged_items[0].draggable = False
                p_tag_was_dropped = True
    
            if dragged_items[0].drag_name == "pTag" and dropped_on.drag_name == "hTagPlace":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                dragged_items[0].draggable = False
                p_tag_was_dropped = False
            
            if dragged_items[0].drag_name == "htmlTag" and dropped_on.drag_name == "htmlTagPlace":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                dragged_items[0].draggable = False
                html_tag_was_dropped = True

            renpy.restart_interaction()


###########################################################################################################################


    ########### RANDOMIZER #################        
    
    def choose_random_minigame():
        minigames = ["minigame1"]#, "minigame2", "minigame3"]
        gameNo = random.choice(minigames)
        return renpy.jump(gameNo)
    
    ########### RANDOMIZER #################   


###########################################################################################################################


    def dragged_func_lesson_1(dragged_items, dropped_on):
        global ans_button_lt_dropped

        if dropped_on is not None:

            ########## answer_< ############

            if dragged_items[0].drag_name == "answer_<":

                if dropped_on.drag_name == "<_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_button_lt_dropped = True

                
            ########## answer_> ############

            if dragged_items[0].drag_name == "answer_>" :

                if dropped_on.drag_name == "<_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_gt_lt_dropped = False
                    
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "<_place":  # Added check to see if dragged away
                    ans_button_lt_dropped = False

        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lesson_2(dragged_items, dropped_on):
        global ans_button_was_dropped
        global ans_gt_was_dropped

        if dropped_on is not None:

            ########## button answer ############

            if dragged_items[0].drag_name == "answer_button":

                if dropped_on.drag_name == ">_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                if dropped_on.drag_name == "button_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_button_was_dropped = True

                #elif dragged_items[0].drag_name != "button_place":  # Added check to see if dragged away
                    #ans_button_was_dropped = False
                
            ########## gt answer ############

            if dragged_items[0].drag_name == "answer_>" :

                if dropped_on.drag_name == "button_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                if dropped_on.drag_name == ">_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_gt_was_dropped = True
                    
                #elif dragged_items[0].drag_name != ">_place":  # Added check to see if dragged away
                    #ans_gt_was_dropped = False
        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "button_place":  # Added check to see if dragged away
                    ans_button_was_dropped = False
        elif dragged_items[0].drag_name != ">_place":  # Added check to see if dragged away
                    ans_tg_was_dropped = False

        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lesson_3(dragged_items, dropped_on):
        global ans_fl2_was_dropped

        if dropped_on is not None:

            ########## answer_< ############

            if dragged_items[0].drag_name == "answer_fl2":

                if dropped_on.drag_name == "fl2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fl2_was_dropped = True

                
            ########## answer_> ############

            if dragged_items[0].drag_name == "answer_<" :

                if dropped_on.drag_name == "fl2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_fl2_was_dropped = False
                    
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "fl2_place":  # Added check to see if dragged away
                    ans_fl2_was_dropped = False

        renpy.restart_interaction()

    
###########################################################################################################################


    def dragged_func_lesson_4(dragged_items, dropped_on):
        global ans_btn_was_dropped 
        global ans_img_was_dropped 
        global ans_tp_was_dropped
        global ans_tbl_was_dropped

        if dropped_on is not None:

            ########## answer_btn ############

            if dragged_items[0].drag_name == "answer_btn":

                if dropped_on.drag_name == "btn_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_btn_was_dropped = True
                
                if dropped_on.drag_name == "img_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "tp_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "tbl_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            ########## answer_img ############

            if dragged_items[0].drag_name == "answer_img":

                if dropped_on.drag_name == "btn_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "img_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_img_was_dropped = True

                if dropped_on.drag_name == "tp_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "tbl_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            ########## answer_tp ############

            if dragged_items[0].drag_name == "answer_tp":

                if dropped_on.drag_name == "btn_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "img_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "tp_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_tp_was_dropped = True
                
                if dropped_on.drag_name == "tbl_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            ########## answer_tbl ############

            if dragged_items[0].drag_name == "answer_tbl":

                if dropped_on.drag_name == "btn_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "img_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "tp_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "tbl_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_tbl_was_dropped = True
                    
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "btn_place":  # Added check to see if dragged away
                    ans_btn_was_dropped = False
        elif dragged_items[0].drag_name != "img_place":  # Added check to see if dragged away
                    ans_img_was_dropped = False
        elif dragged_items[0].drag_name != "tp_place":  # Added check to see if dragged away
                    ans_tp_was_dropped = False
        elif dragged_items[0].drag_name != "tbl_place":  # Added check to see if dragged away
                    ans_tbl_was_dropped = False

        renpy.restart_interaction()


###########################################################################################################################        


    def dragged_func_lo_5(dragged_items, dropped_on):
        global ans_html_was_dropped 
        global ans_js_was_dropped 
        global ans_css_was_dropped

        if dropped_on is not None:


            if dragged_items[0].drag_name == "answer_html":

                if dropped_on.drag_name == "html_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_html_was_dropped = True
                
                if dropped_on.drag_name == "js_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "css_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            


            if dragged_items[0].drag_name == "answer_js":

                if dropped_on.drag_name == "html_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "js_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_js_was_dropped = True

                if dropped_on.drag_name == "css_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            


            if dragged_items[0].drag_name == "answer_css":

                if dropped_on.drag_name == "html_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "js_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "css_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_css_was_dropped = True
            
                    
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "html_place":  # Added check to see if dragged away
                    ans_html_was_dropped = False
        elif dragged_items[0].drag_name != "js_place":  # Added check to see if dragged away
                    ans_js_was_dropped = False
        elif dragged_items[0].drag_name != "css_place":  # Added check to see if dragged away
                    ans_css_was_dropped = False
       
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lo_6(dragged_items, dropped_on):
        global ans_btntg_was_dropped
        global ans_like_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_btntg":

                if dropped_on.drag_name == "btntg_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "like_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_btntg_was_dropped = True
            
         
            if dragged_items[0].drag_name == "answer_like":

                if dropped_on.drag_name == "btntg_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_like_was_dropped = True
                
                if dropped_on.drag_name == "like_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                      
                    
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "btntg_place":  # Added check to see if dragged away
                    ans_btntg_was_dropped = False
        elif dragged_items[0].drag_name != "like_place":  # Added check to see if dragged away
                    ans_like_was_dropped = False
       
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lo_7(dragged_items, dropped_on):
        global ans_tgbtn_was_dropped

        if dropped_on is not None:


            if dragged_items[0].drag_name == "answer_btn":

                if dropped_on.drag_name == "tgbtn_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
            if dragged_items[0].drag_name == "answer_/btn":

                if dropped_on.drag_name == "tgbtn_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_tgbtn_was_dropped = True

                    
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "tgbtn_place":  # Added check to see if dragged away
                    ans_tgbtn_was_dropped = False

        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lo_8(dragged_items, dropped_on):
        global ans_comment_was_dropped

        if dropped_on is not None:


            if dragged_items[0].drag_name == "answer_comment":

                if dropped_on.drag_name == "comment_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_comment_was_dropped = True
                

            if dragged_items[0].drag_name == "answer_like":

                if dropped_on.drag_name == "comment_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                    
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "comment_place":  # Added check to see if dragged away
                    ans_comment_was_dropped = False

        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lo_9(dragged_items, dropped_on):
        global ans_ptag_was_dropped
        global ans_ptag2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_p":

                if dropped_on.drag_name == "p_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ptag_was_dropped = True
                if dropped_on.drag_name == "p2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



            if dragged_items[0].drag_name == "answer_p2" :

                if dropped_on.drag_name == "p2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ptag2_was_dropped = True
                if dropped_on.drag_name == "p_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_img" :

                if dropped_on.drag_name == "p2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "p_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "p_place":  # Added check to see if dragged away
                    ans_ptag_was_dropped = False
        elif dragged_items[0].drag_name != "p2_place":  # Added check to see if dragged away
                    ans_ptag2_was_dropped = False

        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lo_10(dragged_items, dropped_on):
        global ans_ft1_was_dropped
        global ans_ft2_was_dropped
        global ans_ft3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_ft1":

                if dropped_on.drag_name == "ft1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ft1_was_dropped = True

                if dropped_on.drag_name == "ft2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "ft3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



            if dragged_items[0].drag_name == "answer_ft2" :

                if dropped_on.drag_name == "ft1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "ft2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ft2_was_dropped = True

                if dropped_on.drag_name == "ft3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



            if dragged_items[0].drag_name == "answer_ft3" :

                if dropped_on.drag_name == "ft1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "ft2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "ft3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ft3_was_dropped = True

            
            if dragged_items[0].drag_name == "answer_ft4" :

                if dropped_on.drag_name == "ft1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "ft2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "ft3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "ft1_place":  # Added check to see if dragged away
                    ans_ft1_was_dropped = False
        elif dragged_items[0].drag_name != "ft2_place":  # Added check to see if dragged away
                    ans_ft2_was_dropped = False
        elif dragged_items[0].drag_name != "ft3_place":  # Added check to see if dragged away
                    ans_ft3_was_dropped = False

        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lo_11(dragged_items, dropped_on):
        global ans_el1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_el1":

                if dropped_on.drag_name == "el1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_el2" :

                if dropped_on.drag_name == "el1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_el1_was_dropped = True
        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "el1_place":  # Added check to see if dragged away
                    ans_el1_was_dropped = False

        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lo_12(dragged_items, dropped_on):
        global ans_t1_was_dropped
        global ans_t2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_t1":

                if dropped_on.drag_name == "t1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_t1_was_dropped = True
                
                if dropped_on.drag_name == "t2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_t2" :

                if dropped_on.drag_name == "t1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                if dropped_on.drag_name == "t2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_t2_was_dropped = True
        
        ########### Check if drop place is empty ############

        elif dragged_items[0].drag_name != "t1_place":  # Added check to see if dragged away
                    ans_t1_was_dropped = False
        elif dragged_items[0].drag_name != "t2_place":  # Added check to see if dragged away
                    ans_t2_was_dropped = False

        renpy.restart_interaction()


###########################################################################################################################