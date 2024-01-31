default ans_f0_was_dropped = False

init python:
    def IncrementRecitation2():
        persistent.ast1_recitation += 5
        persistent.ast1_accuracy += 5

screen lesson_two_ls1_fill():
    image "images/lesson_two/Lesson 2.1.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
         
        if  ans_f0_was_dropped:
            action [lambda: IncrementRecitation2(), Jump("lessonTwoFilltwo")]
        else:
            action Jump("if_lt1_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("head_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_t1")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 510
            ypos 857
            
            drag_raise True
            drag_name "answer_h1"
            dragged dragged_func_lt_1
            text "<h1>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 380
            ypos 857
            
            drag_raise True
            drag_name "answer_p"
            dragged dragged_func_lt_1
            text "<p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        

        
        
        # Drop Place
        drag:
            xpos 567 
            ypos 367
            drag_raise True
            drag_name "h1_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################
default ans_ft_was_dropped = False

screen lesson_two_ls2_fill():
    image "images/lesson_two/Lesson 2.2.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ft_was_dropped:
            action Jump("lessonTwoFillThree") 
        else:
            action Jump("if_lt2_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("head_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_t2")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 
    draggroup:

        # Draggables
        drag:
            xpos 440
            ypos 857
            
            drag_raise True
            drag_name "answer_/h2"
            dragged dragged_func_lt_2
            text "</h2>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 327
            ypos 857
            
            drag_raise True
            drag_name "answer_h2"
            dragged dragged_func_lt_2
            text "<h2>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        

        
        
        # Drop Place
        drag:
            xpos 500 
            ypos 365
            drag_raise True
            drag_name "h2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################

screen lesson_two_ls4_fill():
    image "images/lesson_two/Lesson 2.4.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run") 


###########################################################################################################################

screen lesson_two_ls5_fill():
    image "images/lesson_two/Lesson 2.5.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_two") 


###########################################################################################################################


screen lesson_two_ls6_fill():
    image "images/ftg_bg.png"
    default line_one_value = ""
    default line_two_value = ""
    default line_three_value = ""
    default line_four_value = ""
    default line_five_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("head_hint")

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if line_one_value == "" and line_two_value == "" and line_three_value == "" and line_four_value == "" and line_five_value == "":
            action ShowMenu("error_msg")
        elif line_one_value == "</h1>" and line_two_value == "<p>" and line_three_value == "<h2>" and line_four_value == "</p>" and line_five_value == "<button>":
            action [lambda: IncrementRecitation2(), Jump("if_lt5_correct")]
        else:
            action ShowMenu("error_msg")

    


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

                text "<h1>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "  Mexico " size 28 color "#4E4E4E" xoffset 6 yoffset 6

                if active_input == 1:
                    input:
                        xoffset 6
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_one_value")
                            
                else:
                    textbutton "[line_one_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 1)
                        
            hbox:
                textbutton "2":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 2)

                
                if active_input == 2:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_two_value") 
                else:
                    textbutton "[line_two_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 2)
                        
                text " Introduction..." size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "</p>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
            
            hbox:
                textbutton "3":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 3)

                
                if active_input == 3:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_three_value")
                else:
                    textbutton "[line_three_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 3)
                        
                text " Food in Mexico" size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "</h2>" size 28 color "#4E4E4E" xoffset 6 yoffset 6


            hbox:
                textbutton "4":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 4)

                text "<p>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "Tacos " size 28 color "#4E4E4E" xoffset 6 yoffset 6
                
                if active_input == 4:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_four_value") 
                else:
                    textbutton "[line_four_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 4)
                        
            hbox:
                textbutton "5":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 5)

                
                if active_input == 5:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_five_value") 
                else:
                    textbutton "[line_five_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 5)
                        
                text " Order Now" size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "</button>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
               
        


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

screen wrong_input_modal():
    modal True
    text "Wrong input. Please try again."
    textbutton "OK":
        action Return()


########################################################################################################################### 

