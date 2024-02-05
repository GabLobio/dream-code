##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  INITIALIATION / LOOP CHECKER                                       ███ ║ 
##  ║ ███  This is the section responsible for going inside the               ███ ║ 
##  ║ ███  quiz, dictating the loop as well aswhen the quiz qill end.         ███ ║  
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

default persistent_quiz_02_q_counter_correct_previous_answer = 0
default persistent_quiz_02_q_counter_correct_answer = 0

label start_quiz_02_initialization:
    if whole_quiz_02_seen == True:
        jump start_quiz_02
    else:
        $ persistent_quiz_02_q_counter_correct_previous_answer = 0
        $ persistent_quiz_02_q_counter_correct_answer = 0

# You place any dialogue or declare image here before quiz starts
label start_quiz_02:
    ## ╔════════════════════════╗
    ## ║ temporary please erase ║
    ## ╚════════════════════════╝ 
    $ persistent_quiz_02_q_01_seen = False
    $ persistent_quiz_02_q_02_seen = False
    $ persistent_quiz_02_q_03_seen = False
    $ persistent_quiz_02_q_04_seen = False
    $ persistent_quiz_02_q_05_seen = False
    $ persistent_quiz_02_q_06_seen = False
    $ persistent_quiz_02_q_07_seen = False
    $ persistent_quiz_02_q_08_seen = False
    $ persistent_quiz_02_q_09_seen = False
    $ persistent_quiz_02_q_10_seen = False
    $ persistent_quiz_02_q_11_seen = False
    $ persistent_quiz_02_q_12_seen = False
    $ persistent_quiz_02_q_13_seen = False
    $ persistent_quiz_02_q_14_seen = False
    $ persistent_quiz_02_q_15_seen = False
    $ persistent_quiz_02_q_16_seen = False
    $ persistent_quiz_02_q_17_seen = False
    $ persistent_quiz_02_q_18_seen = False
    $ persistent_quiz_02_q_19_seen = False
    $ persistent_quiz_02_q_20_seen = False

    $ persistent_quiz_02_q_counter = 0

    jump start_quiz_02_first_check

label start_quiz_02_first_check:
    if whole_quiz_02_seen == True:
        jump start_quiz_02_second_check
    else:    
        jump start_quiz_02_second_check    

label start_quiz_02_second_check:
    if persistent_quiz_02_q_counter_correct_previous_answer == 0:
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 1:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 1
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 2:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 2
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 3:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 3
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 4:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 4
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 5:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 5
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 6:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 6
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 7:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 7
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 8:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 8
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 9:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 9
        jump start_quiz_02_third_check

    elif persistent_quiz_02_q_counter_correct_previous_answer == 10:
        $ persistent_quiz_02_q_counter_correct_previous_answer -= 10
        jump start_quiz_02_third_check

