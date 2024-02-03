

default persistent.chp_three_time = ""
default persistent.chp_prev_three_time = ""
default persistent.formatted_time = ""  # Define as a persistent variable

default persistent.chp_three_prev_date = 0
default persistent.chp_three_date_taken = 0

default persistent.chp_three_prev_score = 0


screen chp_three_assessment():
    image "images/chp_three_asses.png"

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        action Return()

    
    text '{b}[persistent.chp_prev_three_time]{/b}' size 20 color "#87431E" xpos(539) ypos(243)
    text '{b}[persistent.chp_three_prev_date]{/b}' size 20 color "#87431E" xpos(358) ypos(387)
    image Solid("#FF5A00") xsize(persistent.chp_three_prev_score * 80) ysize(45) xpos 435 ypos 301
    text "{b}[persistent.chp_two_three_score]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 301   
    
    text '{b}[persistent.chp_three_time]{/b}' size 20 color "#171716" xpos(539) ypos(541)
    text '{b}[persistent.chp_three_date_taken]{/b}' size 20 color "#171716" xpos(358) ypos(679)
    image Solid("#FF5A00") xsize(persistent_quiz_02_q_counter_correct_answer * 80) ysize(45) xpos 435 ypos 599
    text "{b}[persistent_quiz_02_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 599

