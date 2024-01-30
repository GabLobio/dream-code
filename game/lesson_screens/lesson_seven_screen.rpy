




default ans_fsv_o1_was_dropped = False
default ans_fsv_o2_was_dropped = False
default ans_fsv_o3_was_dropped = False
screen lesson_seven_ls1_fill():
    image "images/lesson_seven/lesson 7.1.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_o1_was_dropped and ans_fsv_o2_was_dropped and ans_fsv_o3_was_dropped:
            action Jump("lessonSevenFillTwo") 
        else:
            action Jump("if_lsv1_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv1")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_1
            text "<footer>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 525
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_1
            text "<main>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 690
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsv_1
            text "<header>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 288
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 375
            ypos 426
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 275
            ypos 473
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsv_t1_was_dropped = False
screen lesson_seven_ls2_fill():
    image "images/lesson_seven/lesson 7.2.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_t1_was_dropped:
            action Jump("lessonSevenFillThree") 
        else:
            action Jump("if_lsv2_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv2")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_2
            text "<head>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 509
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_2
            text "<header>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsv_thr1_was_dropped = False
default ans_fsv_thr2_was_dropped = False
screen lesson_seven_ls3_fill():
    image "images/lesson_seven/lesson 7.3.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_thr1_was_dropped and ans_fsv_thr2_was_dropped:
            action Jump("lessonSevenFillFour") 
        else:
            action Jump("if_lsv3_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv3")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_3
            text "</header>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 551
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_3
            text "<header>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 750
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsv_3
            text "<head>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
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


default ans_fsv_fr1_was_dropped = False
default ans_fsv_fr2_was_dropped = False
screen lesson_seven_ls4_fill():
    image "images/lesson_seven/lesson 7.4.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_fr1_was_dropped and ans_fsv_fr2_was_dropped:
            action Jump("lessonSevenFillFive") 
        else:
            action Jump("if_lsv4_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv4")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_4
            text "important" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 551
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_4
            text "</main>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 750
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsv_4
            text "<main>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
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


default ans_fsv_fv1_was_dropped = False
screen lesson_seven_ls5_fill():
    image "images/lesson_seven/lesson 7.5.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_fv1_was_dropped:
            action Jump("lessonSevenFillSix") 
        else:
            action Jump("if_lsv5_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv5")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")



    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_5
            text "<foot>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 520
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_5
            text "<footer>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 160
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsv_ten1_was_dropped = False
default ans_fsv_ten2_was_dropped = False
default ans_fsv_ten3_was_dropped = False
screen lesson_seven_ls10_fill():
    image "images/lesson_seven/lesson 7.10.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_ten1_was_dropped and ans_fsv_ten2_was_dropped and ans_fsv_ten3_was_dropped:
            action Jump("lessonSevenFillEleven") 
        else:
            action Jump("if_lsv10_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv10")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_10
            text "<h1>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 466
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_10
            text "<header>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 665
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsv_10
            text "<head>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 319
            ypos 395
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 433
            ypos 446
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 396
            ypos 497
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsv_ft1_was_dropped = False
screen lesson_seven_ls14_fill():
    image "images/lesson_seven/lesson 7.14.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_ft1_was_dropped:
            action Jump("lessonSevenFillFifteen") 
        else:
            action Jump("if_lsv14_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv14")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_14
            text "<blog>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 500
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_14
            text "<article>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsv_fft1_was_dropped = False
default ans_fsv_fft2_was_dropped = False
screen lesson_seven_ls15_fill():
    image "images/lesson_seven/lesson 7.15.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_fft1_was_dropped and ans_fsv_fft2_was_dropped:
            action Jump("lessonSevenFillSixteen") 
        else:
            action Jump("if_lsv15_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv15")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_15
            text "</article>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 550
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_15
            text "<article>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
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
            ypos 520
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsv_et1_was_dropped = False
screen lesson_seven_ls18_fill():
    image "images/lesson_seven/lesson 7.18.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_et1_was_dropped:
            action Jump("lessonSevenFillNineteen") 
        else:
            action Jump("if_lsv18_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv18")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_18
            text "<part>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 500
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_18
            text "<section>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsv_nt1_was_dropped = False
default ans_fsv_nt2_was_dropped = False
screen lesson_seven_ls19_fill():
    image "images/lesson_seven/lesson 7.19.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_nt1_was_dropped and ans_fsv_nt2_was_dropped:
            action Jump("lessonSevenFillTwenty") 
        else:
            action Jump("if_lsv19_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv19")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")



    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_19
            text "</section>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 550
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_19
            text "<section>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
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
            ypos 520
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsv_twtt1_was_dropped = False
default ans_fsv_twtt2_was_dropped = False
screen lesson_seven_ls22_fill():
    image "images/lesson_seven/lesson 7.22.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_twtt1_was_dropped and ans_fsv_twtt2_was_dropped:
            action Jump("lessonSevenFillTwentythree") 
        else:
            action Jump("if_lsv22_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv22")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_22
            text "<apart>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 520
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_22
            text "</aside>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 710
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsv_22
            text "<aside>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]



        
        
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
            ypos 520
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fsv_twts1_was_dropped = False
default ans_fsv_twts2_was_dropped = False
default ans_fsv_twts3_was_dropped = False
screen lesson_seven_ls27_fill():
    image "images/lesson_seven/lesson 7.27.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fsv_twts1_was_dropped and ans_fsv_twts2_was_dropped and ans_fsv_twts3_was_dropped:
            action Jump("lessonLayoutTakeaways") 
        else:
            action Jump("if_lsv27_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("layout_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_sv27")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")



    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lsv_27
            text "<section>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 550
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lsv_27
            text "<article>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 740
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lsv_27
            text "<aside>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]



        
        
        # Drop Place
        drag:
            xpos 445
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 534
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 384
            ypos 520
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################