init python:
    import random   


    def dragged_func_lfv_1(dragged_items, dropped_on):
        global ans_ffive_o1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffive_o1_was_dropped = True

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
        
        
        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffive_o1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_2(dragged_items, dropped_on):
        global ans_ffv_two1_was_dropped

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
                    ans_ffv_two1_was_dropped = True
        


        elif dragged_items[0].drag_name != "1_place": 
                    ans_ffv_two1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_3(dragged_items, dropped_on):
        global ans_ffv_the1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_the1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
        


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_the1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_4(dragged_items, dropped_on):
        global ans_ffv_fr1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_fr1_was_dropped = True


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_fr1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_5(dragged_items, dropped_on):
        global ans_ffv_fv1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_fv1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_fv1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_6(dragged_items, dropped_on):
        global ans_ffv_si1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_si1_was_dropped = True


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_si1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_7(dragged_items, dropped_on):
        global ans_ffv_svn1_was_dropped
        global ans_ffv_svn2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_svn1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_svn2_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_svn2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_svn1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_8(dragged_items, dropped_on):
        global ans_ffv_egt1_was_dropped
        global ans_ffv_egt2_was_dropped
        global ans_ffv_egt3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_egt1_was_dropped = True
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_egt1_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_egt1_was_dropped = True


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_egt2_was_dropped = True
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_egt2_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_egt2_was_dropped = True

            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

            if dragged_items[0].drag_name == "answer_4":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_egt3_was_dropped = True
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_egt3_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_egt3_was_dropped = True
                


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_egt1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_egt2_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_ffv_egt3_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_10(dragged_items, dropped_on):
        global ans_ffv_ten1_was_dropped
        global ans_ffv_ten2_was_dropped

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
                    ans_ffv_ten2_was_dropped = True
                    
            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ten1_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ten1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_ten2_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_13(dragged_items, dropped_on):
        global ans_ffv_tht1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_tht1_was_dropped = True


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_tht1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_14(dragged_items, dropped_on):
        global ans_ffv_ft1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ft1_was_dropped = True


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ft1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_15(dragged_items, dropped_on):
        global ans_ffv_fft1_was_dropped
        global ans_ffv_fft2_was_dropped
        global ans_ffv_fft3_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_fft1_was_dropped = True
                
                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_fft2_was_dropped = True
                    
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
                    ans_ffv_fft3_was_dropped = True



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_fft2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_fft1_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_ffv_fft3_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_16(dragged_items, dropped_on):
        global ans_ffv_sixt1_was_dropped
        global ans_ffv_sixt2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_sixt1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_sixt2_was_dropped = True
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_sixt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_sixt1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_17(dragged_items, dropped_on):
        global ans_ffv_sevt1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_sevt1_was_dropped = True
                    
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_sevt1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_18(dragged_items, dropped_on):
        global ans_ffv_eght1_was_dropped
        global ans_ffv_eght2_was_dropped
        global ans_ffv_eght3_was_dropped
        global ans_ffv_eght4_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_eght1_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
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
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_eght2_was_dropped = True

                
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_eght3_was_dropped = True
                
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
                    ans_ffv_eght4_was_dropped = True
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

           



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_eght1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_eght3_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_ffv_eght4_was_dropped = False
        elif dragged_items[0].drag_name != "4_place":  
                    ans_ffv_eght2_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_19(dragged_items, dropped_on):
        global ans_ffv_nnt1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_nnt1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_nnt1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_20(dragged_items, dropped_on):
        global ans_ffv_twt1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_twt1_was_dropped = True



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_twt1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_23(dragged_items, dropped_on):
        global ans_ffv_twth1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_twth1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_twth1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_24(dragged_items, dropped_on):
        global ans_ffv_twtf1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_twtf1_was_dropped = True
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_twtf1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_25(dragged_items, dropped_on):
        global ans_ffv_twtfv1_was_dropped
        global ans_ffv_twtfv2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_twtfv1_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_twtfv2_was_dropped = True
            

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_twtfv1_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_twtfv2_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_27(dragged_items, dropped_on):
        global ans_ffv_twtsv1_was_dropped
        global ans_ffv_twtsv2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_twtsv1_was_dropped = True
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_twtsv2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_twtsv2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_twtsv1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_29(dragged_items, dropped_on):
        global ans_ffv_twtn1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_twtn1_was_dropped = True
            
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_twtn1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_32(dragged_items, dropped_on):
        global ans_ffv_thtt1_was_dropped
        global ans_ffv_thtt2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_thtt1_was_dropped = True
                    

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_thtt2_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_thtt2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_thtt1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_35(dragged_items, dropped_on):
        global ans_ffv_thtfv1_was_dropped

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
                    ans_ffv_thtfv1_was_dropped = True
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_thtfv1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_36(dragged_items, dropped_on):
        global ans_ffv_thtsx1_was_dropped
        global ans_ffv_thtsx2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_thtsx2_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_thtsx1_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    
            
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_thtsx2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_thtsx1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_39(dragged_items, dropped_on):
        global ans_ffv_thtn1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_thtn1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_thtn1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_40(dragged_items, dropped_on):
        global ans_ffv_fty1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_fty1_was_dropped = True

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_fty1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_41(dragged_items, dropped_on):
        global ans_ffv_ftyo1_was_dropped
        global ans_ffv_ftyo2_was_dropped
        global ans_ffv_ftyo3_was_dropped
        global ans_ffv_ftyo4_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftyo1_was_dropped = True
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftyo2_was_dropped = True
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "3_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftyo3_was_dropped = True

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
                
                if dropped_on.drag_name == "4_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftyo4_was_dropped = True
                
                

            
            

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ftyo2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_ftyo3_was_dropped = False
        elif dragged_items[0].drag_name != "3_place":  
                    ans_ffv_ftyo1_was_dropped = False
        elif dragged_items[0].drag_name != "4_place":  
                    ans_ffv_ftyo4_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_42(dragged_items, dropped_on):
        global ans_ffv_ftytw1_was_dropped

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
                    ans_ffv_ftytw1_was_dropped = True

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ftytw1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_43(dragged_items, dropped_on):
        global ans_ffv_ftythr1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftythr1_was_dropped = True

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ftythr1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_44(dragged_items, dropped_on):
        global ans_ffv_ftyfr1_was_dropped
        global ans_ffv_ftyfr2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftyfr1_was_dropped = True 
                    

            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftyfr2_was_dropped = True

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ftyfr2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_ftyfr1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_45(dragged_items, dropped_on):
        global ans_ffv_ftyfv1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftyfv1_was_dropped = True
                
            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ftyfv1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_46(dragged_items, dropped_on):
        global ans_ffv_ftysix1_was_dropped
        global ans_ffv_ftysix2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftysix1_was_dropped = True


            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftysix2_was_dropped = True
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ftysix2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_ftysix1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_48(dragged_items, dropped_on):
        global ans_ffv_ftyet1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                
            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftyet1_was_dropped = True
                    



        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ftyet1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_49(dragged_items, dropped_on):
        global ans_ffv_ftyn1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ftyn1_was_dropped = True
                    

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ftyn1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_50(dragged_items, dropped_on):
        global ans_ffv_ffy1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ffy1_was_dropped = True
                    

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ffy1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_51(dragged_items, dropped_on):
        global ans_ffv_ffyo1_was_dropped
        global ans_ffv_ffyo2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ffyo1_was_dropped = True
            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ffyo2_was_dropped = True
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ffyo2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_ffyo1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_52(dragged_items, dropped_on):
        global ans_ffv_ffyt1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ffyt1_was_dropped = True


            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ffyt1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_53(dragged_items, dropped_on):
        global ans_ffv_ffyth1_was_dropped
        global ans_ffv_ffyth2_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ffyth1_was_dropped = True
            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ffyth2_was_dropped = True
                    
                if dropped_on.drag_name == "2_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ffyth2_was_dropped = False
        elif dragged_items[0].drag_name != "2_place":  
                    ans_ffv_ffyth1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_54(dragged_items, dropped_on):
        global ans_ffv_ffyf1_was_dropped

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
                    ans_ffv_ffyf1_was_dropped = True
                    

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ffyf1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_55(dragged_items, dropped_on):
        global ans_ffv_ffyfv1_was_dropped

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
                    ans_ffv_ffyfv1_was_dropped = True
                    

        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ffyfv1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################


    def dragged_func_lfv_57(dragged_items, dropped_on):
        global ans_ffv_ffysv1_was_dropped

        if dropped_on is not None:

            if dragged_items[0].drag_name == "answer_1":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)

            
            if dragged_items[0].drag_name == "answer_2":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    ans_ffv_ffysv1_was_dropped = True
                    

            if dragged_items[0].drag_name == "answer_3":

                if dropped_on.drag_name == "1_place":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)


        elif dragged_items[0].drag_name != "1_place":  
                    ans_ffv_ffysv1_was_dropped = False
        renpy.restart_interaction()


###########################################################################################################################