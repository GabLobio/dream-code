


screen classroom_ui():
    image "images/bg_classroom.png"

    imagebutton:
        xpos 1233
        ypos 478
        idle "images/mrs_rodriguez_button.png"
        hover "images/mrs_rodriguez_button_hover.png"
        action Jump("lesson_choices")




screen lesson_ui():
    image "images/bg_lesson_choices.png" 
    
    imagebutton:
        xpos 50
        ypos 30
        idle "images/interactive_button/exit_button.png"
        hover "images/interactive_button/exit_button_hover.png"
        action MainMenu()

    imagebutton:
        xpos 436
        ypos 200
        idle "images/interactive_button/btn_lesson_1.png"
        hover "images/interactive_button/hover_lesson_1.png"
        action Jump("lesson_one")


    imagebutton:
        xpos 436
        ypos 330
        idle "images/interactive_button/btn_lesson_2.png"
        hover "images/interactive_button/hover_lesson_2.png"
        action Jump("lesson_two")


    imagebutton:
        xpos 436
        ypos 460
        idle "images/interactive_button/btn_lesson_3.png"
        hover "images/interactive_button/hover_lesson_3.png"
        action Jump("lesson_three")


    imagebutton:
        xpos 436
        ypos 590
        idle "images/interactive_button/btn_lesson_4.png"
        hover "images/interactive_button/hover_lesson_4.png"
        action Jump("lesson_four")


    imagebutton:
        xpos 436
        ypos 720
        idle "images/interactive_button/btn_lesson_5.png"
        hover "images/interactive_button/hover_lesson_5.png"
        action Jump("lesson_five")


    imagebutton:
        xpos 986
        ypos 200
        idle "images/interactive_button/btn_lesson_6.png"
        hover "images/interactive_button/hover_lesson_6.png"
        action Jump("lesson_six")


    imagebutton:
        xpos 986
        ypos 330
        idle "images/interactive_button/btn_lesson_7.png"
        hover "images/interactive_button/hover_lesson_7.png"
        action Jump("lesson_seven")   
    
    
    imagebutton:
        xpos 986
        ypos 460
        idle "images/interactive_button/btn_lesson_8.png"
        hover "images/interactive_button/hover_lesson_8.png"
        action Jump("lesson_eight")


    imagebutton:
        xpos 986
        ypos 590
        idle "images/interactive_button/btn_lesson_9.png"
        hover "images/interactive_button/hover_lesson_9.png"
        action Jump("lesson_nine")


    imagebutton:
        xpos 986
        ypos 720
        idle "images/interactive_button/btn_lesson_10.png"
        hover "images/interactive_button/hover_lesson_10.png"
        action Jump("lesson_ten")  


    #imagebutton:
        #xpos 100
        #ypos 900
        #idle "images/interactive_button/btn_Return.png"
        #hover "images/interactive_button/hover_Return.png"
        #action Jump("main_menu_call_from_progress")         
       





###########################################################################################################################


screen error_msg_final_test():
    image "images/final_browser_screen.png"
    vbox:
        text "Error" size 24 color "#c00000" xpos 105 ypos 210 xoffset 6 yoffset 6
        text "Please, check every line for any errors or mispelled" size 24 color "#c00000" xpos 105 ypos 210 xoffset 6 yoffset 6

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"
        action Return()

###########################################################################################################################


