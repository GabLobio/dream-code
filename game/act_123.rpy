python:

    if problem_1 == "<h1>":
        l1act()
                
    if problem_2 == "</h2>":
        l1act()

    if problem_3 == "</h3>":
        l1act()

    if problem_4 == "button":
        l1act()

    if problem_5 == "p":
        l1act()




init python:
    def l1act1():
        persistent.lesson_1_act1 += 10
    def l1actR():
        persistent.lesson_1_act1 += renpy.random.randint(1, 6)


##### Lesson 1 Activity #######################################################################################

screen l1act1():
    image "images/activity1.png" 
    default active_input = 0
    default problem_1 = ""
    default problem_2 = ""
    default problem_3 = ""
    default problem_4 = ""
    default problem_5 = ""

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"


        if problem_1 == "<p>" and problem_2 == "button" and problem_3 == "span" and problem_4 == "img" and problem_5 == "p":
            action [lambda: l1act1(), Jump("l1_act1_f")]

        elif problem_1 != "" and problem_2 != "" and problem_3 != "" and problem_4 != "" and problem_5 != "":
            action [lambda: l1actR(), Jump("l1_act1_f")]
        
        else:
            action ShowMenu("error_msg_nine")
    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            if active_input == 1:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_1")
                            
            else:
                textbutton '([problem_1])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 1)

            text " This is a paragraph. </p>\n" size 28  color "#ffffff" xoffset 6 yoffset 6

        hbox:

            text "<button> Click me </" size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 2:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_2")
                            
            else:
                textbutton '([problem_2])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 2)
            text ">\n" size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:
            text "<span> This is a span element. </" size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 3:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_3")
                            
            else:
                textbutton '([problem_3])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 3)
            text ">\n" size 28  color "#ffffff" xoffset 6 yoffset 6

        
        hbox:
            text "< " size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 4:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_4")
                            
            else:
                textbutton '([problem_4])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 4)
            text  ' src="image.jpg" alt="Image Description"> \n' size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:

            text "<" size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 5:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_5")
                            
            else:
                textbutton '([problem_5])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 5)
            text "> Another paragraph. </p>\n" size 28  color "#ffffff" xoffset 6 yoffset 6







init python:
    def l2act2():
        persistent.lesson_2_act2 += 10
    def l2actR():
        persistent.lesson_2_act2 += renpy.random.randint(1, 6)

##### Lesson 2 Activity #######################################################################################

screen l2act2():
    image "images/activity1.png" 
    default active_input = 0
    default problem_1 = ""
    default problem_2 = ""
    default problem_3 = ""
    default problem_4 = ""
    default problem_5 = ""

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"

        if problem_1 == "<h1>" and problem_2 == "</h2>" and problem_3 == "</h3>" and problem_4 == "h4" and problem_5 == "h5":
            action [lambda: l2act2(), Jump("l2_act2_f")]
        elif problem_1 != "" and problem_2 != "" and problem_3 != "" and problem_4 != "" and problem_5 != "":
            action [lambda: l2actR(), Jump("l2_act2_f")]
        else:
            action ShowMenu("error_msg_nine")

    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            if active_input == 1:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_1")
                            
            else:
                textbutton '([problem_1])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 1)

            text " Heading 1" size 28  color "#ffffff" xoffset 6 yoffset 6

            text " </h1>\n" size 28  color "#ffffff" xoffset 6 yoffset 6

        hbox:

            text "<h2> Heading 2 " size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 2:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_2")
                            
            else:
                textbutton '([problem_2])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 2)
            text "\n" size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:
            text "<h3> Heading 3 " size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 3:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_3")
                            
            else:
                textbutton '([problem_3])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 3)
            text "\n" size 28  color "#ffffff" xoffset 6 yoffset 6

        
        hbox:
            text "<" size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 4:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_4")
                            
            else:
                textbutton '([problem_4])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 4)
            text "> Heading 4 </h4>\n" size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:

            text "<" size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 5:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_5")
                            
            else:
                textbutton '([problem_5])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 5)
            text "> Heading 5 </h5>\n" size 28  color "#ffffff" xoffset 6 yoffset 6





init python:
    def l3act3():
        persistent.lesson_3_act3 += 10
    def l3actR():
        persistent.lesson_3_act3 += renpy.random.randint(1, 6)

##### Lesson 2 Activity #######################################################################################

screen l3act3():
    image "images/activity1.png" 
    default active_input = 0
    default problem_1 = ""
    default problem_2 = ""
    default problem_3 = ""
    default problem_4 = ""
    default problem_5 = ""

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"

        if problem_1 == "<!--" and problem_2 == "</title>" and problem_3 == "</body>" and problem_4 == "<strong>" and problem_5 == "em":
            action [lambda: l3act3(), Jump("l3_act3_f")]
        elif problem_1 != "" and problem_2 != "" and problem_3 != "" and problem_4 != "" and problem_5 != "":
            action [lambda: l3actR(), Jump("l3_act3_f")]
        else:
            action ShowMenu("error_msg_nine")

    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            if active_input == 1:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_1")
                            
            else:
                textbutton '([problem_1])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 1)

            text " This is a comment. -->\n" size 28  color "#ffffff" xoffset 6 yoffset 6

        hbox:

            text "<title> Your Title " size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 2:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_2")
                            
            else:
                textbutton '([problem_2])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 2)
            
            text "\n" size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:
            text "<body> Body " size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 3:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_3")
                            
            else:
                textbutton '([problem_3])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 3)
            text "\n" size 28  color "#ffffff" xoffset 6 yoffset 6

        
        hbox:
            text "" size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 4:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_4")
                            
            else:
                textbutton '([problem_4])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 4)
            text " This text is strong. </strong>\n" size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:

            text "<" size 28  color "#ffffff" xoffset 6 yoffset 6
            if active_input == 5:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 28
                    length 10
                    value ScreenVariableInputValue("problem_5")
                            
            else:
                textbutton '([problem_5])':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28
                    action SetScreenVariable("active_input", 5)
            text ">This text is emphasized.</em>>\n" size 28  color "#ffffff" xoffset 6 yoffset 6

