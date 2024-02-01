






init python:
    def IncrementRecitation10():
        persistent.ast4_recitation += 20
        persistent.ast4_accuracy += 20


default ans_ften_o1_was_dropped = False
default ans_ften_o2_was_dropped = False
screen lesson_ten_ls1_fill():
    image "images/lesson_ten/lesson 10.1.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        if ans_ften_o1_was_dropped and ans_ften_o2_was_dropped:
            action [lambda: IncrementRecitation10(), Jump("lessonTenFillTwo")]
        else:
            action Jump("if_lten1_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("table_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_ten1")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")



    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lten_1
            text "</table>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 521
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lten_1
            text "<table>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
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


default ans_ften_thr1_was_dropped = False
default ans_ften_thr2_was_dropped = False
default ans_ften_thr3_was_dropped = False
screen lesson_ten_ls3_fill():
    image "images/lesson_ten/lesson 10.3.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"

        if ans_ften_thr1_was_dropped and ans_ften_thr2_was_dropped and ans_ften_thr3_was_dropped:
            action Jump("lessonTenFillFour") 
        else:
            action Jump("if_lten3_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("table_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_ten3")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lten_3
            text "</table>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 521
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lten_3
            text "</tr>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 637
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lten_3
            text "<table>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
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
        
        drag:
            xpos 160
            ypos 567    
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ften_fr1_was_dropped = False
default ans_ften_fr2_was_dropped = False
default ans_ften_fr3_was_dropped = False
default ans_ften_fr4_was_dropped = False
screen lesson_ten_ls4_fill():
    image "images/lesson_ten/lesson 10.4.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ften_fr1_was_dropped and ans_ften_fr2_was_dropped and ans_ften_fr3_was_dropped and ans_ften_fr4_was_dropped:
            action [lambda: IncrementRecitation10(), Jump("lessonTenFillFive")]
        else:
            action Jump("if_lten4_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("table_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_ten4")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lten_4
            text "</tr>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 469
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lten_4
            text "</td>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 604
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lten_4
            text "<table>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 784
            ypos 857
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lten_4
            text "<td>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 160
            ypos 379
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 323
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
        
        drag:
            xpos 160
            ypos 567    
            drag_raise True
            drag_name "4_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


screen lesson_ten_ls5_fill():
    image "images/lesson_ten/lesson 10.5.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_ten_five") 


###########################################################################################################################


screen lesson_ten_ls6_fill():
    image "images/lesson_ten/lesson 10.6.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_ten_six") 


###########################################################################################################################


default ans_ften_et1_was_dropped = False
default ans_ften_et2_was_dropped = False
screen lesson_ten_ls8_fill():
    image "images/lesson_ten/lesson 10.8.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ften_et1_was_dropped and ans_ften_et2_was_dropped:
            action Jump("lessonTenFillNine") 
        else:
            action Jump("if_lten8_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("table_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_ten8")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")




    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lten_8
            text " 3 " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 450
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lten_8
            text " 2 " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 290
            ypos 536
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 338
            ypos 583    
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ften_t1_was_dropped = False
default ans_ften_t2_was_dropped = False
screen lesson_ten_ls10_fill():
    image "images/lesson_ten/lesson 10.10.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ften_t1_was_dropped and ans_ften_t2_was_dropped:
            action [lambda: IncrementRecitation10(), Jump("lessonTenFillEleven")]
        else:
            action Jump("if_lten10_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("table_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_ten10")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lten_10
            text " 3 " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 450
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lten_10
            text " 2 " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 287
            ypos 637
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 340
            ypos 684    
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ften_el1_was_dropped = False
default ans_ften_el2_was_dropped = False
screen lesson_ten_ls11_fill():
    image "images/lesson_ten/lesson 10.11.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        if ans_ften_el1_was_dropped and ans_ften_el2_was_dropped:
            action Jump("lessonTenFillTweleve") 
        else:
            action Jump("if_lten11_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("table_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"
        action Jump("call_ten11")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lten_11
            text "</td>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 476
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lten_11
            text "<th>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 460
            ypos 426
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 507
            ypos 567    
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


screen lesson_ten_ls12_fill():
    image "images/lesson_ten/lesson 10.12.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_ten_tweleve") 


###########################################################################################################################


default ans_ften_thtt1_was_dropped = False
default ans_ften_thtt2_was_dropped = False
screen lesson_ten_ls13_fill():
    image "images/lesson_ten/lesson 10.13.png" 


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        if ans_ften_thtt1_was_dropped and ans_ften_thtt2_was_dropped:
            action [lambda: IncrementRecitation10(), Jump("lessonTenFillFourteen")]
        else:
            action Jump("if_lten13_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("table_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"
        action Jump("call_ten13")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lten_13
            text "</td>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 476
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lten_13
            text "<th>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 468
            ypos 465
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 436
            ypos 559    
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


screen lesson_ten_ls17_fill():
    image "images/lesson_ten/lesson 10.17.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_ten_seventeen") 


###########################################################################################################################


screen lesson_ten_ls18_fill():
    image "images/lesson_ten/lesson 10.18.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_ten_eighteen") 


