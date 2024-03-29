

label lesson_eight:
    $ persistent.rude_lesson = "eight"
    scene bg_classroom
    if lesson_seven_finish:
        jump lessonStyleIntro
    else:
        Tech "Please finish lesson 7"
        call screen lesson_ui

    $ persistent.lesson_8_quiz8 = 0
    $ persistent.lesson_8_act8 = 0

    label lessonStyleIntro:

        $ show_quick_menu = False
        play music "audio/sa_tech.mp3" volume 0.5

        scene lesson_style_intro
        Tech "In this lesson, you`ll start learning how to make breath-taking web pages and better present your brand."
        jump lessonEightFillOne


    label lessonEightFillOne:
        $ ans_fet_o1_was_dropped = False
        scene l8f1
        Tech "Let`s start by changing the {b}color{/b} of text with the style attribute."
        call screen lesson_eight_ls1_fill

        label call_et1:
            $ ans_fet_o1_was_dropped = False
            call screen lesson_eight_ls1_fill
        
        label if_let1_wrong:
            scene l8f1
            Tech "Try again"
            call screen lesson_eight_ls1_fill


    label lessonEightFillTwo:
        $ ans_fet_two1_was_dropped = False
        $ ans_fet_two2_was_dropped = False
        scene l8f2
        Tech"The style attribute can be used to define {b}properties{/b} like color, font size and alignment."
        call screen lesson_eight_ls2_fill

        label call_et2:
            $ ans_fet_two1_was_dropped = False
            $ ans_fet_two2_was_dropped = False
            call screen lesson_eight_ls2_fill
        
        label if_let2_wrong:
            scene l8f2
            Tech"Try again"
            call screen lesson_eight_ls2_fill


    label lessonEightFillThree:
        $ ans_fet_thr1_was_dropped = False
        $ ans_fet_thr2_was_dropped = False
        scene l8f3
        Tech"The style attribute can make your life a whole lot easier when it comes to formatting. You can customize multiple properties at the same time."
        Tech"Just separate each property:value pair with a {b}semicolon (;){/b}"
        
        call screen lesson_eight_ls3_fill

        label call_et3:
            $ ans_fet_thr1_was_dropped = False
            $ ans_fet_thr2_was_dropped = False
            call screen lesson_eight_ls3_fill
        
        label if_let3_wrong:
            scene l8f3
            Tech"Try again"
            call screen lesson_eight_ls3_fill


    label lessonEightFillFour:
        scene lesson_8_4 
        Tech "What will this code display?"

        label choices_fef:
        menu:
            "A red paragraph text, right-aligned":
                Tech"You are correct"
                jump lessonEightFillFive
            "A red paragraph text, center-aligned":
                jump if_let4_wrong
            "A red button, right-aligned":
                jump if_let4_wrong
            "A red heading, right-aligned":
                jump if_let4_wrong
 
        label if_let4_wrong:
            e "incorrect"
            jump choices_fef


    label lessonEightFillFive:
        $ ans_fet_fv1_was_dropped = False
        $ ans_fet_fv2_was_dropped = False
        scene l8f5
        Tech "You can control the font size with the {b}font-size{/b} property."

        label l8Int8:
            menu:
                "Talk to classmate":
                    jump start_hitting_teach3
                    label opsl8_1:
                        $ persistent.ast3_rudeness += 25
                        jump skipped_l8
                "Play with your classmate":
                    jump begin_ho_mg8
                    label opsl8_2:
                        $ persistent.ast3_rudeness += 25
                        jump skipped_l8
                "Raise Hand":
                    pass
                "Ignore":
                    jump lessonEightFillSix

        call screen lesson_eight_ls5_fill

        label call_et5:
            $ ans_fet_fv1_was_dropped = False
            $ ans_fet_fv2_was_dropped = False
            call screen lesson_eight_ls5_fill
        
        label if_let5_wrong:
            scene l8f5
            Tech"Try again"
            call screen lesson_eight_ls5_fill


    label lessonEightFillSix:
        scene lesson_8_6 
        Tech "What will this code display?"

        label choices_fesx:
        menu:
            "A small button":
                jump if_let6_wrong
            "A heading aligned to the left with small font":
                Tech "You are correct"
                jump lessonEightFillSeven
            "A paragraph aligned to the left":
                jump if_let6_wrong
 
        label if_let6_wrong:
            Tech "incorrect"
            jump choices_fesx


    label lessonEightFillSeven:
        scene lesson_8_7
        Tech "What's wrong with this code?"

        label choices_fesv:
        menu:
            "Single quotation marks should be used":
                jump if_let7_wrong
            "The quotation marks don`t match":
                jump if_let7_wrong
            "The style attribute is missing":
                Tech "You are correct"
                jump lessonEightFillEight
            "The paragraph element requires an empty tag":
                jump if_let7_wrong
 
        label if_let7_wrong:
            Tech "incorrect"
            jump choices_fesv


    label lessonEightFillEight:
        $ ans_fet_et1_was_dropped = False
        $ ans_fet_et2_was_dropped = False
        scene l8f8
        e "The {b}background-color{/b} property is useful for styling elements like buttons."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonEightFillNine

        call screen lesson_eight_ls8_fill

        label call_et8:
            $ ans_fet_et1_was_dropped = False
            $ ans_fet_et2_was_dropped = False
            call screen lesson_eight_ls8_fill
        
        label if_let8_wrong:
            scene l8f8
            Tech "Try again"
            call screen lesson_eight_ls8_fill


    label lessonEightFillNine:
        scene lesson_8_9
        Tech "What's wrong with this code?"

        label choices_fenn:
        menu:
            "The button element requires an empty tag":
                jump if_let9_wrong
            "You can`t change the color of a button":
                jump if_let9_wrong
            "Incorrect use of quotation marks":
                jump if_let9_wrong
            "The different properties need to be separated with a semicolon (;)":
                e "You are correct"
                jump lessonEightFillTen
 
        label if_let9_wrong:
            Tech"incorrect"
            jump choices_fenn



    label lessonEightFillTen:
        scene lesson_8_22
        show teacher_crossarm_smile
        Tech"Try to complete the missing code"
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        Tech"The open and close parenthesis indicates the missing tag so click it to input a code"
        hide teacher_closed_happy
        show teacher_crossarm_smile
        Tech"Also if you got an error, you can click the return text button to return to your code"
        hide teacher_crossarm_smile
        call screen lesson_eight_ls10_fill

        label if_le10_correct:
            scene lesson_8_22
            show teacher_closed_happy
            Tech "Hey, you are getting good at this"
            hide teacher_closed_happy
            jump lessonEightFillEleven


    label lessonEightFillEleven:
        scene lesson_8_22
        show teacher_crossarm_smile
        Tech "Let's practice again"
        hide teacher_crossarm_smile
        call screen lesson_eight_ls11_fill

        label if_le11_correct:
            scene lesson_8_22
            show teacher_crossarm_happy
            Tech"Great job"
            hide teacher_crossarm_happy
            jump lessonEightFillTwelve


    label lessonEightFillTwelve:
        $ ans_fet_twv1_was_dropped = False
        $ ans_fet_twv2_was_dropped = False
        scene l8f12
        Tech"Some style properties require multiple values. The border property is an example of that"

        # Classmate Confused Interaction
        blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."
        # Dialogue to nung kaklaseng nyang boy
        "Hey, mind lending a hand? I'm a bit lost with some of the words the teacher just used. Could you help me catch up on what I missed? I'd appreciate it, and maybe we can quickly go through it together so we don't fall too behind."

        menu:
            "Talk to him":
                blank "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
                $ persistent.ast3_kindness = 25
                jump lessonEightFillFifteen
            "Refuse and explain that you can teach him later; choose to focus on the current lesson":
                blank "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
                $ persistent.ast3_kindness = 25
                pass
        
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonEightFillThirteen
        
        

        call screen lesson_eight_ls12_fill

        label call_et12:
            $ ans_fet_twv1_was_dropped = False
            $ ans_fet_twv2_was_dropped = False
            call screen lesson_eight_ls12_fill
        
        label if_let12_wrong:
            scene l8f12
            Tech "Try again"
            call screen lesson_eight_ls12_fill


    label lessonEightFillThirteen:
        $ ans_fet_tht1_was_dropped = False
        $ ans_fet_tht2_was_dropped = False
        $ ans_fet_tht3_was_dropped = False
        scene l8f13
        Tech "The {b}border property{/b} is a short and simple way to refer to 3 different sub-properties. That’s why it can take 3 values."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonStyleTakeaways

        call screen lesson_eight_ls13_fill

        label call_et13:
            $ ans_fet_tht1_was_dropped = False
            $ ans_fet_tht2_was_dropped = False
            $ ans_fet_tht3_was_dropped = False
            call screen lesson_eight_ls13_fill
        
        label if_let13_wrong:
            scene l8f13
            Tech "Try again"
            call screen lesson_eight_ls13_fill


    label lessonStyleTakeaways:
        scene lesson_style_takeaways
        Tech "Next, you`ll learn the 2 types of HTML element."


    label lessonInlineBlockIntro:
        scene lesson_inline_block_intro
        Tech "This is one of the most important things for web designers and developers. Let`s take a look!"
        jump lessonEightFillFourteen

    label lessonEightFillFourteen:
        $ ans_fet_ft1_was_dropped = False
        $ ans_fet_ft2_was_dropped = False
        scene l8f14
        Tech "The {b}border{/b} property’s great for helping us see the difference between these 2 types of HTML element."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonEightFillFifteen

        call screen lesson_eight_ls14_fill

        label call_et14:
            $ ans_fet_ft1_was_dropped = False
            $ ans_fet_ft2_was_dropped = False
            call screen lesson_eight_ls14_fill
        
        label if_let14_wrong:
            scene l8f14
            Tech "Try again"
            call screen lesson_eight_ls14_fill


    label lessonEightFillFifteen:
        scene l8f15
        Tech"The borders of the different elements will help you spot the differences. "
        Tech "Run the code to see the 2 categories of elements."
        call screen lesson_eight_ls15_fill

        label when_run_et_fifteen:
            scene lesson_8_15_run 
            Tech "Try to unalize it better"
            jump lessonEightFillSixteen


    label lessonEightFillSixteen:
        $ ans_fet_sxt1_was_dropped = False
        $ ans_fet_sxt2_was_dropped = False
        scene l8f16
        Tech"Block-level elements always start on a new line.\nInline elements don't start on a new line."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonEightFillSeventeen

        call screen lesson_eight_ls16_fill

        label call_et16:
            $ ans_fet_sxt1_was_dropped = False
            $ ans_fet_sxt2_was_dropped = False
            call screen lesson_eight_ls16_fill
        
        label if_let16_wrong:
            scene l8f16
            Tech"Try again"
            call screen lesson_eight_ls16_fill


    label lessonEightFillSeventeen:
        $ ans_fet_svt1_was_dropped = False
        $ ans_fet_svt2_was_dropped = False
        scene l8f17
        Tech"Block-level elements take up the full width available.\nInline elements only take up as much width as necessary."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonEightFillEightteen

        call screen lesson_eight_ls17_fill

        label call_et17:
            $ ans_fet_svt1_was_dropped = False
            $ ans_fet_svt2_was_dropped = False
            call screen lesson_eight_ls17_fill
        
        label if_let17_wrong:
            scene l8f17
            Tech"Try again"
            call screen lesson_eight_ls17_fill


    label lessonEightFillEightteen:
        scene lesson_8_18
        Tech"This code will result in 2 buttons on the same line. Why?"

        label choices_feet:
        menu:
            "Buttons are block-level elements":
                jump if_let18_wrong
            "Buttons are inline elements":
                Tech "You are correct"
                jump lessonEightFillNineteen
 
        label if_let18_wrong:
            Tech"incorrect"
            jump choices_feet


    label lessonEightFillNineteen:
        $ ans_fet_nt1_was_dropped = False
        $ ans_fet_nt2_was_dropped = False
        $ ans_fet_nt3_was_dropped = False
        scene l8f19
        Tech"Format tags are inline elements."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonEightFillTwenty

        call screen lesson_eight_ls19_fill

        label call_et19:
            $ ans_fet_nt1_was_dropped = False
            $ ans_fet_nt2_was_dropped = False
            $ ans_fet_nt3_was_dropped = False
            call screen lesson_eight_ls19_fill
        
        label if_let19_wrong:
            scene l8f19
            Tech"Try again"
            call screen lesson_eight_ls19_fill


    label lessonEightFillTwenty:
        scene lesson_8_20
        Tech"How many lines will the browser display with this code?"

        label choices_fetwt:
        menu:
            "3":
                jump if_let20_wrong
            "2":
                jump if_let20_wrong
            "1":
                Tech"You are correct"
                jump lessonEightFillTwentyone
 
        label if_let20_wrong:
            Tech"incorrect"
            jump choices_fetwt


    label lessonEightFillTwentyone:
        $ ans_fet_twto1_was_dropped = False
        $ ans_fet_twto2_was_dropped = False
        $ ans_fet_twto3_was_dropped = False
        scene l8f21
        Tech "Format tags are inline elements."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonEightFillTwentytwo

        call screen lesson_eight_ls21_fill

        label call_et21:
            $ ans_fet_twto1_was_dropped = False
            $ ans_fet_twto2_was_dropped = False
            $ ans_fet_twto3_was_dropped = False
            call screen lesson_eight_ls21_fill
        
        label if_let21_wrong:
            scene l8f21
            Tech "Try again"
            call screen lesson_eight_ls21_fill


    label lessonEightFillTwentytwo:
        scene lesson_8_22
        show teacher_crossarm_smile
        e "Select the correct statement:"

        label choices_fetwtt:
        menu:
            "Block-level elements can contain inline elements":
                show teacher_crossarm_happy
                e "You are correct"
                jump lessonEightFillTwentythree
            "Inline elements can contain block elements":
                jump if_let22_wrong
 
        label if_let22_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            jump lessonEightFillTwentytwo


    label lessonEightFillTwentythree:
        scene lesson_8_22
        show teacher_crossarm_smile
        e"True or False?\nBlock-level elements can be nested inside inline elements"

        label choices_fetwtth:
        menu:
            "False":
                show teacher_crossarm_happy
                e "You are correct"
                jump lessonEightFillTwentyfour
            "True":
                jump if_let23_wrong
 
        label if_let23_wrong:
            show teacher_crossarm_sad
            e "incorrect"
            jump choices_fetwtth


    label lessonEightFillTwentyfour:
        scene l8f23
        Tech "Line break <br> tags are used to force inline elements to start on a new line."
        Tech "Run the code to see the difference"
        call screen lesson_eight_ls24_fill

        label when_run_et_twtfr:
            scene lesson_8_23_run 
            Tech"Great! now the other buttons start on new line"
            jump lessonEightFillTwentyfive


    label lessonEightFillTwentyfive:
        scene lesson_8_22
        show teacher_crossarm_smile
        Tech"True or False?\nYou need line break <br> tags to make block-level elements start on a new line."

        label choices_fetfv:
        menu:
            "False":

                jump if_let25_wrong
            "True":
                show teacher_crossarm_happy
                e "You are correct"
                jump lessonEightFillTwentysix
 
        label if_let25_wrong:
            show teacher_crossarm_sad
            e "incorrect"
            jump choices_fetfv


    label lessonEightFillTwentysix:
        scene lesson_8_22
        show teacher_crossarm_smile
        Tech "Line break <br> tags are usually included in forms. Why?"

        label choices_fetsx:
        menu:
            "Form elements like <input> and <label> are block-level elements":
                jump if_let26_wrong
            "Form elements like <input> and <label> are inline elements":
                show teacher_crossarm_happy
                Tech " You are correct"
                jump lessonEightFillTwentyseven
 
        label if_let26_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            jump choices_fetsx


    label lessonEightFillTwentyseven:
        scene lesson_8_26
        Tech"What will this code display?"

        label choices_fetsv:
        menu:
            "A 1-line heading":
                jump if_let27_wrong
            "A 1-line paragraph":
                Tech "You are correct"
                jump lessonEightFillTwentyeight
            "A 3-line heading":
                jump if_let27_wrong
            "A 3-line paragraph":
                jump if_let27_wrong
        
        label if_let27_wrong:
            Tech"incorrect"
            jump choices_fetsv


    label lessonEightFillTwentyeight:
        scene lesson_8_27
        Tech"What will this code display?"

        label choices_fetet:
        menu:
            "A 3-line paragraph":
                Tech "You are correct"
                jump lessonInlineBlockTakeaways
            "A 3-line heading":
                jump if_let28_wrong
            "A 1-line heading":
                jump if_let28_wrong
            "A 1-line paragraph":
                jump if_let28_wrong
        
        label if_let28_wrong:
            Tech"incorrect"
            jump choices_fetet


    label lessonInlineBlockTakeaways:
        scene lesson_inline_block_takeaways
        Tech "Next lesson you’ll learn to group elements to make your pages faster to load and easier to customize."

    stop music fadeout 1.0
    
    play music "audio/quiz.mp3" volume 0.5

    $ persistent.ast3_participation += 25
    label skipped_l8:

    jump start_quiz_07

    label pagtapos_ng_quiz_7:

    $ persistent.lesson_8_quiz8 = persistent_quiz_07_q_counter_correct_answer
    
    
    Tech "Great job on the quiz, class! You all did fantastic."

    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting project related to what you've just learned."
    jump l8_act8
    label pagtapos_ng_act_8:



    stop music fadeout 1.0

    play music "audio/sa_tech.mp3" volume 0.5

    scene bg_classroom

    show teacher_crossarm_smile
    e"Well done young coders. Let's end our class here."
    hide tea
    show teacher_closed_happy
    e"Good bye class"
    hide teacher_closed_happy

    stop music fadeout 1.0

    
    scene bg_8
    blank "End of chapter 8"



    $ lesson_eight_finish = True  
    call screen lesson_ui





    return