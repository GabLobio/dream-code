init: 
    $ diploma_serial = "{:03d}".format(renpy.random.randint(0, 999999999))


label debug:
    #play music "audio/quiz.mp3" volume 0.5
    jump start_quiz_06

#label pagtapos_ng_quiz_6:
    #jump quiz_total_overall_tally








label quiz_menu_screen_debug:
    #----------------------------------------------------------
    #Note: Delete or comment the lines below once finalize. Debug use only
    $ persistent_quiz_00_q_counter_correct_answer = 10
    $ persistent_quiz_01_q_counter_correct_answer = 6
    $ persistent_quiz_02_q_counter_correct_answer = 8
    $ persistent_quiz_03_q_counter_correct_answer = 10
    $ persistent_quiz_04_q_counter_correct_answer = 7
    $ persistent_quiz_05_q_counter_correct_answer = 6
    $ persistent_quiz_06_q_counter_correct_answer = 7
    $ persistent_quiz_07_q_counter_correct_answer = 9
    $ persistent_quiz_08_q_counter_correct_answer = 10
    $ persistent_quiz_08_q_counter_correct_answer = 7
    $ persistent_quiz_09_q_counter_correct_answer = 7

    $ persistent_quiz_total_points_counter_correct_answer = 80

    #$ final_test_undertaken = True #set to true then copy to line before quiz start in script

    $ whole_quiz_00_seen = True
    $ whole_quiz_01_seen = True
    $ whole_quiz_02_seen = True
    $ whole_quiz_03_seen = True
    $ whole_quiz_04_seen = True
    $ whole_quiz_05_seen = True
    $ whole_quiz_06_seen = True
    $ whole_quiz_07_seen = True
    $ whole_quiz_08_seen = True
    $ whole_quiz_09_seen = True











    #Note: Delete or comment lines above once finalize. Debug use only
    #----------------------------------------------------------

    

    call screen quiz_menu_screen_debug_imagemap
    $ result = _return

screen quiz_menu_screen_debug_imagemap:
    viewport:
        draggable True
        imagemap:
            ground 'assets_quiz/background_quiz_01.jpg'
            hover 'assets_quiz/background_quiz_01.jpg'

            text _p("""
                {b}QUIZ 01{/b}{p}{p}
                {b}QUIZ 02{/b}{p}{p}
                {b}QUIZ 03{/b}{p}{p}
                {b}QUIZ 04{/b}{p}{p}
                {b}QUIZ 05{/b}{p}{p}
                {b}RETURN{/b}{p}{p}
                """) xpos 192 ypos 113 size 70 color "#ca4700"

            text _p("""
                {b}QUIZ 06{/b}{p}{p}
                {b}QUIZ 07{/b}{p}{p}
                {b}QUIZ 08{/b}{p}{p}
                {b}QUIZ 09{/b}{p}{p}
                {b}QUIZ 10{/b}{p}{p}
                """) xpos 600 ypos 113 size 70 color "ca4700"

            text _p("""
                {a=jump:quiz_00_result_callback_debug}{b}QUIZ 01{/b}{/a}{p}{p}
                {a=jump:quiz_01_result_callback_debug}{b}QUIZ 02{/b}{/a}{p}{p}
                {a=jump:quiz_02_result_callback_debug}{b}QUIZ 03{/b}{/a}{p}{p}
                {a=jump:quiz_03_result_callback_debug}{b}QUIZ 04{/b}{/a}{p}{p}
                {a=jump:quiz_04_result_callback_debug}{b}QUIZ 05{/b}{/a}{p}{p}
                {a=jump:main_menu_call_from_progress}{b}RETURN{/b}{/a}{p}{p}
                """) xpos 192 ypos 109 size 70 color "#777777"

            text _p("""
                {a=jump:quiz_05_result_callback_debug}{b}QUIZ 06{/b}{/a}{p}{p}
                {a=jump:quiz_06_result_callback_debug}{b}QUIZ 07{/b}{/a}{p}{p}
                {a=jump:quiz_07_result_callback_debug}{b}QUIZ 08{/b}{/a}{p}{p}
                {a=jump:quiz_08_result_callback_debug}{b}QUIZ 09{/b}{/a}{p}{p}
                {a=jump:quiz_09_result_callback_debug}{b}QUIZ 10{/b}{/a}{p}{p}
                """) xpos 600 ypos 109 size 70 color "#777777"

            if persistent.final_test_undertaken == True:    

                text _p("""
                    {b}Summary{/b}{p}{p}
                    {b}Certificate{/b}{p}{p}
                    """) xpos 1200 ypos 113 size 90 color "#ca4700"

                text _p("""
                    {a=jump:quiz_total_overall_tally}{b}Summary{/b}{/a}{p}{p}
                    {a=jump:diploma}{b}Certificate{/b}{/a}{p}{p}
                    """) xpos 1200 ypos 109 size 90 color "#ffffff"



















