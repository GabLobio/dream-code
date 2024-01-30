
image html_peter = Movie(play="images/html_peter.webm")
#image main_menu = Movie(play="html_peter.webm")

screen final_browser():
    image "images/final_browser_screen.png"
    

    hbox:
        xpos 105
        ypos 160    
        text "{b}HTML Lesson{/b}" size 24 color "#3A3A3A"

    viewport:
            xpos 105
            ypos 210
            xysize (1710,790)   
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"



            hbox:
                    
                vbox:

                    #textbutton "Scroll Down" action Function(scroll_viewport, 50)  # Adjust the scrolling amount as needed
                    #textbutton "Scroll Up" action Function(scroll_viewport, -50)  # Adjust the scrolling amount as needed

                    hbox:
                        ############### INPUTS ###############
                        text "{b}HTML{/b}" size 42 color "#3A3A3A"
                    
                    hbox:
                        text "\n " size 20 color "#3A3A3A"

                    hbox:
                        image "images/mrs_rodriguez.png" xysize (111,188)

                
                    hbox:
                        text "\nTeacher Rodriguez" size 20 color "#3A3A3A"
                    
                    hbox:
                        text "\nMy two favorite lesson:" size 20 color "#3A3A3A"
                    
                    hbox:
                        text "\n    • {u}Lesson 5{/u}" size 20 color "#551AA9"
                    hbox:
                        text "    • {u}Lesson 8{/u}" size 20 color "#551AA9"

                    hbox:
                        text "\n{b}Lesson 5: Attribute{/b}" size 28 color "#3A3A3A"
                    
                    hbox:
                        text "\nAttribute concept adds depth to their comprehension of HTML, contributing to a well-rounded understanding of web development." size 20 color "#0000FF"

                    hbox:
                        text "\n{b}Lesson 8: Style Attribute{/b}" size 28 color "#3A3A3A"
                    
                    hbox:
                        text "\nStyle Attribute because they offer practical insights into manipulating webpage aesthetics, allowing students to create visually appealing designs." size 20 color "#FF0000"

                    hbox:
                        text "\nThese are my favorite element tag" size 20 color "#3A3A3A"
                        frame:
                            background Solid("#bdbdbdff")  
                            xoffset 6 
                            yoffset 25
                            padding (1, 1)
                            image "images/dropdown.png" xysize (90,55)
                    
                    hbox:
                        text "\n" size 20 color "#3A3A3A"
                        add "html_peter"


###########################################################################################################################
init python:

    import pygame.scrap

    def copytext(t):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, t.encode("utf-8"))

default attribute_1 = 'Mrs. Rodriguez values the "Attribute" because Attribute concept adds depth to their comprehension of HTML, contributing to a well-rounded understanding of web development'
default style_attribute_8 = 'The "Style Attribute" lesson (Lesson 8) is favored by Mrs. Rodriguez because they offer practical insights into manipulating webpage aesthetics, allowing students to create visually appealing designs. elements - the Anchor Tag and Video Tag'



screen task_final_test():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Task:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    hbox:
                        text 'Mrs. Rodriguez`s favorite lessons are Lesson 5 "Attribute," and Lesson 8 "Style Attribute".' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    hbox:
                        text "\n\n\nWhy:" size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    hbox:
                        text '\n\n{b}1. "Attribute" Concept (Lesson 5){/b}:' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    hbox:         
                        text '\nMrs. Rodriguez values the "Attribute" because Attribute concept adds depth to their comprehension of HTML, contributing to a well-rounded understanding of web development.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    hbox:
                        textbutton "Copy to Clipboard":
                            text_size 24
                            style_prefix "my"
                            action Function(copytext, t=attribute_1)
                    
                    hbox:
                        text '\n\n{b}2. "Style Attribute" (Lesson 8){/b}:' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    hbox:
                        text '\nThe "Style Attribute" lesson (Lesson 8) is favored by Mrs. Rodriguez because they offer practical insights into manipulating webpage aesthetics, allowing students to create visually appealing designs. elements - the Anchor Tag and Video Tag.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "Copy to Clipboard":
                            text_size 24
                            style_prefix "my"
                            action Function(copytext, t=style_attribute_8)

                    hbox:
                        text "\n\n{b}Main Task:{/b}" color "#dfdfdf" xoffset 6 yoffset 6

                    hbox:
                        text '\nComplete the missing tag for the given elements.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    hbox:
                        text '\n\n1. Your title should be "HTML Lesson"' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    hbox:
                        text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    hbox:
                        text '2. Picture: ' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                        text '"mrs_rodriguez_button.png"' size 24 color "#9060db" xoffset 6 yoffset 6

                    hbox:
                        text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    hbox:
                        text '3. Video: ' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                        text '"html_peter.webm" (loop)' size 24 color "#9060db" xoffset 6 yoffset 6
                    
                    hbox:
                        text '\n\n4. Complete some of the missing element tag' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    hbox:
                        text '\n\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    hbox:
                        text '\n\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    hbox:
                        text '\n\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

###########################################################################################################################