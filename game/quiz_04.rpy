##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  INITIALIATION / LOOP CHECKER                                       ███ ║ 
##  ║ ███  This is the section responsible for going inside the               ███ ║ 
##  ║ ███  quiz, dictating the loop as well aswhen the quiz qill end.         ███ ║  
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

default persistent_quiz_04_q_counter_correct_previous_answer = 0
default persistent_quiz_04_q_counter_correct_answer = 0

label start_quiz_04_initialization:
    if whole_quiz_04_seen == True:
        jump start_quiz_04
    else:
        $ persistent_quiz_04_q_counter_correct_previous_answer = 0
        $ persistent_quiz_04_q_counter_correct_answer = 0

# You place any dialogue or declare image here before quiz starts
label start_quiz_04:
    ## ╔════════════════════════╗
    ## ║ temporary please erase ║
    ## ╚════════════════════════╝ 
    $ persistent_quiz_04_q_01_seen = False
    $ persistent_quiz_04_q_02_seen = False
    $ persistent_quiz_04_q_03_seen = False
    $ persistent_quiz_04_q_04_seen = False
    $ persistent_quiz_04_q_05_seen = False
    $ persistent_quiz_04_q_06_seen = False
    $ persistent_quiz_04_q_07_seen = False
    $ persistent_quiz_04_q_08_seen = False
    $ persistent_quiz_04_q_09_seen = False
    $ persistent_quiz_04_q_10_seen = False
    $ persistent_quiz_04_q_11_seen = False
    $ persistent_quiz_04_q_12_seen = False
    $ persistent_quiz_04_q_13_seen = False
    $ persistent_quiz_04_q_14_seen = False
    $ persistent_quiz_04_q_15_seen = False
    $ persistent_quiz_04_q_16_seen = False
    $ persistent_quiz_04_q_17_seen = False
    $ persistent_quiz_04_q_18_seen = False
    $ persistent_quiz_04_q_19_seen = False
    $ persistent_quiz_04_q_20_seen = False

    $ persistent_quiz_04_q_counter = 0

    jump start_quiz_04_first_check

label start_quiz_04_first_check:
    if whole_quiz_04_seen == True:
        jump start_quiz_04_second_check
    else:    
        jump start_quiz_04_second_check    

label start_quiz_04_second_check:
    if persistent_quiz_04_q_counter_correct_previous_answer == 0:
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 1:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 1
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 2:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 2
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 3:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 3
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 4:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 4
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 5:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 5
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 6:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 6
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 7:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 7
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 8:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 8
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 9:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 9
        jump start_quiz_04_third_check

    elif persistent_quiz_04_q_counter_correct_previous_answer == 10:
        $ persistent_quiz_04_q_counter_correct_previous_answer -= 10
        jump start_quiz_04_third_check

