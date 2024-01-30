
##  ╔═════════════════════════════════════════════════════════════════════════════╗
##  ║ ███  INIT SECTION                                                       ███ ║
##  ║ ███  This is the section responsible for initializing things            ███ ║
##  ║ ███  that need to be tracked as well as specific quiz resources.        ███ ║
##  ╚═════════════════════════════════════════════════════════════════════════════╝

init:
    $ persistent_quiz_000_q_01_seen = False
    $ persistent_quiz_000_q_02_seen = False
    $ persistent_quiz_000_q_03_seen = False
    $ persistent_quiz_000_q_04_seen = False
    $ persistent_quiz_000_q_05_seen = False
    $ persistent_quiz_000_q_06_seen = False
    $ persistent_quiz_000_q_07_seen = False
    $ persistent_quiz_000_q_08_seen = False
    $ persistent_quiz_000_q_09_seen = False
    $ persistent_quiz_000_q_10_seen = False
    $ persistent_quiz_000_q_11_seen = False
    $ persistent_quiz_000_q_12_seen = False
    $ persistent_quiz_000_q_13_seen = False
    $ persistent_quiz_000_q_14_seen = False
    $ persistent_quiz_000_q_15_seen = False
    $ persistent_quiz_000_q_16_seen = False
    $ persistent_quiz_000_q_17_seen = False
    $ persistent_quiz_000_q_18_seen = False
    $ persistent_quiz_000_q_19_seen = False
    $ persistent_quiz_000_q_20_seen = False
    $ persistent_quiz_000_q_21_seen = False
    $ persistent_quiz_000_q_22_seen = False
    $ persistent_quiz_000_q_23_seen = False
    $ persistent_quiz_000_q_24_seen = False
    $ persistent_quiz_000_q_25_seen = False
    $ persistent_quiz_000_q_26_seen = False
    $ persistent_quiz_000_q_27_seen = False
    $ persistent_quiz_000_q_28_seen = False
    $ persistent_quiz_000_q_29_seen = False
    $ persistent_quiz_000_q_30_seen = False
    $ persistent_quiz_000_q_31_seen = False
    $ persistent_quiz_000_q_32_seen = False
    $ persistent_quiz_000_q_33_seen = False
    $ persistent_quiz_000_q_34_seen = False
    $ persistent_quiz_000_q_35_seen = False
    $ persistent_quiz_000_q_36_seen = False
    $ persistent_quiz_000_q_37_seen = False
    $ persistent_quiz_000_q_38_seen = False
    $ persistent_quiz_000_q_39_seen = False
    $ persistent_quiz_000_q_40_seen = False
    $ persistent_quiz_000_q_41_seen = False
    $ persistent_quiz_000_q_42_seen = False
    $ persistent_quiz_000_q_43_seen = False
    $ persistent_quiz_000_q_44_seen = False
    $ persistent_quiz_000_q_45_seen = False
    $ persistent_quiz_000_q_46_seen = False
    $ persistent_quiz_000_q_47_seen = False
    $ persistent_quiz_000_q_48_seen = False
    $ persistent_quiz_000_q_49_seen = False
    $ persistent_quiz_000_q_50_seen = False

    image quiz_window_blank = "assets_quiz/quiz_window_blank.jpg"
    image quiz_next_question = "assets_quiz/next_question.png"
    image quiz_start = "assets_quiz/quiz_start.png"
    image blank_question_windows = "assets_quiz/blank_question_windows.png"
    image times_up = "assets_quiz/times_up.png"

    # This keeps track of the questions encountered in quiz 0
    $ persistent_quiz_000_q_counter = 0

    # This keeps track of the correct answers in quiz 0
    $ persistent_quiz_000_q_counter_correct_answer = 0

    










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  INITIALIATION / LOOP CHECKER                                       ███ ║ 
##  ║ ███  This is the section responsible for going inside the               ███ ║ 
##  ║ ███  quiz, dictating the loop as well aswhen the quiz qill end.         ███ ║  
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

# You place any dialogue or declare image here before quiz starts
label start_quiz_000:
    $ renpy.block_rollback()
    $ whole_quiz_000_seen = True
    #"Insert Dialogue Here"
    scene quiz_window_blank 
    show quiz_start with moveinleft
    $ renpy.pause()
    hide quiz_start with moveoutright
    show blank_question_windows with moveinleft
    jump quiz_000_randomizer

# This label will check if you already answered 10 questions. 
# If you have answered 10, you will conclude this set of quiz.
# Else, you will loop back to the randomized
label quiz_000_base_checker:
    if persistent_quiz_000_q_counter == 10:
        jump quiz_000_conclusion
    else:      
        scene quiz_window_blank 
        show blank_question_windows
        hide blank_question_windows with moveoutright
        show quiz_next_question with moveinleft
        $ renpy.pause()
        hide quiz_next_question with moveoutright
        show blank_question_windows with moveinleft
        jump quiz_000_randomizer

