init python:
    def IncrementRecitation8():
        persistent.ast3_recitation += 5
        persistent.ast3_accuracy += 5




default ans_fet_o1_was_dropped = False
screen lesson_eight_ls1_fill():
    image "images/lesson_eight/lesson 8.1.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_o1_was_dropped:
            action [lambda: IncrementRecitation8(), Jump("lessonEightFillTwo")]
        else:
            action Jump("if_let1_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")


    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("style_hint")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et1")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_1
            text "design" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 500
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_1
            text "style" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 255
            ypos 473
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fet_two1_was_dropped = False
default ans_fet_two2_was_dropped = False
screen lesson_eight_ls2_fill():
    image "images/lesson_eight/lesson 8.2.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_two1_was_dropped and ans_fet_two2_was_dropped:
            action Jump("lessonEightFillThree") 
        else:
            action Jump("if_let2_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("style_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et2")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")



    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_2
            text '"color:blue"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 565
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_2
            text "    style" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 245
            ypos 473
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 518
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fet_thr1_was_dropped = False
default ans_fet_thr2_was_dropped = False
screen lesson_eight_ls3_fill():
    image "images/lesson_eight/lesson 8.3.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_thr1_was_dropped and ans_fet_thr2_was_dropped:
            action Jump("lessonEightFillFour") 
        else:
            action Jump("if_let3_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("style_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et3")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")



    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_3
            text "</h1>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 478
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_3
            text ' " ; " ' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 486
            ypos 473
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 294
            ypos 567
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fet_fv1_was_dropped = False
default ans_fet_fv2_was_dropped = False
screen lesson_eight_ls5_fill():
    image "images/lesson_eight/lesson 8.5.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_fv1_was_dropped and ans_fet_fv2_was_dropped:
            action Jump("lessonEightFillSix") 
        else:
            action Jump("if_let5_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("style_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et5")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_5
            text "</p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 465
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_5
            text "style" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 252
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 427
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fet_et1_was_dropped = False
default ans_fet_et2_was_dropped = False
screen lesson_eight_ls8_fill():
    image "images/lesson_eight/lesson 8.8.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_et1_was_dropped and ans_fet_et2_was_dropped:
            action [lambda: IncrementRecitation8(), Jump("lessonEightFillNine")]
        else:
            action Jump("if_let8_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("style_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et8")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")



    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_8
            text "</button>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 544
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_8
            text "   style" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 301
            ypos 473
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 960
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################
###########################################################################################################################


screen lesson_eight_ls10_fill():
    image "images/lesson_eight/lesson 8.22.png" 
    default input_one_value = ""
    default input_two_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if input_one_value == "" and input_two_value == "":
            action ShowMenu("error_msg_et")
        elif input_one_value == "style" and input_two_value == "</h1>":
            action Jump("if_le10_correct")
        else:
            action ShowMenu("error_msg_et")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("style_hint")


    hbox:
        xpos 160
        ypos 191
            
        vbox:
            ############### INPUTS ###############
            text "{b}Complete the code to create a large level 1 heading{/b}\n\n\n\n\n\n" size 28 color "#ffffff" xoffset 6 yoffset 6


            hbox:

                text "<h1 " size 28 color "#ffffff" xoffset 6 yoffset 6

                if active_input == 1:
                    input:
                        xoffset 6
                        yoffset 6
                        size 28
                        length 5
                        value ScreenVariableInputValue("input_one_value")
                            
                else:
                    textbutton '"[input_one_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28     
                        action SetScreenVariable("active_input", 1)

                text '="font-size:large"> Large Heading ' size 28 color "#ffffff" xoffset 6 yoffset 6
                if active_input == 2:
                    input:
                        xoffset 6
                        yoffset 6
                        size 28
                        length 5
                        value ScreenVariableInputValue("input_two_value")
                            
                else:
                    textbutton '"[input_two_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28     
                        action SetScreenVariable("active_input", 2)
                
                        
        


###########################################################################################################################


screen error_msg_et():
    image "images/lesson_eight/lesson 8.22.png" 
        
    text "Error!!!" size 28 color "#ffffff" xpos 160 ypos 191 xoffset 6 yoffset 6
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"
        action Return()


###########################################################################################################################


screen lesson_eight_ls11_fill():
    image "images/lesson_eight/lesson 8.22.png" 
    default input_one_value = ""
    default input_two_value = ""
    default input_three_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if input_one_value == "" and input_two_value == "" and input_three_value == "":
            action ShowMenu("error_msg_et")
        elif input_one_value == "style" and input_two_value == "black" and input_three_value == "color":
            action [lambda: IncrementRecitation8(), Jump("if_le11_correct")]
        else:
            action ShowMenu("error_msg_et")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("style_hint")


    hbox:
        xpos 160
        ypos 191
            
        vbox:
            ############### INPUTS ###############
            text "{b}Complete the code to create a button with white text and black background{/b}\n\n\n\n\n\n" size 28 color "#ffffff" xoffset 6 yoffset 6


            hbox:

                text "<button " size 28 color "#ffffff" xoffset 6 yoffset 6

                if active_input == 1:
                    input:
                        xoffset 6
                        yoffset 6
                        size 28
                        length 5
                        value ScreenVariableInputValue("input_one_value")
                            
                else:
                    textbutton '"[input_one_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28     
                        action SetScreenVariable("active_input", 1)

                text '="background-color:' size 28 color "#ffffff" xoffset 6 yoffset 6

                if active_input == 2:
                    input:
                        xoffset 6
                        yoffset 6
                        size 28
                        length 5
                        value ScreenVariableInputValue("input_two_value")
                            
                else:
                    textbutton '"[input_two_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28     
                        action SetScreenVariable("active_input", 2)
                
                text '; ' size 28 color "#ffffff" xoffset 6 yoffset 6
                
                if active_input == 3:
                    input:
                        xoffset 6
                        yoffset 6
                        size 28
                        length 5
                        value ScreenVariableInputValue("input_three_value")
                            
                else:
                    textbutton '"[input_three_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28     
                        action SetScreenVariable("active_input", 3)
                
                text ':white"> OK </button>' size 28 color "#ffffff" xoffset 6 yoffset 6
        


###########################################################################################################################


default ans_fet_twv1_was_dropped = False
default ans_fet_twv2_was_dropped = False
screen lesson_eight_ls12_fill():
    image "images/lesson_eight/lesson 8.12.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_twv1_was_dropped and ans_fet_twv2_was_dropped:
            action Jump("lessonEightFillThirteen") 
        else:
            action Jump("if_let12_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("style_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et12")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_12
            text "style" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 464
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_12
            text "border" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 250
            ypos 473
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 475
            ypos 473
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fet_tht1_was_dropped = False
default ans_fet_tht2_was_dropped = False
default ans_fet_tht3_was_dropped = False
screen lesson_eight_ls13_fill():
    image "images/lesson_eight/lesson 8.13.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_tht1_was_dropped and ans_fet_tht2_was_dropped and ans_fet_tht3_was_dropped:
            action Jump("lessonStyleTakeaways") 
        else:
            action Jump("if_let13_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("style_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et13")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_13
            text "red" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 441
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_13
            text "solid" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 562
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_let_13
            text "1px" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 758
            ypos 446
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 752
            ypos 497
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 753
            ypos 548
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fet_ft1_was_dropped = False
default ans_fet_ft2_was_dropped = False
screen lesson_eight_ls14_fill():
    image "images/lesson_eight/lesson 8.14.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_ft1_was_dropped and ans_fet_ft2_was_dropped:
            action [lambda: IncrementRecitation8(), Jump("lessonEightFillFifteen")]
        else:
            action Jump("if_let14_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("inline_block_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et14")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_14
            text "border" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 492
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_14
            text "style" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 332
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 547
            ypos 379
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################

screen lesson_eight_ls15_fill():
    image "images/lesson_eight/lesson 8.15.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_et_fifteen") 

###########################################################################################################################


default ans_fet_sxt1_was_dropped = False
default ans_fet_sxt2_was_dropped = False
screen lesson_eight_ls16_fill():
    image "images/lesson_eight/lesson 8.16.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_sxt1_was_dropped and ans_fet_sxt2_was_dropped:
            action Jump("lessonEightFillSeventeen") 
        else:
            action Jump("if_let16_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("inline_block_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et16")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_16
            text "<button>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 533
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_16
            text "<p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 685
            ypos 395
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 683
            ypos 446
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fet_svt1_was_dropped = False
default ans_fet_svt2_was_dropped = False
screen lesson_eight_ls17_fill():
    image "images/lesson_eight/lesson 8.17.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_svt1_was_dropped and ans_fet_svt2_was_dropped:
            action Jump("lessonEightFillEightteen") 
        else:
            action Jump("if_let17_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("inline_block_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et17")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_17
            text "<b>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 454
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_17
            text "<ul>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 685
            ypos 395
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 684    
            ypos 446
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fet_nt1_was_dropped = False
default ans_fet_nt2_was_dropped = False
default ans_fet_nt3_was_dropped = False
screen lesson_eight_ls19_fill():
    image "images/lesson_eight/lesson 8.19.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_nt1_was_dropped and ans_fet_nt2_was_dropped and ans_fet_nt3_was_dropped:
            action [lambda: IncrementRecitation8(), Jump("lessonEightFillTwenty")]
        else:
            action Jump("if_let19_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("inline_block_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et19")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")



    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_19
            text "<i>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 441
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_19
            text "<b>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 554
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_let_19
            text "<u>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 246
            ypos 395
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 249    
            ypos 446
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 343    
            ypos 497
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_fet_twto1_was_dropped = False
default ans_fet_twto2_was_dropped = False
default ans_fet_twto3_was_dropped = False
screen lesson_eight_ls21_fill():
    image "images/lesson_eight/lesson 8.21.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fet_twto1_was_dropped and ans_fet_twto2_was_dropped and ans_fet_twto3_was_dropped:
            action Jump("lessonEightFillTwentytwo") 
        else:
            action Jump("if_let21_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("inline_block_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_et21")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_let_21
            text "</p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 465
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_let_21
            text "</a>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 587
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_let_21
            text "<p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 160
            ypos 332
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 597    
            ypos 379
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 160    
            ypos 426
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################

screen lesson_eight_ls24_fill():
    image "images/lesson_eight/lesson 8.23.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_et_twtfr") 

###########################################################################################################################