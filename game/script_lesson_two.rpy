

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
        Tech "Ready to begin the lesson two?"
        Tech "So our topic for today are Headings and Images"

    label lessonTwoFillone:
        $ ans_f0_was_dropped = False
        scene ltf1
        Tech "{b}Headings{/b} in HTML come in different levels. <h1> defines the most important heading"
        
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
            Tech "You got it wrong"
            $ ls2_numic += 1
            call screen lesson_two_ls1_fill


    label lessonTwoFilltwo:
        $ ls2_numc += 1
        $ ans_ft_was_dropped = False
        scene ltf2
        Tech "You can use up to 6 levels of headings in HTML. The tags for these heading elements are <h1>, <h2>," 

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
            e "You got it wrong"
            $ ls2_numic += 1
            call screen lesson_two_ls2_fill


    label lessonTwoFillThree:
        $ ls2_numc += 1
        scene ltf4
        Tech "You can add different headings to your page to organize the content."
        Tech "In the upcoming section, we'll be entering a {b}Code Playground{/b} to practice writing HTML code."
        Tech "Click the Run button to see what the web browser will display"
        call screen lesson_two_ls4_fill

        label when_run:
            scene lesson_when_run
            Tech "<h1> usually styled with the largest font, and <h6> with the smallest."
            Tech "Let's move on to the next example"
            jump lessonTwoFillFour
    

    label lessonTwoFillFour:
        scene ltf5
        Tech "You can combine headings with other elements."
        Tech "Run the code to see what the web browser will display"
        call screen lesson_two_ls5_fill

        label when_run_two:
            show lesson_when_run_4
            Tech "Let's have another example using the {b}Code playground{/b}"
            jump lessonTwoFillFive

    label lessonTwoFillFive:
        scene ftg_bg
        show teacher_crossarm_smile
        Tech "Ok, in this example, we will be filling up the gap or completing the tag to make the HTML code work."
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        Tech"Before that, let me teach you how to use the {b}Code Playground{/b}."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech "Click on the number or directly on the missing tag if you want to focus the text cursor."
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        Tech "Remember that after we code or complete the missing tags, we click the Run button."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech "After that, it will show the working code, or it may display 'Error' when there are code or tag issues."
        Tech "And if you get an error, you could click the 'Return' button to go back"
        hide teacher_crossarm_smile
        scene ltf6
        call screen lesson_two_ls6_fill
        

        label if_lt5_correct:
            show lesson_4_when_run
            blank "Show result"
            show teacher_crossarm_happy
            Tech "You did a great job, well done!"
            Tech "Moving on..."
            hide teacher_crossarm_happy
            jump lessonTwoFillSeven
    

    label lessonTwoFillSeven:
        $ ls2_numc += 1
        $ ans_fs1_was_dropped = False
        $ ans_fs2_was_dropped = False
        scene ltf7
        Tech "h1 is the most important heading."

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
            Tech "Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls7_fill


    label lessonTwoFillEight:
        $ ls2_numc += 1
        $ ans_fe1_was_dropped = False
        $ ans_fe2_was_dropped = False
        $ ans_fe3_was_dropped = False
        scene ltf8
        Tech "Heading levels need to be used in the correct order (h1, h2, …h6)"

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
        Tech "Many HTML elements require both opening and closing tags to contain elements"
        hide teacher smile
        show teacher_crossarm_smile
        Tech "These tags are also called"

        menu:
            'Empty tag':
                "Try again"
                $ ls2_numic += 1
                jump if_lth9_wrong
            'Container tag':
                show teacher smile
                e "you are correct"
                jump lessonTwoFillTen
            

        
        label if_lth9_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            hide teacher_crossarm_sad
            jump lessonTwoFillNine 

    
    label lessonTwoFillTen:
        $ ls2_numc += 1
        $ ans_ft01_was_dropped = False
        $ ans_ft02_was_dropped = False
        scene ltf10
        Tech "Some HTML elements can be defined with only one tag. They are called {b}empty tags{/b}."
        Tech"The image tag <img> is a good example of an empty tag, it doesn't require a closing tag"

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonHeadTakeaways

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
        Tech "Well done! young coders"
        Tech "Next topic will be about Images"
        jump lessonImgIntro

    label lessonImgIntro:
        show lesson_img_intro
        Tech "In this lesson, you'll learn to add images to your pages."
        Tech "Now let's begin"
        jump lessonTwoFillEleven

    label lessonTwoFillEleven:
        $ ls2_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_happy
        Tech "Images only require one tag to be displayed on your web page."
        hide teacher_crossarm_happy
        show teacher smile
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
            Tech "incorrect"
            $ ls2_numic += 1
            jump lessonTwoFillEleven
        hide teacher smile 
           


    label lessonTwoFillTwelve:
        $ ls2_numc += 1
        $ ans_ftw01_was_dropped = False
        scene ltf12
        Tech "Images are not technically inserted into a web page, they are linked. The source ({b}src{/b}) of the image
        needs to be included in the tag."

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
            Tech "Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls12_fill


    label lessonTwoFillThirteen:
        $ ls2_numc += 1
        $ ans_fth01_was_dropped = False
        scene ltf13
        Tech "You need to tell the browser where to find the image. The source ({b}src{/b}) is the location on the Internet
        where the image is stored."

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
            Tech "Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls13_fill


    label lessonTwoFillFourteen:
        scene ltf14
        show teacher_crossarm_smile
        Tech "Web browsers request information from the Web to put together and display web pages.
        Code, documents and media files such as images and videos are put together by the browser to display
        the resulting web page"
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        Tech "Web servers are computers that are always connected to the internet and continuously listening for
        requests of information."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech "Click the Run button to see what the web browser will display"
        hide teacher_crossarm_smile
        call screen lesson_two_ls14_fill

        label when_run_14:
            scene lesson_14_when_run
            Tech "The source (src) in the image tag points to the server where the image can be found."
            jump lessonTwoFillFifteen
    

    label lessonTwoFillFifteen:
        $ ls2_numc += 1
        $ ans_ffit01_was_dropped = False
        scene ltf15
        Tech "You need to tell the browser where to find the image. The source (src) is the location on the Internet
        where the image is stored."

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
            Tech"Try again"
            $ ls2_numic += 1
            call screen lesson_two_ls15_fill


    label lessonTwoFillSixteen:
        $ ls2_numc += 1
        scene ltf16
        show teacher_crossarm_smile
        Tech "The broken image icon is usually shown in web pages when something is wrong with the image.
        The code below contains an error."
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        e "Web servers are computers that are always connected to the internet and continuously listening for
        requests of information."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        e "Click the Run button to see what the web browser will display"
        hide teacher_crossarm_smile
        call screen lesson_two_ls16_fill

        label when_run_16:
            scene lesson_16_when_run
            Tech "As a result, the image won't be displayed on the page."
            jump lessonTwoFillSeventeen


    label lessonTwoFillSeventeen:
        scene ltf17
        Tech "You can now include 4 different types of elements in your web pages. Let's put this into practice."
        Tech "Click the Run button to see what the web browser will display"
        call screen lesson_two_ls17_fill

        label when_run_17:
            scene lesson_17_when_run
            Tech "Great!"
            jump lessonTwoFillEighteen


    label lessonTwoFillEighteen:
        scene ftg_bg
        show teacher_crossarm_happy
        Tech "The web browser will struggle to understand your code if there are errors. This can result in missing
        elements."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech "Errors in HTML code can include missing quotation marks, missing tags and typos in general. Can you fix
        the errors?"
        hide teacher_crossarm_happy
        scene ltf18
        call screen lesson_two_ls18_fill
        

        label if_lt18_correct:
            scene lesson_18_when_run
            Tech "You did a great job, well done!"
            jump lessonTwoTakeaways
            
    label lessonTwoTakeaways:
        show lesson_two_takeaways
        Tech "Fantastic work, code explorers! Lesson Two unlocked some cool insights: {b}Headings{/b} bring order with up to {b}6{/b} levels, use those {b}container tags{/b} wisely!"
        Tech "{b}Images{/b}, our visual pals, can be {b}linked or embedded{/b}—just share their online {b}address!{/b}"
        Tech "No {b}closing tags{/b} for images, keep the {b}URLs{/b} flowing for pixel perfection!"

    $ show_quick_menu = False
    stop music fadeout 1.0
    
    play music "audio/quiz.mp3" volume 0.5

    $ persistent.ast1_participation += 25
    label skipped_l2:

    jump start_quiz_01

    label pagtapos_ng_quiz_1:



        # Lesson 2 
    $ persistent.lesson_2_quiz2 = persistent_quiz_01_q_counter_correct_answer  # Written Works 10%


    Tech "Great job on the quiz, class! You all did fantastic."

    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting project related to what you've just learned."
    jump l2_act2
    label pagtapos_ng_act_2:
        

    stop music fadeout 1.0

    play music "audio/sa_tech.mp3" volume 0.5

    scene bg_classroom

    show teacher_crossarm_smile
    e"Well done young coders. Let's end our class here."
    hide tea
    show teacher_closed_happy
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