###########################################################################################################################


screen lesson_nine_ls19_fill():
    image "images/lesson_eight/lesson 8.22.png" 
    default input_1_value = ""
    default input_2_value = ""
    default input_3_value = ""
    default input_4_value = ""
    default input_5_value = ""
    default input_6_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if input_1_value == "" and input_2_value == "" and input_3_value == "" and input_4_value == "" and input_5_value == "" and input_6_value == "":
            action ShowMenu("error_msg_nine")
        elif input_1_value == "<table>" and input_2_value == "<th>" and input_3_value == "</th>" and input_4_value == "</tr>" and input_5_value == "</td>" and input_6_value == "<tr>":
            action [lambda: IncrementRecitation10(), Jump("if_ln19_correct")]
        else:
            action ShowMenu("error_msg_nine")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("table_hint")
    


    hbox:
        xpos 160
        ypos 250
            
        vbox:
            ############### INPUTS ###############
            text "Complete the code\n" size 32 color "#ffffff" xoffset 6 yoffset 6
            hbox:


                if active_input == 1:
                    input:
                        style_prefix "my"
                        xoffset 6
                        yoffset 6
                        size 28
                        length 10
                        value ScreenVariableInputValue("input_1_value")
                            
                else:
                    textbutton '"[input_1_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28 
                        action SetScreenVariable("active_input", 1)

            hbox:
                text "  <tr>" size 28 color "#ffffff" xoffset 6 yoffset 6
            
            hbox:
                text "  " size 28 color "#ffffff" xoffset 6 yoffset 6
            
                if active_input == 2:
                    input:
                        style_prefix "my"
                        xoffset 6
                        yoffset 6
                        size 28
                        length 10
                        value ScreenVariableInputValue("input_2_value")
                            
                else:
                    textbutton '"[input_2_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28 
                        action SetScreenVariable("active_input", 2)

                text 'H1</th><th>H2' size 28 color "#ffffff" xoffset 6 yoffset 6

                if active_input == 3:
                    input:
                        style_prefix "my"
                        xoffset 6
                        yoffset 6
                        size 28
                        length 10
                        value ScreenVariableInputValue("input_3_value")
                            
                else:
                    textbutton '"[input_3_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28 
                        action SetScreenVariable("active_input", 3)


            hbox:
                text "  " size 28 color "#ffffff" xoffset 6 yoffset 6
                if active_input == 4:
                    input:
                        style_prefix "my"
                        xoffset 6
                        yoffset 6
                        size 28
                        length 10
                        value ScreenVariableInputValue("input_4_value")
                            
                else:
                    textbutton '"[input_4_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28 
                        action SetScreenVariable("active_input", 4)



            hbox:
                text "  <tr>" size 28 color "#ffffff" xoffset 6 yoffset 6

            
            hbox:
                text "      <td>A</td><td>B" size 28 color "#ffffff" xoffset 6 yoffset 6
                if active_input == 5:
                    input:
                        style_prefix "my"
                        xoffset 6
                        yoffset 6
                        size 28
                        length 10
                        value ScreenVariableInputValue("input_5_value")
                            
                else:
                    textbutton '"[input_5_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28 
                        action SetScreenVariable("active_input", 5)
            

            hbox:
                text "  </tr>" size 28 color "#ffffff" xoffset 6 yoffset 6

            hbox:
                text "  " size 28 color "#ffffff" xoffset 6 yoffset 6
                if active_input == 6:
                    input:
                        style_prefix "my"
                        xoffset 6
                        yoffset 6
                        size 28
                        length 10
                        value ScreenVariableInputValue("input_6_value")
                            
                else:
                    textbutton '"[input_6_value]"':
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28 
                        action SetScreenVariable("active_input", 6)

            hbox:
                text "  <td>C</td><td>D</td>" size 28 color "#ffffff" xoffset 6 yoffset 6
            hbox:
                text "  </tr>" size 28 color "#ffffff" xoffset 6 yoffset 6
            hbox:
                text "</table>" size 28 color "#ffffff" xoffset 6 yoffset 6
                



###########################################################################################################################