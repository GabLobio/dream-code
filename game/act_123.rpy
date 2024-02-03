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

##### Lesson 3 Activity #######################################################################################

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



init python:
    def l4act4():
        persistent.lesson_4_act4 += 10
    def l4actR():
        persistent.lesson_4_act4 += renpy.random.randint(1, 6)

##### Lesson 4 Activity #######################################################################################

screen l4act4():
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

        if problem_1 == "href" and problem_2 == "li" and problem_3 == "<ol>" and problem_4 == "</ul>" and problem_5 == "a":
            action [lambda: l4act4(), Jump("l4_act4_f")]
        elif problem_1 != "" and problem_2 != "" and problem_3 != "" and problem_4 != "" and problem_5 != "":
            action [lambda: l4actR(), Jump("l4_act4_f")]
        else:
            action ShowMenu("error_msg_nine")

    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            text '<a ' size 28  color "#ffffff" xoffset 6 yoffset 6
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

            text '="https://example.com">Visit Example.com</a>\n' size 28  color "#ffffff" xoffset 6 yoffset 6

        hbox:

            text "<li>Item 1</" size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text "<li> Item 1 </li> </ol>\n" size 28  color "#ffffff" xoffset 6 yoffset 6

        
        hbox:
            text "<ul> <li> Item 1 </li> " size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text "\n" size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:

            text '<a href="https://example.com">Visit Example.com</' size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text ">\n" size 28  color "#ffffff" xoffset 6 yoffset 6




init python:
    def l5act5():
        persistent.lesson_5_act5 += 10
    def l5actR():
        persistent.lesson_5_act5 += renpy.random.randint(1, 6)

##### Lesson 5 Activity #######################################################################################

screen l5act5():
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

        if problem_1 == "width" and problem_2 == "</form>" and problem_3 == "alt":
            action [lambda: l5act5(), Jump("l5_act5_f")]
        elif problem_1 != "" and problem_2 != "" and problem_3 != "":
            action [lambda: l5actR(), Jump("l5_act5_f")]
        else:
            action ShowMenu("error_msg_nine")

    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            text '<img src="dog.png" ' size 28  color "#ffffff" xoffset 6 yoffset 6
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

            text '="300">\n' size 28  color "#ffffff" xoffset 6 yoffset 6

        hbox:

            text "<form> Your Form Here " size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text '<img src="image.jpg" ' size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text '="Image Description" width="300">' size 28  color "#ffffff" xoffset 6 yoffset 6




init python:
    def l6act6():
        persistent.lesson_6_act6 += 10
    def l6actR():
        persistent.lesson_6_act6 += renpy.random.randint(1, 6)

##### Lesson 6 Activity #######################################################################################

screen l6act6():
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

        if problem_1 == "video" and problem_2 == "audio" and problem_3 == "/select" and problem_4 == "</option>":
            action [lambda: l6act6(), Jump("l6_act6_f")]
        elif problem_1 != "" and problem_2 != "" and problem_3 != "" and problem_4 != "":
            action [lambda: l6actR(), Jump("l6_act6_f")]
        else:
            action ShowMenu("error_msg_nine")

    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            text '<' size 28  color "#ffffff" xoffset 6 yoffset 6
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

            text ' src="video.mp4" A video tag </video>\n' size 28  color "#ffffff" xoffset 6 yoffset 6

        hbox:

            text "<" size 28  color "#ffffff" xoffset 6 yoffset 6
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
            
            text ' src="audio.mp3" A audio tag </video>\n' size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:
            text "<select> Options here <" size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text "<option> Option tag " size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text "\n" size 28  color "#ffffff" xoffset 6 yoffset 6




init python:
    def l7act7():
        persistent.lesson_7_act7 += 10
    def l7actR():
        persistent.lesson_7_act7 += renpy.random.randint(1, 6)

##### Lesson 7 Activity #######################################################################################