label bawal_dito_wala_pa_exam:
    scene bawal_background
    show teacher_crossarm_sad with dissolve
    Maria "You haven't taken this quiz yet..."
    hide teacher_crossarm_sad with dissolve
    jump quiz_menu_screen_debug



label quiz_total_overall_tally:
    call screen quiz_total_overall_tally_imagemap
    $ result = _return





screen quiz_total_overall_tally_imagemap:
    imagemap:
        ground 'images/blank_bar.png'
        hover 'images/blank_bar.png'
    text _p("""
        {color=#ffffff}{b}[persistent_quiz_total_points_counter_correct_answer]{/b}{/color}
        """) xpos 750 ypos 800 size 150 xsize 374 color "#777777" text_align 0.0
        
    text _p("""
        {color=#ffffff}{b}General Weighted{p}      Average{/b}{/color}
        """) xpos 1000 ypos 830 size 50 color "#bd0000"   
    text _p("""
        {b}Return{/b}{p}
        """) xpos 80 ypos 30 size 70 color "#ca4700" 
        
    text _p("""
        {a=jump:quiz_menu_screen_debug}{b}Return{/b}{/a}{p}
        """) xpos 80 ypos 40 size 70 color "#ffffff"  

    
    image Solid("#FF5A00") xsize(persistent_quiz_00_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 155
    text "{b}[persistent_quiz_00_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 155

    image Solid("#FF5A00") xsize(persistent_quiz_01_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 210
    text "{b}[persistent_quiz_01_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 210
    
    image Solid("#FF5A00") xsize(persistent_quiz_02_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 265
    text "{b}[persistent_quiz_02_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 265

    image Solid("#FF5A00") xsize(persistent_quiz_03_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 320
    text "{b}[persistent_quiz_03_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 320

    image Solid("#FF5A00") xsize(persistent_quiz_04_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 375
    text "{b}[persistent_quiz_04_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 375

    image Solid("#FF5A00") xsize(persistent_quiz_05_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 430
    text "{b}[persistent_quiz_05_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 430
    
    image Solid("#FF5A00") xsize(persistent_quiz_06_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 485
    text "{b}[persistent_quiz_06_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 485

    image Solid("#FF5A00") xsize(persistent_quiz_07_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 540
    text "{b}[persistent_quiz_07_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 540

    image Solid("#FF5A00") xsize(persistent_quiz_08_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 595
    text "{b}[persistent_quiz_08_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 595

    image Solid("#FF5A00") xsize(persistent_quiz_09_q_counter_correct_answer * 80) ysize(45) xpos 867 ypos 650
    text "{b}[persistent_quiz_09_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 1250 ypos 650




    
        

        


        
                
         

label diploma:
    call screen diploma_imagemap
    $ result = _return

screen diploma_imagemap:
    viewport:
        draggable True
        imagemap:

            ground 'assets_quiz/diploma.jpg'
            hover 'assets_quiz/diploma.jpg'

            text _p("""
                {color=#ff0000}{b}[diploma_serial]{/b}{/color}

                """) xpos 1125 ypos 180 size 50 xsize 374 color "#777777" text_align 1.0

            text "{color=#333333}{b}[persistent.POV]{/b}{/color}" xpos 959 ypos 570 size 60 xsize 992 text_align 0.5 xanchor 0.5
            #text _p("""
                #{color=#ff0000}{b}[persistent.namae]{/b}{/color}
                #""") xpos 959 ypos 600 size 60 xsize 992 color "#777777" xalign 0.5 text_align 0.5

            text _p("""
                    {b}Return{/b}{p}
                    """) xpos 800 ypos 950 size 70 color "#ca4700" 
            text _p("""
                    {a=jump:quiz_menu_screen_debug}{b}Return{/b}{/a}{p}
                    """) xpos 800 ypos 946 size 70 color "#ffffff"    










label quiz_00_result_callback_debug:
    if whole_quiz_00_seen == False:
        call bawal_dito_wala_pa_exam from _call_bawal_dito_wala_pa_exam
        return
    elif persistent_quiz_00_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_00_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_00_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_00_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_00_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_00_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_00_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_00_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_00_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_00_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_00_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 



















label quiz_01_result_callback_debug:
    if whole_quiz_01_seen == False:
        call bawal_dito_wala_pa_exam from _call_bawal_dito_wala_pa_exam_1
        return

    elif persistent_quiz_01_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_01_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_01_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_01_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_01_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_01_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_01_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_01_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_01_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_01_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_01_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 



















label quiz_02_result_callback_debug:
    if whole_quiz_02_seen == False:
        call bawal_dito_wala_pa_exam from _call_bawal_dito_wala_pa_exam_2
        return
    
    elif persistent_quiz_02_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_02_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_02_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_02_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_02_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_02_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_02_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_02_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_02_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_02_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_02_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 










label quiz_03_result_callback_debug:
    if whole_quiz_03_seen == False:
        call bawal_dito_wala_pa_exam from _call_bawal_dito_wala_pa_exam_3
        return
    
    elif persistent_quiz_03_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_03_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_03_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_03_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_03_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_03_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_03_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_03_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_03_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_03_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_03_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 




















label quiz_04_result_callback_debug:
    if whole_quiz_04_seen == False:
        call bawal_dito_wala_pa_exam from _call_bawal_dito_wala_pa_exam_4
        return
    
    elif persistent_quiz_04_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_04_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_04_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_04_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_04_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_04_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_04_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_04_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_04_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_04_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_04_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug
















label quiz_05_result_callback_debug:
    if whole_quiz_06_seen == False:
        call bawal_dito_wala_pa_exam from _call_bawal_dito_wala_pa_exam_5
        return
    
    elif persistent_quiz_05_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_05_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_05_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_05_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_05_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_05_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_05_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_05_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_05_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_05_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_05_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug














label quiz_06_result_callback_debug:
    if persistent_quiz_06_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_06_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_06_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_06_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_06_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_06_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_06_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_06_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_06_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_06_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_06_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug






























label quiz_07_result_callback_debug:
    if whole_quiz_07_seen == False:
        call bawal_dito_wala_pa_exam from _call_bawal_dito_wala_pa_exam_6
        return
    
    elif persistent_quiz_07_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_07_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_07_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_07_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_07_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_07_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_07_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_07_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_07_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_07_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_07_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug

























label quiz_08_result_callback_debug:
    if whole_quiz_08_seen == False:
        call bawal_dito_wala_pa_exam from _call_bawal_dito_wala_pa_exam_7
        return
    
    elif persistent_quiz_08_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_08_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_08_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_08_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_08_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_08_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_08_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_08_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_08_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_08_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_08_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug










        













label quiz_09_result_callback_debug:
    if whole_quiz_09_seen == False:
        call bawal_dito_wala_pa_exam from _call_bawal_dito_wala_pa_exam_8
        return
    
    elif persistent_quiz_09_q_counter_correct_answer == 0:
        scene pie_00
        hide blank_question_windows with moveoutright
        blank "Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_09_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        blank "Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_09_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        blank "Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 


    elif persistent_quiz_09_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        blank "Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 
        

    elif persistent_quiz_09_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        blank "Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_09_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        blank "Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_09_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        blank "Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_09_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        blank "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_09_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_09_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        blank "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug 

    elif persistent_quiz_09_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        blank "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        jump quiz_menu_screen_debug