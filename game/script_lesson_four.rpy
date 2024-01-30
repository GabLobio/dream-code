

default persistent.chp_four_time = ""
default persistent.chp_prev_four_time = ""

default persistent.chp_four_prev_date = 0
default persistent.chp_four_date_taken = 0

default persistent.chp_four_prev_score = 0

screen chp_four_assessment():
    image "images/chp_five_asses.png"

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        action Return()

    
    text '{b}[persistent.chp_prev_four_time]{/b}' size 20 color "#87431E" xpos(539) ypos(243)
    text '{b}[persistent.chp_four_prev_date]{/b}' size 20 color "#87431E" xpos(358) ypos(387)
    image Solid("#FF5A00") xsize(persistent.chp_four_prev_score * 80) ysize(45) xpos 435 ypos 301
    text "{b}[persistent.chp_four_prev_score]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 301   
    
    text '{b}[persistent.chp_four_time]{/b}' size 20 color "#171716" xpos(539) ypos(541)
    text '{b}[persistent.chp_four_date_taken]{/b}' size 20 color "#171716" xpos(358) ypos(679)
    image Solid("#FF5A00") xsize(persistent_quiz_03_q_counter_correct_answer * 80) ysize(45) xpos 435 ypos 599
    text "{b}[persistent_quiz_03_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 599


