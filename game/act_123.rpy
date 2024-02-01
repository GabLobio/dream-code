


screen l1act1():
    image "images/lesson_eight/lesson 8.22.png" 
    default input_1_value = "_ _ _"

    default active_input = 0
    default max_input_length = 10

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if input_1_value == "":
            action Return()
        elif input_1_value == "<h2>":
            action Jump("if_ln19_correct")
        else:
            action Return()
    

    text "{b}Complete the tag\n{/  b}" size 48 color "#ffffff" xoffset 6 yoffset 6 xpos(494) ypos(151)
   
            
    vbox:
        ############### INPUTS ###############
        xpos 409
        ypos 500
        hbox:

            
            if active_input == 1:
                input:
                    style_prefix "my"
                    xoffset 6
                    yoffset 6
                    size 36
                    length 10
                    value ScreenVariableInputValue("input_1_value")
                            
            else:
                textbutton '[input_1_value]':
                    xoffset 6 
                    yoffset 6
                    text_color "#ff9900"  # Set the text color here\
                    text_hover_color "#ffffff"
                    text_selected_color "#ff9900"
                    text_size 36
                    action SetScreenVariable("active_input", 1)
            text " Heading 2" size 36  color "#ffffff" xoffset 6 yoffset 6

            text " </h2>" size 36  color "#ffffff" xoffset 6 yoffset 6