screen final_screen():
    image "images/final_screen.png" 

    default input_title = "?"
    default input_img_src = "?"
    default section_1 = "?"

    default section_2_href = "?"
    default section_2 = "?"

    default id_section_1 = "?"
    default section_1_number = "?"
    default section_1_name = "name"
    default section_1_color = "?"
    default section_1_why = "why?"

    default section_2_number = "?"
    default section_2_name = "name"
    default section_2_color = "?"
    default section_2_why = "why?"

    default line_33_div = "?"
    default line_34_for = "?"

    default line_36_tag = "?"
    default line_37_tag = "?"

    default line_38_select = "?"

    default line_41_control = "?"
    default line_42_src = "?"

    default active_input = 0

    imagebutton:
        xpos 50
        ypos 30
        idle "images/interactive_button/exit_button.png"
        hover "images/interactive_button/exit_button_hover.png"
        action Jump("start")

    imagebutton:
        xpos 875
        ypos 30
        idle "images/interactive_button/task_button.png"
        hover "images/interactive_button/hover_task_button.png"
        action ShowMenu("task_final_test")

    imagebutton:
        xpos 1770
        ypos 30
        #text_color "#ff9900"  # Set the text color here\
        #text_hover_color "#ffffff"
        #text_selected_color "#ff9900"
        #text_size 46
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"

        if input_title == "":
            action ShowMenu("error_msg_final_test")
        elif input_title == "HTML Lesson" and input_img_src == '"mrs_rodriguez.png"' and section_1 == "Lesson 5" and section_2_href == "#section2" and section_2 == "Lesson 8" and id_section_1 == "section1" and section_1_number == "5" and section_1_name == "Attribute" and section_1_color == "blue" and section_1_why != "" and  section_2_number == "8" and section_2_name == "Style Attribute" and section_2_color == "red" and section_2_why != "" and line_33_div ==    "<div>" and line_34_for == "fav-tag" and line_36_tag == "Anchor Tag" and line_37_tag == "Video Tag" and line_38_select == "/select" and line_41_control == "loop" and line_42_src == "html_peter.webm":
            action Jump("congrats")
        else:
            action ShowMenu("error_msg_final_test")
 
    viewport:
            xpos 105
            ypos 210
            xysize (1710,790)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Complete the code{/b}\n\n" 

                    hbox:
                        textbutton "  1": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 1)
                        text "<html>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  2": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 2)
                        text "<head>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  3": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 3)

                        text "      <title>" size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 3:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("input_title")
                                    
                        else:
                            textbutton '[input_title]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 3)

                        text "</title>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  4": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 4)
                        text "</head>" size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "  5": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 5)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  6": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 6)
                        text "<body>" size 24 color "#cecece" xoffset 6 yoffset 6




                    hbox:
                        textbutton "  7": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 7)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  8": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 8)
                        text "      <div>" size 24 color "#cecece" xoffset 6 yoffset 6


                    hbox:
                        textbutton "  9": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 9)
                        text "          <h1>HTML</h1>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "10": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 10)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "11": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 11)

                        text '          <img src= ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 11:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 30
                                copypaste True
                                value ScreenVariableInputValue("input_img_src")
                                    
                        else:
                            textbutton '[input_img_src]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 11)

                        text 'alt="Mrs Rodriguez">' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "12": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 12)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "13": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 13)
                        text '          <p>Teacher Rodriguez</p>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "14": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 14)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "15": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 15)
                        text '          <p>My two favorite lesson:</p>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "16": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 16)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "17": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 17)
                        text "          <ul>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "18": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 18)

                        text '              <li><a href="#section1"> ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 18:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("section_1")
                                    
                        else:
                            textbutton '[section_1]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 18)
                        
                        text '</a></li>' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "19": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 19)
                        text '              <li><a href= ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 19:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("section_2_href")
                                    
                        else:
                            textbutton '[section_2_href]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 19)
                        
                        text '>' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 19.2:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("section_2")
                                    
                        else:
                            textbutton '[section_2]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 19.2)

                        text '</a></li>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "20": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 20)
                        text "          </ul>" size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "21": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 21)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6








                    hbox:
                        textbutton "22": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 22)
                        text '          <div id= ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 22:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("id_section_1")
                                    
                        else:
                            textbutton '[id_section_1]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 22)

                        text '>' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "23": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 23)
                        text '              <h2>Lesson ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 23:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("section_1_number")
                                    
                        else:
                            textbutton '[section_1_number]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 23)
                                
                        text ': ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 23.1:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("section_1_name")
                                    
                        else:
                            textbutton '[section_1_name]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 23.1)

                        text '</h2>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "24": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 24)
                        text '              <p style="color: ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 24:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("section_1_color")
                                    
                        else:
                            textbutton '[section_1_color]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 24)

                        text '">' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 24.1:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 200
                                copypaste True
                                value ScreenVariableInputValue("section_1_why")
                                    
                        else:
                            textbutton '[section_1_why]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 24.1)

                        text '</p>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "25": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 25)
                        text '          </div' size 24 color "#cecece" xoffset 6 yoffset 6
                    








                    hbox:
                        textbutton "26": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 26)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "27": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 27)
                        text '          <div id="section2">' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "28": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 28)
                        text '              <h2>Lesson ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 28:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("section_2_number")
                                    
                        else:
                            textbutton '[section_2_number]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 28)
                                
                        text ': ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 28.1:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("section_2_name")
                                    
                        else:
                            textbutton '[section_2_name]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 28.1)

                        text '</h2>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "29": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 29)
                        text '              <p style="color: ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 29:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("section_2_color")
                                    
                        else:
                            textbutton '[section_2_color]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 29)

                        text '">' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 29.1:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 200
                                copypaste True
                                value ScreenVariableInputValue("section_2_why")
                                    
                        else:
                            textbutton '[section_2_why]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 29.1)

                        text '</p>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "30": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 30)
                        text '          </div' size 24 color "#cecece" xoffset 6 yoffset 6

                    
                    hbox:
                        textbutton "31": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 31)
                        text "      </div>" size 24 color "#cecece" xoffset 6 yoffset 6





                    hbox:
                        textbutton "32": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 32)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6



                    hbox:
                        textbutton "33": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 33)
                        text "      " size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 33:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("line_33_div")
                                    
                        else:
                            textbutton '[line_33_div]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 33)
                    
                    hbox:
                        textbutton "34": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 34)
                        text '          <label for= ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 34:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("line_34_for")
                                    
                        else:
                            textbutton '[line_34_for]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 34)

                        text '>These are my two favorite element tag</label>' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "35": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 35)
                        text '          <select id="fav-tag">' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "36": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 36)
                        text '              <option> ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 36:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("line_36_tag")
                                    
                        else:
                            textbutton '[line_36_tag]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 36)

                        text '</option>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "37": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 37)
                        text '              <option> ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 37:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("line_37_tag")
                                    
                        else:
                            textbutton '[line_37_tag]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 37)

                        text '</option>' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "38": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 38)
                        text '          <' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 38:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("line_38_select")
                                    
                        else:
                            textbutton '[line_38_select]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 38)

                        text '>' size 24 color "#cecece" xoffset 6 yoffset 6




                    hbox:
                        textbutton "39": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 39)
                        text "      </div>" size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "40": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 40)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "41": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 40)
                        text "      <video " size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 41:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("line_41_control")
                                    
                        else:
                            textbutton '[line_41_control]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 41)

                        text ">" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "42": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 42)
                            
                        text '              <source src=" ' size 24 color "#cecece" xoffset 6 yoffset 6

                        if active_input == 42:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 25
                                copypaste True
                                value ScreenVariableInputValue("line_42_src")
                                    
                        else:
                            textbutton '[line_42_src]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 42)

                        text '" type="video/webm"' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "43": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 43)
                        text "      </video>" size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    
                    
                    
                    hbox:
                        textbutton "44": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 44)
                        text "</body>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "45": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 45)
                        text "</html>" size 24 color "#cecece" xoffset 6 yoffset 6

                    