label start_quiz_02_third_check:

    if whole_quiz_02_seen == True:
        e "Repeat exam again?"
        e "OK, let's proceed..."
        if persistent_quiz_02_q_counter_correct_answer == 0:
            jump start_quiz_02_resume

        elif persistent_quiz_02_q_counter_correct_answer == 1:
            $ persistent_quiz_02_q_counter_correct_previous_answer += 1 
            $ persistent_quiz_02_q_counter_correct_answer -= 1
            $ persistent_quiz_total_points_counter_correct_answer -= 1 
            jump start_quiz_02_resume 

        elif persistent_quiz_02_q_counter_correct_answer == 2:
            $ persistent_quiz_02_q_counter_correct_previous_answer += 2 
            $ persistent_quiz_02_q_counter_correct_answer -= 2
            $ persistent_quiz_total_points_counter_correct_answer -= 2 
            jump start_quiz_02_resume

        elif persistent_quiz_02_q_counter_correct_answer == 3: 
            $ persistent_quiz_02_q_counter_correct_previous_answer += 3
            $ persistent_quiz_02_q_counter_correct_answer -= 3
            $ persistent_quiz_total_points_counter_correct_answer -= 3
            jump start_quiz_02_resume

        elif persistent_quiz_02_q_counter_correct_answer == 4: 
            $ persistent_quiz_02_q_counter_correct_previous_answer += 4
            $ persistent_quiz_02_q_counter_correct_answer -= 4 
            $ persistent_quiz_total_points_counter_correct_answer -= 4
            jump start_quiz_02_resume

        elif persistent_quiz_02_q_counter_correct_answer == 5:
            $ persistent_quiz_02_q_counter_correct_previous_answer += 5
            $ persistent_quiz_02_q_counter_correct_answer -= 5  
            $ persistent_quiz_total_points_counter_correct_answer -= 5
            jump start_quiz_02_resume

        elif persistent_quiz_02_q_counter_correct_answer == 6: 
            $ persistent_quiz_02_q_counter_correct_previous_answer += 6
            $ persistent_quiz_02_q_counter_correct_answer -= 6 
            $ persistent_quiz_total_points_counter_correct_answer -= 6
            jump start_quiz_02_resume

        elif persistent_quiz_02_q_counter_correct_answer == 7: 
            $ persistent_quiz_02_q_counter_correct_previous_answer += 7
            $ persistent_quiz_02_q_counter_correct_answer -= 7 
            $ persistent_quiz_total_points_counter_correct_answer -= 7
            jump start_quiz_02_resume

        elif persistent_quiz_02_q_counter_correct_answer == 8:  
            $ persistent_quiz_02_q_counter_correct_previous_answer += 8
            $ persistent_quiz_02_q_counter_correct_answer -= 8
            $ persistent_quiz_total_points_counter_correct_answer -= 8
            jump start_quiz_02_resume

        elif persistent_quiz_02_q_counter_correct_answer == 9:  
            $ persistent_quiz_02_q_counter_correct_previous_answer += 9
            $ persistent_quiz_02_q_counter_correct_answer -= 9
            $ persistent_quiz_total_points_counter_correct_answer -= 9
            jump start_quiz_02_resume

        elif persistent_quiz_02_q_counter_correct_answer == 10: 
            $ persistent_quiz_02_q_counter_correct_previous_answer += 10 
            $ persistent_quiz_02_q_counter_correct_answer -= 10
            $ persistent_quiz_total_points_counter_correct_answer -= 10
            jump start_quiz_02_resume

    jump start_quiz_02_resume         






label start_quiz_02_resume:
    $ renpy.block_rollback()
    $ whole_quiz_02_seen = True
    #"Insert Dialogue Here"
    scene quiz_window_blank 
    show quiz_start with moveinleft
    $ renpy.pause()
    hide quiz_start with moveoutright
    show blank_question_windows with moveinleft
    jump quiz_02_randomizer

# This label will check if you already answered 10 questions. 
# If you have answered 10, you will conclude this set of quiz.
# Else, you will loop back to the randomized
label quiz_02_base_checker:
    if persistent_quiz_02_q_counter == 10:
        jump quiz_02_conclusion
    else:      
        scene quiz_window_blank 
        show blank_question_windows
        hide blank_question_windows with moveoutright
        show quiz_next_question with moveinleft
        $ renpy.pause()
        hide quiz_next_question with moveoutright
        show blank_question_windows with moveinleft
        jump quiz_02_randomizer