label lesson_four:
    scene bg_classroom

    $ ls4_numhc = 0
    $ ls4_numc = 0
    $ ls4_numic = 0
    $ l4_takes += 1

    # Start ng Time ###############
    $ save_total_run()
    $ reset_timer()
    show screen timeplayedbutton
    # Start ng Time ###############

    if lesson_three_finish:
        jump lessonFourFillOne
    else:
        Tech "Please finish lesson 3"
        call screen lesson_ui  

    
    label lessonFourFillOne:

        $ show_quick_menu = False
        play music "audio/sa_tech.mp3" volume 0.5

        scene lesson_text_intro
        Tech "Ready to start Text Formatting Lesson?"
        jump lessonFourFillTwo


    label lessonFourFillTwo:
        $ ans_ff_o1_was_dropped = False
        scene l4f2
        Tech "HTML {b}formatting tags{/b} are used to change how text is displayed."
        call screen lesson_four_ls2_fill

        label call_fr2:
            $ ans_ff_o1_was_dropped = False
            call screen lesson_four_ls2_fill
        
        label if_lf2_wrong:
            scene l4f2
            Tech "Try again"
            call screen lesson_four_ls2_fill


    label lessonFourFillThree:
        $ ls4_numc += 1
        $ ans_ff_th01_was_dropped = False
        $ ans_ff_th02_was_dropped = False
        scene l4f3
        Tech"Formatting tags are container tags. This means that both opening and closing tags are required."
        call screen lesson_four_ls3_fill

        label call_fr3:
            $ ans_ff_th01_was_dropped = False
            $ ans_ff_th02_was_dropped = False
            call screen lesson_four_ls3_fill
        
        label if_lf3_wrong:
            scene l4f3
            Tech "Try again"
            call screen lesson_four_ls3_fill


    label lessonFourFillFour:
        $ ls4_numc += 1
        $ ans_ff_fr01_was_dropped = False
        $ ans_ff_fr02_was_dropped = False
        scene l4f4
        Tech "The {b}italic tags <i>{/b} is used to display text in italics."
        call screen lesson_four_ls4_fill

        label call_fr4:
            $ ans_ff_fr01_was_dropped = False
            $ ans_ff_fr02_was_dropped = False
            call screen lesson_four_ls4_fill
        
        label if_lf4_wrong:
            scene l4f4
            Tech "Try again"
            call screen lesson_four_ls4_fill


    label lessonFourFillFive:
        $ ls4_numc += 1
        $ ans_ff_fv01_was_dropped = False
        $ ans_ff_fv02_was_dropped = False
        scene l4f5
        Tech "The {b}underline tags <u>{/b} is used to underline text"
        call screen lesson_four_ls5_fill

        label call_fr5:
            $ ans_ff_fv01_was_dropped = False
            $ ans_ff_fv02_was_dropped = False
            call screen lesson_four_ls5_fill
        
        label if_lf5_wrong:
            scene l4f5
            Tech "Try again"
            call screen lesson_four_ls5_fill


    label lessonFourFillSix:
        $ ls4_numc += 1
        $ ans_ff_sx01_was_dropped = False
        $ ans_ff_sx02_was_dropped = False
        scene l4f6
        Tech "Formatting tags are applied to text and are {b}nested{/b} inside {b}elements{/b}."
        call screen lesson_four_ls6_fill

        label call_fr6:
            $ ans_ff_sx01_was_dropped = False
            $ ans_ff_sx02_was_dropped = False
            call screen lesson_four_ls6_fill
        
        label if_lf6_wrong:
            scene l4f6
            Tech "Try again"
            call screen lesson_four_ls6_fill


    label lessonFourFillSeven:
        $ ls4_numc += 1
        scene l4f7
        show teacher_crossarm_smile
        Tech "The code above shows how the formatting tags are nested inside the paragraph element."
        Tech "Run the code to see what the web browser will display"
        hide teacher_crossarm_smile
        call screen lesson_four_ls7_fill

        label when_run_four_seven:
            scene lesson_4_7_run
            e "Well done!"
            jump lessonFourFillEight


    label lessonFourFillEight:
        scene lesson_intro_9
        Tech "You are getting better at this. Let's go to the next one"
        jump lessonFourFillNine

    
    label lessonFourFillNine:
        $ ans_ff_nn01_was_dropped = False
        $ ans_ff_nn02_was_dropped = False
        scene l4f9
        Tech "There are some HTML formatting tags that you can use to make your web pages more accessible."
        call screen lesson_four_ls9_fill

        label call_fr9:
            $ ans_ff_nn01_was_dropped = False
            $ ans_ff_nn02_was_dropped = False
            call screen lesson_four_ls9_fill
        
        label if_lf9_wrong:
            scene l4f9
            Tech "Try again"
            call screen lesson_four_ls9_fill


    label lessonFourFillTen:
        $ ls4_numc += 1
        scene l4f10
        show teacher_crossarm_happy
        Tech"{b}Strong{/b} text is displayed in bold, just like when you use the {b}<b>{/b} tag." 
        Tech"Run the code to see what the web browser will display"
        hide teacher_crossarm_happy
        call screen lesson_four_ls10_fill

        label when_run_four_ten:
            scene lesson_4_10_run
            Tech"The difference is that the {b}<strong>{/b} tag also has meaning and is used by screen readers."
            jump lessonFourFillEleven
        

    label lessonFourFillEleven:
        $ ans_ff_el01_was_dropped = False
        $ ans_ff_el02_was_dropped = False
        scene l4f11
        
        Tech"The {b}emphasis tag <em>{/b} is used to define emphasized text."
        
        call screen lesson_four_ls11_fill

        label call_fr11:
            $ ans_ff_el01_was_dropped = False
            $ ans_ff_el02_was_dropped = False
            call screen lesson_four_ls11_fill
        
        label if_lf11_wrong:
            scene l4f11
            Tech"Try again"
            call screen lesson_four_ls11_fill


    label lessonFourFillTwelve:
        $ ls4_numc += 1
        scene l4f12
        show teacher_crossarm_happy
        Tech"Emphasized text is displayed in Italic, just like when you use the <i> tag. The difference is that the screen reader will verbally stress the words."
        Tech"Run the code to see what the web browser will display"
        hide teacher_crossarm_happy
        call screen lesson_four_ls12_fill

        label when_run_four_twelve:
            scene lesson_4_12_run
            Tech"It almost look the same but still different"
            jump lessonFourFillThirteen
        

    label lessonFourFillThirteen:
        $ ans_ff_tt01_was_dropped = False
        $ ans_ff_tt02_was_dropped = False
        $ ans_ff_tt03_was_dropped = False
        scene l4f13
        Tech"The <strong> and <em> tags are considered {b}semantic formatting tags{/b} because they add meaning to the content."
        Tech"They can serve as an indication of emphasis to a screen reader."
        call screen lesson_four_ls13_fill

        label call_fr13:
            $ ans_ff_tt01_was_dropped = False
            $ ans_ff_tt02_was_dropped = False
            $ ans_ff_tt03_was_dropped = False
            call screen lesson_four_ls13_fill
        
        label if_lf13_wrong:
            scene l4f13
            Tech"Try again"
            call screen lesson_four_ls13_fill


    label lessonFourFillFourteen:
        $ ls4_numc += 1
        $ ans_ff_ft01_was_dropped = False
        $ ans_ff_ft02_was_dropped = False
        scene l4f14
        call screen lesson_four_ls14_fill

        label call_fr14:
            $ ans_ff_ft01_was_dropped = False
            $ ans_ff_ft02_was_dropped = False
            call screen lesson_four_ls14_fill
        
        label if_lf14_wrong:
            scene l4f14
            Tech"Try again"
            call screen lesson_four_ls14_fill



    label lessonFourTakewaysText:
        $ ls4_numc += 1
        scene lesson_text_takeaways
        Tech"Ready to start HyperText Lesson?"
        jump lessonFourIntroHypertext


    label lessonFourIntroHypertext:
        scene lesson_intro_link
        Tech"In this lesson, you`ll learn to connect web pages with {b}hyperlinks{/b}."
        jump lessonFourFillFifteen    


    label lessonFourFillFifteen:
        scene lesson_8_22 
        show teacher_crossarm_happy
        Tech"{b}Hypertext{/b} is text that contains a link to another page. "
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech"Web pages are called {b}Hypertext{/b} documents because they are connect by?"
        
        menu:
            'field (column) named "radio"':
                jump if_lf15_wrong
            'field (column) named "pay"':
                jump if_lf15_wrong
            'HyperText links (or hyperlinks)':
                show teacher_crossarm_happy
                Tech"you are correct"
                jump lessonFourFillSixteen
 
        label if_lf15_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            jump lessonFourFillFifteen   


    label lessonFourFillSixteen:
        $ ls4_numc += 1
        $ ans_ff_st01_was_dropped = False
        $ ans_ff_st02_was_dropped = False
        scene l4f16
        Tech "{b}Hyperlinks{/b} allows users to…"
        call screen lesson_four_ls16_fill

        label call_fr16:
            $ ans_ff_st01_was_dropped = False
            $ ans_ff_st02_was_dropped = False
            call screen lesson_four_ls16_fill
        
        label if_lf16_wrong:
            scene l4f16
            Tech "Try again"
            call screen lesson_four_ls16_fill


    label lessonFourFillSeventeen:
        $ ls4_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech"The {b}anchor tag <a>{/b} is used to create hyperlink on a web page."
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        Tech"The {b}<a> tag{/b} is a container tag."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech"What does this mean?"

        menu:
            'It requires both opening and closing tags':
                show teacher_crossarm_happy
                Tech "you are correct"
                jump lessonFourFillEighteen
            'It requires an opening tag only':
                jump if_lf17_wrong
            'It’s an empty tag':
                jump if_lf17_wrong
            
 
        label if_lf17_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            jump lessonFourFillSeventeen   


    label lessonFourFillEighteen:
        $ ls4_numc += 1
        $ ans_ff_egt01_was_dropped = False
        scene l4f18
        Tech "Hyperlinks are used to link from one web page to others. To create a link, you need {b}'href'{/b} to add the destination URL ."
        call screen lesson_four_ls18_fill

        label call_fr18:
            $ ans_ff_egt01_was_dropped = False
            call screen lesson_four_ls18_fill
        
        label if_lf18_wrong:
            scene l4f18
            Tech "Try again"
            call screen lesson_four_ls18_fill


    label lessonFourFillNineteen:
        $ ls4_numc += 1
        $ ans_ff_nt01_was_dropped = False
        scene l4f19
        call screen lesson_four_ls19_fill

        label call_fr19:
            $ ans_ff_nt01_was_dropped = False
            call screen lesson_four_ls19_fill
        
        label if_lf19_wrong:
            scene l4f19
            Tech "Try again"
            call screen lesson_four_ls19_fill


    label lessonFourFillTwenty:
        $ ls4_numc += 1
        $ ans_ff_tw01_was_dropped = False
        $ ans_ff_tw02_was_dropped = False
        scene l4f20
        call screen lesson_four_ls20_fill

        label call_fr20:
            $ ans_ff_tw01_was_dropped = False
            $ ans_ff_tw02_was_dropped = False
            call screen lesson_four_ls20_fill
        
        label if_lf20_wrong:
            scene l4f20
            Tech "Try again"
            call screen lesson_four_ls20_fill


    label lessonFourFillTwentyOne:
        $ ls4_numc += 1
        $ ans_ff_two01_was_dropped = False
        $ ans_ff_two02_was_dropped = False
        scene l4f21
        Tech "The URL needs to be enclosed in quotes to work without errors. If you forget to add {b}href{/b} or the {b}quotes{/b}, the <a> tag won't create a hyperlink ."
        call screen lesson_four_ls21_fill

        label call_fr21:
            $ ans_ff_two01_was_dropped = False
            $ ans_ff_two02_was_dropped = False
            call screen lesson_four_ls21_fill
        
        label if_lf21_wrong:
            scene l4f21
            Tech "Try again"
            call screen lesson_four_ls21_fill
    

    label lessonFourFillTwentyTwo:
        $ ls4_numc += 1
        scene lesson_4_22 
        Tech "What’s wrong with this line of code?"

        menu:
            'Matching single quotes are needed to avoid errors':
                jump if_lf22_wrong
            'The quotation marks don’t match':
                jump if_lf22_wrong
            'The href is missing':
                Tech "you are correct"
                jump lessonFourFillTwentyThree
            
            
 
        label if_lf22_wrong:
            Tech "incorrect"
            jump lessonFourFillTwentyTwo 


    label lessonFourFillTwentyThree:
        $ ls4_numc += 1
        scene ftg_bg
        show teacher_crossarm_smile
        Tech "Something is wrong with this code. Can you fix it?"
        Tech "Hint: Try checking each line or number"
        hide teacher_crossarm_smile
        call screen lesson_four_ls23_fill
        

        label if_lf23_correct:
            $ ls4_numc += 1
            show lesson_4_23_run
            Tech "You did a great job, well done!"
            Tech "We will be having a lot of this next lesson"
            jump lessonFourFillTwentyFour


    label lessonFourFillTwentyFour:
        scene l4f24
        show teacher_crossarm_smile
        Tech "You can nest hyperlinks inside other text elements "
        Tech "Run the code to see what the web browser will display"
        hide teacher_crossarm_smile
        call screen lesson_four_ls24_fill

        label when_run_four_TwentyFour:
            scene lesson_4_24_run
            Tech "As you can see it can be used inside <p> tag"
            jump lessonIntrFor25


    label lessonIntrFor25:
        scene lesson_intro_25
        Tech "You can also use hyperlinks to connect pages of the same website."
        jump lessonFourFillTwentyFive

    
    label lessonFourFillTwentyFive:
        $ ans_ff_tf01_was_dropped = False
        $ ans_ff_tf02_was_dropped = False
        $ ans_ff_tf03_was_dropped = False
        scene l4f25
        Tech "HTML stands for {b}HyperText Markup Language{/b}."
        call screen lesson_four_ls25_fill

        label call_fr25:
            $ ans_ff_tf01_was_dropped = False
            $ ans_ff_tf02_was_dropped = False
            $ ans_ff_tf03_was_dropped = False
            call screen lesson_four_ls25_fill
        
        label if_lf25_wrong:
            scene l4f25
            Tech "Try again"
            call screen lesson_four_ls25_fill


    label lessonFourFillTwentySix:
        $ ls4_numc += 1
        $ ans_ff_ts01_was_dropped = False
        $ ans_ff_ts02_was_dropped = False
        $ ans_ff_ts03_was_dropped = False
        scene l4f26
        call screen lesson_four_ls26_fill

        label call_fr26:
            $ ans_ff_ts01_was_dropped = False
            $ ans_ff_ts02_was_dropped = False
            $ ans_ff_ts03_was_dropped = False
            call screen lesson_four_ls26_fill
        
        label if_lf26_wrong:
            scene l4f26
            Tech "Try again"
            call screen lesson_four_ls26_fill


    label lessonLinkTakeaways:
        $ ls4_numc += 1
        scene lesson_link_takeaways
        Tech "Awesome job, young coders! You've just finished learning how to make your words stand out and create clickable links on the web."
        Tech "Your websites are going to look super cool now! Keep up the great work, and soon you'll be web design experts."
        Tech "Way to go and happy coding, little tech wizards!"
        jump lessonListIntro


    label lessonListIntro:
        scene lesson_intro_list
        Tech "Hello, coding enthusiasts! Today, we're diving into the world of HTML lists. We'll explore how to organize content using ordered lists, unordered lists, and the art of nesting." 
        Tech "Get ready to level up your web development skills as we delve into the adventure of list-making!"
        jump lessonFourTwentySeven

    
    label lessonFourTwentySeven:
        $ ans_ff_twts01_was_dropped = False
        scene l4f27
        Tech "A list consists of {b}list items <li>{/b}."
        call screen lesson_four_ls27_fill

        label call_fr27:
            $ ans_ff_twts01_was_dropped = False
            call screen lesson_four_ls27_fill
        
        label if_lf27_wrong:
            scene l4f27
            Tech "Try again"
            call screen lesson_four_ls27_fill
               

    label lessonFourTwentyEight:
        $ ls4_numc += 1
        $ ans_ff_twte01_was_dropped = False
        $ ans_ff_twte02_was_dropped = False
        $ ans_ff_twte03_was_dropped = False
        scene l4f28
        Tech "{b}List items{/b} are container tags."
        call screen lesson_four_ls28_fill

        label call_fr28:
            $ ans_ff_twte01_was_dropped = False
            $ ans_ff_twte02_was_dropped = False
            $ ans_ff_twte03_was_dropped = False
            call screen lesson_four_ls28_fill
        
        label if_lf28_wrong:
            scene l4f28
            Tech "Try again"
            call screen lesson_four_ls28_fill


    label lessonOrderedList:
        scene lesson_ordered_list
        Tech "{b}Ordered lists <ol>{/b} show with numbers (1,2,3…) instead of bullet points. Use <ol> when the points have a certain order, like step by step instructions."
        jump lessonFourTwentyNine


    label lessonFourTwentyNine:
        $ ls4_numc += 1
        $ ans_ff_twtn01_was_dropped = False
        scene l4f29
        call screen lesson_four_ls29_fill

        label call_fr29:
            $ ans_ff_twtn01_was_dropped = False
            call screen lesson_four_ls29_fill
        
        label if_lf29_wrong:
            scene l4f29
            Tech "Try again"
            call screen lesson_four_ls29_fill


    label lessonFourThirty:
        $ ls4_numc += 1
        $ ans_ff_tht01_was_dropped = False
        $ ans_ff_tht02_was_dropped = False
        $ ans_ff_tht03_was_dropped = False
        $ ans_ff_tht04_was_dropped = False
        $ ans_ff_tht05_was_dropped = False
        scene l4f30
        Tech "Lists are also container tags, with the list items nested inside"
        call screen lesson_four_ls30_fill

        label call_fr30:
            $ ans_ff_twt01_was_dropped = False
            $ ans_ff_twt02_was_dropped = False
            $ ans_ff_twt03_was_dropped = False
            $ ans_ff_tht04_was_dropped = False
            $ ans_ff_tht05_was_dropped = False
            call screen lesson_four_ls30_fill
        
        label if_lf30_wrong:
            scene l4f30
            Tech "Try again"
            call screen lesson_four_ls30_fill

            
    label lessonFourThirtyOne:
        $ ls4_numc += 1
        $ ans_ff_thto01_was_dropped = False
        $ ans_ff_thto02_was_dropped = False
        scene l4f31
        Tech "Use {b}unordered lists <ul>{/b} when the order of the items is not important. They are shown with bullet points"
        call screen lesson_four_ls31_fill

        label call_fr31:
            $ ans_ff_twto01_was_dropped = False
            $ ans_ff_twto02_was_dropped = False
            call screen lesson_four_ls31_fill
        
        label if_lf31_wrong:
            scene l4f31
            Tech "Try again"
            call screen lesson_four_ls31_fill



    label lessonFourThirtyTwo:
        $ ls4_numc += 1
        scene l4f32
        Tech "You can nest a list inside another list"
        Tech "Run the code to see what the web browser will display"
        call screen lesson_four_ls32_fill

        label when_run_four_32:
            scene lesson_4_32_run
            Tech "Remember the indention so you won't be confused when you change a list items."
            jump lessonFourThirtyThree


    label lessonFourThirtyThree:
        $ ans_ff_thtt01_was_dropped = False
        $ ans_ff_thtt02_was_dropped = False
        $ ans_ff_thtt03_was_dropped = False
        $ ans_ff_thtt04_was_dropped = False
        scene l4f33
        Tech "A list can contain any number of items."
        call screen lesson_four_ls33_fill

        label call_fr33:
            $ ans_ff_thtt01_was_dropped = False
            $ ans_ff_thtt02_was_dropped = False
            $ ans_ff_thtt03_was_dropped = False
            $ ans_ff_thtt04_was_dropped = False
            call screen lesson_four_ls33_fill
        
        label if_lf33_wrong:
            scene l4f33
            Tech "Try again"
            call screen lesson_four_ls33_fill

    
    label lessonFourThirtyFour:
        $ ls4_numc += 1
        $ ans_ff_thtf01_was_dropped = False
        $ ans_ff_thtf02_was_dropped = False
        $ ans_ff_thtf03_was_dropped = False
        $ ans_ff_thtf04_was_dropped = False
        scene l4f34
        call screen lesson_four_ls34_fill

        label call_fr34:
            $ ans_ff_thtf01_was_dropped = False
            $ ans_ff_thtf02_was_dropped = False
            $ ans_ff_thtf03_was_dropped = False
            $ ans_ff_thtf04_was_dropped = False
            call screen lesson_four_ls34_fill
        
        label if_lf34_wrong:
            scene l4f34
            Tech "Try again"
            call screen lesson_four_ls34_fill


    label lessonFourThirtyFive:
        $ ls4_numc += 1
        scene lesson_4_35 
        Tech "Indentation is used to show nested elements."
        Tech "What's the code showing?"

        menu:
            'An ordered list nested inside an unordered list':
                Tech "you are correct"
                jump lessonFourThirtySix
            'An unordered list nested inside an ordered list':
                jump if_lf35_wrong
            
 
        label if_lf35_wrong:
            Tech "incorrect"
            jump lessonFourThirtyFive 


    label lessonFourThirtySix:
        $ ls4_numc += 1
        scene lesson_4_36 
        Tech "Remember the web browser will ignore line breaks and white spaces in HTML code."
        Tech "What will the web browser display?"

        menu:
            '1 big paragraph element with all the text':
                jump if_lf36_wrong
            '3 separate paragraphs':
                Tech "you are correct"
                jump lessonFourThirtySeven
            '2 paragraphs':
                jump if_lf36_wrong
            
 
        label if_lf36_wrong:
            Tech "incorrect"
            jump lessonFourThirtySix 


    label lessonFourThirtySeven:
        $ ls4_numc += 1
        scene lesson_4_37 
        Tech "Each list item will be displayed on a new line."
        Tech "What will the web browser display?"

        menu:
            '2 unordered list items (A and B) in different lines':
                Tech  "you are correct"
                jump lessonFourThirtyEight
            'Nothing due to errors':
                jump if_lf37_wrong
            '2 unordered list items (A and B) in the same line':
                jump if_lf37_wrong
            
 
        label if_lf37_wrong:
            Tech "incorrect"
            jump lessonFourThirtySeven 


    label lessonFourThirtyEight:
        $ ls4_numc += 1
        scene lesson_4_38 
        Tech  "What will the web browser display?"

        menu:
            '2 ordered list items, 2 lines':
                jump if_lf38_wrong
            '3 ordered list item, 2 lines':
                jump if_lf38_wrong
            '3 ordered list items, 3 lines':
                Tech "you are correct"
                jump lessonListOutro
            
            
 
        label if_lf38_wrong:
            Tech "incorrect"
            jump lessonFourThirtyEight 

    
    label lessonListOutro:
        $ ls4_numc += 1
        scene lesson_list_takeaways
        Tech "Well done, coding trailblazers! In our coding odyssey, you've mastered {b}text formatting{/b} to make your content pop, discovered the magic of {b}hyperlinks{/b} to connect your pages, and delved into the art of {b}lists for organized content{/b}"
        Tech "Bravo! Keep weaving these HTML tags, and your web development journey will continue to shine brightly. Onward to more coding adventures!"

    stop music fadeout 1.0
    
    play music "audio/quiz.mp3" volume 0.5

    jump start_quiz_03

    label pagtapos_ng_quiz_3:

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

   


    $ persistent.chp_four_date_taken = persistent.date_today
    $ persistent.chp_four_time = persistent.formatted_time





    label chp_four_end:
        $ persistent.f_numhc += ls4_numhc
        $ persistent.f_numc += ls4_numc
        $ persistent.f_numic += ls4_numic
        $ save_total_run()
        $ reset_timer()
        call screen chp_four_assessment()
        
        


    ######### Time save ######################################
    
    stop music fadeout 1.0
    jump behavior_four
    label chp_four_ending:
        $ persistent.chp_prev_four_time = persistent.chp_four_time
        $ persistent.chp_four_prev_score = persistent_quiz_03_q_counter_correct_answer
        $ persistent.chp_four_prev_date = persistent.date_today
        scene bg_4
        blank "End of chapter 4"

    $ lesson_four_finish = True
    call screen lesson_ui




    return



label good_job:
    show bg_classroom
    "good"
    return