label quiz_000_base_checker_timeout:
    if persistent_quiz_000_q_counter == 10:
        jump quiz_000_conclusion
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
        jump quiz_000_randomizer










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION RANDOMIZER                                                ███ ║ 
##  ║ ███  This is the section where the questions are selected in random.    ███ ║ 
##  ║ ███                                                                     ███ ║  
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_randomizer:
    $ choice = renpy.random.choice(['q01', 'q02', 'q03', 'q04', 'q05', 'q06', 'q07', 'q08', 'q09', 'q10', 'q11', 'q12', 'q13', 'q14', 'q18', 'q18', 'q18', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40' , 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50'])

    if choice == 'q01': # quiz_01_q_01_checker
        if persistent_quiz_000_q_01_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_01_seen == False: 
            $ persistent_quiz_000_q_01_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_01

    if choice == 'q02': # quiz_01_q_02_checker
        if persistent_quiz_000_q_02_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_02_seen == False: 
            $ persistent_quiz_000_q_02_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_02

    if choice == 'q03': # quiz_01_q_03_checker
        if persistent_quiz_000_q_03_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_03_seen == False: 
            $ persistent_quiz_000_q_03_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_03

    if choice == 'q04': # quiz_01_q_04_checker
        if persistent_quiz_000_q_04_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_04_seen == False: 
            $ persistent_quiz_000_q_04_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_04

    if choice == 'q05': # quiz_01_q_05_checker
        if persistent_quiz_000_q_05_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_05_seen == False: 
            $ persistent_quiz_000_q_05_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_05

    if choice == 'q06': # quiz_01_q_06_checker
        if persistent_quiz_000_q_06_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_06_seen == False: 
            $ persistent_quiz_000_q_06_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_06

    if choice == 'q07': # quiz_01_q_07_checker
        if persistent_quiz_000_q_07_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_07_seen == False: 
            $ persistent_quiz_000_q_07_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_07

    if choice == 'q08': # quiz_01_q_08_checker
        if persistent_quiz_000_q_08_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_08_seen == False: 
            $ persistent_quiz_000_q_08_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_08

    if choice == 'q09': # quiz_01_q_09_checker
        if persistent_quiz_000_q_09_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_09_seen == False: 
            $ persistent_quiz_000_q_09_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_09

    if choice == 'q10': # quiz_01_q_10_checker
        if persistent_quiz_000_q_10_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_10_seen == False: 
            $ persistent_quiz_000_q_10_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_10

    if choice == 'q11': # quiz_01_q_11_checker
        if persistent_quiz_000_q_11_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_11_seen == False: 
            $ persistent_quiz_000_q_11_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_11

    if choice == 'q12': # quiz_01_q_12_checker
        if persistent_quiz_000_q_12_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_12_seen == False: 
            $ persistent_quiz_000_q_12_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_12

    if choice == 'q13': # quiz_01_q_13_checker
        if persistent_quiz_000_q_13_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_13_seen == False: 
            $ persistent_quiz_000_q_13_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_13

    if choice == 'q14': # quiz_01_q_14_checker
        if persistent_quiz_000_q_14_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_14_seen == False: 
            $ persistent_quiz_000_q_14_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_14

    if choice == 'q15': # quiz_01_q_15_checker
        if persistent_quiz_000_q_15_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_15_seen == False: 
            $ persistent_quiz_000_q_15_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_15

    if choice == 'q16': # quiz_01_q_16_checker
        if persistent_quiz_000_q_16_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_16_seen == False: 
            $ persistent_quiz_000_q_16_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_16

    if choice == 'q17': # quiz_01_q_17_checker
        if persistent_quiz_000_q_17_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_17_seen == False: 
            $ persistent_quiz_000_q_17_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_17

    if choice == 'q18': # quiz_01_q_18_checker
        if persistent_quiz_000_q_18_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_18_seen == False: 
            $ persistent_quiz_000_q_18_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_18

    if choice == 'q19': # quiz_01_q_19_checker
        if persistent_quiz_000_q_19_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_19_seen == False: 
            $ persistent_quiz_000_q_19_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_19

    if choice == 'q20': # quiz_01_q_20_checker
        if persistent_quiz_000_q_20_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_20_seen == False: 
            $ persistent_quiz_000_q_20_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_20

    if choice == 'q21': # quiz_01_q_21_checker
        if persistent_quiz_000_q_21_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_21_seen == False: 
            $ persistent_quiz_000_q_21_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_21

    if choice == 'q22': # quiz_01_q_22_checker
        if persistent_quiz_000_q_22_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_22_seen == False: 
            $ persistent_quiz_000_q_22_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_22

    if choice == 'q23': # quiz_01_q_23_checker
        if persistent_quiz_000_q_23_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_23_seen == False: 
            $ persistent_quiz_000_q_23_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_23

    if choice == 'q24': # quiz_01_q_24_checker
        if persistent_quiz_000_q_24_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_24_seen == False: 
            $ persistent_quiz_000_q_24_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_24

    if choice == 'q25': # quiz_01_q_25_checker
        if persistent_quiz_000_q_25_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_25_seen == False: 
            $ persistent_quiz_000_q_25_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_25

    if choice == 'q26': # quiz_01_q_26_checker
        if persistent_quiz_000_q_26_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_26_seen == False: 
            $ persistent_quiz_000_q_26_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_26

    if choice == 'q27': # quiz_01_q_27_checker
        if persistent_quiz_000_q_27_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_27_seen == False: 
            $ persistent_quiz_000_q_27_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_27

    if choice == 'q28': # quiz_01_q_28_checker
        if persistent_quiz_000_q_28_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_28_seen == False: 
            $ persistent_quiz_000_q_28_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_28

    if choice == 'q29': # quiz_01_q_29_checker
        if persistent_quiz_000_q_29_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_29_seen == False: 
            $ persistent_quiz_000_q_29_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_29

    if choice == 'q30': # quiz_01_q_30_checker
        if persistent_quiz_000_q_30_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_30_seen == False: 
            $ persistent_quiz_000_q_30_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_30

    if choice == 'q31': # quiz_01_q_31_checker
        if persistent_quiz_000_q_31_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_31_seen == False: 
            $ persistent_quiz_000_q_31_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_31

    if choice == 'q32': # quiz_01_q_32_checker
        if persistent_quiz_000_q_32_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_32_seen == False: 
            $ persistent_quiz_000_q_32_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_32

    if choice == 'q33': # quiz_01_q_33_checker
        if persistent_quiz_000_q_33_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_33_seen == False: 
            $ persistent_quiz_000_q_33_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_33

    if choice == 'q34': # quiz_01_q_34_checker
        if persistent_quiz_000_q_34_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_34_seen == False: 
            $ persistent_quiz_000_q_34_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_34

    if choice == 'q35': # quiz_01_q_35_checker
        if persistent_quiz_000_q_35_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_35_seen == False: 
            $ persistent_quiz_000_q_35_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_35

    if choice == 'q36': # quiz_01_q_36_checker
        if persistent_quiz_000_q_36_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_36_seen == False: 
            $ persistent_quiz_000_q_36_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_36

    if choice == 'q37': # quiz_01_q_37_checker
        if persistent_quiz_000_q_37_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_37_seen == False: 
            $ persistent_quiz_000_q_37_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_37

    if choice == 'q38': # quiz_01_q_38_checker
        if persistent_quiz_000_q_38_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_38_seen == False: 
            $ persistent_quiz_000_q_38_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_38

    if choice == 'q39': # quiz_01_q_39_checker
        if persistent_quiz_000_q_39_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_39_seen == False: 
            $ persistent_quiz_000_q_39_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_39

    if choice == 'q40': # quiz_01_q_40_checker
        if persistent_quiz_000_q_40_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_40_seen == False: 
            $ persistent_quiz_000_q_40_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_40

    if choice == 'q41': # quiz_01_q_41_checker
        if persistent_quiz_000_q_41_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_41_seen == False: 
            $ persistent_quiz_000_q_41_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_41

    if choice == 'q42': # quiz_01_q_42_checker
        if persistent_quiz_000_q_42_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_42_seen == False: 
            $ persistent_quiz_000_q_42_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_42

    if choice == 'q43': # quiz_01_q_43_checker
        if persistent_quiz_000_q_43_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_43_seen == False: 
            $ persistent_quiz_000_q_43_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_43

    if choice == 'q44': # quiz_01_q_44_checker
        if persistent_quiz_000_q_44_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_44_seen == False: 
            $ persistent_quiz_000_q_44_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_44

    if choice == 'q45': # quiz_01_q_45_checker
        if persistent_quiz_000_q_45_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_45_seen == False: 
            $ persistent_quiz_000_q_45_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_45

    if choice == 'q46': # quiz_01_q_46_checker
        if persistent_quiz_000_q_46_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_46_seen == False: 
            $ persistent_quiz_000_q_46_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_46

    if choice == 'q47': # quiz_01_q_47_checker
        if persistent_quiz_000_q_47_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_47_seen == False: 
            $ persistent_quiz_000_q_47_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_47

    if choice == 'q48': # quiz_01_q_48_checker
        if persistent_quiz_000_q_48_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_48_seen == False: 
            $ persistent_quiz_000_q_48_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_48

    if choice == 'q49': # quiz_01_q_49_checker
        if persistent_quiz_000_q_49_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_49_seen == False: 
            $ persistent_quiz_000_q_49_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_49

    if choice == 'q50': # quiz_01_q_50_checker
        if persistent_quiz_000_q_50_seen == True:
            jump quiz_000_randomizer
        elif persistent_quiz_000_q_50_seen == False: 
            $ persistent_quiz_000_q_50_seen = True
            $ persistent_quiz_000_q_counter +=1
            jump quiz_000_question_50










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 01  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_01:
    call screen quiz_000_question_01_imagemap
    $ result = _return