label start_quiz_04_third_check:

    if whole_quiz_04_seen == True:
        e "Repeat exam again?"
        e "OK, let's proceed..."
        if persistent_quiz_04_q_counter_correct_answer == 0:
            jump start_quiz_04_resume

        elif persistent_quiz_04_q_counter_correct_answer == 1:
            $ persistent_quiz_04_q_counter_correct_previous_answer += 1 
            $ persistent_quiz_04_q_counter_correct_answer -= 1
            $ persistent_quiz_total_points_counter_correct_answer -= 1 
            jump start_quiz_04_resume 

        elif persistent_quiz_04_q_counter_correct_answer == 2:
            $ persistent_quiz_04_q_counter_correct_previous_answer += 2 
            $ persistent_quiz_04_q_counter_correct_answer -= 2
            $ persistent_quiz_total_points_counter_correct_answer -= 2 
            jump start_quiz_04_resume

        elif persistent_quiz_04_q_counter_correct_answer == 3: 
            $ persistent_quiz_04_q_counter_correct_previous_answer += 3
            $ persistent_quiz_04_q_counter_correct_answer -= 3
            $ persistent_quiz_total_points_counter_correct_answer -= 3
            jump start_quiz_04_resume

        elif persistent_quiz_04_q_counter_correct_answer == 4: 
            $ persistent_quiz_04_q_counter_correct_previous_answer += 4
            $ persistent_quiz_04_q_counter_correct_answer -= 4 
            $ persistent_quiz_total_points_counter_correct_answer -= 4
            jump start_quiz_04_resume

        elif persistent_quiz_04_q_counter_correct_answer == 5:
            $ persistent_quiz_04_q_counter_correct_previous_answer += 5
            $ persistent_quiz_04_q_counter_correct_answer -= 5  
            $ persistent_quiz_total_points_counter_correct_answer -= 5
            jump start_quiz_04_resume

        elif persistent_quiz_04_q_counter_correct_answer == 6: 
            $ persistent_quiz_04_q_counter_correct_previous_answer += 6
            $ persistent_quiz_04_q_counter_correct_answer -= 6 
            $ persistent_quiz_total_points_counter_correct_answer -= 6
            jump start_quiz_04_resume

        elif persistent_quiz_04_q_counter_correct_answer == 7: 
            $ persistent_quiz_04_q_counter_correct_previous_answer += 7
            $ persistent_quiz_04_q_counter_correct_answer -= 7 
            $ persistent_quiz_total_points_counter_correct_answer -= 7
            jump start_quiz_04_resume

        elif persistent_quiz_04_q_counter_correct_answer == 8:  
            $ persistent_quiz_04_q_counter_correct_previous_answer += 8
            $ persistent_quiz_04_q_counter_correct_answer -= 8
            $ persistent_quiz_total_points_counter_correct_answer -= 8
            jump start_quiz_04_resume

        elif persistent_quiz_04_q_counter_correct_answer == 9:  
            $ persistent_quiz_04_q_counter_correct_previous_answer += 9
            $ persistent_quiz_04_q_counter_correct_answer -= 9
            $ persistent_quiz_total_points_counter_correct_answer -= 9
            jump start_quiz_04_resume

        elif persistent_quiz_04_q_counter_correct_answer == 10: 
            $ persistent_quiz_04_q_counter_correct_previous_answer += 10 
            $ persistent_quiz_04_q_counter_correct_answer -= 10
            $ persistent_quiz_total_points_counter_correct_answer -= 10
            jump start_quiz_04_resume

    jump start_quiz_04_resume         






label start_quiz_04_resume:
    $ renpy.block_rollback()
    $ whole_quiz_04_seen = True
    #"Insert Dialogue Here"
    scene quiz_window_blank 
    show quiz_start with moveinleft
    $ renpy.pause()
    hide quiz_start with moveoutright
    show blank_question_windows with moveinleft
    jump quiz_04_randomizer

# This label will check if you already answered 10 questions. 
# If you have answered 10, you will conclude this set of quiz.
# Else, you will loop back to the randomized
label quiz_04_base_checker:
    if persistent_quiz_04_q_counter == 10:
        jump quiz_04_conclusion
    else:      
        scene quiz_window_blank 
        show blank_question_windows
        hide blank_question_windows with moveoutright
        show quiz_next_question with moveinleft
        $ renpy.pause()
        hide quiz_next_question with moveoutright
        show blank_question_windows with moveinleft
        jump quiz_04_randomizer

