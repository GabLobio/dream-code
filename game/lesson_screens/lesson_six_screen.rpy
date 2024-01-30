
default ans_fsx_o1_was_dropped = False
screen lesson_six_ls0_fill():
    image "images/lesson_six/lesson 6.0.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_o1_was_dropped:
            action Jump("lessonSixFillOne") 
        else:
            action Jump("if_lsx0_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx0")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("drop_down_hint")

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_0
            text "select" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_0
            text "menu" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 630
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_0
            text "list" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 332
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_on1_was_dropped = False
default ans_fsx_on2_was_dropped = False
default ans_fsx_on3_was_dropped = False
screen lesson_six_ls1_fill():
    image "images/lesson_six/lesson 6.1.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_on1_was_dropped and ans_fsx_on2_was_dropped and ans_fsx_on3_was_dropped:
            action Jump("lessonSixFillTwo") 
        else:
            action Jump("if_lsx1_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("drop_down_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx1")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 346
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_1
            text "</option>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 560
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_1
            text "   Opt 2  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 760
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_1
            text "<option>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 418
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 304
            ypos 465
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 389
            ypos 511
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_two1_was_dropped = False
default ans_fsx_two2_was_dropped = False
default ans_fsx_two3_was_dropped = False
screen lesson_six_ls2_fill():
    image "images/lesson_six/lesson 6.2.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_two1_was_dropped and ans_fsx_two2_was_dropped and ans_fsx_two3_was_dropped:
            action Jump("lessonSixFillThree") 
        else:
            action Jump("if_lsx2_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("drop_down_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx2")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 346
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_2
            text "<select>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 520
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_2
            text "</form>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 690
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_2
            text "</select>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 332
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 160
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 160
            ypos 520
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_thr1_was_dropped = False
screen lesson_six_ls3_fill():
    image "images/lesson_six/lesson 6.3.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_thr1_was_dropped:
            action Jump("lessonSixFillFour") 
        else:
            action Jump("if_lsx3_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("drop_down_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx3")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 346
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_3
            text "property" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 520
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_3
            text "name" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 292
            ypos 332
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################

screen lesson_six_ls5_fill():
    image "images/lesson_six/lesson 6.5.webp" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_six_five") 

screen lesson_six_click():
    image "images/lesson_six/lesson_6_5_run.png" 
    


    vbox:
        xpos 1151
        ypos 206
        textbutton "            ":
            style_prefix "my"
            action Jump("lesson_six_clicked") 


###########################################################################################################################


default ans_fsx_et1_was_dropped = False
default ans_fsx_et2_was_dropped = False
screen lesson_six_ls8_fill():
    image "images/lesson_six/lesson 6.8.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_et1_was_dropped and ans_fsx_et2_was_dropped:
            action Jump("lessonSixFillNine") 
        else:
            action Jump("if_lsx8_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("drop_down_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx8")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 346
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_8
            text "</label>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 520
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_8
            text "<label>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 552
            ypos 379
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_nn1_was_dropped = False
default ans_fsx_nn2_was_dropped = False
screen lesson_six_ls9_fill():
    image "images/lesson_six/lesson 6.9.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_nn1_was_dropped and ans_fsx_nn2_was_dropped:
            action Jump("lessonSixFillTen") 
        else:
            action Jump("if_lsx9_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("drop_down_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx9")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 346
            ypos 860
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_9
            text "id attribute" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 580
            ypos 860
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_9
            text "for attribute" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 311
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 311
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_twl1_was_dropped = False
default ans_fsx_twl2_was_dropped = False
default ans_fsx_twl3_was_dropped = False
screen lesson_six_ls12_fill():
    image "images/lesson_six/lesson 6.12.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_twl1_was_dropped and ans_fsx_twl2_was_dropped and ans_fsx_twl3_was_dropped:
            action Jump("lessonSixFillThirteen") 
        else:
            action Jump("if_lsx12_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("drop_down_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx12")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 337
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_12
            text "</select>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 532
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_12
            text '   "s1"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 643
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_12
            text "    for" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 265
            ypos 332
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 588
            ypos 379
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 160
            ypos 522
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_tht1_was_dropped = False
default ans_fsx_tht2_was_dropped = False
default ans_fsx_tht3_was_dropped = False
default ans_fsx_tht4_was_dropped = False
screen lesson_six_ls13_fill():
    image "images/lesson_six/lesson 6.14.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_tht1_was_dropped and ans_fsx_tht2_was_dropped and ans_fsx_tht3_was_dropped and ans_fsx_tht4_was_dropped:
            action Jump("lessonSixFillFourteen") 
        else:
            action Jump("if_lsx13_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("drop_down_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx13")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    draggroup:

        # Draggables
        drag:
            xpos 337
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_13
            text "radio button" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 572
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_13
            text "checkbox" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 769
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_13
            text "submit button" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 1030
            ypos 857
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lsx_13
            text "text box" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 478
            ypos 332
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 565
            ypos 379
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 495
            ypos 426
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 521
            ypos 473
            drag_raise True
            drag_name "4_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################

screen lesson_six_ls14_fill():
    image "images/lesson_six/lesson 6.15.webp" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_six_fourteen") 

###########################################################################################################################


default ans_fsx_st1_was_dropped = False
screen lesson_six_ls16_fill():
    image "images/lesson_six/lesson 6.16.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_st1_was_dropped:
            action Jump("lessonSixFillSeventeen") 
        else:
            action Jump("if_lsx16_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx16")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 337
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_16
            text "<movie>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 530
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_16
            text "<video>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 710
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_16
            text "<img>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 160
            ypos 418
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_egt1_was_dropped = False
default ans_fsx_egt2_was_dropped = False
screen lesson_six_ls18_fill():
    image "images/lesson_six/lesson 6.18.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_egt1_was_dropped and ans_fsx_egt2_was_dropped:
            action Jump("lessonSixFillNineteen") 
        else:
            action Jump("if_lsx18_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx18")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 345
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_18
            text "</video>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 521
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_18
            text "<video>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 160
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 160
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_nt1_was_dropped = False
screen lesson_six_ls19_fill():
    image "images/lesson_six/lesson 6.19.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_nt1_was_dropped:
            action Jump("lessonSixFillTwenty") 
        else:
            action Jump("if_lsx19_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx19")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 345
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_19
            text "origin" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 470
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_19
            text "<source" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 160
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_twt1_was_dropped = False
default ans_fsx_twt2_was_dropped = False
screen lesson_six_ls20_fill():
    image "images/lesson_six/lesson 6.20.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_twt1_was_dropped and ans_fsx_twt2_was_dropped:
            action Jump("lessonSixFillTwentyone") 
        else:
            action Jump("if_lsx20_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx20")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 345
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_20
            text "    src" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 521
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_20
            text "<source" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 160
            ypos 429
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 349
            ypos 429
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_twto1_was_dropped = False
default ans_fsx_twto2_was_dropped = False
screen lesson_six_ls21_fill():
    image "images/lesson_six/lesson 6.21.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_twto1_was_dropped and ans_fsx_twto2_was_dropped:
            action Jump("lessonSixFillTwentytwo") 
        else:
            action Jump("if_lsx21_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx21")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 345
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_21
            text "  type" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 521
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_21
            text "    src" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 311
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 655
            ypos 426
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_twtt1_was_dropped = False
screen lesson_six_ls22_fill():
    image "images/lesson_six/lesson 6.22.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_twtt1_was_dropped:
            action Jump("lessonSixFillTwentythree") 
        else:
            action Jump("if_lsx22_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx22")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 345
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_22
            text "doc/pdf" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 521
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_22
            text "img/png" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 710
            ypos 856
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_22
            text "video/mp4" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 655
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_twth1_was_dropped = False
default ans_fsx_twth2_was_dropped = False
screen lesson_six_ls23_fill():
    image "images/lesson_six/lesson 6.23.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_twth1_was_dropped and ans_fsx_twth2_was_dropped:
            action Jump("lessonSixFillTwentyfour") 
        else:
            action Jump("if_lsx23_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx23")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 347
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_23
            text "video/webm" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 570
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_23
            text "video/ogg" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 759
            ypos 856
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_23
            text "source" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 201
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 675
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_twts1_was_dropped = False
default ans_fsx_twts2_was_dropped = False
screen lesson_six_ls26_fill():
    image "images/lesson_six/lesson 6.26.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_twts1_was_dropped and ans_fsx_twts2_was_dropped:
            action Jump("lessonSixFillTwentyseven") 
        else:
            action Jump("if_lsx26_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx26")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 361
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_26
            text "video/ogg" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 564
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_26
            text "video/mp4" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 675
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 669
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsx_twtsv1_was_dropped = False
screen lesson_six_ls27_fill():
    image "images/lesson_six/lesson 6.27.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_twtsv1_was_dropped:
            action Jump("lessonSixFillTwentyeight") 
        else:
            action Jump("if_lsx27_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx27")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_27
            text "   play" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 490
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_27
            text "controls" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 670
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_27
            text "volume" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 292
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################

screen lesson_six_ls28_fill():
    image "images/lesson_six/lesson 6.28.webp" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_six_twenteight") 

###########################################################################################################################


default ans_fsx_tty1_was_dropped = False
default ans_fsx_tty2_was_dropped = False
default ans_fsx_tty3_was_dropped = False
default ans_fsx_tty4_was_dropped = False
screen lesson_six_ls30_fill():
    image "images/lesson_six/lesson 6.30.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_tty1_was_dropped and ans_fsx_tty2_was_dropped and ans_fsx_tty3_was_dropped and ans_fsx_tty4_was_dropped:
            action Jump("lessonVideoTakeaways") 
        else:
            action Jump("if_lsx30_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("video_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx30")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 361
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_30
            text "<source>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 556
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_30
            text "src attribute" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 791
            ypos 856
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_30
            text "type attribute" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 1047
            ypos 856
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lsx_30
            text "<video>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 532
            ypos 395
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 537
            ypos 446
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 371
            ypos 501
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 477
            ypos 552
            drag_raise True
            drag_name "4_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        


###########################################################################################################################


default ans_fsx_ttyo1_was_dropped = False
default ans_fsx_ttyo2_was_dropped = False
screen lesson_six_ls31_fill():
    image "images/lesson_six/lesson 6.31.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_ttyo1_was_dropped and ans_fsx_ttyo2_was_dropped:
            action Jump("lessonSixFillThirtytwo") 
        else:
            action Jump("if_lsx31_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("audio_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx31")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_31
            text "<sound>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 527
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_31
            text "</audio>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 714
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_31
            text "<audio>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 160
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)
        
        drag:
            xpos 160
            ypos 465
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)


###########################################################################################################################


default ans_fsx_ttytw1_was_dropped = False
screen lesson_six_ls32_fill():
    image "images/lesson_six/lesson 6.32.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_ttytw1_was_dropped:
            action Jump("lessonSixFillThirtythree") 
        else:
            action Jump("if_lsx32_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("audio_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx32")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_32
            text "option" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 500
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_32
            text "source" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 212
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)
        


###########################################################################################################################


default ans_fsx_ttyfr1_was_dropped = False
default ans_fsx_ttyfr2_was_dropped = False
screen lesson_six_ls34_fill():
    image "images/lesson_six/lesson 6.34.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_ttyfr1_was_dropped and ans_fsx_ttyfr2_was_dropped:
            action Jump("lessonSixFillThirtyfive") 
        else:
            action Jump("if_lsx34_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("audio_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx34")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_34
            text "  type" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 480
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_34
            text "   src" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 318
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)

        drag:
            xpos 533
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)
        


###########################################################################################################################


default ans_fsx_ttyfv1_was_dropped = False
default ans_fsx_ttyfv2_was_dropped = False
screen lesson_six_ls35_fill():
    image "images/lesson_six/lesson 6.35.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_ttyfv1_was_dropped and ans_fsx_ttyfv2_was_dropped:
            action Jump("lessonSixFillThirtysix") 
        else:
            action Jump("if_lsx35_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("audio_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx35")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_35
            text '"video/mpeg"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 596
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_35
            text '"audio/mpeg"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 851
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_35
            text '"audio/ogg"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 618
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)

        drag:
            xpos 611
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)
        


###########################################################################################################################


default ans_fsx_fttw1_was_dropped = False
default ans_fsx_fttw2_was_dropped = False
default ans_fsx_fttw3_was_dropped = False
default ans_fsx_fttw4_was_dropped = False
screen lesson_six_ls42_fill():
    image "images/lesson_six/lesson 6.42.webp" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsx_fttw1_was_dropped and ans_fsx_fttw2_was_dropped and ans_fsx_fttw3_was_dropped and ans_fsx_fttw4_was_dropped:
            action Jump("lessonSixFillFortythree") 
        else:
            action Jump("if_lsx42_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("audio_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sx42")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 337
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsx_42
            text "controls" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 493
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsx_42
            text "loop" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 609
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsx_42
            text "autoplay" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 789
            ypos 857
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lsx_42
            text "muted" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 314
            ypos 395
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)

        drag:
            xpos 596
            ypos 446
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)
        
        drag:
            xpos 411
            ypos 497
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)
        
        drag:
            xpos 510
            ypos 548
            drag_raise True
            drag_name "4_place"
            draggable False
            image Solid("#ffd53d00") xysize(150,50)
        


###########################################################################################################################