## Imagebutton for question 01
screen quiz_000_question_01_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_01_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_01_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_01_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_01_s04")

    ## Place quiz 000 question 01 here
    text _p("""
        {b}INSERT QUESTION 01{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 01 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 01 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 01 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 01 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_01_time_up")   

label quiz_000_q_01_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_01_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_01_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_01_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_01_time_up:
    #$ persistent_quiz_000_q_01_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout









##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 02  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_02:
    call screen quiz_000_question_02_imagemap
    $ result = _return

## Imagebutton for question 02
screen quiz_000_question_02_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_02_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_02_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_02_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_02_s04")

    ## Place quiz 000 question 02 here
    text _p("""
        {b}INSERT QUESTION 02{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 02 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 02 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 02 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 02 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_02_time_up")    

label quiz_000_q_02_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_02_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_02_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_02_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_01_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_02_time_up:
    #$ persistent_quiz_000_q_02_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 03  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_03:
    call screen quiz_000_question_03_imagemap
    $ result = _return

## Imagebutton for question 03
screen quiz_000_question_03_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_03_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_03_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_03_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_03_s04")

    ## Place quiz 000 question 03 here
    text _p("""
        {b}INSERT QUESTION 03{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 03 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 03 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 03 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 03 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_03_time_up")    

label quiz_000_q_03_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_03_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_03_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_03_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_03_time_up:
    #$ persistent_quiz_000_q_03_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 04  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_04:
    call screen quiz_000_question_04_imagemap
    $ result = _return

## Imagebutton for question 04
screen quiz_000_question_04_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_04_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_04_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_04_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_04_s04")

    ## Place quiz 000 question 04 here
    text _p("""
        {b}INSERT QUESTION 04{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 04 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 04 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 04 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 04 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_04_time_up")    

label quiz_000_q_04_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_04_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_04_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_04_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_04_time_up:
    #$ persistent_quiz_000_q_04_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout












##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 05  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_05:
    call screen quiz_000_question_05_imagemap
    $ result = _return

## Imagebutton for question 05
screen quiz_000_question_05_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_05_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_05_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_05_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_05_s04")

    ## Place quiz 000 question 05 here
    text _p("""
        {b}INSERT QUESTION 05{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 05 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 05 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 05 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 05 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_05_time_up")    


label quiz_000_q_05_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_05_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_05_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_05_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_05_time_up:
    #$ persistent_quiz_000_q_05_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 06  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_06:
    call screen quiz_000_question_06_imagemap
    $ result = _return

## Imagebutton for question 06
screen quiz_000_question_06_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_06_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_06_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_06_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_06_s04")

    ## Place quiz 000 question 06 here
    text _p("""
        {b}INSERT QUESTION 06{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 06 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 06 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 06 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 06 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_06_time_up")    

label quiz_000_q_06_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_06_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_06_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_06_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_06_time_up:
    #$ persistent_quiz_000_q_06_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 07  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_07:
    call screen quiz_000_question_07_imagemap
    $ result = _return

## Imagebutton for question 07
screen quiz_000_question_07_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_07_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_07_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_07_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_07_s04")

    ## Place quiz 000 question 07 here
    text _p("""
        {b}INSERT QUESTION 07{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 07 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 07 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 07 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 07 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_07_time_up")    

label quiz_000_q_07_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_07_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_07_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_07_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_07_time_up:
    #$ persistent_quiz_000_q_07_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 08  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_08:
    call screen quiz_000_question_08_imagemap
    $ result = _return

## Imagebutton for question 08
screen quiz_000_question_08_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_08_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_08_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_08_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_08_s04")

    ## Place quiz 000 question 08 here
    text _p("""
        {b}INSERT QUESTION 08{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 08 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 08 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 08 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 08 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_08_time_up")    

label quiz_000_q_08_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_08_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_08_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_08_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_08_time_up:
    #$ persistent_quiz_000_q_08_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 09  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_09:
    call screen quiz_000_question_09_imagemap
    $ result = _return

## Imagebutton for question 09
screen quiz_000_question_09_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_09_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_09_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_09_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_09_s04")

    ## Place quiz 000 question 09 here
    text _p("""
        {b}INSERT QUESTION 09{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 09 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 09 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 09 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 09 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_09_time_up")    

label quiz_000_q_09_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_09_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_09_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_09_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_09_time_up:
    #$ persistent_quiz_000_q_09_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 10  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_10:
    call screen quiz_000_question_10_imagemap
    $ result = _return

## Imagebutton for question 10
screen quiz_000_question_10_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_10_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_10_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_10_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_10_s04")

    ## Place quiz 000 question 10 here
    text _p("""
        {b}INSERT QUESTION 10{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 10 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 10 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 10 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 10 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_10_time_up")    

label quiz_000_q_10_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_10_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_10_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_10_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_10_time_up:
    #$ persistent_quiz_000_q_10_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 11  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_11:
    call screen quiz_000_question_11_imagemap
    $ result = _return

## Imagebutton for question 11
screen quiz_000_question_11_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_11_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_11_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_11_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_11_s04")

    ## Place quiz 000 question 11 here
    text _p("""
        {b}INSERT QUESTION 11{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 11 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 11 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 11 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 11 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_11_time_up")    

label quiz_000_q_11_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_11_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_11_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_11_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_11_time_up:
    #$ persistent_quiz_000_q_11_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 12  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_12:
    call screen quiz_000_question_12_imagemap
    $ result = _return

## Imagebutton for question 12
screen quiz_000_question_12_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_12_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_12_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_12_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_12_s04")

    ## Place quiz 000 question 12 here
    text _p("""
        {b}INSERT QUESTION 12{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 12 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 12 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 12 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 12 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_12_time_up")    

label quiz_000_q_12_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_12_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_12_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_12_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_12_time_up:
    #$ persistent_quiz_000_q_12_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout












##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 13  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_13:
    call screen quiz_000_question_13_imagemap
    $ result = _return

## Imagebutton for question 13
screen quiz_000_question_13_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_13_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_13_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_13_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_13_s04")

    ## Place quiz 000 question 13 here
    text _p("""
        {b}INSERT QUESTION 13{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 13 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 13 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 13 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 13 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_13_time_up")    

label quiz_000_q_13_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_13_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_13_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_13_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_13_time_up:
    #$ persistent_quiz_000_q_13_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 14  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_14:
    call screen quiz_000_question_14_imagemap
    $ result = _return

## Imagebutton for question 14
screen quiz_000_question_14_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_14_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_14_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_14_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_14_s04")

    ## Place quiz 000 question 14 here
    text _p("""
        {b}INSERT QUESTION 14{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 14 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 14 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 14 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 14 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_14_time_up")    

label quiz_000_q_14_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_14_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_14_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_14_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_14_time_up:
    #$ persistent_quiz_000_q_14_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 15  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_15:
    call screen quiz_000_question_15_imagemap
    $ result = _return

## Imagebutton for question 15
screen quiz_000_question_15_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_15_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_15_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_15_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_15_s04")

    ## Place quiz 000 question 15 here
    text _p("""
        {b}INSERT QUESTION 15{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 15 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 15 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 15 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 15 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_15_time_up")    

label quiz_000_q_15_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_15_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_15_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_15_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_15_time_up:
    #$ persistent_quiz_000_q_15_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 16  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_16:
    call screen quiz_000_question_16_imagemap
    $ result = _return

## Imagebutton for question 16
screen quiz_000_question_16_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_16_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_16_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_16_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_16_s04")

    ## Place quiz 000 question 16 here
    text _p("""
        {b}INSERT QUESTION 16{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 16 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 16 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 16 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 16 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_16_time_up")    

label quiz_000_q_16_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_16_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_16_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_16_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_16_time_up:
    #$ persistent_quiz_000_q_16_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 17  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_17:
    call screen quiz_000_question_17_imagemap
    $ result = _return

## Imagebutton for question 17
screen quiz_000_question_17_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_17_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_17_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_17_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_17_s04")

    ## Place quiz 000 question 17 here
    text _p("""
        {b}INSERT QUESTION 17{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 17 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 17 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 17 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 17 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_17_time_up")    

label quiz_000_q_17_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_17_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_17_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_17_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_17_time_up:
    #$ persistent_quiz_000_q_17_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 18  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_18:
    call screen quiz_000_question_18_imagemap
    $ result = _return

## Imagebutton for question 18
screen quiz_000_question_18_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_18_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_18_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_18_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_18_s04")

    ## Place quiz 000 question 18 here
    text _p("""
        {b}INSERT QUESTION 18{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 18 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 18 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 18 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 18 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_18_time_up")    

label quiz_000_q_18_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_18_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_18_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_18_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_18_time_up:
    #$ persistent_quiz_000_q_18_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout












##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 19  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_19:
    call screen quiz_000_question_19_imagemap
    $ result = _return

## Imagebutton for question 19
screen quiz_000_question_19_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_19_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_19_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_19_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_19_s04")

    ## Place quiz 000 question 19 here
    text _p("""
        {b}INSERT QUESTION 19{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 19 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 19 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 19 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 19 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_19_time_up")    

label quiz_000_q_19_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_19_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_19_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_19_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_19_time_up:
    #$ persistent_quiz_000_q_19_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout










##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 20  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_20:
    call screen quiz_000_question_20_imagemap
    $ result = _return

## Imagebutton for question 20
screen quiz_000_question_20_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 01
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_20_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_20_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_20_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_20_s04")

    ## Place quiz 000 question 20 here
    text _p("""
        {b}INSERT QUESTION 20{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 20 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 20 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 20 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 20 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333" 

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_20_time_up")    

label quiz_000_q_20_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_20_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_20_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_20_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_20_time_up:
    #$ persistent_quiz_000_q_20_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 21  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_21:
    call screen quiz_000_question_21_imagemap
    $ result = _return

## Imagebutton for question 21
screen quiz_000_question_21_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 21
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_21_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_21_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_21_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_21_s04")

    ## Place quiz 000 question 21 here
    text _p("""
        {b}INSERT QUESTION 21{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 21 answer 21 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 21 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 21 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 21 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_21_time_up")    

label quiz_000_q_21_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_21_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_21_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_21_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_21_time_up:
    #$ persistent_quiz_000_q_22_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout





##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 22  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_22:
    call screen quiz_000_question_22_imagemap
    $ result = _return

## Imagebutton for question 22
screen quiz_000_question_22_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 22
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_22_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_22_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_22_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_22_s04")

    ## Place quiz 000 question 22 here
    text _p("""
        {b}INSERT QUESTION 22{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 22 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 22 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 22 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 22 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_22_time_up")    

label quiz_000_q_22_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_22_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_22_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_22_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_22_time_up:
    #$ persistent_quiz_000_q_22_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout







##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 23  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_23:
    call screen quiz_000_question_23_imagemap
    $ result = _return

## Imagebutton for question 23
screen quiz_000_question_23_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 23
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_23_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_23_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_23_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_23_s04")

    ## Place quiz 000 question 23 here
    text _p("""
        {b}INSERT QUESTION 23{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 23 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 23 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 23 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 23 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_23_time_up")    

label quiz_000_q_23_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_23_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_23_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_23_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_23_time_up:
    #$ persistent_quiz_000_q_23_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout





##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 24  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_24:
    call screen quiz_000_question_24_imagemap
    $ result = _return

## Imagebutton for question 24
screen quiz_000_question_24_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 24
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_24_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_24_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_24_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_24_s04")

    ## Place quiz 000 question 24 here
    text _p("""
        {b}INSERT QUESTION 24{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 24 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 24 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 24 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 24 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_24_time_up")    

label quiz_000_q_24_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_24_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_24_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_24_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_24_time_up:
    #$ persistent_quiz_000_q_24_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout





##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 25  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_25:
    call screen quiz_000_question_25_imagemap
    $ result = _return

## Imagebutton for question 25
screen quiz_000_question_25_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 25
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_25_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_25_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_25_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_25_s04")

    ## Place quiz 000 question 25 here
    text _p("""
        {b}INSERT QUESTION 25{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 25 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 25 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 25 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 25 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_25_time_up")    

label quiz_000_q_25_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_25_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_25_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_25_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_25_time_up:
    #$ persistent_quiz_000_q_25_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout




##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 26  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_26:
    call screen quiz_000_question_26_imagemap
    $ result = _return

## Imagebutton for question 26
screen quiz_000_question_26_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 26
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_26_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_26_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_26_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_26_s04")

    ## Place quiz 000 question 26 here
    text _p("""
        {b}INSERT QUESTION 26{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 26 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 26 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 26 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 26 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  




##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_26_time_up")    

label quiz_000_q_26_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_26_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_26_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_26_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_26_time_up:
    #$ persistent_quiz_000_q_26_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout






##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 27  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_27:
    call screen quiz_000_question_27_imagemap
    $ result = _return

## Imagebutton for question 27
screen quiz_000_question_27_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 27
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_27_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_27_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_27_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_27_s04")

    ## Place quiz 000 question 27 here
    text _p("""
        {b}INSERT QUESTION 27{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 27 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 27 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 27 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 27 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  




##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_27_time_up")    

label quiz_000_q_27_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_27_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_27_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_27_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_27_time_up:
    #$ persistent_quiz_000_q_27_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout




##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 28  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_28:
    call screen quiz_000_question_28_imagemap
    $ result = _return

## Imagebutton for question 28
screen quiz_000_question_28_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 28
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_28_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_28_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_28_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_28_s04")

    ## Place quiz 000 question 28 here
    text _p("""
        {b}INSERT QUESTION 28{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 28 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 28 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 28 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 28 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  

        
##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_28_time_up")    

label quiz_000_q_28_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_28_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_28_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_28_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_28_time_up:
    #$ persistent_quiz_000_q_28_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout




##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 29  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_29:
    call screen quiz_000_question_29_imagemap
    $ result = _return

## Imagebutton for question 29
screen quiz_000_question_29_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 29
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_29_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_29_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_29_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_29_s04")

    ## Place quiz 000 question 29 here
    text _p("""
        {b}INSERT QUESTION 29{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 29 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 29 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 29 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 29 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  



##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_29_time_up")    

label quiz_000_q_29_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_29_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_29_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_29_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_29_time_up:
    #$ persistent_quiz_000_q_29_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout







##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 30  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_30:
    call screen quiz_000_question_30_imagemap
    $ result = _return

## Imagebutton for question 30
screen quiz_000_question_30_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 30
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_30_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_30_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_30_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_30_s04")

    ## Place quiz 000 question 30 here
    text _p("""
        {b}INSERT QUESTION 30{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 30 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 30 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 30 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 30 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_30_time_up")    

label quiz_000_q_30_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_30_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_30_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_30_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_30_time_up:
    #$ persistent_quiz_000_q_30_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout





##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 31  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_31:
    call screen quiz_000_question_31_imagemap
    $ result = _return

## Imagebutton for question 31
screen quiz_000_question_31_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 31
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_31_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_31_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_31_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_31_s04")

    ## Place quiz 000 question 31 here
    text _p("""
        {b}INSERT QUESTION 31{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 31 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 31 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 31 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 31 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER       █████████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_31_time_up")    

label quiz_000_q_31_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_31_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_31_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_31_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_31_time_up:
    #$ persistent_quiz_000_q_31_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout




##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 32  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_32:
    call screen quiz_000_question_32_imagemap
    $ result = _return

## Imagebutton for question 32
screen quiz_000_question_32_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 32
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_32_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_32_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_32_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_32_s04")

    ## Place quiz 000 question 32 here
    text _p("""
        {b}INSERT QUESTION 32{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 32 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 32 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 32 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 32 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  
##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_32_time_up")    

label quiz_000_q_32_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_32_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_32_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_32_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_32_time_up:
    #$ persistent_quiz_000_q_32_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout




##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 33  ██████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_33:
    call screen quiz_000_question_33_imagemap
    $ result = _return

## Imagebutton for question 33
screen quiz_000_question_33_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 33
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_33_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_33_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_33_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_33_s04")

    ## Place quiz 000 question 33 here
    text _p("""
        {b}INSERT QUESTION 33{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 33 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 33 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 33 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 33 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_33_time_up")    

label quiz_000_q_33_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_33_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_33_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_33_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_33_time_up:
    #$ persistent_quiz_000_q_33_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout




##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 34  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_34:
    call screen quiz_000_question_34_imagemap
    $ result = _return

## Imagebutton for question 34
screen quiz_000_question_34_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 34
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_34_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_34_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_34_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_34_s04")

    ## Place quiz 000 question 34 here
    text _p("""
        {b}INSERT QUESTION 34{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 34 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 34 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 34 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 34 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_34_time_up")    

label quiz_000_q_34_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_34_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_34_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_34_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_34_time_up:
    #$ persistent_quiz_000_q_34_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 35  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_35:
    call screen quiz_000_question_35_imagemap
    $ result = _return

## Imagebutton for question 35
screen quiz_000_question_35_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 35
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_35_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_35_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_35_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_35_s04")

    ## Place quiz 000 question 35 here
    text _p("""
        {b}INSERT QUESTION 35{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 35 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 35 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 35 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 35 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_35_time_up")    

label quiz_000_q_35_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_35_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_35_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_35_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_35_time_up:
    #$ persistent_quiz_000_q_35_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 36  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_36:
    call screen quiz_000_question_36_imagemap
    $ result = _return

## Imagebutton for question 36
screen quiz_000_question_36_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 36
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_36_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_36_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_36_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_36_s04")

    ## Place quiz 000 question 36 here
    text _p("""
        {b}INSERT QUESTION 36{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 36 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 36 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 36 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 36 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_36_time_up")    

label quiz_000_q_36_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_36_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_36_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_36_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_36_time_up:
    #$ persistent_quiz_000_q_36_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout



##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 37  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_37:
    call screen quiz_000_question_37_imagemap
    $ result = _return

## Imagebutton for question 37
screen quiz_000_question_37_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 37
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_37_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_37_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_37_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_37_s04")

    ## Place quiz 000 question 37 here
    text _p("""
        {b}INSERT QUESTION 37{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 37 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 37 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 37 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 37 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_37_time_up")    

label quiz_000_q_37_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_37_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_37_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_37_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_37_time_up:
    #$ persistent_quiz_000_q_37_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 38  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_38:
    call screen quiz_000_question_38_imagemap
    $ result = _return

## Imagebutton for question 38
screen quiz_000_question_38_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 38
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_38_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_38_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_38_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_38_s04")

    ## Place quiz 000 question 38 here
    text _p("""
        {b}INSERT QUESTION 38{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 38 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 38 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 38 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 38 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_38_time_up")    

label quiz_000_q_38_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_38_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_38_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_38_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_38_time_up:
    #$ persistent_quiz_000_q_38_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 39  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_39:
    call screen quiz_000_question_39_imagemap
    $ result = _return

## Imagebutton for question 39
screen quiz_000_question_39_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 39
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_39_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_39_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_39_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_39_s04")

    ## Place quiz 000 question 39 here
    text _p("""
        {b}INSERT QUESTION 39{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 39 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 39 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 39 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 39 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_39_time_up")    

label quiz_000_q_39_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_39_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_39_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_39_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_39_time_up:
    #$ persistent_quiz_000_q_39_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 40  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_40:
    call screen quiz_000_question_40_imagemap
    $ result = _return

## Imagebutton for question 40
screen quiz_000_question_40_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 40
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_40_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_40_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_40_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_40_s04")

    ## Place quiz 000 question 40 here
    text _p("""
        {b}INSERT QUESTION 40{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 40 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 40 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 40 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 40 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_40_time_up")    

label quiz_000_q_40_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_40_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_40_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_40_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_40_time_up:
    #$ persistent_quiz_000_q_40_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 41  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_41:
    call screen quiz_000_question_41_imagemap
    $ result = _return

## Imagebutton for question 41
screen quiz_000_question_41_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 41
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_41_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_41_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_41_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_41_s04")

    ## Place quiz 000 question 41 here
    text _p("""
        {b}INSERT QUESTION 41{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 41 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 41 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 41 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 41 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_41_time_up")    

label quiz_000_q_41_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_41_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_41_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_41_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_41_time_up:
    #$ persistent_quiz_000_q_41_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 42  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_42:
    call screen quiz_000_question_42_imagemap
    $ result = _return

## Imagebutton for question 42
screen quiz_000_question_42_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 42
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_42_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_42_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_42_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_42_s04")

    ## Place quiz 000 question 42 here
    text _p("""
        {b}INSERT QUESTION 42{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 42 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 42 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 42 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 42 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_42_time_up")    

label quiz_000_q_42_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_42_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_42_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_42_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_42_time_up:
    #$ persistent_quiz_000_q_42_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 43  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_43:
    call screen quiz_000_question_43_imagemap
    $ result = _return

## Imagebutton for question 43
screen quiz_000_question_43_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 43
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_43_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_43_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_43_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_43_s04")

    ## Place quiz 000 question 43 here
    text _p("""
        {b}INSERT QUESTION 43{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 43 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 43 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 43 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 43 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_43_time_up")    

label quiz_000_q_43_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_43_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_43_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_43_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_43_time_up:
    #$ persistent_quiz_000_q_43_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 44  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_44:
    call screen quiz_000_question_44_imagemap
    $ result = _return

## Imagebutton for question 44
screen quiz_000_question_44_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 44
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_44_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_44_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_44_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_44_s04")

    ## Place quiz 000 question 44 here
    text _p("""
        {b}INSERT QUESTION 44{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 44 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 44 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 44 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 44 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_44_time_up")    

label quiz_000_q_44_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_44_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_44_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_44_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_44_time_up:
    #$ persistent_quiz_000_q_44_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 45  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_45:
    call screen quiz_000_question_45_imagemap
    $ result = _return

## Imagebutton for question 45
screen quiz_000_question_45_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 45
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_45_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_45_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_45_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_45_s04")

    ## Place quiz 000 question 45 here
    text _p("""
        {b}INSERT QUESTION 45{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 45 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 45 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 45 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 45 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_45_time_up")    

label quiz_000_q_45_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_45_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_45_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_45_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_45_time_up:
    #$ persistent_quiz_000_q_45_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 46  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_46:
    call screen quiz_000_question_46_imagemap
    $ result = _return

## Imagebutton for question 46
screen quiz_000_question_46_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 46
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_46_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_46_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_46_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_46_s04")

    ## Place quiz 000 question 46 here
    text _p("""
        {b}INSERT QUESTION 46{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 46 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 46 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 46 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 46 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_46_time_up")    

label quiz_000_q_46_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_46_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_46_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_46_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_46_time_up:
    #$ persistent_quiz_000_q_46_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 47  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_47:
    call screen quiz_000_question_47_imagemap
    $ result = _return

## Imagebutton for question 47
screen quiz_000_question_47_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 47
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_47_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_47_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_47_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_47_s04")

    ## Place quiz 000 question 47 here
    text _p("""
        {b}INSERT QUESTION 47{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 47 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 47 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 47 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 47 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_47_time_up")    

label quiz_000_q_47_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_47_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_47_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_47_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_47_time_up:
    #$ persistent_quiz_000_q_47_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout



##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 48  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_48:
    call screen quiz_000_question_48_imagemap
    $ result = _return

## Imagebutton for question 48
screen quiz_000_question_48_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 48
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_48_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_48_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_48_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_48_s04")

    ## Place quiz 000 question 48 here
    text _p("""
        {b}INSERT QUESTION 48{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 48 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 48 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 48 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 48 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_48_time_up")    

label quiz_000_q_48_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_48_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_48_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_48_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_48_time_up:
    #$ persistent_quiz_000_q_48_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 49  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_49:
    call screen quiz_000_question_49_imagemap
    $ result = _return

## Imagebutton for question 49
screen quiz_000_question_49_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 49
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_49_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_49_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_49_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_49_s04")

    ## Place quiz 000 question 49 here
    text _p("""
        {b}INSERT QUESTION 49{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 49 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 49 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 49 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 49 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  


##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_49_time_up")    

label quiz_000_q_49_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_49_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_49_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_49_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_49_time_up:
    #$ persistent_quiz_000_q_49_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout

##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  QUESTION 000 - QUESTION 50  ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝ 

label quiz_000_question_50:
    call screen quiz_000_question_50_imagemap
    $ result = _return

## Imagebutton for question 50
screen quiz_000_question_50_imagemap:
    imagemap:
        ground 'quiz_animated_countdown_timer'
        idle 'quiz_animated_countdown_timer'
        hover 'assets_quiz/quiz_window_hover.jpg'

    imagebutton: ## Imagebutton for question 50
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 390
        action Jump("quiz_000_q_50_s01")

    imagebutton: ## Imagebutton for question 02
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 390
        action Jump("quiz_000_q_50_s02")

    imagebutton: ## Imagebutton for question 03
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 98 ypos 717
        action Jump("quiz_000_q_50_s03")

    imagebutton: ## Imagebutton for question 04
        idle 'assets_quiz/quiz_button.png'
        hover 'assets_quiz/quiz_window_hover.png'
        xpos 998 ypos 717
        action Jump("quiz_000_q_50_s04")

    ## Place quiz 000 question 50 here
    text _p("""
        {b}INSERT QUESTION 50{/b}
        """) xpos 138 ypos 128 size 50 xsize 1500 color "#333333" 

    ## Place quiz 000 question 50 answer 01 here
    text _p("""
        {b}ANSWER 01{/b}
        """) xpos 138 ypos 411 size 40 xsize 840 color "#333333" 

    ## Place quiz 000 question 50 answer 02 here
    text _p("""
        {b}ANSWER 02{/b}
        """) xpos 1038 ypos 411 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 50 answer 03 here
    text _p("""
        {b}ANSWER 03{/b}
        """) xpos 138 ypos 738 size 40 xsize 880  color "#333333" 

    ## Place quiz 000 question 50 answer 04 here
    text _p("""
        {b}ANSWER 04{/b}
        """) xpos 1038 ypos 738 size 40 xsize 880  color "#333333"  



##  ╔═════════════════════════════════════════════════════════════════════════════╗ 
##  ║ ███  DEBUG MODE COUNTER         ███████████████████████████████████████████ ║ 
##  ╚═════════════════════════════════════════════════════════════════════════════╝
    text "{b}DEBUG COUNTER MODE{/b}{p}{b}{size=23}{color=#666666}Quiz Count [persistent_quiz_000_q_counter]{/color}{/size}{/b}{p}{b}{size=23}{color=#666666}Correct Answers [persistent_quiz_000_q_counter_correct_answer]{/color}{/size}{/b}" xpos 20 ypos 20 size 20 xsize 270 color "#333333"

    timer 30.0 action Jump("quiz_000_q_50_time_up")    

label quiz_000_q_50_s01:
    # Uncomment below is the correct answer for quiz
    $ persistent_quiz_000_q_counter_correct_answer +=1
    $ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_50_s02:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_50_s03:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1 
    #$ persistent_quiz_total_points_counter_correct_answer +=1 
    jump quiz_000_base_checker

label quiz_000_q_50_s04:
    # Uncomment below is the correct answer for quiz
    #$ persistent_quiz_000_q_counter_correct_answer +=1
    #$ persistent_quiz_total_points_counter_correct_answer +=1
    jump quiz_000_base_checker

label quiz_000_q_50_time_up:
    #$ persistent_quiz_000_q_50_seen = True
    #$ persistent_quiz_000_q_counter +=1
    jump quiz_000_base_checker_timeout







##  ╔═════════════════════════════════════════════════════════════════════════════╗
##  ║ ███  RESULTS                                                            ███ ║
##  ║ ███  This is the section responsible for showing your results in a      ███ ║
##  ║ ███  verbal way. Can be changed to suite needs.                         ███ ║
##  ╚═════════════════════════════════════════════════════════════════════════════╝

label quiz_000_conclusion:
    if persistent_quiz_000_q_counter_correct_answer == 0:
        scene pie_000
        hide blank_question_windows with moveoutright
        "Teka?... Ni isa wala kang nasagutan na tama?"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit()
        jump pagtapos_ng_quiz_000 

    elif persistent_quiz_000_q_counter_correct_answer == 1:
        scene pie_01 
        hide blank_question_windows with moveoutright
        "As in isa lang nasagot mo!?"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit()
        jump pagtapos_ng_quiz_000


    elif persistent_quiz_000_q_counter_correct_answer == 2:
        scene pie_02
        hide blank_question_windows with moveoutright
        "Bakit dalawa lang nakuha mong tamang sagot?"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit() 
        jump pagtapos_ng_quiz_000


    elif persistent_quiz_000_q_counter_correct_answer == 3:
        scene pie_03 
        hide blank_question_windows with moveoutright
        "Bakit tatlo lang nakuha mong tamang sagot?"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit()  
        jump pagtapos_ng_quiz_000
        

    elif persistent_quiz_000_q_counter_correct_answer == 4:
        scene pie_04
        hide blank_question_windows with moveoutright
        "As in apat lang nasagot mo?"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit()  
        jump pagtapos_ng_quiz_000

    elif persistent_quiz_000_q_counter_correct_answer == 5:
        scene pie_05
        hide blank_question_windows with moveoutright
        "Kalahati lang nasagutan mo. Mukhang tagilid ah..."
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit()  
        jump pagtapos_ng_quiz_000

    elif persistent_quiz_000_q_counter_correct_answer == 6:
        scene pie_06 
        hide blank_question_windows with moveoutright
        "Anim lang?... Nakupo, mukhang medyo nakalimot ka ata."
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit()  
        jump pagtapos_ng_quiz_000

    elif persistent_quiz_000_q_counter_correct_answer == 7:
        scene pie_07
        hide blank_question_windows with moveoutright
        "Medyo sinuwerte ka at pito nasagutan mo."
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit()  
        jump pagtapos_ng_quiz_000

    elif persistent_quiz_000_q_counter_correct_answer == 8:
        scene pie_08 
        hide blank_question_windows with moveoutright
        "Walo nasagutan mo? Puwede na."
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit()   
        jump pagtapos_ng_quiz_000

    elif persistent_quiz_000_q_counter_correct_answer == 9:
        scene pie_09
        hide blank_question_windows with moveoutright
        "9"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit()  
        jump pagtapos_ng_quiz_000

    elif persistent_quiz_000_q_counter_correct_answer == 10:
        scene pie_10
        hide blank_question_windows with moveoutright
        "Whoa! Nasagutan mo lahat!? OK!"
        scene quiz_window_blank with dissolve
        $ renpy.pause(1.0)
        #$ renpy.quit() 
        jump pagtapos_ng_quiz_000