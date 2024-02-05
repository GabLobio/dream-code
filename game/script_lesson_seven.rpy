









label lesson_seven:
    $ persistent.q2_previous_overall_grade = persistent.q2_overall_grade
    $ persistent.rude_lesson = "seven"


    scene bg_classroom
    if lesson_six_finish:
        jump lessonPageIntro
    else:
        Tech "Please finish lesson 6"
        call screen lesson_ui

    $ persistent.ast3_kindness = 10
    $ persistent.ast3_rudeness = 10
    $ persistent.ast3_recitation = 5
    $ persistent.ast3_participation = 5
    $ persistent.ast3_accuracy = 5

    $ persistent.lesson_7_quiz7 = 0
    $ persistent.lesson_7_act7 = 0

    label lessonPageIntro:

        $ show_quick_menu = False
        play music "audio/sa_tech.mp3" volume 0.5


        scene lesson_page_intro
        Tech "In this lesson, you`ll learn to apply a layout to your web pages."
        Tech "Read the lesson plan for 7 to 9"
        call screen lesson_plan_q3
        jump lessonSevenFillOne


    label lessonSevenFillOne:
        $ ans_fsv_o1_was_dropped = False
        $ ans_fsv_o2_was_dropped = False
        $ ans_fsv_o3_was_dropped = False
        scene l7f1
        Tech "The body of a web page can be divided into 3 parts."
        call screen lesson_seven_ls1_fill

        label call_sv1:
            $ ans_fsv_o1_was_dropped = False
            $ ans_fsv_o2_was_dropped = False
            $ ans_fsv_o3_was_dropped = False
            call screen lesson_seven_ls1_fill
        
        label if_lsv1_wrong:
            scene l7f1
            Tech "Try again"
            call screen lesson_seven_ls1_fill


    label lessonSevenFillTwo:
        $ ans_fsv_t1_was_dropped = False
        scene l7f2
        Tech"The {b}<header>{/b} container tag usually contains introductory information."
        Tech"You can add several header elements to a web page."
        call screen lesson_seven_ls2_fill

        label call_sv2:
            $ ans_fsv_t1_was_dropped = False
            call screen lesson_seven_ls2_fill
        
        label if_lsv2_wrong:
            scene l7f2
            Tech"Try again"
            call screen lesson_seven_ls2_fill


    label lessonSevenFillThree:
        $ ans_fsv_thr1_was_dropped = False
        $ ans_fsv_thr2_was_dropped = False
        scene l7f3 
        Tech"The {b}header{/b} often contains navigation links, a menu and/or a search bar. Brand elements like logos are usually found in the header too."

        label l7Int7:
            menu:
                "Talk to classmate":
                    jump start_hitting_teach3
                    label opsl7_1:
                        $ persistent.ast3_rudeness += 50
                        jump skipped_l7
                "Play with your classmate":
                    jump begin_ho_mg7
                    label opsl7_2:
                        $ persistent.ast3_rudeness += 50
                        jump skipped_l7
                "Raise Hand":
                    pass
                "Ignore":
                    jump lessonSevenFillFour

        call screen lesson_seven_ls3_fill

        label call_sv3:
            $ ans_fsv_thr1_was_dropped = False
            $ ans_fsv_thr2_was_dropped = False
            call screen lesson_seven_ls3_fill
        
        label if_lsv3_wrong:
            scene l7f3
            Tech"Try again"
            call screen lesson_seven_ls3_fill


    label lessonSevenFillFour:
        $ ans_fsv_fr1_was_dropped = False
        $ ans_fsv_fr2_was_dropped = False
        scene l7f4
        Tech"The {b}<main>{/b} container tag is used to include the main content of a web page."
        Tech"There must not be more than one {b}<main>{/b} element in a document."
        call screen lesson_seven_ls4_fill

        label call_sv4:
            $ ans_fsv_fr1_was_dropped = False
            $ ans_fsv_fr2_was_dropped = False
            call screen lesson_seven_ls4_fill
        
        label if_lsv4_wrong:
            scene l7f4
            Tech"Try again"
            call screen lesson_seven_ls4_fill


    label lessonSevenFillFive:
        $ ans_fsv_fv1_was_dropped = False
        scene l7f5
        Tech"The {b}<footer>{/b} container tag often contains contact and legal information and links."
        Tech"You can have several {b}<footer>{/b} elements in one document."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSevenFillSix

        call screen lesson_seven_ls5_fill

        label call_sv5:
            $ ans_fsv_fv1_was_dropped = False
            call screen lesson_seven_ls5_fill
        
        label if_lsv5_wrong:
            scene l7f5
            Tech"Try again"
            call screen lesson_seven_ls5_fill


    label lessonSevenFillSix:
        scene lesson_7_6
        Tech"{b}<header>{/b}, {b}<main>{/b} and {b}<footer>{/b} elements are nested inside the <body> container tag"
        jump lessonSevenFillSeven


    label lessonSevenFillSeven:
        scene lesson_7_7 
        show teacher_crossarm_happy
        Tech"New web designers and developers often confuse <header> with other HTML elements. Let`s practice a bit."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech"Which  elements must be nested inside {b}<body>{/b}?"

        label choices_fs:
        menu:
            "<head>":
                jump if_lsv7_wrong
            "<header>":
                show teacher_crossarm_happy
                Tech"You are correct"
                jump lessonSevenFillEight
 
        label if_lsv7_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            hide teacher_crossarm_sad
            jump lessonSevenFillSeven


    label lessonSevenFillEight:
        scene lesson_7_7 
        show teacher_crossarm_happy
        e "Which of the following elements is used to include technical information about the page like title, description, author and keywords?"

        label choices_fe:
        menu:
            "<header>":
                jump if_lsv8_wrong
            "<head>":
                show teacher_crossarm_happy
                Tech"You are correct"
                jump lessonSevenFillNine
 
        label if_lsv8_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            jump choices_fe


    label lessonSevenFillNine:
        scene lesson_7_7 
        show teacher_crossarm_smile
        e "Which of the following elements is {b}not{/b} shown to the visitor by the web browser?"

        label choices_fn:
        menu:
            "<header>":
                jump if_lsv9_wrong
            "<head>":
                show teacher_crossarm_happy
                Tech"You are correct"
                jump lessonSevenFillTen
 
        label if_lsv9_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            jump choices_fn


    label lessonSevenFillTen:
        $ ans_fsv_ten1_was_dropped = False
        $ ans_fsv_ten2_was_dropped = False
        $ ans_fsv_ten3_was_dropped = False
        scene l7f10 

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSevenFillEleven
        
        # Classmate Confused Interaction
        blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."
        # Dialogue to nung kaklaseng nyang boy
        "Hey, mind lending a hand? I'm a bit lost with some of the words the teacher just used. Could you help me catch up on what I missed? I'd appreciate it, and maybe we can quickly go through it together so we don't fall too behind."

        menu:
            "Talk to him":
                blank "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
                $ persistent.ast3_kindness = 50
                jump lessonSevenFillFifteen
            "Refuse and explain that you can teach him later; choose to focus on the current lesson":
                blank "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
                $ persistent.ast3_kindness = 50
                pass

        call screen lesson_seven_ls10_fill

        label call_sv10:
            $ ans_fsv_ten1_was_dropped = False
            $ ans_fsv_ten2_was_dropped = False
            $ ans_fsv_ten3_was_dropped = False
            call screen lesson_seven_ls10_fill
        
        label if_lsv10_wrong:
            scene l7f10
            Tech"Try again"
            call screen lesson_seven_ls10_fill


    label lessonSevenFillEleven:
        scene lesson_7_7 
        show teacher_crossarm_smile
        e 'Where would you add a "back to top of the page" link?'

        label choices_fel:
        menu:
            "<header>":
                jump if_lsv11_wrong
            "<footer>":
                show teacher_crossarm_happy
                Tech"You are correct"
                jump lessonSevenFillThirteen
            "<head>":
                jump if_lsv11_wrong

        label if_lsv11_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            jump choices_fel


    label lessonSevenFillThirteen:
        scene lesson_page_takeaways
        Tech "In the next lesson, you`ll dive deeper into page layout and structure."


    label lessonLayoutIntro:
        scene lesson_layout_intro 
        Tech "In this lesson, you`ll learn to structure web pages with layouts that improve accessibility and make the content easier to understand for both search engines and users."


    label lessonSevenFillFourteen:
        $ ans_fsv_ft1_was_dropped = False
        scene l7f14
        Tech "{b}<article>{/b} represents an independent, self-contained piece of content."
        call screen lesson_seven_ls14_fill

        label call_sv14:
            $ ans_fsv_ft1_was_dropped = False
            call screen lesson_seven_ls14_fill
        
        label if_lsv14_wrong:
            scene l7f14
            Tech "Try again"
            call screen lesson_seven_ls14_fill


    label lessonSevenFillFifteen:
        $ ans_fsv_fft1_was_dropped = False
        $ ans_fsv_fft2_was_dropped = False
        scene l7f15 
        Tech "An article is content that would make sense on its own."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSevenFillSixteen

        call screen lesson_seven_ls15_fill

        label call_sv15:
            $ ans_fsv_fft1_was_dropped = False
            $ ans_fsv_fft2_was_dropped = False
            call screen lesson_seven_ls15_fill
        
        label if_lsv15_wrong:
            scene l7f15
            Tech "Try again"
            call screen lesson_seven_ls15_fill


    label lessonSevenFillSixteen:
        scene lesson_7_7 
        show teacher_crossarm_happy
        e 'The {b}<article> tag{/b} clearly indicates the role for its content. It`s used for content like news stories, and blog posts.'
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech "So <article> is an example of…"

        label choices_fst:
        menu:
            "an empty tag":
                jump if_lsv16_wrong
            "a semantic tag":
                show teacher_crossarm_happy
                e "You are correct"
                jump lessonSevenFillSeventeen

        label if_lsv16_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            jump choices_fst


    label lessonSevenFillSeventeen:
        scene lesson_7_7 
        show teacher_crossarm_smile
        Tech "Layout tags like {b}<header>{/b}, {b}<main>{/b}, {b}<footer>{/b} and {b}<article>{/b} are semantic tags because they…"

        label choices_fsvt:
        menu:
            "use angle brackets <>":
                jump if_lsv17_wrong
            "give information about what they contain":
                show teacher_crossarm_happy
                Tech "You are correct"
                jump lessonSevenFillEighteen

        label if_lsv17_wrong:
            show teacher_crossarm_sad
            Tech "incorrect"
            jump choices_fsvt


    label lessonSevenFillEighteen:
        $ ans_fsv_et1_was_dropped = False
        scene l7f18 
        Tech "{b}<section>{/b} helps to break down the content into parts."
        call screen lesson_seven_ls18_fill

        label call_sv18:
            $ ans_fsv_et1_was_dropped = False
            call screen lesson_seven_ls18_fill
        
        label if_lsv18_wrong:
            scene l7f18
            Tech "Try again"
            call screen lesson_seven_ls18_fill


    label lessonSevenFillNineteen:
        $ ans_fsv_nt1_was_dropped = False
        $ ans_fsv_nt2_was_dropped = False
        scene l7f19 
        Tech "{b}<section>{/b} helps to break down the content into parts."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSevenFillTwenty

        call screen lesson_seven_ls19_fill

        label call_sv19:
            $ ans_fsv_nt1_was_dropped = False
            $ ans_fsv_nt2_was_dropped = False
            call screen lesson_seven_ls19_fill
        
        label if_lsv19_wrong:
            scene l7f19
            Tech "Try again"
            call screen lesson_seven_ls19_fill


    label lessonSevenFillTwenty:
        scene lesson_7_7 
        show teacher_crossarm_smile
        Tech"A web page could be split into separate sections for introduction, contact information, etc."
        Tech"{b}<section>{/b} is…"

        label choices_ftwt:
        menu:
            "an empty tag":
                jump if_lsv20_wrong
            "a container tag":
                show teacher_crossarm_happy
                Tech "You are correct"
                jump lessonSevenFillTwentyone

        label if_lsv20_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            jump choices_ftwt


    label lessonSevenFillTwentyone:
        scene lesson_7_7 
        show teacher_crossarm_happy
        Tech"{b}<section>{/b} can be used to separate each chapter, news item, etc."
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech"{b}<section>{/b} is a…"

        label choices_ftwto:
        menu:
            "non-semantic tag":
                show teacher_crossarm_happy
                Tech"You are correct"
                jump lessonSevenFillTwentytwo
            "semantic tag":
                jump if_lsv21_wrong

        label if_lsv21_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            jump choices_ftwto


    label lessonSevenFillTwentytwo:
        $ ans_fsv_twtt1_was_dropped = False
        $ ans_fsv_twtt2_was_dropped = False
        scene l7f22
        Tech"{b}<aside>{/b} is used for secondary, additional or somehow related content."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSevenFillTwentythree

        call screen lesson_seven_ls22_fill

        label call_sv22:
            $ ans_fsv_twtt1_was_dropped = False
            $ ans_fsv_twtt2_was_dropped = False
            call screen lesson_seven_ls22_fill
        
        label if_lsv22_wrong:
            scene l7f22
            Tech "Try again"
            call screen lesson_seven_ls22_fill


    label lessonSevenFillTwentythree:
        scene lesson_7_23
        Tech"You can combine these elements to create a well-structured semantic layout for your content."
        jump lessonSevenFillTwentyfour


    label lessonSevenFillTwentyfour:
        scene lesson_7_7 
        show teacher_crossarm_smile
        Tech"Which element should be used to divide a story into chapters?"

        label choices_ftwfr:
        menu:
            "<article>":
                jump if_lsv24_wrong
            "<section>":
                show teacher_crossarm_happy
                e "You are correct"
                jump lessonSevenFillTwentyfive
            "<main>":
                jump if_lsv24_wrong

        label if_lsv24_wrong:
            show teacher_crossarm_sad
            Tech"incorrect"
            jump choices_ftwfr


    label lessonSevenFillTwentyfive:
        scene lesson_7_23
        Tech "Semantic tags don`t give any visual effect to the content. You can nest layout elements to create organized and accessible pages."
        jump lessonSevenFillTwentysix


    label lessonSevenFillTwentysix:
        scene lesson_7_7 
        show teacher_crossarm_smile
        Tech "What would you use <article> for?"

        label choices_ftwsx:
        menu:
            "Today`s news brief":
                show teacher_crossarm_happy
                Tech "You are correct"
                jump lessonSevenFillTwentyseven
            "Navigation menu":
                jump if_lsv26_wrong
            "Sidebar":
                jump if_lsv26_wrong

        label if_lsv26_wrong:
            show teacher_crossarm_sad
            e "incorrect"
            jump choices_ftwsx



    label lessonSevenFillTwentyseven:
        $ ans_fsv_twts1_was_dropped = False
        $ ans_fsv_twts2_was_dropped = False
        $ ans_fsv_twts3_was_dropped = False

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonLayoutTakeaways

        call screen lesson_seven_ls27_fill

        label call_sv27:
            $ ans_fsv_twts1_was_dropped = False
            $ ans_fsv_twts2_was_dropped = False
            $ ans_fsv_twts3_was_dropped = False
            call screen lesson_seven_ls27_fill
        
        label if_lsv27_wrong:
            scene l7f27
            Tech"Try again"
            call screen lesson_seven_ls27_fill


    label lessonLayoutTakeaways:
        scene lesson_layout_takeaways
        Tech"Take the next lesson to learn even more layout skills."

    stop music fadeout 1.0
    
    play music "audio/quiz.mp3" volume 0.5

    $ persistent.ast3_participation += 50
    label skipped_l7:

    jump start_quiz_06

    label pagtapos_ng_quiz_6:

    $ persistent.lesson_7_quiz7 = persistent_quiz_06_q_counter_correct_answer
    
    Tech "Great job on the quiz, class! You all did fantastic."

    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting project related to what you've just learned."
    jump l7_act7
    label pagtapos_ng_act_7:

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

    
    scene bg_7
    blank "End of chapter 7"




    $ lesson_seven_finish = True
    call screen lesson_ui






    return