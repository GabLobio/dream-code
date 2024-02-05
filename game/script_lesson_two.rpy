

default persistent.chp_two_time = ""
default persistent.chp_prev_two_time = ""
default persistent.formatted_time = ""  # Define as a persistent variable

default persistent.chp_two_prev_date = 0
default persistent.chp_two_date_taken = 0

default persistent.chp_two_prev_score = 0


screen chp_two_assessment():
    image "images/chp_two_asses.png"

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        action Return()

    
    text '{b}[persistent.chp_prev_two_time]{/b}' size 20 color "#87431E" xpos(539) ypos(243)
    text '{b}[persistent.chp_two_prev_date]{/b}' size 20 color "#87431E" xpos(358) ypos(387)
    image Solid("#FF5A00") xsize(persistent.chp_two_prev_score * 80) ysize(45) xpos 435 ypos 301
    text "{b}[persistent.chp_two_prev_score]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 301   
    
    text '{b}[persistent.chp_two_time]{/b}' size 20 color "#171716" xpos(539) ypos(541)
    text '{b}[persistent.chp_two_date_taken]{/b}' size 20 color "#171716" xpos(358) ypos(679)
    image Solid("#FF5A00") xsize(persistent_quiz_01_q_counter_correct_answer * 80) ysize(45) xpos 435 ypos 599
    text "{b}[persistent_quiz_01_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 599
    