screen lesson_two_ls7_fill():
    image "images/ftg_bg.png"
    default line_one_value = ""
    default line_two_value = ""
    default line_three_value = ""
    default line_four_value = ""
    default line_five_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("head_hint")

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if line_one_value == "" and line_two_value == "" and line_three_value == "" and line_four_value == "" and line_five_value == "":
            action ShowMenu("error_msg")
        elif line_one_value == "</h1>" and line_two_value == "<p>" and line_three_value == "<h2>" and line_four_value == "</p>" and line_five_value == "<button>":
            action [lambda: IncrementRecitation2(), Jump("if_lt5_correct")]
        else:
            action ShowMenu("error_msg")
    


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

                text "<h1>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "  Mexico " size 28 color "#4E4E4E" xoffset 6 yoffset 6

                text " " size 28 color "#4E4E4E" xoffset 6 yoffset 6
                if active_input == 1:
                    input:
                        xoffset 6   
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_one_value")
                            
                else:
                    textbutton "[line_one_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 1)
                        
            hbox:
                textbutton "2":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 2)

                
                if active_input == 2:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_two_value") 
                else:
                    textbutton "[line_two_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 2)
                        
                text " Introduction..." size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "</p>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
            
            hbox:
                textbutton "3":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 3)

                
                if active_input == 3:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_three_value")
                else:
                    textbutton "[line_three_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 3)
                        
                text " Food in Mexico" size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "</h2>" size 28 color "#4E4E4E" xoffset 6 yoffset 6


            hbox:
                textbutton "4":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 4)

                text "<p>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "Tacos " size 28 color "#4E4E4E" xoffset 6 yoffset 6
                
                if active_input == 4:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_four_value") 
                else:
                    textbutton "[line_four_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 4)
                        
            hbox:
                textbutton "5":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 5)

                
                if active_input == 5:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 28
                        length 10
                        value ScreenVariableInputValue("line_five_value") 
                else:
                    textbutton "[line_five_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 5)
                        
                text " Order Now" size 28 color "#4E4E4E" xoffset 6 yoffset 6
                text "</button>" size 28 color "#4E4E4E" xoffset 6 yoffset 6
               
        


###########################################################################################################################


default ans_fs1_was_dropped = False
default ans_fs2_was_dropped = False
screen lesson_two_ls7_fill():
    image "images/lesson_two/Lesson 2.7.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_fs1_was_dropped and ans_fs2_was_dropped:
            action [lambda: IncrementRecitation2(), Jump("lessonTwoFillEight")]
        else:
            action Jump("if_lt7_wrong")
        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("head_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_t7")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 327
            ypos 857
            
            drag_raise True
            drag_name "answer_h2"
            dragged dragged_func_lt_7
            text "<h2>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 430
            ypos 857
            
            drag_raise True
            drag_name "answer_/h2"
            dragged dragged_func_lt_7
            text "</h2>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        

        
        
        # Drop Place
        drag:
            xpos 177 
            ypos 426
            drag_raise True
            drag_name "h2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)

        drag:
            xpos 400 
            ypos 426
            drag_raise True
            drag_name "/h2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