label quiz_02_base_checker_timeout:
    if persistent_quiz_02_q_counter == 10:
        jump quiz_02_conclusion
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
        jump quiz_02_randomizer










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION RANDOMIZER                                                ███ ║ 
##  ║ ███  This is the section where the questions are selected in random.    ███ ║ 
##  ║ ███                                                                     ███ ║  
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_randomizer:
    $ choice = renpy.random.choice(['q01', 'q02', 'q03', 'q04', 'q05', 'q06', 'q07', 'q08', 'q09', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20'])

    if choice == 'q01': # quiz_01_q_01_checker
        if persistent_quiz_02_q_01_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_01_seen == False: 
            $ persistent_quiz_02_q_01_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_01

    if choice == 'q02': # quiz_01_q_02_checker
        if persistent_quiz_02_q_02_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_02_seen == False: 
            $ persistent_quiz_02_q_02_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_02

    if choice == 'q03': # quiz_01_q_03_checker
        if persistent_quiz_02_q_03_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_03_seen == False: 
            $ persistent_quiz_02_q_03_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_03

    if choice == 'q04': # quiz_01_q_04_checker
        if persistent_quiz_02_q_04_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_04_seen == False: 
            $ persistent_quiz_02_q_04_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_04

    if choice == 'q05': # quiz_01_q_05_checker
        if persistent_quiz_02_q_05_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_05_seen == False: 
            $ persistent_quiz_02_q_05_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_05

    if choice == 'q06': # quiz_01_q_06_checker
        if persistent_quiz_02_q_06_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_06_seen == False: 
            $ persistent_quiz_02_q_06_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_06

    if choice == 'q07': # quiz_01_q_07_checker
        if persistent_quiz_02_q_07_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_07_seen == False: 
            $ persistent_quiz_02_q_07_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_07

    if choice == 'q08': # quiz_01_q_08_checker
        if persistent_quiz_02_q_08_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_08_seen == False: 
            $ persistent_quiz_02_q_08_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_08

    if choice == 'q09': # quiz_01_q_09_checker
        if persistent_quiz_02_q_09_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_09_seen == False: 
            $ persistent_quiz_02_q_09_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_09

    if choice == 'q10': # quiz_01_q_10_checker
        if persistent_quiz_02_q_10_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_10_seen == False: 
            $ persistent_quiz_02_q_10_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_10

    if choice == 'q11': # quiz_01_q_11_checker
        if persistent_quiz_02_q_11_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_11_seen == False: 
            $ persistent_quiz_02_q_11_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_11

    if choice == 'q12': # quiz_01_q_12_checker
        if persistent_quiz_02_q_12_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_12_seen == False: 
            $ persistent_quiz_02_q_12_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_12

    if choice == 'q13': # quiz_01_q_13_checker
        if persistent_quiz_02_q_13_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_13_seen == False: 
            $ persistent_quiz_02_q_13_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_13

    if choice == 'q14': # quiz_01_q_14_checker
        if persistent_quiz_02_q_14_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_14_seen == False: 
            $ persistent_quiz_02_q_14_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_14

    if choice == 'q15': # quiz_01_q_15_checker
        if persistent_quiz_02_q_15_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_15_seen == False: 
            $ persistent_quiz_02_q_15_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_15

    if choice == 'q16': # quiz_01_q_16_checker
        if persistent_quiz_02_q_16_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_16_seen == False: 
            $ persistent_quiz_02_q_16_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_16

    if choice == 'q17': # quiz_01_q_17_checker
        if persistent_quiz_02_q_17_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_17_seen == False: 
            $ persistent_quiz_02_q_17_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_17

    if choice == 'q18': # quiz_01_q_18_checker
        if persistent_quiz_02_q_18_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_18_seen == False: 
            $ persistent_quiz_02_q_18_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_18

    if choice == 'q19': # quiz_01_q_19_checker
        if persistent_quiz_02_q_19_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_19_seen == False: 
            $ persistent_quiz_02_q_19_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_19

    if choice == 'q20': # quiz_01_q_20_checker
        if persistent_quiz_02_q_20_seen == True:
            jump quiz_02_randomizer
        elif persistent_quiz_02_q_20_seen == False: 
            $ persistent_quiz_02_q_20_seen = True
            $ persistent_quiz_02_q_counter +=1
            jump quiz_02_question_20







##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 01  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_01:
    call screen quiz_02_question_01_imagemap
    $ result = _return

## Imagebutton for question 01
screen quiz_02_question_01_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_01_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_01_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_01_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_01_s04")

    ## Place quiz 02 question 01 here
    text _p("""
        {b} Content elements like buttons, paragraphs, and images need to be nested inside … {/b}
        """) xpos 138 ypos 128 size 50 xsize 1552 color "#333333" 

    ## Place quiz 02 question 01 answer 01 here
    text _p("""
        {b}The tail container{/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 01 answer 02 here
    text _p("""
        {b}The head container{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 01 answer 03 here
    text _p("""
        {b} The body container{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 01 answer 04 here
    text _p("""
        {b} The end container{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_01_time_up")   

label quiz_02_q_01_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_01_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_01_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_01_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_01_time_up:
    #$ persistent_quiz_02_q_01_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout









##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 02  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_02:
    call screen quiz_02_question_02_imagemap
    $ result = _return

## Imagebutton for question 02
screen quiz_02_question_02_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_02_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_02_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_02_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_02_s04")

    ## Place quiz 02 question 02 here
    text _p("""
        {b}Complete the code to disable the button \n
        \" ____ <button>OK</button> ____{/b} \"
        """) xpos 138 ypos 128 size 50 xsize 1552 color "#333333" 

    ## Place quiz 02 question 02 answer 01 here
    text _p("""
        {b} \"<!--\" , \"-->\" {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 02 answer 02 here
    text _p("""
        {b} \" <!-- \"  {/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 02 answer 03 here
    text _p("""
        {b}\" "--> \" {/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 02 answer 04 here
    text _p("""
        {b} None of the above {/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_02_time_up")    

label quiz_02_q_02_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_02_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_02_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_02_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_02_time_up:
    #$ persistent_quiz_02_q_02_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 03  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_03:
    call screen quiz_02_question_03_imagemap
    $ result = _return

## Imagebutton for question 03
screen quiz_02_question_03_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_03_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_03_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_03_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_03_s04")

    ## Place quiz 02 question 03 here
    text _p("""
        {b}Specific and technical information like title, description, author and keywords are nested inside …{/b}
        """) xpos 138 ypos 128 size 40 xsize 1552 color "#333333" 

    ## Place quiz 02 question 03 answer 01 here
    text _p("""
        {b}The tail container{/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 03 answer 02 here
    text _p("""
        {b}The head container{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 03 answer 03 here
    text _p("""
        {b} The body container{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 03 answer 04 here
    text _p("""
        {b}The end container{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_03_time_up")    

label quiz_02_q_03_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_03_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_03_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_03_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_03_time_up:
    #$ persistent_quiz_02_q_03_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 04  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_04:
    call screen quiz_02_question_04_imagemap
    $ result = _return

## Imagebutton for question 04
screen quiz_02_question_04_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_04_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_04_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_04_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_04_s04")

    ## Place quiz 02 question 04 here
    text _p("""
        {b}What's wrong with this code? \n
        <h1>Welcome to my website!</h1> \n
        <p>This is the home page.</p> \n
        <h1>About me</h1>{/b}
        """) xpos 138 ypos 128 size 20 xsize 1602 color "#333333" 

    ## Place quiz 02 question 04 answer 01 here
    text _p("""
        {b}It uses multiple \"<p>\" tagsm {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 04 answer 02 here
    text _p("""
        {b} It uses multiple \"</p>\" tags{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 04 answer 03 here
    text _p("""
        {b}It uses multiple \"<h1>\" tags{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 04 answer 04 here
    text _p("""
        {b}\"<p>\" tags shouldn't be nested inside the body.{/b}
        """) xpos 1038 ypos 738 size 40 xsize 780  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_04_time_up")    

label quiz_02_q_04_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_04_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_04_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_04_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_04_time_up:
    #$ persistent_quiz_02_q_04_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout












##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 05  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_05:
    call screen quiz_02_question_05_imagemap
    $ result = _return

## Imagebutton for question 05
screen quiz_02_question_05_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_05_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_05_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_05_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_05_s04")

    ## Place quiz 02 question 05 here
    text _p("""
        {b}Complete the code to make a comment
        \" < !-- Explanation - - ____ \"{/b} 
        """) xpos 138 ypos 128 size 40 xsize 1602 color "#333333" 

    ## Place quiz 02 question 05 answer 01 here
    text _p("""
        {b}\" < \"  {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 05 answer 02 here
    text _p("""
        {b} \" > \"{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 05 answer 03 here
    text _p("""
        {b} \" = \"{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 05 answer 04 here
    text _p("""
        {b} \" * \" {/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_05_time_up")    


label quiz_02_q_05_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_05_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_05_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_05_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_05_time_up:
    #$ persistent_quiz_02_q_05_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 06  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_06:
    call screen quiz_02_question_06_imagemap
    $ result = _return

## Imagebutton for question 06
screen quiz_02_question_06_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_06_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_06_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_06_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_06_s04")

    ## Place quiz 02 question 06 here
    text _p("""
        {b} Complete the code to make a comment \n
        \" ____ !-- Explanation - - > \" {/b}
        """) xpos 138 ypos 128 size 50 xsize 1602 color "#333333" 

    ## Place quiz 02 question 06 answer 01 here
    text _p("""
        {b} \" < \" {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 06 answer 02 here
    text _p("""
        {b} \" > \"{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 06 answer 03 here
    text _p("""
        {b} \" = \" {/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 06 answer 04 here
    text _p("""
        {b} \" * \"{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_06_time_up")    

label quiz_02_q_06_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_06_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_06_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_06_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_06_time_up:
    #$ persistent_quiz_02_q_06_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 07  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_07:
    call screen quiz_02_question_07_imagemap
    $ result = _return

## Imagebutton for question 07
screen quiz_02_question_07_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_07_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_07_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_07_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_07_s04")

    ## Place quiz 02 question 07 here
    text _p("""
        {b}Match the terms with their definitions \n
        Display the web page: ________{/b}
        """) xpos 138 ypos 128 size 40 xsize 1602 color "#333333" 

    ## Place quiz 02 question 07 answer 01 here
    text _p("""
        {b}\" Web server \"{/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 07 answer 02 here
    text _p("""
        {b}\" Web browser \"{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 07 answer 03 here
    text _p("""
        {b} \" Website \"{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 07 answer 04 here
    text _p("""
        {b} None of the above {/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_07_time_up")    

label quiz_02_q_07_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_07_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_07_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_07_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_07_time_up:
    #$ persistent_quiz_02_q_07_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 08  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_08:
    call screen quiz_02_question_08_imagemap
    $ result = _return

## Imagebutton for question 08
screen quiz_02_question_08_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_08_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_08_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_08_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_08_s04")

    ## Place quiz 02 question 08 here
    text _p("""
        {b}Match the terms with their definitions \n
        Stores and provides information: _____{/b}
        """) xpos 138 ypos 128 size 50 xsize 1602 color "#333333" 

    ## Place quiz 02 question 08 answer 01 here
    text _p("""
        {b} \"Web server \" {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 08 answer 02 here
    text _p("""
        {b} \" Web browser \"{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 08 answer 03 here
    text _p("""
        {b} \" Website \" {/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 08 answer 04 here
    text _p("""
        {b} None of the above {/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_08_time_up")    

label quiz_02_q_08_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_08_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_08_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_08_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_08_time_up:
    #$ persistent_quiz_02_q_08_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 09  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_09:
    call screen quiz_02_question_09_imagemap
    $ result = _return

## Imagebutton for question 09
screen quiz_02_question_09_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_09_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_09_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_09_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_09_s04")

    ## Place quiz 02 question 09 here
    text _p("""
        {b} How many lines will the browser display \n
            <p>Welcome! \n
            Enter your name</p> {/b}
        """) xpos 138 ypos 128 size 30 xsize 1602 color "#333333" 

    ## Place quiz 02 question 09 answer 01 here
    text _p("""
        {b} 1 line {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 09 answer 02 here
    text _p("""
        {b} 2 lines {/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 09 answer 03 here
    text _p("""
        {b} 3 lines {/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 09 answer 04 here
    text _p("""
        {b} 4 lines {/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_09_time_up")    

label quiz_02_q_09_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_09_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_09_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_09_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_09_time_up:
    #$ persistent_quiz_02_q_09_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 10  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_10:
    call screen quiz_02_question_10_imagemap
    $ result = _return

## Imagebutton for question 10
screen quiz_02_question_10_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_10_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_10_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_10_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_10_s04")

    ## Place quiz 02 question 10 here
    text _p("""
        {b}How many lines will the browser display \n
            <h1> Welcome! </h1> \n
            p> Enter your name</p>{/b}
        """) xpos 138 ypos 128 size 30 xsize 1602 color "#333333" 

    ## Place quiz 02 question 10 answer 01 here
    text _p("""
        {b} 1 line {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 10 answer 02 here
    text _p("""
        {b} 2 lines {/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 10 answer 03 here
    text _p("""
        {b} 3 lines {/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 10 answer 04 here
    text _p("""
        {b} 4 lines {/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_10_time_up")    

label quiz_02_q_10_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_10_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_10_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_10_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_10_time_up:
    #$ persistent_quiz_02_q_10_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 11  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_11:
    call screen quiz_02_question_11_imagemap
    $ result = _return

## Imagebutton for question 11
screen quiz_02_question_11_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_11_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_11_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_11_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_11_s04")

    ## Place quiz 02 question 11 here
    text _p("""
        {b}How many lines will the browser display \n
            \" <h1> Welcome! </h1>\" \n
            \" <!-- <p> Very sunny</p> --> \" {/b}
        """) xpos 138 ypos 128 size 30 xsize 1602 color "#333333" 

    ## Place quiz 02 question 11 answer 01 here
    text _p("""
        {b} 1 line {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 11 answer 02 here
    text _p("""
        {b} 2 lines {/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 11 answer 03 here
    text _p("""
        {b} 3 lines  {/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 11 answer 04 here
    text _p("""
        {b}4 lines{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_11_time_up")    

label quiz_02_q_11_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_11_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_11_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_11_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_11_time_up:
    #$ persistent_quiz_02_q_11_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 12  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_12:
    call screen quiz_02_question_12_imagemap
    $ result = _return

## Imagebutton for question 12
screen quiz_02_question_12_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_12_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_12_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_12_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_12_s04")

    ## Place quiz 02 question 12 here
    text _p("""
        {b} Create a paragraph with comment \n
            \"___<p> Great work </p> ___ \"{/b}
        """) xpos 138 ypos 128 size 50 xsize 1602 color "#333333" 

    ## Place quiz 02 question 12 answer 01 here
    text _p("""
        {b} \"h1 \"  , \" /h1 \"{/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 12 answer 02 here
    text _p("""
        {b} \"p \" ,  \" /p \"{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 12 answer 03 here
    text _p("""
        {b} \"<!-- \" , \"<-->\" {/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 12 answer 04 here
    text _p("""
        {b} \" <img> \"{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_12_time_up")    

label quiz_02_q_12_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_12_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_12_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_12_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_12_time_up:
    #$ persistent_quiz_02_q_12_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout












##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 13  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_13:
    call screen quiz_02_question_13_imagemap
    $ result = _return

## Imagebutton for question 13
screen quiz_02_question_13_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_13_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_13_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_13_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_13_s04")

    ## Place quiz 02 question 13 here
    text _p("""
        {b}Complete the code \n
            \" <h1>Weather Forecast<____> \" \n
            \" <!-- <p> Very sunny</p> ___ \" {/b}
        """) xpos 138 ypos 128 size 30 xsize 1602 color "#333333" 

    ## Place quiz 02 question 13 answer 01 here
    text _p("""
        {b} \" <!-- \" , \" p \" {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 13 answer 02 here
    text _p("""
        {b} \" /h2 \" , \" p \"  {/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 13 answer 03 here
    text _p("""
        {b} \" /h1 \" , \" p \"  {/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 13 answer 04 here
    text _p("""
        {b} \" /h1 \" , \" !--> \" {/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_13_time_up")    

label quiz_02_q_13_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_13_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_13_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_13_s04:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_13_time_up:
    #$ persistent_quiz_02_q_13_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 14  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_14:
    call screen quiz_02_question_14_imagemap
    $ result = _return

## Imagebutton for question 14
screen quiz_02_question_14_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_14_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_14_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_14_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_14_s04")

    ## Place quiz 02 question 14 here
    text _p("""
        {b} Complete the code to create a comment \n
        \" ____ Paragraph element below - - > \" \n
        \" <p>This product is awesome</p> \" {/b}
        """) xpos 138 ypos 128 size 30 xsize 1602 color "#333333" 

    ## Place quiz 02 question 14 answer 01 here
    text _p("""
        {b} \" # \" {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 14 answer 02 here
    text _p("""
        {b}\" <!-- \" {/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 14 answer 03 here
    text _p("""
        {b}\" --> \"{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 14 answer 04 here
    text _p("""
        {b}\" --!> \"{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_14_time_up")    

label quiz_02_q_14_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_14_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_14_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_14_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_14_time_up:
    #$ persistent_quiz_02_q_14_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 15  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_15:
    call screen quiz_02_question_15_imagemap
    $ result = _return

## Imagebutton for question 15
screen quiz_02_question_15_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_15_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_15_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_15_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_15_s04")

    ## Place quiz 02 question 15 here
    text _p("""
        {b}Complete the code \n
            \" <!-- <p> click to submit</p> \" \n
            \" <button>submit<____>{/b} \"
        """) xpos 138 ypos 128 size 30 xsize 1602 color "#333333" 

    ## Place quiz 02 question 15 answer 01 here
    text _p("""
        {b} \"<!--\" , \"button\"{/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 15 answer 02 here
    text _p("""
        {b} \"/h1\" , \"/button\"{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 15 answer 03 here
    text _p("""
        {b} \"-->\" , \"/button\"{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 15 answer 04 here
    text _p("""
        {b} \"/p\" , \"-->\"{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_15_time_up")    

label quiz_02_q_15_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_15_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_15_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_15_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_15_time_up:
    #$ persistent_quiz_02_q_15_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 16  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_16:
    call screen quiz_02_question_16_imagemap
    $ result = _return

## Imagebutton for question 16
screen quiz_02_question_16_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_16_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_16_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_16_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_16_s04")

    ## Place quiz 02 question 16 here
    text _p("""
        {b}Fill the blank \n
        Web pages ____ with different browsers and devices{/b}
        """) xpos 138 ypos 128 size 30 xsize 1602 color "#333333" 

    ## Place quiz 02 question 16 answer 01 here
    text _p("""
        {b} \"collaboration\" {/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 16 answer 02 here
    text _p("""
        {b} \"compatible\" {/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 16 answer 03 here
    text _p("""
        {b} \"cooperation\" {/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 16 answer 04 here
    text _p("""
        {b} None of the above {/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_16_time_up")    

label quiz_02_q_16_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_16_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_16_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_16_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_16_time_up:
    #$ persistent_quiz_02_q_16_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 17  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_17:
    call screen quiz_02_question_17_imagemap
    $ result = _return

## Imagebutton for question 17
screen quiz_02_question_17_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_17_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_17_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_17_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_17_s04")

    ## Place quiz 02 question 17 here
    text _p("""
        {b}Fill the blank \n
        Standards and best practices are needed to make: \n
        Teamwork and ____ more effective{/b}
        """) xpos 138 ypos 128 size 30 xsize 1602 color "#333333" 

    ## Place quiz 02 question 17 answer 01 here
    text _p("""
        {b}\"collaboration\"{/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 17 answer 02 here
    text _p("""
        {b}\"compatible\"{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 17 answer 03 here
    text _p("""
        {b}\"cooperation\"{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 17 answer 04 here
    text _p("""
        {b}None of the above{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_17_time_up")    

label quiz_02_q_17_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_17_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_17_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_17_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_17_time_up:
    #$ persistent_quiz_02_q_17_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 18  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_18:
    call screen quiz_02_question_18_imagemap
    $ result = _return

## Imagebutton for question 18
screen quiz_02_question_18_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_18_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_18_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_18_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_18_s04")

    ## Place quiz 02 question 18 here
    text _p("""
        {b}Some HTML tags need to be placed inside others. This is called?{/b}
        """) xpos 138 ypos 128 size 40 xsize 1602 color "#333333" 

    ## Place quiz 02 question 18 answer 01 here
    text _p("""
        {b}Feathering{/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 18 answer 02 here
    text _p("""
        {b}Egging{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 18 answer 03 here
    text _p("""
        {b}Nesting{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 18 answer 04 here
    text _p("""
        {b}None of the above{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_18_time_up")    

label quiz_02_q_18_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_18_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_18_s03:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_18_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_18_time_up:
    #$ persistent_quiz_02_q_18_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout












##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 19  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_19:
    call screen quiz_02_question_19_imagemap
    $ result = _return

## Imagebutton for question 19
screen quiz_02_question_19_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_19_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_19_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_19_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_19_s04")

    ## Place quiz 02 question 19 here
    text _p("""
        {b} Complete the code to add the head \n
            _____ \n
        \"    <title>Gardening</title>      \" \n
            _____{/b}
        """) xpos 138 ypos 128 size 20 xsize 1602 color "#333333" 

    ## Place quiz 02 question 19 answer 01 here
    text _p("""
        {b}\"</head>\" ,  \"<head>\"{/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 19 answer 02 here
    text _p("""
        {b} \"<head>\" , \"</head>\"{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 19 answer 03 here
    text _p("""
        {b}\"<p>\" , \"</p>\"{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 19 answer 04 here
    text _p("""
        {b} \"feet\" , \"/feet\"{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_19_time_up")    

label quiz_02_q_19_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_19_s02:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1 
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_19_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_19_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_19_time_up:
    #$ persistent_quiz_02_q_19_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 02 - QUESTION 20  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_02_question_20:
    call screen quiz_02_question_20_imagemap
    $ result = _return

## Imagebutton for question 20
screen quiz_02_question_20_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_02_q_20_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_02_q_20_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_02_q_20_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_02_q_20_s04")

    ## Place quiz 02 question 20 here
    text _p("""
        {b} Choose the coding best practices {/b}
        """) xpos 138 ypos 128 size 50 xsize 1602 color "#333333" 

    ## Place quiz 02 question 20 answer 01 here
    text _p("""
        {b}Indented code{/b}
        """) xpos 138 ypos 411 size 40 xsize 800 color "#333333" 

    ## Place quiz 02 question 20 answer 02 here
    text _p("""
        {b}All code contained in one long line{/b}
        """) xpos 1038 ypos 411 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 20 answer 03 here
    text _p("""
        {b}Code organized into different lines{/b}
        """) xpos 138 ypos 738 size 40 xsize 800  color "#333333" 

    ## Place quiz 02 question 20 answer 04 here
    text _p("""
        {b}a and c are correct answers{/b}
        """) xpos 1038 ypos 738 size 40 xsize 800  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    

    timer 10.0 action Jump("quiz_02_q_20_time_up")    

label quiz_02_q_20_s01:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_20_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_20_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_02_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_02_base_checker

label quiz_02_q_20_s04:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_02_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_02_base_checker

label quiz_02_q_20_time_up:
    #$ persistent_quiz_02_q_20_seen = True
    #$ persistent_quiz_02_q_counter +=1
    jump quiz_02_base_checker_timeout











##  ╔═════════════════════════════════════════════════════════════════════════════╗
##  ║ ███  RESULTS                                                            ███ ║
##  ║ ███  This is the section responsible for showing your results in a      ███ ║
##  ║ ███  verbal way. Can be changed to suite needs.                         ███ ║
##  ╚═════════════════════════════════════════════════════════════════════════════╝

label quiz_02_conclusion:
    if persistent_quiz_02_q_counter_correct_answer == 0:
        scene pie_02
        hide blank_question_windows with moveoutright
        e"Oh no?! Your score is 0 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2


    elif persistent_quiz_02_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        e"Your score is 1 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2


    elif persistent_quiz_02_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        e"Your score is 2 please study more"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit() 
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2


    elif persistent_quiz_02_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        e"Your score is 3 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2
        

    elif persistent_quiz_02_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        e"Your score is 4 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2

    elif persistent_quiz_02_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright      
        e"Your score is 5 better luck next time"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2

    elif persistent_quiz_02_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        e"Your score is 6 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2

    elif persistent_quiz_02_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        e "Your score is 7 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2

    elif persistent_quiz_02_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        e "Whoa! your score is 8 not bad"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2

    elif persistent_quiz_02_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        e "Whoa! your score is 9. Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2

    elif persistent_quiz_02_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        e "Whoa! You got perfect score Congrats"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        $ whole_quiz_02_seen == True
        jump pagtapos_ng_quiz_2

























#label before_pagtapos_ng_quiz_2:
    
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

#label quiz_02_repeat_landing_label_seen:
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

