


default persistent.chp_five_time = ""
default persistent.chp_prev_five_time = ""

default persistent.chp_five_prev_date = 0
default persistent.chp_five_date_taken = 0

default persistent.chp_five_prev_score = 0


screen chp_five_assessment():
    image "images/chp_five_asses.png"

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        action Return()

    
    text '{b}[persistent.chp_prev_five_time]{/b}' size 20 color "#87431E" xpos(539) ypos(243)
    text '{b}[persistent.chp_five_prev_date]{/b}' size 20 color "#87431E" xpos(358) ypos(387)
    image Solid("#FF5A00") xsize(persistent.chp_five_prev_score * 80) ysize(45) xpos 435 ypos 301
    text "{b}[persistent.chp_five_prev_score]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 301   
    
    text '{b}[persistent.chp_five_time]{/b}' size 20 color "#171716" xpos(539) ypos(541)
    text '{b}[persistent.chp_five_date_taken]{/b}' size 20 color "#171716" xpos(358) ypos(679)
    image Solid("#FF5A00") xsize(persistent_quiz_04_q_counter_correct_answer * 80) ysize(45) xpos 435 ypos 599
    text "{b}[persistent_quiz_04_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 599


label lesson_five:
    $ persistent.rude_lesson = "five"
    scene bg_classroom

    $ ls5_numhc = 0
    $ ls5_numc = 0
    $ ls5_numic = 0
    $ l5_takes += 1

    if lesson_four_finish:
        jump lessonAttributeIntro
    else:
        Tech "Please finish lesson 4"
        call screen lesson_ui

    #jump lessonFiveFillFourtyseven

    $ persistent.lesson_5_quiz5 = 0
    $ persistent.lesson_5_act5 = 0

    label lessonAttributeIntro:

        # Start ng Time ###############
        $ save_total_run()
        $ reset_timer()
        show screen timeplayedbutton
        # Start ng Time ###############
        $ show_quick_menu = False

        play music "audio/sa_tech.mp3" volume 0.5

        scene lesson_attributes_intro
        Tech "Ready to start Attribute Topic?"
        jump lessonFiveFillOne


    label lessonFiveFillOne:
        $ ans_ffive_o1_was_dropped = False
        scene l5f1
        Tech "{b}Attributes{/b} can be {b}optional{/b} or {b}required{/b}. You already know some required attributes."
        Tech "The image tag requires an attribute to work correctly."
        call screen lesson_five_ls1_fill

        label call_fv1:
            $ ans_ffive_o1_was_dropped = False
            call screen lesson_five_ls1_fill
        
        label if_lfv1_wrong:
            scene l5f1
            Tech"Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls1_fill

    
    label lessonFiveFilltwo:
        $ ls5_numc += 1
        $ ans_ffv_two1_was_dropped = False
        scene l5f2
        Tech "For container tags, the attributes always go in the opening tag. The anchor tag is another example of an HTML element that requires an attribute to work correctly."

        label l5Int5:
            menu:
                "Talk to classmate":
                    jump start_hitting_teach3
                    label opsl5_1:
                        $ persistent.ast1_rudeness += 50
                        jump skipped_l5
                "Play with your classmate":
                    jump begin_ho_mg5
                    label opsl5_2:
                        $ persistent.ast1_rudeness += 50
                        jump skipped_l5
                "Raise Hand":
                    pass
                "Ignore":
                    jump lessonFiveFillthree

        call screen lesson_five_ls2_fill

        label call_fv2:
            $ ans_ffv_two1_was_dropped = False
            call screen lesson_five_ls2_fill
        
        label if_lfv2_wrong:
            scene l5f2
            Tech"Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls2_fill

    label lessonFiveFillthree:
        $ ls5_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech "href (in the anchor tag) and src (in the image tag) are examples of?   "

        menu:
            "attributes":
                show teacher_crossarm_happy
                Tech "You are correct"
                jump lessonFiveFillFour
            "values":
                jump if_lfv3_wrong
            "properties":
                jump if_lfv3_wrong
 
        label if_lfv3_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillthree
    



    label lessonFiveFillFour:
        $ ls5_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech "In the container tags, attributes always go to what tag?"

        menu:
            "in the closing tag":
                jump if_lfv4_wrong
            "in the opening tag":
                show teacher_crossarm_happy
                Tech "You are correct"
                jump lessonFiveFillFive
 
        label if_lfv4_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFour

    
    label lessonFiveFillFive:
        $ ls5_numc += 1
        $ ans_ffv_fv1_was_dropped = False
        scene l5f5
        Tech "It's best practice to describe what images are showing. The {b}alt{/b} attribute (alternative text) is used to add image descriptions."
        call screen lesson_five_ls5_fill

        label call_fv5:
            $ ans_ffv_fv1_was_dropped = False
            call screen lesson_five_ls5_fill
        
        label if_lfv5_wrong:
            scene l5f5
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls5_fill

    
    label lessonFiveFillSix:
        $ ls5_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech "The alt attribute can be read aloud by screen readers "
        hide teacher_crossarm_smile
        show teacher_crossarm_happy
        Tech "shown when the image doesn`t load " 
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech "read by search engines "
        Tech "Is adding alternative text to images makes your page more accessible?"

        menu:
            "False":
                jump if_lfv6_wrong
            "True":
                show teacher_crossarm_smile
                Tech "You are correct"
                jump lessonFiveFillSeven
 
        label if_lfv6_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillSix


    label lessonFiveFillSeven:
        $ ls5_numc += 1
        $ ans_ffv_svn1_was_dropped = False
        $ ans_ffv_svn2_was_dropped = False
        scene l5f7

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillEight

        call screen lesson_five_ls7_fill

        label call_fv7:
            $ ans_ffv_svn1_was_dropped = False
            $ ans_ffv_svn2_was_dropped = False
            call screen lesson_five_ls7_fill
        
        label if_lfv7_wrong:
            scene l5f7
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls7_fill


    label lessonFiveFillEight:
        $ ls5_numc += 1
        $ ans_ffv_egt1_was_dropped = False
        $ ans_ffv_egt2_was_dropped = False
        $ ans_ffv_egt3_was_dropped = False
        scene l5f8

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillNine
        
        # Classmate Confused Interaction
        blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."
        # Dialogue to nung kaklaseng nyang boy
        "Hey, mind lending a hand? I'm a bit lost with some of the words the teacher just used. Could you help me catch up on what I missed? I'd appreciate it, and maybe we can quickly go through it together so we don't fall too behind."

        menu:
            "Talk to him":
                blank "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
                $ persistent.ast2_kindness = 25
                jump lessonFourFillThirteen
            "Refuse and explain that you can teach him later; choose to focus on the current lesson":
                blank "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
                $ persistent.ast2_kindness = 25
                pass

        call screen lesson_five_ls8_fill

        label call_fv8:
            $ ans_ffv_egt1_was_dropped = False
            $ ans_ffv_egt2_was_dropped = False
            $ ans_ffv_egt3_was_dropped = False
            call screen lesson_five_ls8_fill
        
        label if_lfv8_wrong:
            scene l5f8
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls8_fill


    label lessonFiveFillNine:
        $ ls5_numc += 1
        scene l5f9
        Tech "You can control the size of images in your web pages. {b}width{/b} is an optional attribute. Run the code to see what the web browser will display"
        call screen lesson_five_ls9_fill

        label when_run_five_nine:
            scene lesson_5_9_run
            Tech "See the difference? The attribute width added a width length of 300 pixel"
            jump lessonFiveFillTen    


    label lessonFiveFillTen:
        $ ans_ffv_ten1_was_dropped = False
        $ ans_ffv_ten2_was_dropped = False
        scene l5f10

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillEleven

        call screen lesson_five_ls10_fill

        label call_fv10:
            $ ans_ffv_ten1_was_dropped = False
            $ ans_ffv_ten2_was_dropped = False
            call screen lesson_five_ls10_fill
        
        label if_lfv10_wrong:
            scene l5f10
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls10_fill


    label lessonFiveFillEleven:
        $ ls5_numc += 1
        scene l5f11
        Tech "{b}height{/b} is an optional attribute for the image element. Run the code to see what the web browser will display"
        call screen lesson_five_ls11_fill

        label when_run_five_eleven:
            scene lesson_5_11_run
            Tech "See the difference? The attribute height added a height length of 300 pixel"
            jump lessonFiveFillTwelve


    label lessonFiveFillTwelve:
        $ ls5_numc += 1
        scene l5f12
        Tech "You can provide both {b}width and height{/b}. Run the code to see what the web browser will display"
        call screen lesson_five_ls12_fill

        label when_run_five_twelve:
            scene lesson_5_12_run
            Tech "See the difference? Also Changing the {b}aspect ratio{/b} between width and height will distort the image."
            jump lessonFiveFillThirteen


    label lessonFiveFillThirteen:
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech "When only one of the 2 attributes is given, the web browser will calculate the other based on the {b}aspect ratio{/b} so the image is not stretched or squeezed"
        Tech "True or False? The aspect ratio of an image determines its rectangular shape."

        menu:
            "False":
                jump if_lfv13_wrong
            "True":
                show teacher_crossarm_happy
                Tech "You are correct"
                jump lessonFiveFillFourteen
 
        label if_lfv13_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillThirteen



    label lessonFiveFillFourteen:
        $ ls5_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech "Changing the {b}aspect ratio{/b} of an image causes distortion, which can look bad."
        Tech "Changing the aspect ration will result in image of what?"

        menu:
            "Black and white":
                jump if_lfv14_wrong
            "Stretched or squeeze":
                show teacher_crossarm_happy
                Tech "You are correct"
                jump lessonAttributeTakeaways
 
        label if_lfv14_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFourteen


    label lessonAttributeTakeaways:
        $ ls5_numc += 1
        scene lesson_attributes_takeaways
        Tech "In the next topic, you`ll create menus for your website with navigation links."
        jump lessonMenuIntro
    

    label lessonMenuIntro:
        scene lesson_menus_navigation
        Tech "In this topic, you`ll learn to help users to find what they`re looking for with navigation {b}links{/b}."
        jump lessonFiveFillFifteen

    
    label lessonFiveFillFifteen:
        $ ans_ffv_fft1_was_dropped = False
        $ ans_ffv_fft2_was_dropped = False
        $ ans_ffv_fft3_was_dropped = False
        scene l5f15

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillSixteen

        call screen lesson_five_ls15_fill

        label call_fv15:
            $ ans_ffv_fft1_was_dropped = False
            $ ans_ffv_fft2_was_dropped = False
            $ ans_ffv_fft3_was_dropped = False
            call screen lesson_five_ls15_fill
        
        label if_lfv15_wrong:
            scene l5f15
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls15_fill

        
    label lessonFiveFillSixteen:
        $ ls5_numc += 1
        $ ans_ffv_sixt1_was_dropped = False
        $ ans_ffv_sixt2_was_dropped = False
        scene l5f16

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillSeventeen

        call screen lesson_five_ls16_fill

        label call_fv16:
            $ ans_ffv_sixt1_was_dropped = False
            $ ans_ffv_sixt2_was_dropped = False
            call screen lesson_five_ls16_fill
        
        label if_lfv16_wrong:
            scene l5f16
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls16_fill

    
    label lessonFiveFillSeventeen:
        $ ls5_numc += 1
        $ ans_ffv_sevt1_was_dropped = False
        scene l5f17
        Tech "The {b}<nav>{/b} container tag defines a set of links that allows the user to navigate between pages of a website."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillEighteen

        call screen lesson_five_ls17_fill

        label call_fv17:
            $ ans_ffv_sevt1_was_dropped = False
            call screen lesson_five_ls17_fill
        
        label if_lfv17_wrong:
            scene l5f17
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls17_fill

    
    label lessonFiveFillEighteen:
        $ ls5_numc += 1
        $ ans_ffv_eght1_was_dropped = False
        $ ans_ffv_eght2_was_dropped = False
        $ ans_ffv_eght3_was_dropped = False
        $ ans_ffv_eght4_was_dropped = False
        scene l5f18
        Tech "Links to the different pages are added with the anchor tag <a> and nested inside the <nav> container tag."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillNineteen

        call screen lesson_five_ls18_fill

        label call_fv18:
            $ ans_ffv_eght1_was_dropped = False
            $ ans_ffv_eght2_was_dropped = False
            $ ans_ffv_eght3_was_dropped = False
            $ ans_ffv_eght4_was_dropped = False
            call screen lesson_five_ls18_fill
        
        label if_lfv18_wrong:
            scene l5f18
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls18_fill


    label lessonFiveFillNineteen:
        $ ls5_numc += 1
        $ ans_ffv_nnt1_was_dropped = False
        scene l5f19
        Tech "The HTML project for a multi-page website is made of different HTML documents (or files)."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillTwenty

        call screen lesson_five_ls19_fill

        label call_fv19:
            $ ans_ffv_nnt1_was_dropped = False
            call screen lesson_five_ls19_fill
        
        label if_lfv19_wrong:
            scene l5f19
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls19_fill


    label lessonFiveFillTwenty:
        $ ls5_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_happy
        Tech "HTML documents must be saved with the right {b}file extension{/b} (file type) for web browsers to recognize them."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech "What do you think is the file extension for an HTML document?"

        menu:
            ".pdf":
                jump if_lfv20_wrong
            ".html":
                Tech "You are correct"
                jump lessonFiveFillTwentyOne
 
        label if_lfv20_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillTwenty


    label lessonFiveFillTwentyOne:
        $ ls5_numc += 1
        scene l5f21
        Tech "Run the code to see what the web browser will display"
        call screen lesson_five_ls21_fill

        label when_run_five_twentyone:
            scene lesson_5_21_run
            Tech "Clicking the link will take you to the their respective pages, also you need to provide the content for the other two HTML documents."
            jump lessonFiveFillTwentyTwo


    label lessonFiveFillTwentyTwo:
        scene lesson_5_22
        Tech "It`s best practice to name your homepage index.html so that the web browser can find and load it."
        jump lessonFiveFillTwentyThree

    
    label lessonFiveFillTwentyThree:
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech "How many HTML documents(or files) will the project of a single-page website contain?"

        menu:
            "1":
                show teacher_crossarm_happy
                Tech "You are correct"
                jump lessonFiveFillTwentyFour
            "As many files as the number of sections":
                jump if_lfv23_wrong
            "2":
                jump if_lfv23_wrong
 
        label if_lfv23_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillTwentyThree


    label lessonFiveFillTwentyFour:
        $ ls5_numc += 1
        $ ans_ffv_twtf1_was_dropped = False
        scene l5f24
        Tech "To jump to a specific part of a single-page website, first you need to mark the section with the {b}id (ID){/b} attribute."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillTwentyFive

        call screen lesson_five_ls24_fill

        label call_fv24:
            $ ans_ffv_twtf1_was_dropped = False
            call screen lesson_five_ls24_fill
        
        label if_lfv24_wrong:
            scene l5f24
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls24_fill


    label lessonFiveFillTwentyFive:
        $ ls5_numc += 1
        $ ans_ffv_twtfv1_was_dropped = False
        $ ans_ffv_twtfv2_was_dropped = False
        scene l5f25
        Tech "The {b}id{/b} attribute is used to identify the element you want to target with the navigation link."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillTwentySeven

        call screen lesson_five_ls25_fill

        label call_fv25:
            $ ans_ffv_twtfv1_was_dropped = False
            $ ans_ffv_twtfv2_was_dropped = False
            call screen lesson_five_ls25_fill
        
        label if_lfv25_wrong:
            scene l5f25
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls25_fill

        
    
    label lessonFiveFillTwentySeven:
        $ ls5_numc += 1
        $ ans_ffv_twtsv1_was_dropped = False
        $ ans_ffv_twtsv2_was_dropped = False
        scene l5f27

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillTwentyEight


        call screen lesson_five_ls27_fill

        label call_fv27:
            $ ans_ffv_twtsv1_was_dropped = False
            $ ans_ffv_twtsv2_was_dropped = False
            call screen lesson_five_ls27_fill
        
        label if_lfv27_wrong:
            scene l5f27
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls27_fill


    label lessonFiveFillTwentyEight:
        $ ls5_numhc += 1
        scene lesson_5_28
        jump lessonMenuTakeaways

    
    label lessonMenuTakeaways:
        scene lesson_menus_takeaways
        jump lessonForm


    label lessonForm:
        scene lesson_forms
        Tech "You can use forms to let your visitors: "
        Tech " get in contact with you "
        Tech " send orders, requests and other information "  
        Tech " create an account or register and much more"
        jump lessonFiveFillTwentyNine


    label lessonFiveFillTwentyNine:
        $ ans_ffv_twtn1_was_dropped = False
        scene l5f29
        Tech "Forms are made of input elements like text fields, checkboxes, and submit buttons. These input elements are nested inside the <form> container tag."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillThirty


        call screen lesson_five_ls29_fill

        label call_fv29:
            $ ans_ffv_twtn1_was_dropped = False
            call screen lesson_five_ls29_fill
        
        label if_lfv29_wrong:
            scene l5f29
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls29_fill        


    label lessonFiveFillThirty:
        $ ls5_numc += 1
        scene l5f30
        Tech "Run the code to see what the web browser will display"
        call screen lesson_five_ls30_fill

        label when_run_five_thirty:
            scene lesson_5_30_run
            Tech "The most common form element is <input>. There are many forms of <input> element, depending on the type attribute."
            Tech "input could be text, radio, or checkbox"
            jump lessonFiveFillThirtyone


    label lessonFiveFillThirtyone:
        scene l5f31
        Tech "Run the code to see what the web browser will display"
        call screen lesson_five_ls31_fill

        label when_run_five_thirtyone:
            scene lesson_5_31_run
            Tech "Form elements will be displayed in the same line unless we use the {b}<br> (line break) tag{/b}."
            jump lessonFiveFillThirtytwo


    label lessonFiveFillThirtytwo:
        $ ans_ffv_thtt1_was_dropped = False
        $ ans_ffv_thtt2_was_dropped = False
        scene l5f32
        Tech"Labels can be added for the different input elements with the {b}<label> tag{/b}."
        Tech "Also remember that labels and inputs are inline elements, meaning they will not start on a new line"
        Tech "You will have to use <br> so it doesnt end up on the same line"
        call screen lesson_five_ls32_fill

        label call_fv32:
            $ ans_ffv_thtt1_was_dropped = False
            $ ans_ffv_thtt2_was_dropped = False
            call screen lesson_five_ls32_fill
        
        label if_lfv32_wrong:
            scene l5f32
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls32_fill    



    label lessonFiveFillThirtythree:
        $ ls5_numc += 1
        scene l5f33
        Tech" Run the code to see what the web browser will display"
        call screen lesson_five_ls33_fill

        label when_run_five_thirtythree:
            scene lesson_5_33_run
            Tech "As you can see we use <br> tag to separate the labels and inputs that accords to its input form"
            Tech "Next with paragraph tag"
            jump lessonFiveFillThirtyfour


    label lessonFiveFillThirtyfour:
        scene l5f34
        Tech "Run the code to see what the web browser will display"
        call screen lesson_five_ls34_fill

        label when_run_five_thirtyfour:
            scene lesson_5_34_run
            Tech "It's considered a very good practice to connect the label to the input elements with the use of {b}for{/b} and {b}id{/b} attributes."
            jump lessonFiveFillThirtyfive


    label lessonFiveFillThirtyfive:
        $ ans_ffv_thtfv1_was_dropped = False
        scene l5f35
        Tech "The {b}id{/b} attribute is used to identify a unique input element. The {b}for{/b} attribute in a label targets (and matches!) an input`s id. "

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillThirtysix

        call screen lesson_five_ls35_fill

        label call_fv35:
            $ ans_ffv_thtfv1_was_dropped = False
            call screen lesson_five_ls35_fill
        
        label if_lfv35_wrong:
            scene l5f35
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls35_fill 


    label lessonFiveFillThirtysix:
        $ ls5_numc += 1
        $ ans_ffv_thtsx1_was_dropped = False
        $ ans_ffv_thtsx2_was_dropped = False
        scene l5f36
        Tech "To connect labels and inputs, their {b}id{/b} and {b}for{/b} attribute values must match up exactly."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillThirtynine

        call screen lesson_five_ls36_fill

        label call_fv36:
            $ ans_ffv_thtsx1_was_dropped = False
            $ ans_ffv_thtsx2_was_dropped = False
            call screen lesson_five_ls36_fill
        
        label if_lfv36_wrong:
            scene l5f36
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls36_fill


    label lessonFiveFillThirtynine:
        $ ls5_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_happy
        Tech"The {b}id{/b} attribute is used to identify unique elements in an HTML document."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech"True or False? You can give multiple elements to the same id in one HTML document"

        menu:
            "False":
                show teacher_crossarm_happy
                Tech"You are correct"
                jump lessonFiveFillFourty
            "True":
                jump if_lfv39_wrong
 
        label if_lfv39_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            jump lessonFiveFillThirtynine


    label lessonFiveFillFourty:
        $ ls5_numc += 1
        scene lesson_5_40 
        Tech"There's something wrong with the form code. Can you identify it?"

        menu:
            "missing id attributes":
                Tech "You are correct"
                jump lessonFiveFillFourtyone
            "labels should appear before the inputs":
                jump if_lfv40_wrong
            "<label> is an empty tag":
                jump if_lfv40_wrong
 
        label if_lfv40_wrong:
            Tech "incorrect"
            jump lessonFiveFillFourty


    label lessonFiveFillFourtyone:
        $ ls5_numc += 1
        $ ans_ffv_ftyo1_was_dropped = False
        $ ans_ffv_ftyo2_was_dropped = False
        $ ans_ffv_ftyo3_was_dropped = False
        $ ans_ffv_ftyo4_was_dropped = False
        scene l5f41

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillFourtytwo


        call screen lesson_five_ls41_fill

        label call_fv41:
            $ ans_ffv_ftyo1_was_dropped = False
            $ ans_ffv_ftyo2_was_dropped = False
            $ ans_ffv_ftyo3_was_dropped = False
            $ ans_ffv_ftyo4_was_dropped = False
            call screen lesson_five_ls41_fill
        
        label if_lfv41_wrong:
            scene l5f41
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls41_fill


    label lessonFiveFillFourtytwo:
        $ ls5_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech"When labels and form fields are correctly connected... The what?"

        menu:
            "label and form fields are displayed on the same line":
                jump if_lfv42_wrong
            "label and form fields are displayed in the same color":
                jump if_lfv42_wrong
            "hitting the label selects the form field":
                show teacher_crossarm_happy
                Tech"You are correct"
                jump lessonFormtakeaways
 
        label if_lfv42_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFourtytwo


    label lessonFormtakeaways:
        $ ls5_numc += 1
        scene lesson_form_takeaways
        Tech"In the next lesson, you'll take your web form skills to the next level."
    
    label lessonFormSubmit:
        scene lesson_form_submit
        Tech"In this lesson, you`ll learn to submit form data."
        jump lessonFiveFillFourtythree
    

    label lessonFiveFillFourtythree:
        scene lesson_5_43 
        Tech"What will the browser display?"

        menu:
            "A table":
                jump if_lfv43_wrong
            "A form with two input field":
                Tech"You are correct"
                jump lessonFiveFillFourtyfour
 
        label if_lfv43_wrong:
            Tech"incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFourtythree


    label lessonFiveFillFourtyfour:
        $ ls5_numc += 1
        $ ans_ffv_ftyfr1_was_dropped = False
        $ ans_ffv_ftyfr2_was_dropped = False
        scene l5f44
        Tech "A {b}submit{/b} button is used to send the data in a form. The {b}submit{/b} type of input adds a button to the form."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillFourtyfive

        call screen lesson_five_ls44_fill

        label call_fv44:
            $ ans_ffv_ftyfr1_was_dropped = False
            $ ans_ffv_ftyfr2_was_dropped = False
            call screen lesson_five_ls44_fill
        
        label if_lfv44_wrong:
            scene l5f44
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls44_fill


    label lessonFiveFillFourtyfive:
        $ ls5_numc += 1
        scene lesson_8_22 
        show teacher_crossarm_smile
        Tech"You can use the {b}submit{/b} input to send the data in the form to a database hosted in a server."
        Tech"Do you remember what a server is?"


        menu:
            "A computer that is always connected to the internet and listening for request informations":
                show teacher_crossarm_happy
                Tech "You are correct"
                jump lessonFiveFillFourtysix
            "The device that is being used to access the web":
                jump if_lfv45_wrong
 
        label if_lfv45_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFourtyfive


    label lessonFiveFillFourtysix:
        $ ls5_numc += 1
        $ ans_ffv_ftysix1_was_dropped = False
        $ ans_ffv_ftysix2_was_dropped = False
        scene l5f46
        Tech "The {b}name{/b} attribute is used to reference the data after submitting the form "

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillFourtyseven

        call screen lesson_five_ls46_fill

        label call_fv46:
            $ ans_ffv_ftysix1_was_dropped = False
            $ ans_ffv_ftysix2_was_dropped = False
            call screen lesson_five_ls46_fill
        
        label if_lfv46_wrong:
            scene l5f46
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls46_fill



    label lessonFiveFillFourtyseven:
        $ ls5_numc += 1
        scene lesson_5_47
        Tech "Only form elements with a name attribute will have their values passed to the database when submitting a form."
        jump lessonFiveFillFourtyeight


    label lessonFiveFillFourtyeight:
        scene lesson_5_48 
        Tech "Where will the text entered by the user in the second field go?"

        menu:
            'to the "email" field (column) in the database':
                jump if_lfv48_wrong
            'to the "city" field (column) in the database':
                Tech "you are correct"
                jump lessonFiveFillFourtynine
 
        label if_lfv48_wrong:
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFourtyeight


    label lessonFiveFillFourtynine:
        $ ls5_numc += 1
        scene lesson_5_49 
        Tech "The form above will not send data to the database when submitted. Why?"

        menu:
            'submit button is missing':
                jump if_lfv49_wrong
            'input fields don’t have names':
                Tech "you are correct"
                jump lessonFiveFillFifty
 
        label if_lfv49_wrong:
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFourtynine


    label lessonFiveFillFifty:
        $ ls5_numc += 1
        scene lesson_5_50 
        Tech "The name attribute is used to put the input from the user in the correct field (column) in the database."
        Tech "Name attributes need to be added to what?"

        menu:
            'label':
                jump if_lfv50_wrong
            'input fields':
                Tech"you are correct"
                jump lessonFiveFillFiftyone
 
        label if_lfv50_wrong:
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFifty

    label lessonFiveFillFiftyone:
        $ ls5_numc += 1
        $ ans_ffv_ffyo1_was_dropped = False
        $ ans_ffv_ffyo2_was_dropped = False
        scene l5f51
        Tech "Remember labels and input fields need to be correctly paired"

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillFiftytwo

        call screen lesson_five_ls51_fill

        label call_fv51:
            $ ans_ffv_ffyo1_was_dropped = False
            $ ans_ffv_ffyo2_was_dropped = False
            call screen lesson_five_ls51_fill
        
        label if_lfv51_wrong:
            scene l5f51
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls51_fill


    label lessonFiveFillFiftytwo:
        $ ls5_numc += 1
        scene lesson_5_52 
        Tech "How will the email field be referenced in the database?"

        menu:
            "co":
                jump if_lfv52_wrong
            "em":
                Tech "You are correct"
                jump lessonFiveFillFiftythree
            "email":
                jump if_lfv52_wrong
 
        label if_lfv52_wrong:
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFiftytwo


    label lessonFiveFillFiftythree:
        $ ls5_numc += 1
        $ ans_ffv_ffyth1_was_dropped = False
        $ ans_ffv_ffyth2_was_dropped = False
        scene l5f53
        Tech "Names and values are needed to correctly store information in the database. The HTML code needs to include where and what to put in the database."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonFiveFillFiftyfour

        call screen lesson_five_ls53_fill

        label call_fv53:
            $ ans_ffv_ffyth1_was_dropped = False
            $ ans_ffv_ffyth2_was_dropped = False
            call screen lesson_five_ls53_fill
        
        label if_lfv53_wrong:
            scene l5f53
            Tech "Try again"
            $ ls5_numic += 1
            call screen lesson_five_ls53_fill


    label lessonFiveFillFiftyfour:
        $ ls5_numc += 1
        scene lesson_5_54 
        Tech "What will this form send to the database when the second radio button is selected?"

        menu:
            'label':
                jump if_lfv54_wrong
            'cash':
                jump if_lfv54_wrong
            'card':
                Tech "you are correct"
                jump lessonFiveFillFiftyfive
            
 
        label if_lfv54_wrong:
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFiftyfour


    label lessonFiveFillFiftyfive:
        $ ls5_numc += 1
        scene lesson_5_55 
        Tech "Where will the users’ choice of payment method be stored in the database?"

        menu:
            'field (column) named "cash"':
                e "you are correct"
                jump lessonFiveFillFiftysix
            'field (column) named "radio"':
                jump if_lfv55_wrong
            'field (column) named "pay"':
                jump if_lfv55_wrong
            
 
        label if_lfv55_wrong:
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFiftyfive


    label lessonFiveFillFiftysix:
        $ ls5_numc += 1
        scene l5f56
        Tech "For the case of text inputs, you can use the value attribute to define a default value that will be submitted unless a different value is provided by the user."
        Tech "Run the code to see what the web browser will display"
        call screen lesson_five_ls56_fill

        label when_run_five_fiftysix:
            scene lesson_5_56_run
            Tech "Well done"
            jump lessonFiveFillFiftyseven


    label lessonFiveFillFiftyseven:
        scene lesson_5_57 
        Tech "The {b}value{/b} in the text input above will be sent to the database?"

        menu:
            'only when the user doesn’t provide a different value':
                Tech "you are correct"
                jump lessonFormSubmitTakeaways
            'always':
                jump if_lfv57_wrong
            
 
        label if_lfv57_wrong:
            Tech "incorrect"
            $ ls5_numic += 1
            jump lessonFiveFillFiftyseven


    label lessonFormSubmitTakeaways:
        $ ls5_numc += 1
        scene lesson_submit_takeaways
        Tech "Bravo! Your coding skills are reaching new heights. Keep exploring, and may your web development adventures continue to thrive!"


    stop music fadeout 1.0
    
    play music "audio/quiz.mp3" volume 0.5


    

    $ persistent.ast2_participation += 25
    label skipped_l5:

    e "Let's Start the Quiz 5"
    jump start_quiz_04

    label pagtapos_ng_quiz_4:

    $ persistent.lesson_5_quiz5 = persistent_quiz_04_q_counter_correct_answer
    
    
    Tech "Great job on the quiz, class! You all did fantastic."

    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting project related to what you've just learned."
    jump l5_act5
    label pagtapos_ng_act_5:









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

   


    $ persistent.chp_five_date_taken = persistent.date_today
    $ persistent.chp_five_time = persistent.formatted_time





    label chp_five_end:
        #$ persistent.f_numhc += ls5_numhc
        #$ persistent.f_numc += ls5_numc
        #$ persistent.f_numic += ls5_numic
        $ save_total_run()
        $ reset_timer()
        #call screen chp_five_assessment()
        
        


    ######### Time save ######################################

    stop music fadeout 1.0
    #jump behavior_five
    label chp_five_ending:
        #$ persistent.chp_prev_five_time = persistent.chp_five_time
        #$ persistent.chp_five_prev_score = persistent_quiz_04_q_counter_correct_answer
        #$ persistent.chp_five_prev_date = persistent.date_today
        scene bg_5
        blank "End of chapter 5"


    $ lesson_five_finish = True
    call screen lesson_ui



    return