label lesson_two:
    $ persistent.rude_lesson = "ten"
    scene bg_classroom
    $ ls2_numhc = 0
    $ ls2_numc = 0
    $ ls2_numic = 0
    $ l2_takes += 1

    $ persistent.lesson_2_quiz2 = 0
    $ persistent.lesson_2_act2 = 0

    # Start ng Time ###############
    $ save_total_run()
    $ reset_timer()
    show screen timeplayedbutton
    # Start ng Time ###############

    $ show_quick_menu = False
    play music "audio/sa_tech.mp3" volume 0.5
    
    if lesson_one_finish:
        jump lessonTwoIntro
    else:
        Tech "Please finish lesson 1"
        call screen lesson_ui


    label lessonTwoIntro:

        stop music fadeout 1.0
        $ show_quick_menu = False
        play music "audio/sa_tech.mp3" volume 0.5
        
        show lesson_two_intro
        play sound "T_audio/les2/2.1.mp3" volume 0.8
        Tech "Ready to begin the lesson two?"
        play sound "T_audio/les2/2.2.mp3" volume 0.8
        Tech "So our topic for today are Headings and Images"

    label lessonTwoFillone:
        $ ans_f0_was_dropped = False
        scene ltf1
        play sound "T_audio/les2/2.3.mp3" volume 0.8
        Tech "{b}Headings{/b} in HTML come in different levels. <h1> defines the most important heading"
        
        play sound "T_audio/anyone_wants.mp3" volume 0.8
        e "Anyone wants to answer this problem?"

        label l2Int2:
            menu:
                "Talk to classmate":
                    jump start_hitting_teach2
                    label opsl2_1:
                        $ persistent.ast1_rudeness += 25
                        jump skipped_l2
                "Play with your classmate":
                    jump begin_ho_mg2
                    label opsl2_2:
                        $ persistent.ast1_rudeness += 25
                        jump skipped_l2
                "Raise Hand":
                    pass
                "Ignore":
                    jump lessonTwoFilltwo

        call screen lesson_two_ls1_fill

        label call_t1:
            $ ans_f0_was_dropped = False
            call screen lesson_two_ls1_fill

        label if_lt1_wrong:
            scene ltf1
            play sound "T_audio/you_got_it_wrong.mp3" volume 0.8
            Tech "You got it wrong"
            $ ls2_numic += 1
            call screen lesson_two_ls1_fill


    label lessonTwoFilltwo:
        $ ls2_numc += 1
        $ ans_ft_was_dropped = False
        scene ltf2
        play sound "T_audio/les2/2.4.mp3" volume 0.8
        Tech "You can use up to 6 levels of headings in HTML. The tags for these heading elements are <h1>, <h2>," 

        play sound "T_audio/anyone_wants.mp3" volume 0.8
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonTwoFillThree

        call screen lesson_two_ls2_fill

        label call_t2:
            $ ans_ft_was_dropped = False
            call screen lesson_two_ls2_fill

        label if_lt2_wrong:
            scene ltf2
            play sound "T_audio/you_got_it_wrong.mp3" volume 0.8
            e "You got it wrong"
            $ ls2_numic += 1
            call screen lesson_two_ls2_fill


    label lessonTwoFillThree:
        $ ls2_numc += 1
        scene ltf4
        play sound "T_audio/les2/2.5.mp3" volume 0.8
        Tech "You can add different headings to your page to organize the content."
        play sound "T_audio/les2/2.6.mp3" volume 0.8
        Tech "In the upcoming section, we'll be entering a {b}Code Playground{/b} to practice writing HTML code."
        play sound "T_audio/les2/2.7.mp3" volume 0.8
        Tech "Click the Run button to see what the web browser will display"
        call screen lesson_two_ls4_fill

        label when_run:
            scene lesson_when_run
            play sound "T_audio/les2/2.8.mp3" volume 0.8
            Tech "<h1> usually styled with the largest font, and <h6> with the smallest."
            play sound "T_audio/les2/2.9.mp3" volume 0.8
            Tech "Let's move on to the next example"
            jump lessonTwoFillFour
    

    label lessonTwoFillFour:
        scene ltf5
        play sound "T_audio/les2/2.10.mp3" volume 0.8
        Tech "You can combine headings with other elements."
        play sound "T_audio/les2/2.11.mp3" volume 0.8
        Tech "Run the code to see what the web browser will display"
        call screen lesson_two_ls5_fill

        label when_run_two:
            show lesson_when_run_4
            play sound "T_audio/les2/2.12.mp3" volume 0.8
            Tech "Let's have another example using the {b}Code playground{/b}"
            jump lessonTwoFillFive

    label lessonTwoFillFive:
        scene ftg_bg
        show teacher_crossarm_smile
        play sound "T_audio/les2/2.13.mp3" volume 0.8
        Tech "Ok, in this example, we will be filling up the gap or completing the tag to make the HTML code work."
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        play sound "T_audio/les2/2.14.mp3" volume 0.8
        Tech"Before that, let me teach you how to use the {b}Code Playground{/b}."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        play sound "T_audio/les2/2.15.mp3" volume 0.8
        Tech "Click on the number or directly on the missing tag if you want to focus the text cursor."
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        play sound "T_audio/les2/2.16.mp3" volume 0.8
        Tech "Remember that after we code or complete the missing tags, we click the Run button."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        play sound "T_audio/les2/2.18.mp3" volume 0.8
        Tech "After that, it will show the working code, or it may display 'Error' when there are code or tag issues."
        play sound "T_audio/les2/2.19.mp3" volume 0.8
        Tech "And if you get an error, you could click the 'Return' button to go back"
        hide teacher_crossarm_smile
        scene ltf6
        call screen lesson_two_ls6_fill
        

        label if_lt5_correct:
            show lesson_4_when_run
            blank "Show result"
            show teacher_crossarm_happy
            play sound "T_audio/do_did_a_great_job.mp3" volume 0.8
            Tech "You did a great job, well done!"
            play sound "T_audio/moving_on.mp3" volume 0.8
            Tech "Moving on..."
            hide teacher_crossarm_happy
            jump lessonTwoFillSeven
    

    label lessonTwoFillSeven:
        $ ls2_numc += 1
        $ ans_fs1_was_dropped = False
        $ ans_fs2_was_dropped = False
        scene ltf7
        play sound "T_audio/les2/2.20.mp3" volume 0.8
        Tech "h1 is the most important heading."
        play sound "T_audio/anyone_wants.mp3" volume 0.8
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonTwoFillEight

        call screen lesson_two_ls7_fill

        label call_t7:
            $ ans_fs1_was_dropped = False
            $ ans_fs2_was_dropped = False
            call screen lesson_two_ls7_fill
        
        label if_lt7_wrong:
            scene ltf7
            play sound "T_audio/Try_again.mp3" volume 0.8
            Tech "Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls7_fill


    label lessonTwoFillEight:
        $ ls2_numc += 1
        $ ans_fe1_was_dropped = False
        $ ans_fe2_was_dropped = False
        $ ans_fe3_was_dropped = False
        scene ltf8
        play sound "T_audio/les2/2.21.mp3" volume 0.8
        Tech "Heading levels need to be used in the correct order (h1, h2, …h6)"

        play sound "T_audio/anyone_wants.mp3" volume 0.8
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonTwoFillNine

        call screen lesson_two_ls8_fill

        label call_t8:
            $ ans_fe1_was_dropped = False
            $ ans_fe2_was_dropped = False
            $ ans_fe3_was_dropped = False
            call screen lesson_two_ls8_fill
        
        label if_lt8_wrong:
            scene ltf8
            Tech "Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls8_fill


    label lessonTwoFillNine:
        $ ls2_numc += 1
        scene lesson_8_22 
        show teacher smile
        play sound "T_audio/les2/2.22.mp3" volume 0.8
        Tech "Many HTML elements require both opening and closing tags to contain elements"
        hide teacher smile
        show teacher_crossarm_smile
        play sound "T_audio/les2/2.23.mp3" volume 0.8
        Tech "These tags are also called?"

        menu:
            'Empty tag':
                "Try again"
                $ ls2_numic += 1
                jump if_lth9_wrong
            'Container tag':
                show teacher smile

                play sound "T_audio/correct.mp3" volume 0.8
                e "correct"
                jump lessonTwoFillTen
            

        
        label if_lth9_wrong:
            show teacher_crossarm_sad
            play sound "T_audio/incorrect.mp3" volume 0.8
            Tech "incorrect"
            hide teacher_crossarm_sad
            jump lessonTwoFillNine 

    
    label lessonTwoFillTen:
        $ ls2_numc += 1
        $ ans_ft01_was_dropped = False
        $ ans_ft02_was_dropped = False
        scene ltf10
        play sound "T_audio/les2/2.24.mp3" volume 0.8
        Tech "Some HTML elements can be defined with only one tag. They are called {b}empty tags{/b}."
        play sound "T_audio/les2/2.25.mp3" volume 0.8
        Tech"The image tag <img> is a good example of an empty tag, it doesn't require a closing tag"

        play sound "T_audio/anyone_wants.mp3" volume 0.8
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonHeadTakeaways
        
        # Classmate Confused Interaction
        blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."
        # Dialogue to nung kaklaseng nyang boy
        show boy2
        blank "Hey, mind lending a hand? I'm a bit lost with some of the words the teacher just used. Could you help me catch up on what I missed? I'd appreciate it, and maybe we can quickly go through it together so we don't fall too behind."
        hide boy2
        menu:
            "Talk to him":
                blank "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
                $ persistent.ast1_kindness = 25
                jump lessonTwoFillTwelve
            "Refuse and explain that you can teach him later; choose to focus on the current lesson":
                blank "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
                $ persistent.ast1_kindness = 25
                pass

        call screen lesson_two_ls10_fill

        label call_t10:
            $ ans_ft01_was_dropped = False
            $ ans_ft02_was_dropped = False
            call screen lesson_two_ls10_fill
        
        label if_lt10_wrong:
            scene ltf10
            Tech "Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls10_fill

    label lessonHeadTakeaways:
        show lesson_head_takeaways
        play sound "T_audio/well done young coders.mp3" volume 0.8
        Tech "Well done! young coders"
        play sound "T_audio/les2/2.26.mp3" volume 0.8
        Tech "Next topic will be about Images"
        jump lessonImgIntro

    label lessonImgIntro:
        show lesson_img_intro
        play sound "T_audio/les2/2.27.mp3" volume 0.8
        Tech "In this lesson, you'll learn to add images to your pages."
        play sound "T_audio/les2/2.28.mp3" volume 0.8
        Tech "Now let's begin"
        jump lessonTwoFillEleven

    label lessonTwoFillEleven:
        $ ls2_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_happy
        play sound "T_audio/les2/2.29.mp3" volume 0.8
        Tech "Images only require one tag to be displayed on your web page."
        hide teacher_crossarm_happy
        show teacher smile
        play sound "T_audio/les2/2.32.mp3" volume 0.8
        Tech "What's the HTML tag for the image element?"
        


        menu:
            '<img>':
                e "you are correct"
                jump lessonTwoFillTwelve
            '<img></img>':
                jump if_lth11_wrong
            

        
        label if_lth11_wrong:
            hide teacher smile 
            show teacher_crossarm_sad
            play sound "T_audio/incorrect.mp3" volume 0.8
            Tech "incorrect"
            $ ls2_numic += 1
            jump lessonTwoFillEleven
        hide teacher smile 
           


    label lessonTwoFillTwelve:
        $ ls2_numc += 1
        $ ans_ftw01_was_dropped = False
        scene ltf12
        play sound "T_audio/les2/2.33.mp3" volume 0.8
        Tech "Images are not technically inserted into a web page, they are linked. The source ({b}src{/b}) of the image
        needs to be included in the tag."

        play sound "T_audio/anyone_wants.mp3" volume 0.8
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonTwoFillThirteen

        call screen lesson_two_ls12_fill

        label call_12:
            $ ans_ftw01_was_dropped = False
            call screen lesson_two_ls12_fill

        
        
        label if_lt12_wrong:
            scene ltf12
            play sound "T_audio/Try_again.mp3" volume 0.8
            Tech "Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls12_fill


    label lessonTwoFillThirteen:
        $ ls2_numc += 1
        $ ans_fth01_was_dropped = False
        scene ltf13
        play sound "T_audio/les2/2.34.mp3" volume 0.8
        Tech "You need to tell the browser where to find the image. The source ({b}src{/b}) is the location on the Internet
        where the image is stored."
        
        play sound "T_audio/anyone_wants.mp3" volume 0.8
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonTwoFillFourteen

        call screen lesson_two_ls13_fill

        label call_13:
            $ ans_fth01_was_dropped = False
            call screen lesson_two_ls13_fill

        
        
        label if_lt13_wrong:
            scene ltf13
            play sound "T_audio/Try_again.mp3" volume 0.8
            Tech "Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls13_fill


    label lessonTwoFillFourteen:
        scene ltf14
        show teacher_crossarm_smile
        play sound "T_audio/les2/2.35.mp3" volume 0.8
        Tech "Web browsers request information from the Web to put together and display web pages.
        Code, documents and media files such as images and videos are put together by the browser to display
        the resulting web page"
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        play sound "T_audio/les2/2.36.mp3" volume 0.8
        Tech "Web servers are computers that are always connected to the internet and continuously listening for
        requests of information."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        play sound "T_audio/les2/2.37.mp3" volume 0.8
        Tech "Click the Run button to see what the web browser will display"
        hide teacher_crossarm_smile
        call screen lesson_two_ls14_fill

        label when_run_14:
            scene lesson_14_when_run
            play sound "T_audio/les2/2.38.mp3" volume 0.8
            Tech "The source (src) in the image tag points to the server where the image can be found."
            jump lessonTwoFillFifteen
    

    label lessonTwoFillFifteen:
        $ ls2_numc += 1
        $ ans_ffit01_was_dropped = False
        scene ltf15
        play sound "T_audio/les2/2.39.mp3" volume 0.8
        Tech "You need to tell the browser where to find the image. The source (src) is the location on the Internet
        where the image is stored."

        play sound "T_audio/anyone_wants.mp3" volume 0.8
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonTwoFillSixteen

        call screen lesson_two_ls15_fill

        label call_15:
            $ ans_ffit01_was_dropped = False
            call screen lesson_two_ls15_fill
        
        label if_lt15_wrong:
            scene ltf15
            play sound "T_audio/Try_again.mp3" volume 0.8
            Tech"Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls15_fill


    label lessonTwoFillSixteen:
        $ ls2_numc += 1
        scene ltf16
        show teacher_crossarm_smile
        play sound "T_audio/les2/2.40.mp3" volume 0.8
        Tech "The broken image icon is usually shown in web pages when something is wrong with the image.
        The code below contains an error."
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        play sound "T_audio/les2/2.42.mp3" volume 0.8
        e "Web servers are computers that are always connected to the internet and continuously listening for
        requests of information."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        play sound "T_audio/les2/2.43.mp3" volume 0.8
        e "Click the Run button to see what the web browser will display"
        hide teacher_crossarm_smile
        call screen lesson_two_ls16_fill

        label when_run_16:
            scene lesson_16_when_run
            play sound "T_audio/les2/2.44.mp3" volume 0.8
            Tech "As a result, the image won't be displayed on the page."
            jump lessonTwoFillSeventeen


    label lessonTwoFillSeventeen:
        scene ltf17
        play sound "T_audio/les2/2.45.mp3" volume 0.8
        Tech "You can now include 4 different types of elements in your web pages. Let's put this into practice."
        play sound "T_audio/les2/2.46.mp3" volume 0.8
        Tech "Click the Run button to see what the web browser will display"
        call screen lesson_two_ls17_fill

        label when_run_17:
            scene lesson_17_when_run
            play sound "T_audio/great.mp3" volume 0.8
            Tech "Great!"
            jump lessonTwoFillEighteen


    label lessonTwoFillEighteen:
        scene ftg_bg
        show teacher_crossarm_happy
        play sound "T_audio/les2/2.47.mp3" volume 0.8
        Tech "The web browser will struggle to understand your code if there are errors. This can result in missing
        elements."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        play sound "T_audio/les2/2.49.mp3" volume 0.8
        Tech "Errors in HTML code can include missing quotation marks, missing tags and typos in general. Can you fix
        the errors?"
        hide teacher_crossarm_happy
        scene ltf18
        call screen lesson_two_ls18_fill
        

        label if_lt18_correct:
            scene lesson_18_when_run
            play sound "T_audio/do_did_a_great_job.mp3" volume 0.8
            Tech "You did a great job, well done!"
            jump lessonTwoTakeaways
            
    label lessonTwoTakeaways:
        show lesson_two_takeaways
        play sound "T_audio/les2/2.50.mp3" volume 0.8
        Tech "Fantastic work, code explorers! Lesson Two unlocked some cool insights: {b}Headings{/b} bring order with up to {b}6{/b} levels, use those {b}container tags{/b} wisely!"
        play sound "T_audio/les2/2.51.mp3" volume 0.8
        Tech "{b}Images{/b}, our visual pals, can be {b}linked or embedded{/b}—just share their online {b}address!{/b}"
        play sound "T_audio/les2/2.52.mp3" volume 0.8
        Tech "No {b}closing tags{/b} for images, keep the {b}URLs{/b} flowing for pixel perfection!"

    $ show_quick_menu = False
    stop music fadeout 1.0
    
    

    $ persistent.ast1_participation += 25
    label skipped_l2:

    play music "audio/quiz.mp3" volume 0.5
    call start_quiz_01

