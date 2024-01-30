



default ans_ffive_o1_was_dropped = False
screen lesson_five_ls1_fill():
    image "images/lesson_five/lesson 5.1.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffive_o1_was_dropped:
            action Jump("lessonFiveFilltwo") 
        else:
            action Jump("if_lfv1_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("attribute_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv1")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_1
            text "    link  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_1
            text "    url  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 630
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_1
            text "source" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 517
            ypos 402
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_two1_was_dropped = False
screen lesson_five_ls2_fill():
    image "images/lesson_five/lesson 5.2.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_two1_was_dropped:
            action Jump("lessonFiveFillthree") 
        else:
            action Jump("if_lfv2_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("attribute_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv2")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_2
            text "    url  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_2
            text "    link  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 630
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_2
            text "   href  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 509
            ypos 402
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_fr1_was_dropped = False
screen lesson_five_ls4_fill():
    image "images/lesson_five/lesson 5.4.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_fr1_was_dropped:
            action Jump("lessonFiveFillFive") 
        else:
            action Jump("if_lfv4_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("attribute_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv4")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_4
            text "in the closing tag" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 660
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_4
            text "in the opening tag" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 600
            ypos 402
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_fv1_was_dropped = False
screen lesson_five_ls5_fill():
    image "images/lesson_five/lesson 5.5.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_fv1_was_dropped:
            action Jump("lessonFiveFillSix") 
        else:
            action Jump("if_lfv5_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("attribute_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv5")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_5
            text "  alt  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_5
            text "desc" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 751
            ypos 402
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_svn1_was_dropped = False
default ans_ffv_svn2_was_dropped = False
screen lesson_five_ls7_fill():
    image "images/lesson_five/lesson 5.7.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_svn1_was_dropped and ans_ffv_svn2_was_dropped:
            action Jump("lessonFiveFillEight") 
        else:
            action Jump("if_lfv7_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("attribute_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv7")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_7
            text '"http://www.image.png"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 787
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_7
            text "src" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 404
            ypos 543
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(300,50)

        drag:
            xpos 404
            ypos 590
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(300,50)


###########################################################################################################################


default ans_ffv_egt1_was_dropped = False
default ans_ffv_egt2_was_dropped = False
default ans_ffv_egt3_was_dropped = False
screen lesson_five_ls8_fill():
    image "images/lesson_five/lesson 5.8.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_egt1_was_dropped and ans_ffv_egt2_was_dropped and ans_ffv_egt3_was_dropped:
            action Jump("lessonFiveFillNine") 
        else:
            action Jump("if_lfv8_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("attribute_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv8")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_8
            text "src" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_8
            text "alt" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 590
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_8
            text "img" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 710
            ypos 855
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lfv_8
            text "href" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 381
            ypos 402
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 656
            ypos 402
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 1002
            ypos 402
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################

screen lesson_five_ls9_fill():
    image "images/lesson_five/lesson 5.9.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_five_nine") 


###########################################################################################################################


default ans_ffv_ten1_was_dropped = False
default ans_ffv_ten2_was_dropped = False
screen lesson_five_ls10_fill():
    image "images/lesson_five/lesson 5.10.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ten1_was_dropped and ans_ffv_ten2_was_dropped:
            action Jump("lessonFiveFillEleven") 
        else:
            action Jump("if_lfv10_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("attribute_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv10")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_10
            text '"alt"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_10
            text '"300"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 610
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_10
            text "width" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 267
            ypos 441
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(300,50)

        drag:
            xpos 267
            ypos 488
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(300,50)


###########################################################################################################################


screen lesson_five_ls11_fill():
    image "images/lesson_five/lesson 5.11.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_five_eleven") 


###########################################################################################################################


screen lesson_five_ls12_fill():
    image "images/lesson_five/lesson 5.12.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_five_twelve") 


###########################################################################################################################



default ans_ffv_fft1_was_dropped = False
default ans_ffv_fft2_was_dropped = False
default ans_ffv_fft3_was_dropped = False
screen lesson_five_ls15_fill():
    image "images/lesson_five/lesson 5.15.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_fft1_was_dropped and ans_ffv_fft2_was_dropped and ans_ffv_fft3_was_dropped:
            action Jump("lessonFiveFillSixteen") 
        else:
            action Jump("if_lfv15_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("menus_nav_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv15")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_15
            text "user" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_15
            text "navigate" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 670
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_15
            text "rankings" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]


        
        
        # Drop Place
        drag:
            xpos 460
            ypos 335
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 597
            ypos 382
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 578
            ypos 429
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_sixt1_was_dropped = False
default ans_ffv_sixt2_was_dropped = False
screen lesson_five_ls16_fill():
    image "images/lesson_five/lesson 5.16.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_sixt1_was_dropped and ans_ffv_sixt2_was_dropped:
            action Jump("lessonFiveFillSeventeen") 
        else:
            action Jump("if_lfv16_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("menus_nav_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv16")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_16
            text "Navigating" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 580
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_16
            text "Multi-page" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        


        
        
        # Drop Place
        drag:
            xpos 173
            ypos 335
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 173
            ypos 382
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_sevt1_was_dropped = False
screen lesson_five_ls17_fill():
    image "images/lesson_five/lesson 5.17.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_sevt1_was_dropped:
            action Jump("lessonFiveFillEighteen") 
        else:
            action Jump("if_lfv17_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("menus_nav_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv17")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_17
            text "<url>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 490
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_17
            text "<nav>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 640
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_17
            text "<a>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 402
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_eght1_was_dropped = False
default ans_ffv_eght2_was_dropped = False
default ans_ffv_eght3_was_dropped = False
default ans_ffv_eght4_was_dropped = False
screen lesson_five_ls18_fill():
    image "images/lesson_five/lesson 5.18.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_eght1_was_dropped and ans_ffv_eght2_was_dropped and ans_ffv_eght3_was_dropped and ans_ffv_eght4_was_dropped:
            action Jump("lessonFiveFillNineteen") 
        else:
            action Jump("if_lfv18_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("menus_nav_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv18")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 350
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_18
            text "<nav>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 490
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_18
            text "</nav>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 640
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_18
            text "<a>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 740
            ypos 855
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lfv_18
            text "</a>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        


        
        
        # Drop Place
        drag:
            xpos 160
            ypos 355
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 160
            ypos 402
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 599
            ypos 449
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 160
            ypos 543
            drag_raise True
            drag_name "4_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_nnt1_was_dropped = False
screen lesson_five_ls19_fill():
    image "images/lesson_five/lesson 5.19.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_nnt1_was_dropped:
            action Jump("lessonFiveFillTwenty") 
        else:
            action Jump("if_lfv19_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("menus_nav_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv19")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 350
            ypos 855
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_19
            text "4" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 490
            ypos 855
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_19
            text "3" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 640
            ypos 855
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_19
            text "5" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        # Drop Place
        drag:
            xpos 1041
            ypos 261
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


screen lesson_five_ls21_fill():
    image "images/lesson_five/lesson 5.21.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_five_twentyone") 


###########################################################################################################################


default ans_ffv_twth1_was_dropped = False
screen lesson_five_ls23_fill():
    image "images/lesson_five/lesson 5.23.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_twth1_was_dropped:
            action Jump("lessonFiveFillTwentyFour") 
        else:
            action Jump("if_lfv23_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("menus_nav_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv23")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 372
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_23
            text "1" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 448
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_23
            text "As many files as the number of sections" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 1160
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_23
            text "2" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
    
        
        
        # Drop Place
        drag:
            xpos 435
            ypos 527
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(700,50)


###########################################################################################################################


default ans_ffv_twtf1_was_dropped = False
screen lesson_five_ls24_fill():
    image "images/lesson_five/lesson 5.24.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_twtf1_was_dropped:
            action Jump("lessonFiveFillTwentyFive") 
        else:
            action Jump("if_lfv24_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("menus_nav_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv24")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 380
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_24
            text "jump" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 490
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_24
            text "  id" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        
        # Drop Place
        drag:
            xpos 501
            ypos 402
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_twtfv1_was_dropped = False
default ans_ffv_twtfv2_was_dropped = False
screen lesson_five_ls25_fill():
    image "images/lesson_five/lesson 5.25.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_twtfv1_was_dropped and ans_ffv_twtfv2_was_dropped:
            action Jump("lessonFiveFillTwentySeven") 
        else:
            action Jump("if_lfv25_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("menus_nav_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv25")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 380
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_25
            text "id" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 490
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_25
            text ' " ' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 600
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_25
            text "link" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        
        
        # Drop Place
        drag:
            xpos 272
            ypos 540
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 424
            ypos 540
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_twtsv1_was_dropped = False
default ans_ffv_twtsv2_was_dropped = False
screen lesson_five_ls27_fill():
    image "images/lesson_five/lesson 5.27.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_twtsv1_was_dropped and ans_ffv_twtsv2_was_dropped:
            action Jump("lessonFiveFillTwentyEight") 
        else:
            action Jump("if_lfv27_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("menus_nav_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv27")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 
    draggroup:

        # Draggables
        drag:
            xpos 380
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_27
            text "</a>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 510
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_27
            text 'href' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
            
        
        
        # Drop Place
        drag:
            xpos 250
            ypos 441
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 687
            ypos 441
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_twtn1_was_dropped = False
screen lesson_five_ls29_fill():
    image "images/lesson_five/lesson 5.29.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_twtn1_was_dropped:
            action Jump("lessonFiveFillThirty") 
        else:
            action Jump("if_lfv29_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")


    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv29")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 380
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_29
            text "survey" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 550
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_29
            text '<form>' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
            
        
        
        # Drop Place
        drag:
            xpos 160
            ypos 449
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


screen lesson_five_ls30_fill():
    image "images/lesson_five/lesson 5.30.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_five_thirty") 


###########################################################################################################################


screen lesson_five_ls31_fill():
    image "images/lesson_five/lesson 5.31.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_five_thirtyone") 


###########################################################################################################################


default ans_ffv_thtt1_was_dropped = False
default ans_ffv_thtt2_was_dropped = False
screen lesson_five_ls32_fill():
    image "images/lesson_five/lesson 5.32.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_thtt1_was_dropped and ans_ffv_thtt2_was_dropped:
            action Jump("lessonFiveFillThirtythree") 
        else:
            action Jump("if_lfv32_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv32")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 380
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_32
            text "</form>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 580
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_32
            text '</label>' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
            
        
        
        # Drop Place
        drag:
            xpos 372
            ypos 496
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 160
            ypos 590
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


screen lesson_five_ls33_fill():
    image "images/lesson_five/lesson 5.33.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_five_thirtythree") 


###########################################################################################################################


screen lesson_five_ls34_fill():
    image "images/lesson_five/lesson 5.34.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_five_thirtyfour") 


###########################################################################################################################


default ans_ffv_thtfv1_was_dropped = False
screen lesson_five_ls35_fill():
    image "images/lesson_five/lesson 5.35.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_thtfv1_was_dropped:
            action Jump("lessonFiveFillThirtysix") 
        else:
            action Jump("if_lfv35_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv35")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 380
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_35
            text '"radio1"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 580
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_35
            text '"r2"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 700
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_35
            text '"r1"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
            
        
        
        # Drop Place
        drag:
            xpos 372
            ypos 496
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_thtsx1_was_dropped = False
default ans_ffv_thtsx2_was_dropped = False
screen lesson_five_ls36_fill():
    image "images/lesson_five/lesson 5.36.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_thtsx1_was_dropped and ans_ffv_thtsx2_was_dropped:
            action Jump("lessonFiveFillThirtynine") 
        else:
            action Jump("if_lfv36_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv36")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 
    draggroup:

        # Draggables
        drag:
            xpos 380
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_36
            text 'id' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_36
            text 'for' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 292
            ypos 449
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 292
            ypos 496
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_fty1_was_dropped = False
screen lesson_five_ls40_fill():
    image "images/lesson_five/lesson 5.40.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_fty1_was_dropped:
            action Jump("lessonFiveFillFourtyone") 
        else:
            action Jump("if_lfv40_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv40")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 335
            ypos 766
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_40
            text 'missing id attributes' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 335
            ypos 820
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_40
            text 'labels should appear before the inputs' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 335
            ypos 874
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_40
            text '<label> is an empty tag' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 185
            ypos 671
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(700,50)


###########################################################################################################################


default ans_ffv_ftyo1_was_dropped = False
default ans_ffv_ftyo2_was_dropped = False
default ans_ffv_ftyo3_was_dropped = False
default ans_ffv_ftyo4_was_dropped = False
screen lesson_five_ls41_fill():
    image "images/lesson_five/lesson 5.41.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ftyo1_was_dropped and ans_ffv_ftyo2_was_dropped and ans_ffv_ftyo3_was_dropped and ans_ffv_ftyo4_was_dropped:
            action Jump("lessonFiveFillFourtytwo") 
        else:
            action Jump("if_lfv41_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv41")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 330
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_41
            text '     for' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_41
            text '<label' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 580
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_41
            text '      id' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 720
            ypos 857
            
            drag_raise True
            drag_name "answer_4"
            dragged dragged_func_lfv_41
            text '</form>' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 160
            ypos 382
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 465
            ypos 429
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 269
            ypos 476
            drag_raise True
            drag_name "3_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 160
            ypos 570
            drag_raise True
            drag_name "4_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_ftytw1_was_dropped = False
screen lesson_five_ls42_fill():
    image "images/lesson_five/lesson 5.42.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ftytw1_was_dropped:
            action Jump("lessonFormtakeaways") 
        else:
            action Jump("if_lfv42_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv42")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 335
            ypos 766
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_42
            text 'label and form fields are displayed on the same line' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 335
            ypos 820
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_42
            text 'label and form fields are displayed in the same color' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 335
            ypos 874
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_42
            text 'hitting the label selects the form field' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 242
            ypos 473
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(700,50)


###########################################################################################################################


default ans_ffv_ftythr1_was_dropped = False
screen lesson_five_ls43_fill():
    image "images/lesson_five/lesson 5.43.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ftythr1_was_dropped:
            action Jump("lessonFiveFillFourtyfour") 
        else:
            action Jump("if_lfv43_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv43")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 335
            ypos 768
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_43
            text 'A table' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 335
            ypos 820
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_43
            text 'A form with two input fields' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 657
            ypos 241
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(700,50)


###########################################################################################################################


default ans_ffv_ftyfr1_was_dropped = False
default ans_ffv_ftyfr2_was_dropped = False
screen lesson_five_ls44_fill():
    image "images/lesson_five/lesson 5.44.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ftyfr1_was_dropped and ans_ffv_ftyfr2_was_dropped:
            action Jump("lessonFiveFillFourtyfive") 
        else:
            action Jump("if_lfv44_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv44")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 344
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_44
            text '"submit"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 520
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_44
            text 'type' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 291
            ypos 570
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        
        drag:
            xpos 502
            ypos 570
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)


###########################################################################################################################


default ans_ffv_ftyfv1_was_dropped = False
screen lesson_five_ls45_fill():
    image "images/lesson_five/lesson 5.45.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ftyfv1_was_dropped:
            action Jump("lessonFiveFillFourtysix") 
        else:
            action Jump("if_lfv45_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv45")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 
    draggroup:

        # Draggables
        drag:
            xpos 338
            ypos 767
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_45
            text 'A computer that is always connected to the Internet and \n              listening for requests of information' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 338
            ypos 874
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_45
            text 'The device that is being used to access the Web' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 306    
            ypos 476
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        


###########################################################################################################################


default ans_ffv_ftysix1_was_dropped = False
default ans_ffv_ftysix2_was_dropped = False
screen lesson_five_ls46_fill():
    image "images/lesson_five/lesson 5.46.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ftysix1_was_dropped and ans_ffv_ftysix2_was_dropped:
            action Jump("lessonFiveFillFourtyeight") 
        else:
            action Jump("if_lfv46_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv46")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 362
            ypos 856
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_46
            text '"city"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 523
            ypos 856
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_46
            text 'name' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 516    
            ypos 382
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 629    
            ypos 429
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)
        


###########################################################################################################################


default ans_ffv_ffy1_was_dropped = False
screen lesson_five_ls50_fill():
    image "images/lesson_five/lesson 5.50.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ffy1_was_dropped:
            action Jump("lessonFiveFillFiftyone") 
        else:
            action Jump("if_lfv50_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv50")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 338
            ypos 767
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_50
            text 'label' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 338
            ypos 830
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_50
            text 'input fields' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 216    
            ypos 617
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(700,50)
        


###########################################################################################################################


default ans_ffv_ffyo1_was_dropped = False
default ans_ffv_ffyo2_was_dropped = False
screen lesson_five_ls51_fill():
    image "images/lesson_five/lesson 5.51.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ffyo1_was_dropped and ans_ffv_ffyo2_was_dropped:
            action Jump("lessonFiveFillFiftytwo") 
        else:
            action Jump("if_lfv51_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv51")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_51
            text 'id' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 421
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_51
            text 'for' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 330    
            ypos 335
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 502    
            ypos 476
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)        


###########################################################################################################################


default ans_ffv_ffyt1_was_dropped = False
screen lesson_five_ls52_fill():
    image "images/lesson_five/lesson 5.52.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ffyt1_was_dropped:
            action Jump("lessonFiveFillFiftythree") 
        else:
            action Jump("if_lfv52_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv52")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 365
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_52
            text '  co' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_52
            text '  em' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 627
            ypos 857
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_52
            text 'email' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 1040    
            ypos 241
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)       


###########################################################################################################################


default ans_ffv_ffyth1_was_dropped = False
default ans_ffv_ffyth2_was_dropped = False
screen lesson_five_ls53_fill():
    image "images/lesson_five/lesson 5.53.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ffyth1_was_dropped and ans_ffv_ffyth2_was_dropped:
            action Jump("lessonFiveFillFiftyfour") 
        else:
            action Jump("if_lfv53_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv53")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 341
            ypos 857
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_53
            text 'value' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 470
            ypos 857
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_53
            text 'name' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 607    
            ypos 523
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)

        drag:
            xpos 432    
            ypos 617
            drag_raise True
            drag_name "2_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)        


###########################################################################################################################


default ans_ffv_ffyfv1_was_dropped = False
screen lesson_five_ls55_fill():
    image "images/lesson_five/lesson 5.55.png" 
    
    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if ans_ffv_ffyfv1_was_dropped:
            action Jump("lessonFiveFillFiftysix") 
        else:
            action Jump("if_lfv55_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")

    imagebutton:
        xpos 1510
        ypos 30
        idle "images/interactive_button/hint_button.png"
        hover "images/interactive_button/hint_button_hover.png"
        action ShowMenu("form_hint")

    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_fv55")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 353
            ypos 766
            
            drag_raise True
            drag_name "answer_1"
            dragged dragged_func_lfv_55
            text 'field (column) named "cash"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 353
            ypos 817
            
            drag_raise True
            drag_name "answer_2"
            dragged dragged_func_lfv_55
            text 'field (column) named "radio"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        
        drag:
            xpos 354
            ypos 868
            
            drag_raise True
            drag_name "answer_3"
            dragged dragged_func_lfv_55
            text 'field (column) named "pay"' size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]
        

        
        
        # Drop Place
        drag:
            xpos 346    
            ypos 230
            drag_raise True
            drag_name "1_place"
            draggable False
            image Solid("#ffd53d00") xysize(200,50)       


###########################################################################################################################


screen lesson_five_ls56_fill():
    image "images/lesson_five/lesson 5.56.png" 
    


    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("when_run_five_fiftysix") 


###########################################################################################################################