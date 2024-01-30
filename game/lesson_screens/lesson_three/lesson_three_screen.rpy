screen error_msg():
    image "images/transparent_bg.png"
        
    text "Error!!!" size 28 color "#4E4E4E" xpos 990 ypos 215 xoffset 6 yoffset 6
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"
        action Return()


###########################################################################################################################


default ans_f3o01_was_dropped = False
screen lesson_three_ls1_fill():
    image "images/lesson_three/Lesson 3.1.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3o01_was_dropped:
            action Jump("lessonThreeFillTwo") 
        else:
            action Jump("if_lth1_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("comment_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th1")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 
    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_1
            text " # " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 430
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_1
            text " <!-- " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 190 
            ypos 380
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################    


default ans_f3t01_was_dropped = False
default ans_f3t02_was_dropped = False
screen lesson_three_ls2_fill():
    image "images/lesson_three/Lesson 3.2.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3t01_was_dropped and ans_f3t02_was_dropped:
            action Jump("lessonThreeFillThree") 
        else:
            action Jump("if_lth2_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("comment_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th2")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_2
            text " <!-- " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 450
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_2
            text " --> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 190 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)
        
        drag:
            xpos 750 
            ypos 380
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################  


screen lesson_three_ls3_fill():
    image "images/lesson_three/lesson 3.3.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("llt_when_run") 


########################################################################################################################### 


default ans_f3f01_was_dropped = False
default ans_f3f02_was_dropped = False
screen lesson_three_ls4_fill():
    image "images/lesson_three/Lesson 3.4.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3f01_was_dropped and ans_f3f02_was_dropped:
            action Jump("lessonThreeFillFive") 
        else:
            action Jump("if_lth4_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("comment_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th4")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_4
            text " <!-- " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 450
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_4
            text " --> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 190 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)
        
        drag:
            xpos 680 
            ypos 380
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


########################################################################################################################### 


screen lesson_three_ls5_fill():
    image "images/lesson_three/lesson 3.5.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("lthf_when_run") 


###########################################################################################################################


screen lesson_three_ls6_fill():
    image "images/lesson_three/lesson 3.6.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("lths_when_run") 


###########################################################################################################################


default ans_f3e01_was_dropped = False
screen lesson_three_ls8_fill():
    image "images/lesson_three/Lesson 3.8.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3e01_was_dropped:
            action Jump("lessonThreeFillNine") 
        else:
            action Jump("if_lth8_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("comment_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th8")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_8
            text "<enter>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 530
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_8
            text "<br>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 510 
            ypos 380
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,60)


###########################################################################################################################


screen lesson_three_ls9_fill():
    image "images/lesson_three/lesson 3.9.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("lthn_when_run") 


###########################################################################################################################s


default ans_f3tw01_was_dropped = False
screen lesson_three_ls12_fill():
    image "images/lesson_three/Lesson 3.12.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3tw01_was_dropped:
            action Jump("lessonCommentTakeaways") 
        else:
            action Jump("if_lth12_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("comment_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th12")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_12
            text " br " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 460
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_12
            text " /p " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 450 
            ypos 380
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,60)


###########################################################################################################################


default ans_f3th01_was_dropped = False
default ans_f3th02_was_dropped = False
screen lesson_three_ls13_fill():
    image "images/lesson_three/Lesson 3.13.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3th01_was_dropped and ans_f3th02_was_dropped:
            action Jump("lessonThreeFillFourteen") 
        else:
            action Jump("if_lth13_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("standards_best_practices_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th13")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_13
            text "Collaboration" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 660
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_13
            text "Compatible" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 390 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,60)

        drag:
            xpos 450 
            ypos 475
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,60)


###########################################################################################################################


default ans_f3ft01_was_dropped = False
screen lesson_three_ls14_fill():
    image "images/lesson_three/Lesson 3.14.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3ft01_was_dropped:
            action Jump("lessonThreeFillFifteen") 
        else:
            action Jump("if_lth14_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("standards_best_practices_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th14")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_14
            text "<tail>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 490
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_14
            text "<body>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 180 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,60)


###########################################################################################################################


default ans_f3fit01_was_dropped = False
default ans_f3fit02_was_dropped = False
screen lesson_three_ls15_fill():
    image "images/lesson_three/Lesson 3.15.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3fit01_was_dropped and ans_f3fit02_was_dropped:
            action Jump("lessonThreeFillSixteen") 
        else:
            action Jump("if_lth15_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("standards_best_practices_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th15")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_15
            text "</body>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 530
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_15
            text "<body>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 170 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,60)
        
        drag:
            xpos 170 
            ypos 520
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,60)


###########################################################################################################################


default ans_f3sit01_was_dropped = False
default ans_f3sit02_was_dropped = False
default ans_f3sit03_was_dropped = False
screen lesson_three_ls16_fill():
    image "images/lesson_three/Lesson 3.16.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3sit01_was_dropped and ans_f3sit02_was_dropped and ans_f3sit03_was_dropped:
            action Jump("lessonThreeFillSeventeen") 
        else:
            action Jump("if_lth16_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("standards_best_practices_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th16")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_16
            text "</body>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 530
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_16
            text "<body>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 690
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lth_16
            text "<p>The content of the page</p> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 170 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(301,60)
        
        drag:
            xpos 170 
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(301,60)

        drag:
            xpos 170 
            ypos 470
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(301,60)


###########################################################################################################################


default ans_f3set01_was_dropped = False
screen lesson_three_ls17_fill():
    image "images/lesson_three/Lesson 3.17.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3set01_was_dropped:
            action Jump("lessonThreeFillEighteen") 
        else:
            action Jump("if_lth17_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("standards_best_practices_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th17")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_17
            text "/tail" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 490
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_17
            text "body" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 200 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,60)


###########################################################################################################################


default ans_f3nit01_was_dropped = False
default ans_f3nit02_was_dropped = False
screen lesson_three_ls19_fill():
    image "images/lesson_three/Lesson 3.19.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3nit01_was_dropped and ans_f3nit02_was_dropped:
            action Jump("lessonThreeFillTwenty") 
        else:
            action Jump("if_lth19_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("standards_best_practices_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th19")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_19
            text "<head>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 590
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_19
            text "</body>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 170 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(131,60)
        
        drag:
            xpos 170 
            ypos 615
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(131,60)


###########################################################################################################################


default ans_f3twt01_was_dropped = False
default ans_f3twt02_was_dropped = False
screen lesson_three_ls20_fill():
    image "images/lesson_three/Lesson 3.20.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3twt01_was_dropped and ans_f3twt02_was_dropped:
            action Jump("lessonThreeFillTwentyOne") 
        else:
            action Jump("if_lth20_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("standards_best_practices_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th20")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_20
            text "<head>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 530
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_20
            text "</head>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 170 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(131,60)
        
        drag:
            xpos 170 
            ypos 520
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(131,60)


###########################################################################################################################


default ans_f3twet01_was_dropped = False
default ans_f3twet02_was_dropped = False
screen lesson_three_ls21_fill():
    image "images/lesson_three/Lesson 3.21.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3twet01_was_dropped and ans_f3twet01_was_dropped:
            action Jump("lessonThreeFillTwentyTwo") 
        else:
            action Jump("if_lth21_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("standards_best_practices_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th21")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_21
            text "<head>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 530
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_21
            text "<body>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 170 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(131,60)
        
        drag:
            xpos 170 
            ypos 520
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(131,60)


###########################################################################################################################


screen lesson_three_ls22_fill():
    image "images/lesson_three/lesson 3.22.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("lth22_when_run") 


###########################################################################################################################


screen lesson_three_ls23_fill():
    image "images/lesson_three/lesson 3.23.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("lth23_when_run") 


###########################################################################################################################


screen lesson_three_ls24_fill():
    image "images/lesson_three/lesson 3.24.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("lth24_when_run") 


###########################################################################################################################


default ans_f3twef01_was_dropped = False
default ans_f3twef02_was_dropped = False
screen lesson_three_ls24_fill():
    image "images/lesson_three/Lesson 3.24.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_f3twef01_was_dropped and ans_f3twef02_was_dropped:
            action Jump("lessoThreeOutro") 
        else:
            action Jump("if_lth24_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("standards_best_practices_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_th24")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 310
            ypos 785    
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lth_24
            text " Indented code " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 310
            ypos 830
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lth_24
            text " Code organized into different lines" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 310
            ypos 880
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lth_24
            text " Spaces" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 170 
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(300,60)
        
        drag:
            xpos 170 
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(300,60)


###########################################################################################################################