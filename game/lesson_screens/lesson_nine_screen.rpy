











default ans_fnn_o1_was_dropped = False
screen lesson_nine_ls1_fill():
    image "images/lesson_nine/lesson 9.1.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_fnn_o1_was_dropped:
            action Jump("lessonNineFillTwo") 
        else:
            action Jump("if_lnn1_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("div_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_nn1")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lnn_1
            text "<div>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 479
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lnn_1
            text "</div>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 520
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


screen lesson_nine_ls4_fill():
    image "images/lesson_nine/lesson 9.4.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_nn_four") 


###########################################################################################################################


screen error_msg_nine():
    image "images/lesson_eight/lesson 8.22.png" 
        
    text "Error!!!" size 28 color "#ffffff" xpos 160 ypos 191 xoffset 6 yoffset 6
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"
        action Return()


###########################################################################################################################


screen lesson_nine_ls5_fill():
    image "images/lesson_eight/lesson 8.22.png" 
    default input_1_value = ""
    default input_2_value = ""
    default input_3_value = ""
    default input_4_value = ""
    default input_5_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if input_1_value == "" and input_2_value == "" and input_3_value == "" and input_4_value == "" and input_5_value == "":
            action ShowMenu("error_msg_nine")
        elif input_1_value == "<div>" and input_2_value == "<h2>" and input_3_value == "</h2>" and input_4_value == "<p>" and input_5_value == "src":
            action Jump("if_ln5_correct")
        else:
            action ShowMenu("error_msg_nine")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("div_hint")


    hbox:
        xpos 160
        ypos 191
            
        vbox:
            ############### INPUTS ###############
            text "{b}Complete the code to group the HTML elements{/b}\n\n\n\n\n\n" size 28 color "#ffffff" xoffset 6 yoffset 6


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

                text 'Heading 2 ' size 28 color "#ffffff" xoffset 6 yoffset 6

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

                text 'Paragraph </p>' size 28 color "#ffffff" xoffset 6 yoffset 6


            hbox:

                text '<img ' size 28 color "#ffffff" xoffset 6 yoffset 6

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

                text '="url">' size 28 color "#ffffff" xoffset 6 yoffset 6

            hbox:

                text '</div>' size 28 color "#ffffff" xoffset 6 yoffset 6


###########################################################################################################################


screen lesson_nine_ls7_fill():
    image "images/lesson_nine/lesson 9.7.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_nn_seven") 


###########################################################################################################################


screen lesson_nine_ls9_fill():
    image "images/lesson_eight/lesson 8.22.png" 
    default input_1_value = ""
    default input_2_value = ""
    default input_3_value = ""
    default input_4_value = ""
    default input_5_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if input_1_value == "" and input_2_value == "" and input_3_value == "" and input_4_value == "" and input_5_value == "":
            action ShowMenu("error_msg_nine")
        elif input_1_value == "<div>" and input_2_value == "<h2>" and input_3_value == "</h2>" and input_4_value == "<p>" and input_5_value == "src":
            action Jump("if_ln5_correct")
        else:
            action ShowMenu("error_msg_nine")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("div_hint")


    hbox:
        xpos 160
        ypos 191
            
        vbox:
            ############### INPUTS ###############
            text "{b}Complete the code to group the HTML elements{/b}\n\n\n\n\n\n" size 28 color "#ffffff" xoffset 6 yoffset 6


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

                text 'Heading 2 ' size 28 color "#ffffff" xoffset 6 yoffset 6

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

                text 'Paragraph </p>' size 28 color "#ffffff" xoffset 6 yoffset 6


            hbox:

                text '<img ' size 28 color "#ffffff" xoffset 6 yoffset 6

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

                text '="url>"' size 28 color "#ffffff" xoffset 6 yoffset 6

            hbox:

                text '</div>' size 28 color "#ffffff" xoffset 6 yoffset 6


###########################################################################################################################


screen lesson_nine_ls11_fill():
    image "images/lesson_nine/lesson 9.11.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_nn_eleven") 


###########################################################################################################################


default ans_fnn_twv1_was_dropped = False
default ans_fnn_twv2_was_dropped = False
screen lesson_nine_ls12_fill():
    image "images/lesson_nine/lesson 9.12.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"

        if ans_fnn_twv1_was_dropped and ans_fnn_twv2_was_dropped:
            action Jump("lessonNineFillThirteen") 
        else:
            action Jump("if_nnt12_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("div_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_nn12")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")


    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lnn_12
            text "blue" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 456
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lnn_12
            text "red" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 435
            ypos 387
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 409
            ypos 534
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


screen lesson_nine_ls17_fill():
    image "images/lesson_eight/lesson 8.22.png" 
    default input_1_value = ""
    default input_2_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if input_1_value == "" and input_2_value == "":
            action ShowMenu("error_msg_nine")
        elif input_1_value == "style" and input_2_value == "</div>":
            action Jump("if_ln17_correct")
        else:
            action ShowMenu("error_msg_nine")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("div_hint")


    hbox:
        xpos 160
        ypos 191
            
        vbox:
            ############### INPUTS ###############
            text "{b}Complete the code{/b}\n\n\n\n\n\n" size 28 color "#ffffff" xoffset 6 yoffset 6


            hbox:

                text '<div  ' size 28 color "#ffffff" xoffset 6 yoffset 6

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

                text '="text-align:center">' size 28 color "#ffffff" xoffset 6 yoffset 6
            
            hbox:
                text '   <h2>Heading 2</h2>' size 28 color "#ffffff" xoffset 6 yoffset 6
            hbox:
                text '   <h3>Heading 3</h3>' size 28 color "#ffffff" xoffset 6 yoffset 6
            hbox:
                text '   <p>Paragraph</p>' size 28 color "#ffffff" xoffset 6 yoffset 6

            hbox:

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



###########################################################################################################################