label quiz_04_base_checker_timeout:
    if persistent_quiz_04_q_counter == 10:
        jump quiz_04_conclusion
    else:      
        scene quiz_window_blank 
        show blank_question_windows
        hide blank_question_windows with moveoutright
        show times_up with moveinleft
        $ renpy.pause(1.0)
        hide times_up with moveoutright
        show quiz_next_question with moveinleft
        $ renpy.pause()
        hide quiz_next_question with moveoutright
        show blank_question_windows with moveinleft
        jump quiz_04_randomizer










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION RANDOMIZER                                                ███ ║ 
##  ║ ███  This is the section where the questions are selected in random.    ███ ║ 
##  ║ ███                                                                     ███ ║  
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_randomizer:
    $ choice = renpy.random.choice(['q01', 'q02', 'q03', 'q04', 'q05', 'q06', 'q07', 'q08', 'q09', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20'])

    if choice == 'q01': # quiz_01_q_01_checker
        if persistent_quiz_04_q_01_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_01_seen == False: 
            $ persistent_quiz_04_q_01_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_01

    if choice == 'q02': # quiz_01_q_02_checker
        if persistent_quiz_04_q_02_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_02_seen == False: 
            $ persistent_quiz_04_q_02_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_02

    if choice == 'q03': # quiz_01_q_03_checker
        if persistent_quiz_04_q_03_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_03_seen == False: 
            $ persistent_quiz_04_q_03_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_03

    if choice == 'q04': # quiz_01_q_04_checker
        if persistent_quiz_04_q_04_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_04_seen == False: 
            $ persistent_quiz_04_q_04_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_04

    if choice == 'q05': # quiz_01_q_05_checker
        if persistent_quiz_04_q_05_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_05_seen == False: 
            $ persistent_quiz_04_q_05_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_05

    if choice == 'q06': # quiz_01_q_06_checker
        if persistent_quiz_04_q_06_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_06_seen == False: 
            $ persistent_quiz_04_q_06_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_06

    if choice == 'q07': # quiz_01_q_07_checker
        if persistent_quiz_04_q_07_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_07_seen == False: 
            $ persistent_quiz_04_q_07_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_07

    if choice == 'q08': # quiz_01_q_08_checker
        if persistent_quiz_04_q_08_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_08_seen == False: 
            $ persistent_quiz_04_q_08_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_08

    if choice == 'q09': # quiz_01_q_09_checker
        if persistent_quiz_04_q_09_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_09_seen == False: 
            $ persistent_quiz_04_q_09_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_09

    if choice == 'q10': # quiz_01_q_10_checker
        if persistent_quiz_04_q_10_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_10_seen == False: 
            $ persistent_quiz_04_q_10_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_10

    if choice == 'q11': # quiz_01_q_11_checker
        if persistent_quiz_04_q_11_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_11_seen == False: 
            $ persistent_quiz_04_q_11_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_11

    if choice == 'q12': # quiz_01_q_12_checker
        if persistent_quiz_04_q_12_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_12_seen == False: 
            $ persistent_quiz_04_q_12_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_12

    if choice == 'q13': # quiz_01_q_13_checker
        if persistent_quiz_04_q_13_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_13_seen == False: 
            $ persistent_quiz_04_q_13_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_13

    if choice == 'q14': # quiz_01_q_14_checker
        if persistent_quiz_04_q_14_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_14_seen == False: 
            $ persistent_quiz_04_q_14_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_14

    if choice == 'q15': # quiz_01_q_15_checker
        if persistent_quiz_04_q_15_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_15_seen == False: 
            $ persistent_quiz_04_q_15_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_15

    if choice == 'q16': # quiz_01_q_16_checker
        if persistent_quiz_04_q_16_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_16_seen == False: 
            $ persistent_quiz_04_q_16_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_16

    if choice == 'q17': # quiz_01_q_17_checker
        if persistent_quiz_04_q_17_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_17_seen == False: 
            $ persistent_quiz_04_q_17_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_17

    if choice == 'q18': # quiz_01_q_18_checker
        if persistent_quiz_04_q_18_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_18_seen == False: 
            $ persistent_quiz_04_q_18_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_18

    if choice == 'q19': # quiz_01_q_19_checker
        if persistent_quiz_04_q_19_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_19_seen == False: 
            $ persistent_quiz_04_q_19_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_19

    if choice == 'q20': # quiz_01_q_20_checker
        if persistent_quiz_04_q_20_seen == True:
            jump quiz_04_randomizer
        elif persistent_quiz_04_q_20_seen == False: 
            $ persistent_quiz_04_q_20_seen = True
            $ persistent_quiz_04_q_counter +=1
            jump quiz_04_question_20










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 01  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_01:
    call screen quiz_04_question_01_imagemap
    $ result = _return

## Imagebutton for question 01
screen quiz_04_question_01_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_01_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_01_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_01_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_01_s04")

    ## Place quiz 04 question 01 here
    text _p("""
        {b} HTML code is used to ?{/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 01 answer 01 here
    text _p("""
        {b}program robots{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 01 answer 02 here
    text _p("""
        {b}Analyze data {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 01 answer 03 here
    text _p("""
        {b}Build and structure web pages{/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 01 answer 04 here
    text _p("""
        {b} None of the above{/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_01_time_up")   

label quiz_04_q_01_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_01_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_01_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_01_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_01_time_up:
    #$ persistent_quiz_04_q_01_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout









##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 02  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_02:
    call screen quiz_04_question_02_imagemap
    $ result = _return

## Imagebutton for question 02
screen quiz_04_question_02_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_02_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_02_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_02_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_02_s04")

    ## Place quiz 04 question 02 here
    text _p("""
        {b} Complete the button element tag : \n 
            ____ button >{/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 02 answer 01 here
    text _p("""
        {b} Hashtag \" # \"  {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 02 answer 02 here
    text _p("""
        {b}Greater than symbol \" > \"  {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 02 answer 03 here
    text _p("""
        {b}Less than symbol \" < \" {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 02 answer 04 here
    text _p("""
        {b} Asterisk \" * \"  {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_02_time_up")    

label quiz_04_q_02_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_02_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_02_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    
    jump quiz_04_base_checker

label quiz_04_q_02_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_02_time_up:
    #$ persistent_quiz_04_q_02_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 03  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_03:
    call screen quiz_04_question_03_imagemap
    $ result = _return

## Imagebutton for question 03
screen quiz_04_question_03_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_03_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_03_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_03_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_03_s04")

    ## Place quiz 04 question 03 here
    text _p("""
        {b}  Complete the button element tag : \n 
            < button _____{/b}
        """) xpos 138 ypos 128 size 50 xsize 1704 color "#333333" 

    ## Place quiz 04 question 03 answer 01 here
    text _p("""
        {b} Hashtag \" # \"  {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 03 answer 02 here
    text _p("""
        {b} Greater than symbol \" > \" {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 03 answer 03 here
    text _p("""
        {b} Less than symbol \" < \" {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 03 answer 04 here
    text _p("""
        {b} Asterisk \" * \" {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_03_time_up")    

label quiz_04_q_03_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_03_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_03_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_03_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_03_time_up:
    #$ persistent_quiz_04_q_03_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 04  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_04:
    call screen quiz_04_question_04_imagemap
    $ result = _return

## Imagebutton for question 04
screen quiz_04_question_04_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_04_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_04_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_04_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_04_s04")

    ## Place quiz 04 question 04 here
    text _p("""
        {b}  Complete the image tag : 
        \n < img ___{/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 04 answer 01 here
    text _p("""
        {b} Hashtag \" # \" {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 04 answer 02 here
    text _p("""
        {b} Greater than symbol \" > \" {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 04 answer 03 here
    text _p("""
        {b} Less than symbol \" < \" {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 04 answer 04 here
    text _p("""
        {b} Asterisk \" * \" {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_04_time_up")    

label quiz_04_q_04_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_04_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_04_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_04_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_04_time_up:
    #$ persistent_quiz_04_q_04_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout












##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 05  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_05:
    call screen quiz_04_question_05_imagemap
    $ result = _return

## Imagebutton for question 05
screen quiz_04_question_05_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_05_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_05_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_05_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_05_s04")

    ## Place quiz 04 question 05 here
    text _p("""
        {b}  For HTML tag is <img> ? {/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 05 answer 01 here
    text _p("""
        {b} Button {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 05 answer 02 here
    text _p("""
        {b} Image {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 05 answer 03 here
    text _p("""
        {b}Text Paragraph {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 05 answer 04 here
    text _p("""
        {b} Table {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_05_time_up")    


label quiz_04_q_05_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_05_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_05_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_05_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_05_time_up:
    #$ persistent_quiz_04_q_05_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 06  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_06:
    call screen quiz_04_question_06_imagemap
    $ result = _return

## Imagebutton for question 06
screen quiz_04_question_06_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_06_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_06_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_06_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_06_s04")

    ## Place quiz 04 question 06 here
    text _p("""*
        {b}  For HTML tag is \" <p> \" ? {/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 06 answer 01 here
    text _p("""
        {b} Button {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 06 answer 02 here
    text _p("""
        {b} Image {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 06 answer 03 here
    text _p("""
        {b}Text Paragraph {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 06 answer 04 here
    text _p("""
        {b}Table {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_06_time_up")    

label quiz_04_q_06_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_06_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_06_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    
    jump quiz_04_base_checker

label quiz_04_q_06_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_06_time_up:
    #$ persistent_quiz_04_q_06_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 07  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_07:
    call screen quiz_04_question_07_imagemap
    $ result = _return

## Imagebutton for question 07
screen quiz_04_question_07_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_07_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_07_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_07_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_07_s04")

    ## Place quiz 04 question 07 here
    text _p("""
        {b} It controls the structure of a web page  {/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 07 answer 01 here
    text _p("""
        {b} CSS {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 07 answer 02 here
    text _p("""
        {b} HTML {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 07 answer 03 here
    text _p("""
        {b} JavaScript {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 07 answer 04 here
    text _p("""
        {b}Python{/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_07_time_up")    

label quiz_04_q_07_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_07_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_07_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_07_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_07_time_up:
    #$ persistent_quiz_04_q_07_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 08  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_08:
    call screen quiz_04_question_08_imagemap
    $ result = _return

## Imagebutton for question 08
screen quiz_04_question_08_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_08_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_08_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_08_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_08_s04")

    ## Place quiz 04 question 08 here
    text _p("""
        {b}  It controls the presentation of a web. {/b}
        """) xpos 138 ypos 128 size 50 xsize 1704 color "#333333" 

    ## Place quiz 04 question 08 answer 01 here
    text _p("""
        {b} CSS {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 08 answer 02 here
    text _p("""
        {b} HTML {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 08 answer 03 here
    text _p("""
        {b} JavaScript {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 08 answer 04 here
    text _p("""
        {b} Python {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_08_time_up")    

label quiz_04_q_08_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_08_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_08_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_08_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_08_time_up:
    #$ persistent_quiz_04_q_08_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 09  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_09:
    call screen quiz_04_question_09_imagemap
    $ result = _return

## Imagebutton for question 09
screen quiz_04_question_09_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_09_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_09_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_09_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_09_s04")

    ## Place quiz 04 question 09 here
    text _p("""
        {b} It controls the behavior of a web page {/b}
        """) xpos 138 ypos 128 size 50 xsize 1704 color "#333333" 

    ## Place quiz 04 question 09 answer 01 here
    text _p("""
        {b} CSS {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 09 answer 02 here
    text _p("""
        {b} HTML {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 09 answer 03 here
    text _p("""
        {b} JavaScript {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 09 answer 04 here
    text _p("""
        {b} Python {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_09_time_up")    

label quiz_04_q_09_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_09_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_09_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    
    jump quiz_04_base_checker

label quiz_04_q_09_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_09_time_up:
    #$ persistent_quiz_04_q_09_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 10  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_10:
    call screen quiz_04_question_10_imagemap
    $ result = _return

## Imagebutton for question 10
screen quiz_04_question_10_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_10_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_10_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_10_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_10_s04")

    ## Place quiz 04 question 10 here
    text _p("""
        {b}  Who is the founder of HTML? {/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 10 answer 01 here
    text _p("""
        {b} Tim Berners-Lee  {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 10 answer 02 here
    text _p("""
        {b} Wium Lie {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 10 answer 03 here
    text _p("""
        {b} James Gosling {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 10 answer 04 here
    text _p("""
        {b} Guido van Rossum {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_10_time_up")    

label quiz_04_q_10_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_10_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_10_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_10_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_10_time_up:
    #$ persistent_quiz_04_q_10_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 11  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_11:
    call screen quiz_04_question_11_imagemap
    $ result = _return

## Imagebutton for question 11
screen quiz_04_question_11_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_11_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_11_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_11_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_11_s04")

    ## Place quiz 04 question 11 here
    text _p("""
        {b}  When was HTML developed? {/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 11 answer 01 here
    text _p("""
        {b} 1981 {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 11 answer 02 here
    text _p("""
        {b} 1985 {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 11 answer 03 here
    text _p("""
        {b} 1991 {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 11 answer 04 here
    text _p("""
        {b} 2040 {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_11_time_up")    

label quiz_04_q_11_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_11_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_11_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    
    jump quiz_04_base_checker

label quiz_04_q_11_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_11_time_up:
    #$ persistent_quiz_04_q_11_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 12  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_12:
    call screen quiz_04_question_12_imagemap
    $ result = _return

## Imagebutton for question 12
screen quiz_04_question_12_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_12_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_12_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_12_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_12_s04")

    ## Place quiz 04 question 12 here
    text _p("""
        {b} Fill thae black: HTML can be used only to develop \n
            _____ Webpages {/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 12 answer 01 here
    text _p("""
        {b} Lack of security {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 12 answer 02 here
    text _p("""
        {b} Static {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 12 answer 03 here
    text _p("""
        {b} Styling {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 12 answer 04 here
    text _p("""
        {b} Complex {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_12_time_up")    

label quiz_04_q_12_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_12_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_12_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_12_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_12_time_up:
    #$ persistent_quiz_04_q_12_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout












##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 13  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_13:
    call screen quiz_04_question_13_imagemap
    $ result = _return

## Imagebutton for question 13
screen quiz_04_question_13_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_13_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_13_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_13_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_13_s04")

    ## Place quiz 04 question 13 here
    text _p("""
        {b}  What is IDE? {/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 13 answer 01 here
    text _p("""
        {b} Integrated Development Environment {/b}
        """) xpos 138 ypos 411 size 40 xsize 740 color "#333333" 

    ## Place quiz 04 question 13 answer 02 here
    text _p("""
        {b} Interactive Development Environment {/b}
        """) xpos 1038 ypos 411 size 40 xsize 740  color "#333333" 

    ## Place quiz 04 question 13 answer 03 here
    text _p("""
        {b} Interaction Debugging Environment {/b}
        """) xpos 138 ypos 738 size 40 xsize 740  color "#333333" 

    ## Place quiz 04 question 13 answer 04 here
    text _p("""
        {b} Integrated Debugging Environment {/b}
        """) xpos 1038 ypos 738 size 40 xsize 740  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
   # text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_13_time_up")    

label quiz_04_q_13_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_13_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_13_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_13_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_13_time_up:
    #$ persistent_quiz_04_q_13_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 14  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_14:
    call screen quiz_04_question_14_imagemap
    $ result = _return

## Imagebutton for question 14
screen quiz_04_question_14_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_14_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_14_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_14_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_14_s04")

    ## Place quiz 04 question 14 here
    text _p("""
        {b}  What is the mening of GUI? {/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 14 answer 01 here
    text _p("""
        {b}Game User Involve  {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 14 answer 02 here
    text _p("""
        {b} Graphical User Integrated {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 14 answer 03 here
    text _p("""
        {b} Graphical User Interface {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 14 answer 04 here
    text _p("""
        {b} Game User Important {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_14_time_up")    

label quiz_04_q_14_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_14_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_14_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_14_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_14_time_up:
    #$ persistent_quiz_04_q_14_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 15  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_15:
    call screen quiz_04_question_15_imagemap
    $ result = _return

## Imagebutton for question 15
screen quiz_04_question_15_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_15_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_15_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_15_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_15_s04")

    ## Place quiz 04 question 15 here
    text _p("""
        {b} Complete the line to code a "Like" button \n
            <button>______ </button>{/b}
        """) xpos 138 ypos 128 size 50 xsize 1604 color "#333333" 

    ## Place quiz 04 question 15 answer 01 here
    text _p("""
        {b} Like {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 15 answer 02 here
    text _p("""
        {b} Dislike {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 15 answer 03 here
    text _p("""
        {b} Heart {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 15 answer 04 here
    text _p("""
        {b} Click {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
   #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_15_time_up")    

label quiz_04_q_15_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_15_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_15_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_15_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_15_time_up:
    #$ persistent_quiz_04_q_15_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 16  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_16:
    call screen quiz_04_question_16_imagemap
    $ result = _return

## Imagebutton for question 16
screen quiz_04_question_16_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_16_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_16_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_16_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_16_s04")

    ## Place quiz 04 question 16 here
    text _p("""
        {b} Complete the code for the button \n
            <button> Like ________{/b}
        """) xpos 138 ypos 128 size 50 xsize 1604 color "#333333" 

    ## Place quiz 04 question 16 answer 01 here
    text _p("""
        {b} <button>  {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 16 answer 02 here
    text _p("""
        {b} </button> {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 16 answer 03 here
    text _p("""
        {b} <img> {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 16 answer 04 here
    text _p("""
        {b} Like {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
   # text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_16_time_up")    

label quiz_04_q_16_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_16_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_16_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_16_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_16_time_up:
    #$ persistent_quiz_04_q_16_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 17  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_17:
    call screen quiz_04_question_17_imagemap
    $ result = _return

## Imagebutton for question 17
screen quiz_04_question_17_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_17_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_17_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_17_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_17_s04")

    ## Place quiz 04 question 17 here
    text _p("""
        {b} Complete the code for a valid paragraph text \n
            <p> TEXT ______{/b}
        """) xpos 138 ypos 128 size 50 xsize 1604 color "#333333" 

    ## Place quiz 04 question 17 answer 01 here
    text _p("""
        {b} \" <p> \" {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 17 answer 02 here
    text _p("""
        {b} \" </b> \" {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 17 answer 03 here
    text _p("""
        {b}\" </p> \"{/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 17 answer 04 here
    text _p("""
        {b} \" <b> \" {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_17_time_up")    

label quiz_04_q_17_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_17_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_17_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    
    jump quiz_04_base_checker

label quiz_04_q_17_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_17_time_up:
    #$ persistent_quiz_04_q_17_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 18  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_18:
    call screen quiz_04_question_18_imagemap
    $ result = _return

## Imagebutton for question 18
screen quiz_04_question_18_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_18_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_18_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_18_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_18_s04")

    ## Place quiz 04 question 18 here
    text _p("""
        {b}  What’s the correct way to code a paragraph text? {/b}
        """) xpos 138 ypos 128 size 50 xsize 1604 color "#333333" 

    ## Place quiz 04 question 18 answer 01 here
    text _p("""
        {b} \" <p> Text <p> \" {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 18 answer 02 here
    text _p("""
        {b} \" <p> Text </p> \" {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 18 answer 03 here
    text _p("""
        {b} \" <b> Text </b> \" {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 18 answer 04 here
    text _p("""
        {b} \" <p> Text  \" {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_18_time_up")    

label quiz_04_q_18_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_18_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_18_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_18_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_18_time_up:
    #$ persistent_quiz_04_q_18_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout












##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 19  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_19:
    call screen quiz_04_question_19_imagemap
    $ result = _return

## Imagebutton for question 19
screen quiz_04_question_19_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_19_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_19_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_19_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_19_s04")

    ## Place quiz 04 question 19 here
    text _p("""
        {b} What’s the content of this web page? \n
        <p>This product is awesome</p> \n
        <button>Buy</button> \n
        {/b}
        """) xpos 138 ypos 128 size 30 xsize 1604 color "#333333" 

    ## Place quiz 04 question 19 answer 01 here
    text _p("""
        {b} An image and a button{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 19 answer 02 here
    text _p("""
        {b} A table and a button {/b}
        """) xpos 1038 ypos 411 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 19 answer 03 here
    text _p("""
        {b} A paragraph text and a button {/b}
        """) xpos 138 ypos 738 size 40 xsize 840  color "#333333" 

    ## Place quiz 04 question 19 answer 04 here
    text _p("""
        {b} An image and a paragraph {/b}
        """) xpos 1038 ypos 738 size 40 xsize 840  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    #text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_19_time_up")    

label quiz_04_q_19_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_19_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_19_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    
    jump quiz_04_base_checker

label quiz_04_q_19_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_19_time_up:
    #$ persistent_quiz_04_q_19_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 04 - QUESTION 20  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_04_question_20:
    call screen quiz_04_question_20_imagemap
    $ result = _return

## Imagebutton for question 20
screen quiz_04_question_20_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_04_q_20_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_04_q_20_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_04_q_20_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_04_q_20_s04")

    ## Place quiz 04 question 20 here
    text _p("""
        {b}  A web browser is _____. {/b}
        """) xpos 138 ypos 128 size 40 xsize 1550 color "#333333" 

    ## Place quiz 04 question 20 answer 01 here
    text _p("""
        {b} Requires the user to understand HTML code {/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 04 question 20 answer 02 here
    text _p("""
        {b} Provides a graphical user interface that translates HTML code {/b}
        """) xpos 1038 ypos 411 size 40 xsize 704  color "#333333" 

    ## Place quiz 04 question 20 answer 03 here
    text _p("""
        {b} A multi-platform language that can be used as a platform in itself.{/b}
        """) xpos 138 ypos 738 size 40 xsize 704  color "#333333" 

    ## Place quiz 04 question 20 answer 04 here
    text _p("""
        {b}  High-level programming language with dynamic semantics {/b}
        """) xpos 1038 ypos 738 size 40 xsize 704  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
   # text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_04_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_04_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_04_q_20_time_up")    

label quiz_04_q_20_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_20_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_04_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    
    jump quiz_04_base_checker

label quiz_04_q_20_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_04_base_checker

label quiz_04_q_20_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_04_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_04_base_checker

label quiz_04_q_20_time_up:
    #$ persistent_quiz_04_q_20_seen = True
    #$ persistent_quiz_04_q_counter +=1
    jump quiz_04_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗
##  ║ ███  RESULTS                                                            ███ ║
##  ║ ███  This is the section responsible for showing your results in a      ███ ║
##  ║ ███  verbal way. Can be changed to suite needs.                         ███ ║
##  ╚═════════════════════════════════════════════════════════════════════════════╝

label quiz_04_conclusion:
    if persistent_quiz_04_q_counter_correct_answer == 0:
        scene pie_04
        hide blank_question_windows with moveoutright
        e"Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4


    elif persistent_quiz_04_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        e"Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4


    elif persistent_quiz_04_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        e"Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit() 
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4


    elif persistent_quiz_04_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        e"Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4
        

    elif persistent_quiz_04_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        e"Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4

    elif persistent_quiz_04_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright      
        e"Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4

    elif persistent_quiz_04_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        e"Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4

    elif persistent_quiz_04_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        e "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4

    elif persistent_quiz_04_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        e "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4

    elif persistent_quiz_04_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        e "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4

    elif persistent_quiz_04_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        e "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_04_seen == True
        jump pagtapos_ng_quiz_4

























#label before_pagtapos_ng_quiz_4:
    
    ## ╔════════════════════════╗
    ## ║ temporary please erase ║
    ## ╚════════════════════════╝
    #"First time mo take itong quiz"
    #call screen chp_one_assessment()
    #return 
    ## ╔════════════════════════╗
    ## ║ temporary please erase ║
    ## ╚════════════════════════╝ 
    #$ renpy.quit() 

#label quiz_04_repeat_landing_label_seen:
    #put label kung saan mo gusto ilaghay
    ## ╔════════════════════════╗
    ## ║ temporary please erase ║
    ## ╚════════════════════════╝
    #"Inulit mo itong quiz"
    #call screen chp_one_assessment()
    #return 
    ## ╔════════════════════════╗
    ## ║ temporary please erase ║
    ## ╚════════════════════════╝ 
    #$ renpy.quit()  

    #$ renpy.quit() 

