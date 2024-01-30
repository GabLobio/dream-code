default p_tag_was_dropped = False
default html_tag_was_dropped = False 


########## Lesson one answers ###############

#### Fill one
default ans_lt_was_dropped = False
#### Fill two
default ans_button_was_dropped = False
default ans_gt_was_dropped = False
#### Fill three
default ans_fl2_was_dropped = False
#### Fill four
default ans_btn_was_dropped = False
default ans_img_was_dropped = False
default ans_tp_was_dropped = False
default ans_tbl_was_dropped = False
#### Fill five
default ans_html_was_dropped = False
default ans_js_was_dropped = False
default ans_css_was_dropped = False
#### Fill six
default ans_btntg_was_dropped = False
default ans_like_was_dropped = False
#### Fill seven
default ans_tgbtn_was_dropped = False
#### Fill eighth
default ans_comment_was_dropped = False
#### Fill nine
default ans_ptag_was_dropped = False
default ans_ptag2_was_dropped = False
#### Fill ten
default ans_ft1_was_dropped = False
default ans_ft2_was_dropped = False
default ans_ft3_was_dropped = False
#### Fill eleven
default ans_el1_was_dropped = False
#### Fill twelve
default ans_t1_was_dropped = False
default ans_t2_was_dropped = False

init python:
    def IncrementRecitation1():
        persistent.ast1_recitation += 10
        persistent.ast1_accuracy += 10


screen lesson_one_fill():
    image "images/lesson_one/Lesson 1.1.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_button_lt_dropped:
            action [lambda: IncrementRecitation1(), Jump("lessonOneFillTwo")]  
        else:
            action Jump("if_wrong")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o1")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 327
            ypos 857

            drag_raise True
            drag_name "answer_<"
            dragged dragged_func_lesson_1
            text " < " size 40 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 385
            ypos 857
            
            drag_raise True
            drag_name "answer_>"
            dragged dragged_func_lesson_1
            text " > " size 40 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ] 

        
        
        # Drop Place
        drag:
            xpos 620
            ypos 384
            drag_raise True
            drag_name "<_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


screen lesson_two_fill():
    image "images/lesson_one/Lesson 1.2.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_button_was_dropped == True and ans_gt_was_dropped == True:
            action Jump("lessonOneFillThree") 
        else:
            action Jump("if_wrong_l2")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o2")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 


    draggroup:

        # Draggables
        drag:
            xpos 345
            ypos 857
            drag_raise True
            drag_name "answer_button"
            dragged dragged_func_lesson_2
            text "button" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 470
            ypos 857
            drag_raise True
            drag_name "answer_>"
            dragged dragged_func_lesson_2
            text "   >   " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 630 
            ypos 364

            drag_raise True
            drag_name "button_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(101,30)

        drag:
            xpos 770 
            ypos 364

            drag_raise True
            drag_name ">_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


screen lesson_three_fill():
    image "images/lesson_one/Lesson 1.3.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_fl2_was_dropped:
            action [lambda: IncrementRecitation1(), Jump("lessonOneFillFour")]
        else:
            action Jump("if_wrong_l3")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o3")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 400
            ypos 857
                
            drag_raise True
            drag_name "answer_fl2"
            dragged dragged_func_lesson_3
            default wasDropped = False
            text ">" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 480
            ypos 857
                
            drag_raise True
            drag_name "answer_<"
            dragged dragged_func_lesson_3
            default wasDropped = False
            text "<" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

            
            
        # Drop Place
        drag:
            xpos 778 
            ypos 368
            drag_raise True
            drag_name "fl2_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


