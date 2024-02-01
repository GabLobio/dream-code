init python:
    def IncrementRecitation4():
        persistent.ast2_recitation += 10
        persistent.ast2_accuracy += 10

default ans_ff_o1_was_dropped = False
screen lesson_four_ls2_fill():
    image "images/lesson_four/Lesson 4.2.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_o1_was_dropped:
            action Jump("lessonFourFillThree") 
        else:
            action Jump("if_lf2_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("text_formatting_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr2")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_2
            text "</d>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_2
            text "<b>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 520
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_th01_was_dropped = False
default ans_ff_th02_was_dropped = False
screen lesson_four_ls3_fill():
    image "images/lesson_four/Lesson 4.3.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_th01_was_dropped and ans_ff_th02_was_dropped:
            action [lambda: IncrementRecitation4(), Jump("lessonFourFillFour")]
        else:
            action Jump("if_lf3_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("text_formatting_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr3")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_3
            text "</d>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_3
            text "<b>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 600
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_3
            text "</b>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 530
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 870
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_fr01_was_dropped = False
default ans_ff_fr02_was_dropped = False
screen lesson_four_ls4_fill():
    image "images/lesson_four/Lesson 4.4.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_fr01_was_dropped and ans_ff_fr02_was_dropped:
            action Jump("lessonFourFillFive") 
        else:
            action Jump("if_lf4_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("text_formatting_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr4")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_4
            text "</t>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_4
            text "<i>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 600
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_4
            text "</i>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 500
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 915
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_fv01_was_dropped = False
default ans_ff_fv02_was_dropped = False
screen lesson_four_ls5_fill():
    image "images/lesson_four/Lesson 4.5.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_fv01_was_dropped and ans_ff_fv02_was_dropped:
            action Jump("lessonFourFillSix") 
        else:
            action Jump("if_lf5_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("text_formatting_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr5")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_5
            text "</s>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_5
            text "<u>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 600
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_5
            text "</u>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 510
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 890
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_sx01_was_dropped = False
default ans_ff_sx02_was_dropped = False
screen lesson_four_ls6_fill():
    image "images/lesson_four/Lesson 4.6.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_sx01_was_dropped and ans_ff_sx02_was_dropped:
            action [lambda: IncrementRecitation4(), Jump("lessonFourFillSeven")] 
        else:
            action Jump("if_lf6_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("text_formatting_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr6")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_6
            text "</t>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_6
            text "<i>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 600
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_6
            text "</i>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 640
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 860
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################

screen lesson_four_ls7_fill():
    image "images/lesson_four/Lesson 4.7.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_four_seven") 


###########################################################################################################################


default ans_ff_nn01_was_dropped = False
default ans_ff_nn02_was_dropped = False
screen lesson_four_ls9_fill():
    image "images/lesson_four/Lesson 4.9.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_nn01_was_dropped and ans_ff_nn02_was_dropped:
            action Jump("lessonFourFillTen") 
        else:
            action Jump("if_lf9_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("text_formatting_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr9")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 320
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_9
            text "    </s>  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_9
            text "<strong>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 690
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_9
            text "</strong>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 485
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 835
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################

screen lesson_four_ls10_fill():
    image "images/lesson_four/Lesson 4.10.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_four_ten") 


###########################################################################################################################


default ans_ff_el01_was_dropped = False
default ans_ff_el02_was_dropped = False
screen lesson_four_ls11_fill():
    image "images/lesson_four/Lesson 4.11.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_el01_was_dropped and ans_ff_el02_was_dropped:
            action Jump("lessonFourFillTwelve") 
        else:
            action Jump("if_lf11_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("text_formatting_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr11")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_11
            text "</p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_11
            text "<em>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 640
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_11
            text "</em>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 495
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 885
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


screen lesson_four_ls12_fill():
    image "images/lesson_four/Lesson 4.12.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_four_twelve") 


###########################################################################################################################


default ans_ff_tt01_was_dropped = False
default ans_ff_tt02_was_dropped = False
default ans_ff_tt03_was_dropped = False
screen lesson_four_ls13_fill():
    image "images/lesson_four/Lesson 4.13.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_tt01_was_dropped and ans_ff_tt02_was_dropped and ans_ff_tt03_was_dropped:
            action [lambda: IncrementRecitation4(), Jump("lessonFourFillFourteen")]
        else:
            action Jump("if_lf13_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("text_formatting_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr13")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")



    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_13
            text " /strong " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 520
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_13
            text "    em    " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 640
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_13
            text "     /p    " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 420
            ypos 475
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 260
            ypos 615
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 190
            ypos 665
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_ft01_was_dropped = False
default ans_ff_ft02_was_dropped = False
screen lesson_four_ls14_fill():
    image "images/lesson_four/Lesson 4.14.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_ft01_was_dropped and ans_ff_ft02_was_dropped:
            action Jump("lessonFourTakewaysText") 
        else:
            action Jump("if_lf14_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("text_formatting_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr14")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_14
            text "  /u  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_14
            text "  u  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 640
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_14
            text "  /p  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 285
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 605
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_st01_was_dropped = False
default ans_ff_st02_was_dropped = False
screen lesson_four_ls16_fill():
    image "images/lesson_four/Lesson 4.16.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_st01_was_dropped and ans_ff_st02_was_dropped:
            action Jump("lessonFourFillSeventeen") 
        else:
            action Jump("if_lf16_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("links_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr16")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 

    draggroup:

        # Draggables
        drag:
            xpos 330
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_16
            text "information" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 530
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_16
            text "     move    " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]



        
        
        # Drop Place
        drag:
            xpos 210
            ypos 420
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 295
            ypos 465
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_egt01_was_dropped = False
screen lesson_four_ls18_fill():
    image "images/lesson_four/Lesson 4.18.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_egt01_was_dropped:
            action Jump("lessonFourFillNineteen") 
        else:
            action Jump("if_lf18_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("links_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr18")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 

 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_18
            text " link " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_18
            text " href " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]



        

        
        
        # Drop Place
        drag:
            xpos 610
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_nt01_was_dropped = False
screen lesson_four_ls19_fill():
    image "images/lesson_four/Lesson 4.19.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_nt01_was_dropped:
            action [lambda: IncrementRecitation4(), Jump("lessonFourFillTwenty")]
        else:
            action Jump("if_lf19_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("links_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr19")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 
 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_19
            text " </i> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_19
            text " </a> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]



        

        
        
        # Drop Place
        drag:
            xpos 485
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_tw01_was_dropped = False
default ans_ff_tw02_was_dropped = False
screen lesson_four_ls20_fill():
    image "images/lesson_four/Lesson 4.20.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_tw01_was_dropped and ans_ff_tw02_was_dropped:
            action Jump("lessonFourFillTwentyOne") 
        else:
            action Jump("if_lf20_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("links_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr20")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 

 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_20
            text " </a> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_20
            text " <a> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 600
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_20
            text  ' href ' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]



        

        
        
        # Drop Place
        drag:
            xpos 220
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)

        drag:
            xpos 485
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_two01_was_dropped = False
default ans_ff_two02_was_dropped = False
screen lesson_four_ls21_fill():
    image "images/lesson_four/Lesson 4.21.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_two01_was_dropped and ans_ff_two02_was_dropped:
            action Jump("lessonFourFillTwentyTwo") 
        else:
            action Jump("if_lf21_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("links_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr21")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 


    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_21
            text " </a> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_21
            text " <a> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 600
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_21
            text  '    "   ' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]



        

        
        
        # Drop Place
        drag:
            xpos 320
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)

        drag:
            xpos 550
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_twt01_was_dropped = False
screen lesson_four_ls22_fill():
    image "images/lesson_four/Lesson 4.22.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_twt01_was_dropped:
            action Jump("lessonFourFillTwentyThree") 
        else:
            action Jump("if_lf22_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("links_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr22")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 
 

    draggroup:

        # Draggables
        drag:
            xpos 240
            ypos 770
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_22
            text "The quotation marks dont match" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 210
            ypos 820
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_22
            text "       The href is missing      " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 455
            ypos 465
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,100)


###########################################################################################################################


screen lesson_four_ls23_fill():
    image "images/ftg_bg.png"
    default line_six_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if line_six_value == "":
            action ShowMenu("error_msg")
        elif line_six_value == '"':
            action Jump("if_lf23_correct")
        else:
            action ShowMenu("error_msg")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("links_hint")   


    hbox:
        xpos 100
        ypos 200
            
        vbox:
            ############### INPUTS ###############

            hbox:
                textbutton "1": 
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28     
                    action SetScreenVariable("active_input", 1)
                text "<html>" size 28 color "#4E4E4E" xoffset 6 yoffset 6

            hbox:
                textbutton "2": 
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28    
                    action SetScreenVariable("active_input", 2)
                text "  <head>" size 28 color "#4E4E4E" xoffset 6 yoffset 6

            hbox:
                textbutton "3": 
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28   
                    action SetScreenVariable("active_input", 3)
                text "      <title>Hyperlinks</title>" size 28 color "#4E4E4E" xoffset 6 yoffset 6

            hbox:
                textbutton "4": 
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28     
                    action SetScreenVariable("active_input", 4)
                text "  </head>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
            
            hbox:
                textbutton "5": 
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28     
                    action SetScreenVariable("active_input", 5)
                text "  <body>" size 28 color "#4E4E4E" xoffset 6 yoffset 6

            hbox:
                textbutton "6": 
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28     
                    action SetScreenVariable("active_input", 6)

                text "      <a href=" size 28 color "#4E4E4E" xoffset 6 yoffset 6

                text " " size 28 color "#4E4E4E" xoffset 6 yoffset 6
                if active_input == 6:
                    input:
                        xoffset 6
                        yoffset 6
                        size 28
                        length 5
                        value ScreenVariableInputValue("line_six_value")
                            
                else:
                    textbutton "[line_six_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28     
                        action SetScreenVariable("active_input", 6)
                
                text 'https://www.google.com">Google</a>' size 28 color "#4E4E4E" xoffset 6 yoffset 6
                        
            hbox:
                textbutton "7": 
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28     
                    action SetScreenVariable("active_input", 7)
                text "  </body>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
            
            hbox:
                textbutton "8": 
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28 
                    action SetScreenVariable("active_input", 8)
                text "</html>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
        


###########################################################################################################################


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

screen lesson_four_ls24_fill():
    image "images/lesson_four/Lesson 4.24.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_four_TwentyFour") 


###########################################################################################################################


default ans_ff_tf01_was_dropped = False
default ans_ff_tf02_was_dropped = False
default ans_ff_tf03_was_dropped = False
screen lesson_four_ls25_fill():
    image "images/lesson_four/Lesson 4.25.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ff_tf01_was_dropped and ans_ff_tf02_was_dropped and ans_ff_tf03_was_dropped:
            action Jump("lessonFourFillTwentySix") 
        else:
            action Jump("if_lf25_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("links_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr25")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 

 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_25
            text " symbols " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 530
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_25
            text " links " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 640
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_25
            text  '  </>  ' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]



        

        
        
        # Drop Place
        drag:
            xpos 990
            ypos 430
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(100,30)

        drag:
            xpos 705
            ypos 475
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(100,30)

        drag:
            xpos 935
            ypos 475
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(100,30)


###########################################################################################################################


default ans_ff_ts01_was_dropped = False
default ans_ff_ts02_was_dropped = False
default ans_ff_ts03_was_dropped = False
screen lesson_four_ls26_fill():
    image "images/lesson_four/Lesson 4.26.png" 

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ff_ts01_was_dropped and ans_ff_ts02_was_dropped and ans_ff_ts03_was_dropped:
            action [lambda: IncrementRecitation4(), Jump("lessonLinkTakeaways")]
        else:
            action Jump("if_lf26_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("links_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr26")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 
 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_26
            text "  a  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_26
            text "href" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 600
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_26
            text  '  /a  ' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]



        

        
        
        # Drop Place
        drag:
            xpos 210
            ypos 425
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(100,30)

        drag:
            xpos 330
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(100,30)

        drag:
            xpos 600
            ypos 425
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(100,30)


###########################################################################################################################


default ans_ff_twts01_was_dropped = False
screen lesson_four_ls27_fill():
    image "images/lesson_four/Lesson 4.27.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ff_twts01_was_dropped:
            action Jump("lessonFourTwentyEight") 
        else:
            action Jump("if_lf27_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("list_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr27")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")  


    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_27
            text "<item>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 500
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_27
            text "<li>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 170
            ypos 475
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,100)


###########################################################################################################################


default ans_ff_twte01_was_dropped = False
default ans_ff_twte02_was_dropped = False
default ans_ff_twte03_was_dropped = False
screen lesson_four_ls28_fill():
    image "images/lesson_four/Lesson 4.28.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ff_twte01_was_dropped and ans_ff_twte02_was_dropped and ans_ff_twte03_was_dropped:
            action Jump("lessonOrderedList") 
        else:
            action Jump("if_lf28_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("list_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr28")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")  

        
 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_28
            text "<li>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 460
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_28
            text "Item 2" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 620
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_28
            text "</li>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 170
            ypos 430
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 250
            ypos 475
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 350
            ypos 520
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_twtn01_was_dropped = False
screen lesson_four_ls29_fill():
    image "images/lesson_four/Lesson 4.29.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ff_twtn01_was_dropped:
            action Jump("lessonFourThirty") 
        else:
            action Jump("if_lf29_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("list_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr29")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 

        


    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_29
            text "<order>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 500
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_29
            text "<ol>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 170
            ypos 380
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_tht01_was_dropped = False
default ans_ff_tht02_was_dropped = False
default ans_ff_tht03_was_dropped = False
default ans_ff_tht04_was_dropped = False
default ans_ff_tht05_was_dropped = False
screen lesson_four_ls30_fill():
    image "images/lesson_four/Lesson 4.30.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ff_tht01_was_dropped and ans_ff_tht02_was_dropped and ans_ff_tht03_was_dropped and ans_ff_tht04_was_dropped:
            action Jump("lessonFourThirtyOne") 
        else:
            action Jump("if_lf30_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("list_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr30")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 


    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_30
            text "<li>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 440
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_30
            text "tea" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 530
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_30
            text "</li>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 640
            ypos 855
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lf_30
            text "</ol>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 170
            ypos 480
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 240
            ypos 520
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 310
            ypos 570
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 170
            ypos 620
            drag_raise True
            drag_name "4_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_thto01_was_dropped = False
default ans_ff_thto02_was_dropped = False
screen lesson_four_ls31_fill():
    image "images/lesson_four/Lesson 4.31.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ff_thto01_was_dropped and ans_ff_thto02_was_dropped:
            action Jump("lessonFourThirtyTwo") 
        else:
            action Jump("if_lf31_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("list_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr31")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 


    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_31
            text "</ul>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_31
            text "<ul>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 170
            ypos 385
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 170
            ypos 570
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


screen lesson_four_ls32_fill():
    image "images/lesson_four/lesson 4.32.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_four_32") 


###########################################################################################################################


default ans_ff_thtt01_was_dropped = False
default ans_ff_thtt02_was_dropped = False
default ans_ff_thtt03_was_dropped = False
default ans_ff_thtt04_was_dropped = False
screen lesson_four_ls33_fill():
    image "images/lesson_four/Lesson 4.33.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ff_thtt01_was_dropped and ans_ff_thtt02_was_dropped and ans_ff_thtt03_was_dropped and ans_ff_thtt04_was_dropped:
            action Jump("lessonFourThirtyFour") 
        else:
            action Jump("if_lf33_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("list_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr33")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 


    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_33
            text "</ul>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_33
            text "<li>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 580
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_33
            text "</li>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 690
            ypos 855
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lf_33
            text "</p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 500
            ypos 360
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 355
            ypos 455
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 160
            ypos 500
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 160
            ypos 690
            drag_raise True
            drag_name "4_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_thtf01_was_dropped = False
default ans_ff_thtf02_was_dropped = False
default ans_ff_thtf03_was_dropped = False
default ans_ff_thtf04_was_dropped = False
screen lesson_four_ls34_fill():
    image "images/lesson_four/Lesson 4.34.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ff_thtf01_was_dropped and ans_ff_thtf02_was_dropped and ans_ff_thtf03_was_dropped and ans_ff_thtf04_was_dropped:
            action Jump("lessonFourThirtyFive") 
        else:
            action Jump("if_lf34_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("list_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr34")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

  


    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_34
            text "</li>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_34
            text "<li>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 580
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lf_34
            text "<ol>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 690
            ypos 855
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lf_34
            text "</h1>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 640
            ypos 360
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 160
            ypos 405
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 160
            ypos 455
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)
        
        drag:
            xpos 345
            ypos 595
            drag_raise True
            drag_name "4_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


default ans_ff_thtfv01_was_dropped = False
screen lesson_four_ls35_fill():
    image "images/lesson_four/Lesson 4.35.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ff_thtfv01_was_dropped:
            action Jump("lessonFourThirtySix") 
        else:
            action Jump("if_lf35_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("list_hint")  

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fr35")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 800
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lf_35
            text "An ordered list nested inside an unordered list" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 340
            ypos 860
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lf_35
            text "An unordered list nested inside an ordered list" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 160
            ypos 240
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################