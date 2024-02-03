















label lesson_nine:
    $ persistent.rude_lesson = "nine"
    scene bg_classroom
    if lesson_eight_finish:
        jump lessonDivideIntro
    else:
        e "Please finish lesson 8"
        call screen lesson_ui

    $ persistent.lesson_9_quiz9 = 0
    $ persistent.lesson_9_act9 = 0

    label lessonDivideIntro:

        $ show_quick_menu = False
        play music "audio/sa_tech.mp3" volume 0.5 

        scene lesson_divide_intro
        Tech "In this lesson, you`ll learn to group related elements."
        jump lessonNineFillOne


    label lessonNineFillOne:
        $ ans_fnn_o1_was_dropped = False
        scene l9f1
        e "The {b}<div>{/b} element is a container for HTML elements that keeps your pages organized"
        call screen lesson_nine_ls1_fill

        label call_nn1:
            $ ans_fnn_o1_was_dropped = False
            call screen lesson_nine_ls1_fill
        
        label if_lnn1_wrong:
            scene l9f1
            e "Try again"
            call screen lesson_nine_ls1_fill


    label lessonNineFillTwo:
        scene lesson_8_22 
        show teacher_crossarm_smile
        e "The {b}<div>{/b} element always takes up the full width available. This means the <div> element is …"

        label choices_n2:
        menu:
            "an inline element":
                jump if_ln2_wrong
            "a block-level element":
                show teacher_crossarm_happy
                e "You are correct"
                jump lessonNineFillThree
 
        label if_ln2_wrong:
            show teacher_crossarm_sad
            e"incorrect"
            jump lessonNineFillTwo


    label lessonNineFillThree:
        scene lesson_8_22 
        show teacher_crossarm_happy
        e "{b}<div>{/b} is a block-level element. This means it…"

        label choices_n3:
        menu:
            "doesn`t start on a new line":
                show teacher_crossarm_sad
                jump if_ln3_wrong
            "starts on a new line":
                e "You are correct"
                jump lessonNineFillFour
 
        label if_ln3_wrong:
            show teacher_crossarm_happy
            e"incorrect"
            jump lessonNineFillThree


    label lessonNineFillFour:
        scene l9f4
        e"Elements grouped in a {b}<div>{/b} can be styled quicker, all at once."
        e"Run the code to see the div tag styled"
        call screen lesson_nine_ls4_fill

        label when_run_nn_four:
            scene lesson_9_4_run 
            e"As you can see the style was applied to all element tag inside a {b}div tag{/b}"
            jump lessonNineFillFive


    label lessonNineFillFive:
        scene l9f5
        e"Let's practice again"

        label l9Int9:
            menu:
                "Talk to classmate":
                    jump start_hitting_teach3
                    label opsl9_1:
                        $ persistent.ast3_rudeness += 25
                        jump skipped_l9
                "Play with your classmate":
                    jump begin_ho_mg9
                    label opsl9_2:
                        $ persistent.ast3_rudeness += 25
                        jump skipped_l9
                "Raise Hand":
                    pass
                "Ignore":
                    jump lessonNineFillSix

        call screen lesson_nine_ls5_fill

        label if_ln5_correct:
            scene lesson_8_22
            show teacher_closed_happy
            e"Great job"
            hide teacher_closed_happy
            jump lessonNineFillSix


    label lessonNineFillSix:
        scene lesson_9_6
        e"because it’s a what...?"

        label choices_n6:
        menu:
            "non-semantic tag":
                e"You are correct"
                jump lessonNineFillSeven
            "semantic tag":
                jump if_ln6_wrong
 
        label if_ln6_wrong:
            e"incorrect"
            jump lessonNineFillSix


    label lessonNineFillSeven:
        scene l9f7
        e"<div> doesn't add any visual effect unless you add a style to it. It’s often used by web developers to group and style HTML elements."
        e"Run the code to see the div tag styled"
        call screen lesson_nine_ls7_fill

        label when_run_nn_seven:
            scene lesson_9_7_run 
            e"As you can see the style was applied to all element tag inside a {b}div tag{/b}"
            jump lessonNineFillEight


    label lessonNineFillEight:
        scene lesson_8_22  
        show teacher_crossarm_smile  
        e"You can use <div> to apply the same style to a group of elements"

        label choices_n8:
        menu:
            "False":
                jump if_ln8_wrong
            "True":
                show teacher_crossarm_happy
                e"You are correct"
                jump lessonNineFillTen
 
        label if_ln8_wrong:
            show teacher_crossarm_sad
            e"incorrect"
            jump lessonNineFillEight


    label lessonNineFillTen:
        scene lesson_9_10
        e"In which color will the paragraph element be displayed?"

        label choices_n10:
        menu:
            "red":
                e"You are correct"
                jump lessonNineFillEleven
            "green":
                jump if_ln10_wrong
            "black":
                jump if_ln10_wrong

        label if_ln10_wrong:
            e"incorrect"
            jump lessonNineFillTen


    label lessonNineFillEleven:
        scene l9f11
        e"The style in a <div> container will apply to all its nested elements unless you give them their own."
        e"Run the code to see the div tag styled"
        call screen lesson_nine_ls11_fill

        label when_run_nn_eleven:
            scene lesson_9_11_run 
            e"It will always prioritize the inline style"
            jump lessonNineFillTweleve


    label lessonNineFillTweleve:
        $ ans_fnn_twv1_was_dropped = False
        $ ans_fnn_twv2_was_dropped = False
        scene l9f12
        e"Complete the code to make the text in the paragraph blue"

        # Classmate Confused Interaction
        blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."
        # Dialogue to nung kaklaseng nyang boy
        "Hey, mind lending a hand? I'm a bit lost with some of the words the teacher just used. Could you help me catch up on what I missed? I'd appreciate it, and maybe we can quickly go through it together so we don't fall too behind."

        menu:
            "Talk to him":
                blank "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
                $ persistent.ast3_kindness = 25
                jump lessonNineFillSeventeen
            "Refuse and explain that you can teach him later; choose to focus on the current lesson":
                blank "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
                $ persistent.ast3_kindness = 25
                pass

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonNineFillThirteen

        call screen lesson_nine_ls12_fill

        label call_nn12:
            $ ans_fnn_twv1_was_dropped = False
            $ ans_fnn_twv2_was_dropped = False
            call screen lesson_nine_ls12_fill
        
        label if_lnn12_wrong:
            scene l9f12
            e"Try again"
            call screen lessonNineFillTweleve


    label lessonNineFillThirteen:
        scene lesson_9_13
        e"In which color will the level-3 heading be displayed?"

        label choices_n13:
        menu:
            "black":
                jump if_ln13_wrong
            "green":
                e"You are correct"
                jump lessonNineFillFourteen
            "red":
                jump if_ln13_wrong

        label if_ln13_wrong:
            e"incorrect"
            jump lessonNineFillThirteen


    label lessonNineFillFourteen:
        scene lesson_9_14
        e"In which color will {b}Heading{/b} 2 be displayed?"

        label choices_n14:
        menu:
            "black":
                jump if_ln14_wrong
            "green":
                jump if_ln14_wrong
            "red":
                e"You are correct"
                jump lessonNineFillFifteen

        label if_ln14_wrong:
            e"incorrect"
            jump lessonNineFillFourteen


    label lessonNineFillFifteen:
        scene lesson_9_15
        e"Remember black is the default color for text. In which color will the {b}Heading{/b} 2 element be displayed?"

        label choices_n15:
        menu:
            "black":
                e"You are correct"
                jump lessonNineFillSixteen
            "green":
                jump if_ln15_wrong
            "red":
                jump if_ln15_wrong

        label if_ln15_wrong:
            e"incorrect"
            jump lessonNineFillFifteen


    label lessonNineFillSixteen:
        scene lesson_9_16
        e"Which element will be displayed in blue?"

        label choices_n16:
        menu:
            "Heading 4":
                e"You are correct"
                jump lessonNineFillSeventeen
            "Paragraph":
                jump if_ln16_wrong
            "Heading 5":
                jump if_ln16_wrong

        label if_ln16_wrong:
            e"incorrect"
            jump lessonNineFillSixteen


    label lessonNineFillSeventeen:
        scene lesson_8_22
        show teacher_crossarm_happy
        e"Complete the code to group and align the elements to the center"
        call screen lesson_nine_ls17_fill

        label if_ln17_correct:
            scene lesson_8_22
            show teacher_closed_happy
            e"Great job"
            jump lessonDivideTakeaways


    label lessonDivideTakeaways:
        scene lesson_divide_takeaways
        e "In the next lesson, you’ll learn to create tables."

    e"Now lets have quiz"

    stop music fadeout 1.0
    
    play music "audio/quiz.mp3" volume 0.5

    $ persistent.ast3_participation += 25
    label skipped_l9:

    jump start_quiz_08

    label pagtapos_ng_quiz_8:

    $ persistent.lesson_9_quiz9 = persistent_quiz_08_q_counter_correct_answer
    
    Tech "Great job on the quiz, class! You all did fantastic."

    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting project related to what you've just learned."
    jump l9_act9
    label pagtapos_ng_act_9:

    Tech "I hope you're all doing well. Today, I have an important announcement to make."

    Tech "We've covered a lot of material in lessons 7 to 9, and I've been impressed with your engagement and dedication."

    Tech "As a way to assess your understanding and progress, we'll be having an exam next"

    Tech "Ok! Let's start the examination"

    jump Third_one
    label tapos_exam3:

    stop music fadeout 1.0

    play music "audio/sa_tech.mp3" volume 0.5

    scene bg_classroom

    show teacher_crossarm_smile
    e "I want to acknowledge your hard work and dedication in preparing for this exam. It's a crucial part of our learning journey."
    e"Well done young coders. Let's end our class here."
    hide tea
    show teacher_closed_happy
    e"Good bye class"
    e"You can now veiw your lesson 7 to 9 assessment"
    hide teacher_closed_happy

    stop music fadeout 1.0

    
    scene bg_9
    blank "End of chapter 9"




    $ lesson_nine_finish = True
    jump assessment_three
    call screen lesson_ui






    return