screen lesson_four_fill():
    image "images/lesson_one/Lesson 1.4.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_btn_was_dropped == True and ans_img_was_dropped == True and ans_tp_was_dropped == True and ans_tbl_was_dropped == True:
            action Jump("lessonOneIntro") 
        else:
            action Jump("if_wrong_l4")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o4")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 

    draggroup:

        # Draggables
        drag:
            xpos 350
            ypos 857
                
            drag_raise True
            drag_name "answer_btn"
            dragged dragged_func_lesson_4
            text "<button>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 550
            ypos 857
                
            drag_raise True
            drag_name "answer_img"
            dragged dragged_func_lesson_4
            text "<img>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 700
            ypos 857
                
            drag_raise True
            drag_name "answer_tp"
            dragged dragged_func_lesson_4
            text "<p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 810
            ypos 857
                
            drag_raise True
            drag_name "answer_tbl"
            dragged dragged_func_lesson_4
            text "<table>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

            
            
        # Drop Place
        drag:
            xpos 287 
            ypos 363
            drag_raise True
            drag_name "btn_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(200,30)

        drag:
            xpos 279 
            ypos 441
            drag_raise True
            drag_name "img_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(200,30)

        drag:
            xpos 417 
            ypos 519
            drag_raise True
            drag_name "tp_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(200,30)

        drag:
            xpos 269 
            ypos 597
            drag_raise True
            drag_name "tbl_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


screen lesson_five_fill():
    image "images/lesson_one/Lesson 1.5.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_html_was_dropped and ans_js_was_dropped and ans_css_was_dropped:
            action [lambda: IncrementRecitation1(), Jump("lessonHtmlTakeaways")]
        else:
            action Jump("if_wrong_l5")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o5")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 

    draggroup:

        # Draggables
        drag:
            xpos 350
            ypos 857
                
            drag_raise True
            drag_name "answer_html"
            dragged dragged_func_lo_5
            text "HTML" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 470
            ypos 857
                
            drag_raise True
            drag_name "answer_js"
            dragged dragged_func_lo_5
            text "JavaScript" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 660
            ypos 857
                
            drag_raise True
            drag_name "answer_css"
            dragged dragged_func_lo_5
            text "CSS" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

            
        # Drop Place
        drag:
            xpos 327 
            ypos 520
            drag_raise True
            drag_name "html_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(200,30)

        drag:
            xpos 263 
            ypos 366
            drag_raise True
            drag_name "css_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(200,30)

        drag:
            xpos 366 
            ypos 444    
            drag_raise True
            drag_name "js_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(200,30)


###########################################################################################################################


screen lesson_six_fill():
    image "images/lesson_one/Lesson 1.6.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_btntg_was_dropped and ans_like_was_dropped:
            action Jump("lessonOneFillSeven") 
        else:
            action Jump("if_wrong_l6")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o6")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 


    draggroup:

        # Draggables
        drag:
            xpos 310
            ypos 857
            
            drag_raise True
            drag_name "answer_like"
            dragged dragged_func_lo_6
            text "    Like  " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 470
            ypos 857
            
            drag_raise True
            drag_name "answer_btntg"
            dragged dragged_func_lo_6
            text "<button>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 476 
            ypos 405

            drag_raise True
            drag_name "like_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)

        drag:
            xpos 677
            ypos 405

            drag_raise True
            drag_name "btntg_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


screen lesson_seven_fill():
    image "images/lesson_one/Lesson 1.7.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_tgbtn_was_dropped:
            action Jump("lessonOneFillEighth") 
        else:
            action Jump("if_wrong_l7")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o7")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 


    draggroup:

        # Draggables
        drag:
            xpos 350
            ypos 857
            
            drag_raise True
            drag_name "answer_btn"
            dragged dragged_func_lo_7
            text "</close>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 540
            ypos 857
            
            drag_raise True
            drag_name "answer_/btn"
            dragged dragged_func_lo_7
            text "</button>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 780 
            ypos 366

            drag_raise True
            drag_name "tgbtn_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


screen lesson_eighth_fill():
    image "images/lesson_one/Lesson 1.8.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_comment_was_dropped:
            action [lambda: IncrementRecitation1(), Jump("lessonOneFillNine")]
        else:
            action Jump("if_wrong_l8")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o8")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 


    draggroup:

        # Draggables
        drag:
            xpos 350
            ypos 857
            
            drag_raise True
            drag_name "answer_like"
            dragged dragged_func_lo_8
            text "    like   " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 500
            ypos 857
            
            drag_raise True
            drag_name "answer_comment"
            dragged dragged_func_lo_8
            text "comment" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 667 
            ypos 366

            drag_raise True
            drag_name "comment_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