label pagtapos_ng_quiz_1:
    stop music fadeout 1.0

    play music "audio/sa_tech.mp3" volume 0.5
    scene bg_classroom
    
    show teacher_crossarm_smile
        # Lesson 2 
    $ persistent.lesson_2_quiz2 = persistent_quiz_01_q_counter_correct_answer  # Written Works 10%

    play sound "T_audio/quiz_class.mp3" volume 0.8
    Tech "Great job on the quiz, class! You all did fantastic."
    hide teacher_crossarm_smile
    show teacher_closed_happy
    play sound "T_audio/0.6.mp3" volume 0.8
    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting project related to what you've just learned."
    hide teacher_closed_happy
    play music "audio/office.mp3" volume 0.5
    jump l2_act2
    label pagtapos_ng_act_2:
        

    stop music fadeout 1.0

    play music "audio/sa_tech.mp3" volume 0.5

    scene bg_classroom

    show teacher_crossarm_smile
    play sound "T_audio/well done young coders.mp3" volume 0.8
    e"Well done young coders. Let's end our class here."
    hide teacher_crossarm_smile
    show teacher_closed_happy
    play sound "T_audio/goodbye class.mp3" volume 0.8
    e"Good bye class"
    hide teacher_closed_happy

    ######### Time save ######################################

   


    $ persistent.chp_two_date_taken = persistent.date_today
    $ persistent.chp_two_time = persistent.formatted_time





    label chp_two_end:
        #$ persistent.f_numhc += ls2_numhc
        #$ persistent.f_numc += ls2_numc
        #$ persistent.f_numic += ls2_numic
        $ save_total_run()
        $ reset_timer()
        #call screen chp_two_assessment()
        
        


    ######### Time save ######################################


    stop music fadeout 1.0


    stop music fadeout 1.0
    #jump behavior_two
    label chp_two_ending:
        #$ persistent.chp_prev_two_time = persistent.chp_two_time
        #$ persistent.chp_two_prev_score = persistent_quiz_02_q_counter_correct_answer
        #$ persistent.chp_two_prev_date = persistent.date_today
        #jump FBA
        scene bg_lesson_choices
        blank "End of chapter 2"
    
    $ lesson_two_finish = True

    call screen lesson_ui




    return