screen l7act7():
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

        if problem_1 == "<header>" and problem_2 == "</main>" and problem_3 == "<footer>":
            action [lambda: l7act7(), Jump("l7_act7_f")]
        elif problem_1 != "" and problem_2 != "" and problem_3 != "":
            action [lambda: l7actR(), Jump("l7_act7_f")]
        else:
            action ShowMenu("error_msg_nine")

    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            text '' size 28  color "#ffffff" xoffset 6 yoffset 6
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

            text ' Header Section </header>\n' size 28  color "#ffffff" xoffset 6 yoffset 6

        hbox:

            text "<main> Main Section " size 28  color "#ffffff" xoffset 6 yoffset 6
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
            
            text '\n' size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:
            text "" size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text " Footer Section </footer>\n" size 28  color "#ffffff" xoffset 6 yoffset 6




init python:
    def l8act8():
        persistent.lesson_8_act8 += 10
    def l8actR():
        persistent.lesson_8_act8 += renpy.random.randint(1, 6)

##### Lesson 8 Activity #######################################################################################

screen l8act8():
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

        if problem_1 == "blue" and problem_2 == "style" and problem_3 == "color":
            action [lambda: l8act8(), Jump("l8_act8_f")]
        elif problem_1 != "" and problem_2 != "" and problem_3 != "":
            action [lambda: l8actR(), Jump("l8_act8_f")]
        else:
            action ShowMenu("error_msg_nine")

    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            text '<p style="color: ' size 28  color "#ffffff" xoffset 6 yoffset 6
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

            text ';"> This text is blue. </p>\n' size 28  color "#ffffff" xoffset 6 yoffset 6

        hbox:

            text "<h2 " size 28  color "#ffffff" xoffset 6 yoffset 6
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
            
            text '="font-size: 24px;"> This heading has a font size of 24 pixels. </h2>\n' size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:
            text '<p style="' size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text ': green;"> This text is green. </p>' size 28  color "#ffffff" xoffset 6 yoffset 6




init python:
    def l9act9():
        persistent.lesson_9_act9 += 10
    def l9actR():
        persistent.lesson_9_act9 += renpy.random.randint(1, 6)

##### Lesson 9 Activity #######################################################################################

screen l9act9():
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

        if problem_1 == "style" and problem_2 == "</div>" and problem_3 == "</div>":
            action [lambda: l9act9(), Jump("l9_act9_f")]
        elif problem_1 != "" and problem_2 != "" and problem_3 != "":
            action [lambda: l9actR(), Jump("l9_act9_f")]
        else:
            action ShowMenu("error_msg_nine")

    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            text '<div ' size 28  color "#ffffff" xoffset 6 yoffset 6

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

            text ';"> This text is blue. </p>\n' size 28  color "#ffffff" xoffset 6 yoffset 6

   

            text '="color: blue"> Your Div Content Here ' size 28  color "#ffffff" xoffset 6 yoffset 6
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
            
            text '\n' size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:
            text '<div style="color: green"> Your Div Content Here ' size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text '' size 28  color "#ffffff" xoffset 6 yoffset 6




init python:
    def l10act10():
        persistent.lesson_10_act10 += 10
    def l10actR():
        persistent.lesson_10_act10 += renpy.random.randint(1, 6)

##### Lesson 10 Activity #######################################################################################

screen l10act10():
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

        if problem_1 == "</table>" and problem_2 == "<tr>" and problem_3 == "</td>":
            action [lambda: l10act10(), Jump("l10_act10_f")]
        elif problem_1 != "" and problem_2 != "" and problem_3 != "":
            action [lambda: l10actR(), Jump("l10_act10_f")]
        else:
            action ShowMenu("error_msg_nine")

    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 160
        ypos 350

        hbox:
            text '<table> <tr><td> Table Data 1 </td></tr>' size 28  color "#ffffff" xoffset 6 yoffset 6

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

            text '\n' size 28  color "#ffffff" xoffset 6 yoffset 6

   
        hbox:

            text '<table> ' size 28  color "#ffffff" xoffset 6 yoffset 6
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
            
            text '<td> Table Data 2 </td></tr></table>\n' size 28  color "#ffffff" xoffset 6 yoffset 6


        hbox:
            text '<table> <tr><td> Table Data 3 ' size 28  color "#ffffff" xoffset 6 yoffset 6
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
            text '</tr></table>' size 28  color "#ffffff" xoffset 6 yoffset 6