default ans_fe1_was_dropped = False
default ans_fe2_was_dropped = False
default ans_fe3_was_dropped = False
screen lesson_two_ls8_fill():
    image "images/lesson_two/Lesson 2.8.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_fe1_was_dropped and ans_fe2_was_dropped and ans_fe2_was_dropped:
            action Jump("lessonTwoFillNine") 
        else:
            action Jump("if_lt8_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("head_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_t8")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 327
            ypos 760
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lt_8
            text "<h1> Best Product Ever </h1>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 327
            ypos 810
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lt_8
            text "<h2> Product Features </h2>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 327
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lt_8
            text "<h3> About Feature #1 </h3>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        

        
        
        # Drop Place
        drag:
            xpos 160 
            ypos 375
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(201,30)

        drag:
            xpos 160 
            ypos 425
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(201,30)

        drag:
            xpos 160 
            ypos 470
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(201,30)


###########################################################################################################################


default ans_fn1_was_dropped = False
screen lesson_two_ls9_fill():
    image "images/lesson_two/Lesson 2.9.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if   ans_fn1_was_dropped:
            action Jump("lessonTwoFillTen") 
        else:
            action Jump("if_lt9_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_t9")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 

    draggroup:

        # Draggables
        drag:
            xpos 327
            ypos 820
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lt_9
            text "Empty tags" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 327
            ypos 860
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lt_9
            text "Container tags" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 160 
            ypos 420
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(500,30)


###########################################################################################################################


default ans_ft01_was_dropped = False
default ans_ft02_was_dropped = False
screen lesson_two_ls10_fill():
    image "images/lesson_two/Lesson 2.10.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if   ans_ft01_was_dropped and ans_ft02_was_dropped:
            action [lambda: IncrementRecitation2(), Jump("lessonHeadTakeaways")]
        else:
            action Jump("if_lt10_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("img_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_t10")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 
 

    draggroup:

        # Draggables
        drag:
            xpos 327
            ypos 860
            
            drag_raise True
            drag_name "answer_02"
            dragged dragged_func_lt_10
            text "<img>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 460
            ypos 860
            
            drag_raise True
            drag_name "answer_01"
            dragged dragged_func_lt_10
            text "<h1></h1>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

  
        
        # Drop Place
        drag:
            xpos 395 
            ypos 375
            drag_raise True
            drag_name "01_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)

        drag:
            xpos 395 
            ypos 425
            drag_raise True
            drag_name "02_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


default ans_fe01_was_dropped = False
screen lesson_two_ls11_fill():
    image "images/lesson_two/Lesson 2.11.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if   ans_fe01_was_dropped:
            action Jump("lessonTwoFillTwelve") 
        else:
            action Jump("if_lt11_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("img_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_11")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 
 

    draggroup:

        # Draggables
        drag:
            xpos 460
            ypos 860
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lt_11
            text "<img></img>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 327
            ypos 860
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lt_11
            text "<img>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 160 
            ypos 380
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(301,30)


###########################################################################################################################


default ans_ftw01_was_dropped = False
screen lesson_two_ls12_fill():
    image "images/lesson_two/Lesson 2.12.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if   ans_ftw01_was_dropped:
            action Jump("lessonTwoFillThirteen") 
        else:
            action Jump("if_lt12_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("img_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_12")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button") 

 

    draggroup:

        # Draggables
        drag:
            xpos 420
            ypos 860
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lt_12
            text "p" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 327
            ypos 860
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lt_12
            text "img" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 195 
            ypos 380
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


default ans_fth01_was_dropped = False
screen lesson_two_ls13_fill():
    image "images/lesson_two/Lesson 2.13.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_fth01_was_dropped:
            action Jump("lessonTwoFillFourteen") 
        else:
            action Jump("if_lt13_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("img_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_13")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 420
            ypos 860
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lt_13
            text "h1" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 327
            ypos 860
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lt_13
            text "src" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 270 
            ypos 380
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


screen lesson_two_ls14_fill():
    image "images/lesson_two/Lesson 2.14.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_14") 


###########################################################################################################################


default ans_ffit01_was_dropped = False
screen lesson_two_ls15_fill():
    image "images/lesson_two/Lesson 2.15.png" #blur 10.0
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ffit01_was_dropped:
            action Jump("lessonTwoFillSixteen") 
        else:
            action Jump("if_lt15_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("img_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_15")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 420
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lt_15
            text "</p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 627
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lt_15
            text "https://www.img.png" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        

        
        
        # Drop Place
        drag:
            xpos 370 
            ypos 380
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(300,30)


###########################################################################################################################


screen lesson_two_ls16_fill():
    image "images/lesson_two/Lesson 2.16.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_16") 


###########################################################################################################################


screen lesson_two_ls17_fill():
    image "images/lesson_two/Lesson 2.17.png" #blur 10.0
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_17") 


###########################################################################################################################


screen lesson_two_ls18_fill():
    image "images/ftg_bg.png"
    default line_one_value = ""
    default line_two_value = ""
    default line_three_value = ""

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if line_one_value == "" and line_two_value == "" and line_three_value == "":
            action ShowMenu("error_msg")
        elif line_one_value == "/" and line_two_value == '"' and line_three_value == "<button>":
            action Jump("if_lt18_correct")
        else:
            action ShowMenu("error_msg")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("img_hint")



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

                text "<p>" size 24 color "#4E4E4E" xoffset 6 yoffset 6
                text "  Save the trees " size 24 color "#4E4E4E" xoffset 6 yoffset 6

                text "<" size 24 color "#4E4E4E" xoffset 6 yoffset 6
                if active_input == 1:
                    input:
                        xoffset 6
                        yoffset 6
                        color "#ff9900"
                        size 24
                        length 5
                        value ScreenVariableInputValue("line_one_value")
                            
                else:
                    textbutton "[line_one_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 1)
                text "p>" size 24 color "#4E4E4E" xoffset 6 yoffset 6
                        
            hbox:
                textbutton "2":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 2)

                text "<img src=" size 24 color "#4E4E4E" xoffset 6 yoffset 6
                if active_input == 2:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 24
                        length 3
                        value ScreenVariableInputValue("line_two_value") 
                else:
                    textbutton "[line_two_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 2)
                        
                text 'http://www.google.com/images/tree.jpg">' size 24 color "#4E4E4E" xoffset 6 yoffset 6

            hbox:
                textbutton "3":
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 28  
                    action SetScreenVariable("active_input", 3)

                
                if active_input == 3:
                    input:
                        xoffset 6 
                        yoffset 6
                        color "#ff9900"
                        size 24
                        length 10
                        value ScreenVariableInputValue("line_three_value")
                else:
                    textbutton "[line_three_value]":
                        xoffset 6 
                        yoffset 6
                        text_color "#ff9900"  # Set the text color here\
                        text_hover_color "#ffffff"
                        text_selected_color "#ff9900"
                        text_size 28
                        action SetScreenVariable("active_input", 3)
                        
                text "Click Me</button>" size 24 color "#4E4E4E" xoffset 6 yoffset 6
               
        


########################################################################################################################### 