label lesson_three:
    scene bg_classroom
    $ ls3_numhc = 0
    $ ls3_numc = 0
    $ ls3_numic = 0
    $ l3_takes += 1

    $ persistent.lesson_3_quiz3 = 0
    $ persistent.lesson_3_act3 = 0
    # Start ng Time ###############
    $ save_total_run()
    $ reset_timer()
    show screen timeplayedbutton
    # Start ng Time ###############

    if lesson_two_finish:
        jump lessonThreeIntro
    else:
        Tech"Please finish lesson 2"
        call screen lesson_ui    


    label lessonThreeIntro:

        stop music fadeout 1.0
        $ show_quick_menu = False
        play music "audio/sa_tech.mp3" volume 0.5

        scene lesson_three_intro
        Tech"Are you ready to take lesson Three? CLICK!!!"
        jump lessonThreeFillOne

    label lessonThreeFillOne:
        $ ans_f3o01_was_dropped = False
        scene l3f1
        Tech"{b}Comments{/b} help other humans to read your code."
        Tech"You can add notes or explanations to your code with the comment tag: {b}<!--...-->{/b}"
        call screen lesson_three_ls1_fill

        label call_th1:
            $ ans_f3o01_was_dropped = False
            call screen lesson_three_ls1_fill

        
        
        label if_lth1_wrong:
            scene l3f1
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls1_fill


    label lessonThreeFillTwo:
        $ ls3_numc += 1
        $ ans_f3t01_was_dropped = False
        $ ans_f3t02_was_dropped = False
        scene l3f2
        
        Tech"It's a good practice to use comments in your HTML code. They explain what the code does."
        hide teacher_crossarm_smile

        label l3Int3:
            menu:
                "Talk to classmate":
                    jump start_hitting_teach3
                    label opsl3_1:
                        $ persistent.ast1_rudeness += 25
                        jump skipped_l3
                "Play with your classmate":
                    jump begin_ho_mg3
                    label opsl3_2:
                        $ persistent.ast1_rudeness += 25
                        jump skipped_l3
                "Raise Hand":
                    pass
                "Ignore":
                    jump lessonThreeFillThree

        call screen lesson_three_ls2_fill

        label call_th2:
            $ ans_f3t01_was_dropped = False
            $ ans_f3t02_was_dropped = False
            call screen lesson_three_ls2_fill

        
        
        label if_lth2_wrong:
            scene l3f2
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls2_fill


    label lessonThreeFillThree:
        $ ls3_numc += 1
        scene l3f3
        show teacher_crossarm_smile
        Tech"It's a good practice to use comments in your HTML code. They explain what the code does."
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        Tech"Comments are ignored by browsers and not displayed on the web page."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech"Click the Run button to see what the web browser will display"
        hide teacher_crossarm_smile

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillFour

        call screen lesson_three_ls3_fill

        label llt_when_run:
            scene lesson_th_3_when_run
            Tech"As you can see, it didn't show up on the browser."
            Tech"The purpose of comment is to give label or description of the code line"
            Tech"Comments in code are for the humans working on the HTML file"
            jump lessonThreeFillFour
    
    
    label lessonThreeFillFour:
        $ ans_f3f01_was_dropped = False
        $ ans_f3f02_was_dropped = False
        scene l3f4
        Tech"You can use comments to temporarily disable part of your code so its not displayed by the browser."
        Tech"Enclose the whole tag with comment"

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillFive

        call screen lesson_three_ls4_fill

        label call_th4:
            $ ans_f3f01_was_dropped = False
            $ ans_f3f02_was_dropped = False
            call screen lesson_three_ls4_fill

        
        
        label if_lth4_wrong:
            scene l3f4
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls4_fill


    label lessonThreeFillFive:
        $ ls3_numc += 1
        scene l3f5
        show teacher_crossarm_smile
        Tech"HTML is a case - insensitive language. This means that the web browser will understand the tags in both upper and lowercase form."
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        Tech"Click the Run button to see what the web browser will display"
        hide teacher_crossarm_happy

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillSix

        call screen lesson_three_ls5_fill

        label lthf_when_run:
            scene lesson_th_5_when_run
            Tech"It still works"
            Tech"But its good practice to use lowercase, to make your code consistent and easy to read."
            jump lessonThreeFillSix


    label lessonThreeFillSix:
        scene l3f6
        show teacher_crossarm_smile
        Tech"The web browser will ignore white spaces and line breaks in your code. Still, its a good practice to organize your code into different lines so it's easier to read by humans."
        Tech"Click the Run button to see what the web browser will display"
        hide teacher_crossarm_smile
        
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillSeven

        call screen lesson_three_ls6_fill

        label lths_when_run:
            scene lesson_th_6_when_run
            Tech"It still works"
            jump lessonThreeFillSeven


    label lessonThreeFillSeven:
        scene lesson_3_7 
        Tech"Line breaks in elements like the paragraph are ignored by the browser."
        Tech"How many line will the browser display"

        menu:
            '1':
                Tech "you are correct"
                $ ls3_numc += 1
                jump lessonThreeFillEight
            '2':
                jump if_lth7_wrong
        
        label if_lth7_wrong:
            Tech"incorrect"
            $ ls3_numic += 1
            jump lessonThreeFillSeven 

    
    label lessonThreeFillEight:
        $ ans_f3e01_was_dropped = False
        scene l3f8
        Tech"If you need to create a line break you can use the <br> tag. <br> will force a line break."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillNine

        call screen lesson_three_ls8_fill

        label call_th8:
            $ ans_f3e01_was_dropped = False
            call screen lesson_three_ls8_fill

        
        
        label if_lth8_wrong:
            scene l3f8
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls8_fill


    label lessonThreeFillNine:
        $ ls3_numc += 1
        scene l3f9
        show teacher_crossarm_happy
        Tech"Elements like headings and paragraphs automatically start on a new line when you create them."
        Tech"Click the Run button to see what the web browser will display"
        hide teacher_crossarm_happy

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillTen

        call screen lesson_three_ls9_fill

        label lthn_when_run:
            scene lesson_th_9_when_run
            Tech "Well done!"
            Tech"However, other elements like the <button> require the use of <br> to be separated into different lines."
            Tech"It behaves like an inline element, meaning that it will flow within the content of a line and won't start on a new line."
            jump lessonThreeFillTen


    label lessonThreeFillTen:
        scene lesson_3_10 
        Tech"How many lines do you think this code will display"

        menu:
            '1':
                jump if_lth10_wrong
            '4':
                Tech"you are correct"
                jump lessonThreeFillTwelve
            '2':
                jump if_lth10_wrong
            
        
        label if_lth10_wrong:
            Tech"incorrect"
            $ ls3_numic += 1
            jump lessonThreeFillTen 



    label lessonThreeFillTwelve:
        $ ls3_numc += 1
        $ ans_f3tw01_was_dropped = False
        scene l3f12

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonCommentTakeaways

        call screen lesson_three_ls12_fill

        label call_th12:
            $ ans_f3tw01_was_dropped = False
            call screen lesson_three_ls12_fill

        
        
        label if_lth12_wrong:
            scene l3f12
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls12_fill


    label lessonCommentTakeaways:
        scene lesson_comment_takeaways
        Tech"Well done, make sure you review this section"
        Tech"Next topic will be the standards and best practices"
        jump lessonThreeFillThirteen


    label lessonThreeFillThirteen:
        $ ls3_numc += 1
        $ ans_f3th01_was_dropped = False
        $ ans_f3th02_was_dropped = False
        scene l3f13
        Tech"In this lesson you'll start applying some of the standards and best practices used in the web industry."
        
        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillFourteen

        call screen lesson_three_ls13_fill

        label call_th13:
            $ ans_f3th01_was_dropped = False
            $ ans_f3th02_was_dropped = False
            call screen lesson_three_ls13_fill

        
        
        label if_lth13_wrong:
            scene l3f13
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls13_fill


    label lessonThreeFillFourteen:
        $ ls3_numc += 1
        $ ans_f3ft01_was_dropped = False
        scene l3f14
        Tech"The {b}<body> container tag{/b} is used to group everything that gets displayed on a page when loaded in a browser."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillFifteen

        call screen lesson_three_ls14_fill

        label call_th14:
            $ ans_f3ft01_was_dropped = False
            call screen lesson_three_ls14_fill

        
        
        label if_lth14_wrong:
            scene l3f14
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls14_fill


    label lessonThreeFillFifteen:
        $ ls3_numc += 1
        $ ans_f3fit01_was_dropped = False
        $ ans_f3fit02_was_dropped = False
        scene l3f15
        Tech"{b}Body tags{/b} are needed for your page to be compatible with {b}all{/b} web browsers."
        Tech"A web page can contain only {b}one body element{/b}"

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillSixteen

        call screen lesson_three_ls15_fill
        
        label call_th15:
            $ ans_f3fit01_was_dropped = False
            $ ans_f3fit02_was_dropped = False
            call screen lesson_three_ls15_fill

        
        
        label if_lth15_wrong:
            scene l3f15
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls15_fill


    label lessonThreeFillSixteen:
        $ ls3_numc += 1
        $ ans_f3sit01_was_dropped = False
        $ ans_f3sit02_was_dropped = False
        $ ans_f3sit03_was_dropped = False
        scene l3f16
        Tech"All the content elements that you need to display (like paragraphs, headings, buttons, and images) need to be inside the {b}<body> container bag{/b}."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillSeventeen

        call screen lesson_three_ls16_fill
        
        label call_th16:
            $ ans_f3sit01_was_dropped = False
            $ ans_f3sit02_was_dropped = False
            $ ans_f3sit03_was_dropped = False
            call screen lesson_three_ls16_fill

        
        
        label if_lth16_wrong:
            scene l3f16
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls16_fill


    label lessonThreeFillSeventeen:
        $ ls3_numc += 1
        $ ans_f3set01_was_dropped = False
        scene l3f17
        Tech"The <body> container tags needs to surround all the elements displayed on the page. When some HTML tags go inside others, this is called {b}nesting{/b}."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillEighteen

        call screen lesson_three_ls17_fill

        label call_th17:
            $ ans_f3set01_was_dropped = False
            call screen lesson_three_ls17_fill

        
        
        label if_lth17_wrong:
            scene l3f17
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls17_fill
    

    label lessonThreeFillEighteen:
        $ ls3_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech"Some HTML tags need to be placed inside others. This is called?"

        menu:
            'Feathering':
                jump if_lth18_wrong
            'Egging':
                jump if_lth18_wrong
            'Nesting':
                show teacher_crossarm_happy
                Tech "you are correct"
                jump lessonThreeFillNineteen
            

        
        label if_lth18_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            $ ls3_numic += 1
            jump lessonThreeFillEighteen 


    label lessonThreeFillNineteen:
        $ ls3_numc += 1
        $ ans_f3nit01_was_dropped = False
        $ ans_f3nit02_was_dropped = False
        scene l3f19
        Tech"Websites do more than just display content. The {b}<head> container tag{/b} is used to include technical information about the page."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillTwenty

        call screen lesson_three_ls19_fill
        
        label call_th19:
            $ ans_f3nit01_was_dropped = False
            $ ans_f3nit02_was_dropped = False
            call screen lesson_three_ls19_fill

        
        
        label if_lth19_wrong:
            scene l3f19
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls19_fill
    

    label lessonThreeFillTwenty:
        $ ls3_numc += 1
        $ ans_f3twt01_was_dropped = False
        $ ans_f3twt02_was_dropped = False
        scene l3f20
        Tech"You can use the head to help increase visibility and traffic from search engines like Google."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillTwentyOne


        call screen lesson_three_ls20_fill

        label call_th20:
            $ ans_f3twt01_was_dropped = False
            $ ans_f3twt02_was_dropped = False
            call screen lesson_three_ls20_fill

        
        
        label if_lth20_wrong:
            scene l3f20
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls20_fill


    label lessonThreeFillTwentyOne:
        $ ls3_numc += 1
        $ ans_f3twet01_was_dropped = False
        $ ans_f3twet02_was_dropped = False
        scene l3f21
        Tech"The head needs to be placed before the body."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillTwentyTwo

        call screen lesson_three_ls21_fill
        
        label call_th21:
            $ ans_f3twet01_was_dropped = False
            $ ans_f3twet02_was_dropped = False
            call screen lesson_three_ls21_fill

        
        
        label if_lth21_wrong:
            scene l3f21
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls21_fill


    label lessonThreeFillTwentyTwo:
        $ ls3_numc += 1
        scene l3f22
        Tech"The information in the head is not displayed on the web page. Only the title is shown, in search engine results (e.g. Google) and in the browser tab."
        Tech"Click the Run button to see what the web browser will display"
        call screen lesson_three_ls22_fill

        label lth22_when_run:
            scene lesson_th_22_when_run
            Tech"As you can see it changes the browser tab title into 'Title of the page'"
            Tech"Next, we will be talking about code indention"
            jump lessonThreeFillTwentyThree


    label lessonThreeFillTwentyThree:
        scene l3f23
        show teacher_crossarm_smile
        Tech"Today, the majority of web professionals always wrap their HTML code in <html> tags. The {b}<html> tag{/b} is a container tag." 
        Tech"{b}Head{/b} and {b}body{/b} are {b}nested{/b} inside the {b}<html> tags{/b}."
        Tech"{b}Indentation{/b} is considered a very good practice to improve code readability. Indentation is the spaces at the beginning of lines."
        Tech"To show what HTML code can be produced if indentation is used, click the Run button."
        hide teacher_crossarm_smile

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonThreeFillTwentyFour

        call screen lesson_three_ls23_fill

        label lth23_when_run:
            scene lesson_th_23_when_run
            Tech"Different levels of indentation are used to show nesting."
            jump lessonThreeFillTwentyFour


    label lessonThreeFillTwentyFour:
        $ ans_f3twef01_was_dropped = False
        $ ans_f3twef02_was_dropped = False
        scene l3f24
        Tech"Select all correct answers."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessoThreeOutro

        call screen lesson_three_ls24_fill

        label call_th24:
            $ ans_f3twef01_was_dropped = False
            $ ans_f3twef02_was_dropped = False
            call screen lesson_three_ls24_fill

        
        
        label if_lth24_wrong:
            scene l3f24
            Tech"Try again"
            $ ls3_numic += 1
            call screen lesson_three_ls24_fill    


    label lessoThreeOutro:
        $ ls3_numc += 1
        scene lesson_three_outro
        Tech"Bravo, coding champions! In this lesson, you harnessed the power of {b}comments{/b} for clarity, wielded the {b}<!--...--> tag{/b} as a code whisperer, mastered the {b}<br> ta{/b}g for line breaks"
        Tech"Organized HTML into {b}head{/b} and {b}body{/b} realms, invoked {b}<html>{/b} for universal harmony, and embraced the art of {b}indentation{/b} for readable collaborations."
        Tech "Your coding journey is flourishing—keep up the great work, young {b}coders{/b}! "

    

    $ show_quick_menu = False

    stop music fadeout 1.0
    
    play music "audio/quiz.mp3" volume 0.5
    $ persistent.ast1_participation += 25
    label skipped_l3:

    jump start_quiz_02

    label pagtapos_ng_quiz_2:

    # Lesson 3 
    $ persistent.lesson_3_quiz3 = persistent_quiz_02_q_counter_correct_answer
    
    Tech "Great job on the quiz, class! You all did fantastic."

    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting activity related to what you've just learned."
    jump l3_act3
    label pagtapos_ng_act_3:

    Tech "I hope you're all doing well. Today, I have an important announcement to make."

    Tech "We've covered a lot of material in lessons 1 to 3, and I've been impressed with your engagement and dedication."

    Tech "As a way to assess your understanding and progress, we'll be having an exam next"

    Tech "Ok! Let's start the examination"
    jump First_one
    label tapos_exam1:


    stop music fadeout 1.0

    $ show_quick_menu = True

    play music "audio/sa_tech.mp3" volume 0.5

    scene bg_classroom

    show teacher_crossarm_smile
    e "I want to acknowledge your hard work and dedication in preparing for this exam. It's a crucial part of our learning journey."
    e"Well done young coders. Let's end our class here."
    hide teacher_crossarm_smile
    show teacher_closed_happy
    e"Good bye class"
    e"You can now veiw your lesson 1 to 3 assessment"
    hide teacher_closed_happy

    ######### Time save ######################################

   


    $ persistent.chp_two_date_taken = persistent.date_today
    $ persistent.chp_two_time = persistent.formatted_time





    label chp_three_end:
        #$ persistent.f_numhc += ls3_numhc
        #$ persistent.f_numc += ls3_numc
        #$ persistent.f_numic += ls3_numic
        $ save_total_run()
        $ reset_timer()
        #call screen chp_three_assessment()
        
        


    ######### Time save ######################################
    #jump behavior_three
    stop music fadeout 1.0
    label chp_three_ending:
        #$ persistent.chp_prev_three_time = persistent.chp_three_time
        #$ persistent.chp_three_prev_score = persistent_quiz_03_q_counter_correct_answer
        #$ persistent.chp_three_prev_date = persistent.date_today
        scene bg_3
        blank "End of chapter 3"
        
    $ lesson_three_finish = True
    jump assessment_one
    call screen lesson_ui

    return