screen lesson_nine_fill():
    image "images/lesson_one/Lesson 1.9.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ptag_was_dropped and ans_ptag2_was_dropped:
            action Jump("lessonOneFillTen") 
        else:
            action Jump("if_wrong_l9")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o9")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 


    draggroup:

        # Draggables
        drag:
            xpos 340
            ypos 857
            
            drag_raise True
            drag_name "answer_p"
            dragged dragged_func_lo_9
            text " <p> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 450
            ypos 857
            
            drag_raise True
            drag_name "answer_p2"
            dragged dragged_func_lo_9
            text " </p> " size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 580
            ypos 857
            
            drag_raise True
            drag_name "answer_img"
            dragged dragged_func_lo_9
            text "<img>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 450 
            ypos 366

            drag_raise True
            drag_name "p_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(101,30)

        drag:
            xpos 938 
            ypos 366

            drag_raise True
            drag_name "p2_place"
            draggable False
            dragged dragged_func
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


screen lesson_ten_fill():
    image "images/lesson_one/Lesson 1.10.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_ft1_was_dropped and ans_ft2_was_dropped and ans_ft3_was_dropped:
            action [lambda: IncrementRecitation1(), Jump("lessonOneBeforeEleven")]
        else:
            action Jump("if_wrong_l10")


        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o10")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 


    draggroup:

        # Draggables
        drag:
            xpos 350
            ypos 857
            
            drag_raise True
            drag_name "answer_ft1"
            dragged dragged_func_lo_10
            text "<p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 450
            ypos 857
            
            drag_raise True
            drag_name "answer_ft2"
            dragged dragged_func_lo_10
            text "text" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 540
            ypos 857
            
            drag_raise True
            drag_name "answer_ft3"
            dragged dragged_func_lo_10
            text "</p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        
        # Drop Place
        drag:
            xpos 585
            ypos 366

            drag_raise True
            drag_name "ft1_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)
        
        drag:
            xpos 705
            ypos 366

            drag_raise True
            drag_name "ft2_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)
        
        drag:
            xpos 825
            ypos 366

            drag_raise True
            drag_name "ft3_place"
            draggable False
            image Solid("#ffd53d00") xysize(101,30)


###########################################################################################################################


screen lesson_before_eleven_fill():

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        action Jump("lesson_one_11_run") 

###########################################################################################################################

screen lesson_eleven_fill():
    image "images/lesson_one/Lesson 1.11.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_el1_was_dropped:
            action Jump("lessonOneFillTwelve") 
        else:
            action Jump("if_wrong_l11")

        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o11")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")
 


    draggroup:

        # Draggables
        drag:
            xpos 350
            ypos 770
            
            drag_raise True
            drag_name "answer_el1"
            dragged dragged_func_lo_11
            text "An image and button" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 350
            ypos 830
            
            drag_raise True
            drag_name "answer_el2"
            dragged dragged_func_lo_11
            text "A paragraph text and a button" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        # Drop Place
        drag:
            xpos 160
            ypos 518

            drag_raise True
            drag_name "el1_place"
            draggable False
            image Solid("#ffd53d00") xysize(500,30)


###########################################################################################################################


screen lesson_twelve_fill():
    image "images/lesson_one/Lesson 1.12.png" #blur 10.0

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        if  ans_t1_was_dropped and ans_t2_was_dropped:
            action Jump("webBrowser") 
        else:
            action Jump("if_wrong_l12")

        
        hovered Show("next_button")
        unhovered Hide ("next_button")



    imagebutton:
        xpos 1640
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"

        action Jump("call_o12")   

        hovered Show("reset_button")
        unhovered Hide ("reset_button")

 


    draggroup:

        # Draggables
        drag:
            xpos 360
            ypos 857
            
            drag_raise True
            drag_name "answer_t1"
            dragged dragged_func_lo_12
            text "<p>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        drag:
            xpos 490
            ypos 857
            
            drag_raise True
            drag_name "answer_t2"
            dragged dragged_func_lo_12
            text "</button>" size 32 color "#ffffff" outlines [ (1, "#ffa217b9", 0, 0) ]

        
        # Drop Place
        drag:
            xpos 160 
            ypos 366

            drag_raise True
            drag_name "t1_place"
            draggable False
            image Solid("#ffd53d00") xysize(201,30)
        
        drag:
            xpos 458
            ypos 405

            drag_raise True
            drag_name "t2_place"
            draggable False
            image Solid("#ffd53d00") xysize(201,30)

###########################################################################################################################