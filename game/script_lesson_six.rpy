







label lesson_six:
    scene bg_classroom
    $ persistent.rude_lesson = "six"




    if lesson_five_finish:
        jump lessonDropDownIntro
    else:
        Tech "Please finish lesson 5"
        call screen lesson_ui


    $ persistent.lesson_6_quiz6 = 0  # Written Works 10%
    $ persistent.lesson_6_act6 = 0  # Performance Task 10%

    label lessonDropDownIntro:

        $ show_quick_menu = False
        play music "audio/sa_tech.mp3" volume 0.5

        show lesson_drop_down_intro
        Tech "In this lesson, you`ll learn to add drop-down lists to your page."
        jump lessonSixFillZero
        

    label lessonSixFillZero:
        $ ans_fsx_o1_was_dropped = False
        scene l6f0
        call screen lesson_six_ls0_fill

        label call_sx0:
            $ ans_fsx_o1_was_dropped = False
            call screen lesson_six_ls0_fill
        
        label if_lsx0_wrong:
            scene l6f0
            Tech "Try again"
            call screen lesson_six_ls0_fill


    label lessonSixFillOne:
        $ ans_fsx_on1_was_dropped = False
        $ ans_fsx_on2_was_dropped = False
        $ ans_fsx_on3_was_dropped = False
        scene l6f1
        call screen lesson_six_ls1_fill

        label call_sx1:
            $ ans_fsx_on1_was_dropped = False
            $ ans_fsx_on2_was_dropped = False
            $ ans_fsx_on3_was_dropped = False
            call screen lesson_six_ls1_fill
        
        label if_lsx1_wrong:
            scene l6f1
            Tech "Try again"
            call screen lesson_six_ls1_fill


    label lessonSixFillTwo:
        $ ans_fsx_two1_was_dropped = False
        $ ans_fsx_two2_was_dropped = False
        $ ans_fsx_two3_was_dropped = False
        scene l6f2

        label l6Int6:
            menu:
                "Talk to classmate":
                    jump start_hitting_teach3
                    label opsl6_1:
                        $ persistent.ast1_rudeness += 50
                        jump skipped_l6
                "Play with your classmate":
                    jump begin_ho_mg6
                    label opsl6_2:
                        $ persistent.ast1_rudeness += 50
                        jump skipped_l6
                "Raise Hand":
                    pass
                "Ignore":
                    jump lessonSixFillThree

        call screen lesson_six_ls2_fill

        label call_sx2:
            $ ans_fsx_two1_was_dropped = False
            $ ans_fsx_two2_was_dropped = False
            $ ans_fsx_two3_was_dropped = False
            call screen lesson_six_ls2_fill
        
        label if_lsx2_wrong:
            scene l6f2
            Tech "Try again"
            call screen lesson_six_ls2_fill


    label lessonSixFillThree:
        $ ans_fsx_thr1_was_dropped = False
        scene l6f3
        Tech "Submitting a form sends information to a database. The {b}name{/b} attribute is needed to submit the form data."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillFour

        call screen lesson_six_ls3_fill

        label call_sx3:
            $ ans_fsx_thr1_was_dropped = False
            call screen lesson_six_ls3_fill
        
        label if_lsx3_wrong:
            scene l6f3
            Tech "Try again"
            call screen lesson_six_ls3_fill


    label lessonSixFillFour:
        scene lesson_6_4
        Tech "The name attribute is used to tell the database…"

        label begin_question_four:
        menu:
            "the value to be stored":
                jump if_lsx4_wrong
            "where to store the data":
                Tech "You are correct"
                jump lessonSixFillFive
 
        label if_lsx4_wrong:
            Tech "incorrect"
            jump begin_question_four


    label lessonSixFillFive:
        scene l6f5
        Tech "Data will be sent when the form is submitted. You can control the data each option sends with the {b}value{b} attribute."
        Tech "Run the code to see what will the code display"
        call screen lesson_six_ls5_fill

        label when_run_six_five:
            scene lesson_6_5_run
            Tech "You can also click the drop-down menu. See what are the options"
            call screen lesson_six_click

            label lesson_six_clicked:
                scene lesson_6_5_run_clicked
                Tech "Perfect now you can see the options"
                jump lessonSixFillSix


    label lessonSixFillSix:
        scene lesson_6_6 
        Tech "What will this form send to the database when the second option is selected?"

        label begin_question_six:
        menu:
            "Opt 2":
                jump if_lsx6_wrong
            "cat":
                jump if_lsx6_wrong
            "dog":
                Tech "You are correct"
                jump lessonSixFillSeven
 
        label if_lsx6_wrong:
            Tech "incorrect"
            jump begin_question_six


    label lessonSixFillSeven:
        scene lesson_6_7  
        Tech "Which of the options has been pre-selected?"

        label begin_question_seven:
        menu:
            "Red":
                jump if_lsx7_wrong
            "Blue":
                Tech "You are correct"
                jump lessonSixFillEight
 
        label if_lsx7_wrong:
            Tech "You are incorrect"
            jump begin_question_seven


    label lessonSixFillEight:
        $ ans_fsx_et1_was_dropped = False
        $ ans_fsx_et2_was_dropped = False
        scene l6f8
        Tech "Complete the code"

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillNine

        # Classmate Confused Interaction
        blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."
        # Dialogue to nung kaklaseng nyang boy
        "Hey, mind lending a hand? I'm a bit lost with some of the words the teacher just used. Could you help me catch up on what I missed? I'd appreciate it, and maybe we can quickly go through it together so we don't fall too behind."

        menu:
            "Talk to him":
                blank "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
                $ persistent.ast2_kindness = 25
                jump lessonSixFillTwelve
            "Refuse and explain that you can teach him later; choose to focus on the current lesson":
                blank "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
                $ persistent.ast2_kindness = 25
                pass

        call screen lesson_six_ls8_fill

        label call_sx8:
            $ ans_fsx_et1_was_dropped = False
            $ ans_fsx_et2_was_dropped = False
            call screen lesson_six_ls8_fill
        
        label if_lsx8_wrong:
            scene l6f8
            Tech "Try again"
            call screen lesson_six_ls8_fill


    label lessonSixFillNine:
        $ ans_fsx_nn1_was_dropped = False
        $ ans_fsx_nn2_was_dropped = False
        scene l6f9
        Tech "Labels and drop-down menus are connected with {b}for{/b} and {b}id{/b} attributes, just like any other form element."
        Tech "Correctly connecting labels and form fields will increase hit area and improve accessibility."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillTen

        call screen lesson_six_ls9_fill

        label call_sx9:
            $ ans_fsx_nn1_was_dropped = False
            $ ans_fsx_nn2_was_dropped = False
            call screen lesson_six_ls9_fill
        
        label if_lsx9_wrong:
            scene l6f9
            Tech "Try again"
            call screen lesson_six_ls9_fill


    label lessonSixFillTen:
        scene lesson_6_10  
        Tech "Do you rememeber it?"

        label begin_question_ten:
        menu:
            "label and form fields are displayed on the same line":
                jump if_lsx10_wrong
            "label and form fields are displayed in the same color":
                jump if_lsx10_wrong
            "hitting the label selects the form field":
                Tech "You are correct"
                jump lessonSixFillEleven
 
        label if_lsx10_wrong:
            Tech "incorrect"
            jump begin_question_ten


    label lessonSixFillEleven:
        scene lesson_6_11 
        Tech "Select the only {b}incorrect{/b} statement about the id attribute"

        label begin_question_eleven:
        menu:
            "You cannot have more than one element with the same id in an HTML document":
                jump if_lsx11_wrong
            "You can use the same id multiple times in an HTML document":
                Tech "You are correct"
                jump lessonSixFillTwelve
            "It`s used to give a unique id to an HTML element":
                e "You are correct"
                jump if_lsx11_wrong
 
        label if_lsx11_wrong:
            Tech "incorrect"
            jump begin_question_eleven


    label lessonSixFillTwelve:
        $ ans_fsx_twl1_was_dropped = False
        $ ans_fsx_twl2_was_dropped = False
        $ ans_fsx_twl3_was_dropped = False
        scene l6f12

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillThirteen

        call screen lesson_six_ls12_fill

        label call_sx12:
            $ ans_fsx_twl1_was_dropped = False
            $ ans_fsx_twl2_was_dropped = False
            $ ans_fsx_twl3_was_dropped = False
            call screen lesson_six_ls12_fill
        
        label if_lsx12_wrong:
            scene l6f12
            Tech "Try again"
            call screen lesson_six_ls12_fill


    label lessonSixFillThirteen:
        $ ans_fsx_tht1_was_dropped = False
        $ ans_fsx_tht2_was_dropped = False
        $ ans_fsx_tht3_was_dropped = False
        $ ans_fsx_tht4_was_dropped = False
        scene l6f13

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillFourteen

        call screen lesson_six_ls13_fill

        label call_sx13:
            $ ans_fsx_tht1_was_dropped = False
            $ ans_fsx_tht2_was_dropped = False
            $ ans_fsx_tht3_was_dropped = False
            $ ans_fsx_tht4_was_dropped = False
            call screen lesson_six_ls13_fill
        
        label if_lsx13_wrong:
            scene l6f13
            Tech "Try again"
            call screen lesson_six_ls13_fill


    label lessonSixFillFourteen:
        scene l6f14
        Tech "There are many other types of input elements that you can use in your forms. "
        Tech "Run the code to explore some more"
        call screen lesson_six_ls14_fill

        label when_run_six_fourteen:
            scene lesson_6_15_run 
            Tech "It also have different display"
            jump lessonDropDownTakeaways

    
    label lessonDropDownTakeaways:
        scene lesson_drop_down_takeaways
        Tech "In the next lesson, you`ll learn to add videos to your web pages."
        jump lessonVideoIntro
    
    label lessonVideoIntro:
        scene lesson_video_intro
        Tech "In this lesson, you`ll learn to add videos to spice up your pages."
        jump lessonSixFillSixteen


    label lessonSixFillSixteen:
        $ ans_fsx_st1_was_dropped = False
        scene l6f16
        Tech "Complete code"
        call screen lesson_six_ls16_fill

        label call_sx16:
            $ ans_fsx_st1_was_dropped = False
            call screen lesson_six_ls16_fill
        
        label if_lsx16_wrong:
            scene l6f16
            Tech "Try again"
            call screen lesson_six_ls16_fill


    label lessonSixFillSeventeen:
        scene lesson_6_17  
        Tech "What does that mean?"

        label begin_question_st:
        menu:
            "The video needs to be stored on the viewer’s device":
                jump if_lsx17_wrong
            "The source (or location) URL of the video needs to be provided":
                Tech "You are correct"
                jump lessonSixFillEighteen
 
        label if_lsx17_wrong:
            Tech "incorrect"
            jump begin_question_st


    label lessonSixFillEighteen:
        $ ans_fsx_egt1_was_dropped = False
        $ ans_fsx_egt2_was_dropped = False
        scene l6f18
        Tech "You can add video files in different formats. Common video formats are: {b}MP4, OGG and WebM{/b}."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillNineteen

        call screen lesson_six_ls18_fill

        label call_sx18:
            $ ans_fsx_st1_was_dropped = False
            $ ans_fsx_egt2_was_dropped = False
            call screen lesson_six_ls18_fill
        
        label if_lsx18_wrong:
            scene l6f18
            Tech "Try again"
            call screen lesson_six_ls18_fill


    label lessonSixFillNineteen:
        $ ans_fsx_nt1_was_dropped = False
        scene l6f19
        Tech "The <source> empty tag provides the location and format of the video file."
        call screen lesson_six_ls19_fill

        label call_sx19:
            $ ans_fsx_nt1_was_dropped = False
            call screen lesson_six_ls19_fill
        
        label if_lsx19_wrong:
            scene l6f19
            Tech "Try again"
            call screen lesson_six_ls19_fill


    label lessonSixFillTwenty:
        $ ans_fsx_twt1_was_dropped = False
        $ ans_fsx_twt2was_dropped = False
        scene l6f20
        Tech "You can add video files in different formats. Common video formats are: {b}MP4, OGG and WebM{/b}."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillTwentyone


        call screen lesson_six_ls20_fill

        label call_sx20:
            $ ans_fsx_twt1_was_dropped = False
            $ ans_fsx_twt2_was_dropped = False
            call screen lesson_six_ls20_fill
        
        label if_lsx20_wrong:
            scene l6f20
            Tech "Try again"
            call screen lesson_six_ls20_fill


    label lessonSixFillTwentyone:
        $ ans_fsx_twto1_was_dropped = False
        $ ans_fsx_twto2_was_dropped = False
        scene l6f21
        Tech "The type attribute specifies the format of the video file."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillTwentytwo

        call screen lesson_six_ls21_fill

        label call_sx21:
            $ ans_fsx_twto1_was_dropped = False
            $ ans_fsx_twto2_was_dropped = False
            call screen lesson_six_ls21_fill
        
        label if_lsx21_wrong:
            scene l6f21
            Tech "Try again"
            call screen lesson_six_ls21_fill


    label lessonSixFillTwentytwo:
        $ ans_fsx_twtt1_was_dropped = False
        scene l6f22
        call screen lesson_six_ls22_fill

        label call_sx22:
            $ ans_fsx_twtt1_was_dropped = False
            call screen lesson_six_ls22_fill
        
        label if_lsx22_wrong:
            scene l6f22
            e "Try again"
            call screen lesson_six_ls22_fill


    label lessonSixFillTwentythree:
        $ ans_fsx_twth1_was_dropped = False
        $ ans_fsx_twth2_was_dropped = False
        scene l6f23
        Tech "Different media formats are needed for compatibility with different browsers and devices."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillTwentyfour


        call screen lesson_six_ls23_fill

        label call_sx23:
            $ ans_fsx_twth1_was_dropped = False
            $ ans_fsx_twth2_was_dropped = False
            call screen lesson_six_ls23_fill
        
        label if_lsx23_wrong:
            scene l6f23
            Tech "Try again"
            call screen lesson_six_ls23_fill


    label lessonSixFillTwentyfour:
        scene lesson_6_24  
        Tech "When different <source> options are included, the browser will choose the first one it supports."
        Tech "But which do you think it is?"

        label begin_question_tf:
        menu:
            "webm":
                jump if_lsx24_wrong
            "mp4":
                Tech "You are correct"
                jump lessonSixFillTwentyfive
 
        label if_lsx24_wrong:
            Tech "incorrect"
            jump begin_question_tf


    label lessonSixFillTwentyfive:
        scene lesson_6_25  
        Tech "You can add text between the <video> tags. The text will only be displayed in browsers that don’t support the video element."
        Tech "Which one do you think will be display"

        label begin_question_tfv:
        menu:
            "Not found":
                jump if_lsx25_wrong
            "WebM":
                jump if_lsx25_wrong
            "404 error code":
                jump if_lsx25_wrong
            "Video not supported":
                Tech "You are correct"
                jump lessonSixFillTwentysix
 
        label if_lsx25_wrong:
            Tech "incorrect"
            jump begin_question_tfv


    label lessonSixFillTwentysix:
        $ ans_fsx_twts1_was_dropped = False
        $ ans_fsx_twts2_was_dropped = False
        scene l6f26

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillTwentyseven

        call screen lesson_six_ls26_fill

        label call_sx26:
            $ ans_fsx_twts1_was_dropped = False
            $ ans_fsx_twts2_was_dropped = False
            call screen lesson_six_ls26_fill
        
        label if_lsx26_wrong:
            scene l6f26
            Tech "Try again"
            call screen lesson_six_ls26_fill


    label lessonSixFillTwentyseven:
        $ ans_fsx_twtsv1_was_dropped = False
        scene l6f27
        Tech "You can display play/pause, volume and other video controls with the {b}controls{/b} attribute."
        call screen lesson_six_ls27_fill

        label call_sx27:
            $ ans_fsx_twtsv1_was_dropped = False
            call screen lesson_six_ls27_fill
        
        label if_lsx27_wrong:
            scene l6f27
            Tech  "Try again"
            call screen lesson_six_ls27_fill


    label lessonSixFillTwentyeight:
        scene l6f28
        Tech"Add the {b}controls{/b} attribute if you want to show default video controls like play, pause, etc.  "
        Tech "Run the code to see the video with controls embedded in the page"
        call screen lesson_six_ls28_fill

        label when_run_six_twenteight:
            show lesson_6_28_run 
            Tech"Now the video has play, pause, etc."
            jump lessonSixFillTwentynine


    label lessonSixFillTwentynine:
        scene lesson_6_29  
        Tech"What`s wrong with this code?"

        label begin_question_tn:
        menu:
            "The video tag is an empty tag":
                jump if_lsx29_wrong
            "The source is a container tag":
                jump if_lsx29_wrong
            "The controls attribute should be used to add play/pause controls":
                Tech "You are correct"
                jump lessonSixFillThirty
 
        label if_lsx29_wrong:
            Tech "incorrect"
            jump begin_question_tn


    label lessonSixFillThirty:
        $ ans_fsx_tty1_was_dropped = False
        $ ans_fsx_tty2_was_dropped = False
        $ ans_fsx_tty3_was_dropped = False
        $ ans_fsx_tty4_was_dropped = False
        scene l6f30

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonVideoTakeaways

        call screen lesson_six_ls30_fill

        label call_sx30:
            $ ans_fsx_tty1_was_dropped = False
            $ ans_fsx_tty2_was_dropped = False
            $ ans_fsx_tty3_was_dropped = False
            $ ans_fsx_tty4_was_dropped = False
            call screen lesson_six_ls30_fill
        
        label if_lsx30_wrong:
            scene l6f30
            Tech "Try again"
            call screen lesson_six_ls30_fill


    label lessonVideoTakeaways:
        scene lesson_video_takeaways
        Tech "In the next lesson, you`ll learn to embed audio into your pages."
        jump lessonAudioIntro


    label lessonAudioIntro:
        scene lesson_audio_intro
        Tech "In this lesson, you'll learn to add audio to your sites."
        jump lessonSixFillThirtyone


    label lessonSixFillThirtyone:
        $ ans_fsx_ttyo1_was_dropped = False
        $ ans_fsx_ttyo2_was_dropped = False
        scene l6f31

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillThirtytwo

        call screen lesson_six_ls31_fill

        label call_sx31:
            $ ans_fsx_ttyo1_was_dropped = False
            $ ans_fsx_ttyo2_was_dropped = False
            call screen lesson_six_ls31_fill
        
        label if_lsx31_wrong:
            scene l6f31
            Tech "Try again"
            call screen lesson_six_ls31_fill    


    label lessonSixFillThirtytwo:
        $ ans_fsx_ttytw1_was_dropped = False
        scene l6f32
        Tech "Just like video, the {b}<source> tag{/b} is used to add source options for audio."
        call screen lesson_six_ls32_fill

        label call_sx32:
            $ ans_fsx_ttytw1_was_dropped = False
            call screen lesson_six_ls32_fill
        
        label if_lsx32_wrong:
            scene l6f32
            Tech "Try again"
            call screen lesson_six_ls32_fill    


    label lessonSixFillThirtythree:
        scene lesson_6_33 with dissolve
        Tech"Which one do you think??"

        label begin_question_tth:
        menu:
            "a closing tag":
                jump if_lsx33_wrong
            "a container tag":
                jump if_lsx33_wrong
            "an empty tag":
                Tech "You are correct"
                jump lessonSixFillThirtyfour
 
        label if_lsx33_wrong:
            Tech"incorrect"
            jump begin_question_tth


    label lessonSixFillThirtyfour:
        $ ans_fsx_ttyfr1_was_dropped = False
        $ ans_fsx_ttyfr2_was_dropped = False
        scene l6f34
        Tech "Just like video, the {b}src attribute{/b} adds the audio file URL. The {b}type attribute{/b} adds the format."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillThirtyfive

        call screen lesson_six_ls34_fill

        label call_sx34:
            $ ans_fsx_ttyfr1_was_dropped = False
            $ ans_fsx_ttyfr2_was_dropped = False
            call screen lesson_six_ls34_fill
        
        label if_lsx34_wrong:
            scene l6f34
            Tech "Try again"
            call screen lesson_six_ls34_fill    


    label lessonSixFillThirtyfive:
        $ ans_fsx_ttyfv1_was_dropped = False
        $ ans_fsx_ttyfv2_was_dropped = False
        scene l6f35
        Tech "Just like video, you can add audio files in different formats. Common audio formats are: MP3, OGG and WAV."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillThirtysix

        call screen lesson_six_ls35_fill

        label call_sx35:
            $ ans_fsx_ttyfv1_was_dropped = False
            $ ans_fsx_ttyfv2_was_dropped = False
            call screen lesson_six_ls35_fill
        
        label if_lsx35_wrong:
            scene l6f35
            Tech "Try again"
            call screen lesson_six_ls35_fill   


    label lessonSixFillThirtysix:
        scene lesson_6_36  
        Tech "Is what?"

        label begin_question_tsx:
        menu:
            "Nesting all <source> options inside <audio>":
                Tech "You are correct"
                jump lessonSixFillThirtyeight
            "Adding <audio> tags for each source option":
                jump if_lsx36_wrong
 
        label if_lsx36_wrong:
            Tech "incorrect"
            jump begin_question_tsx


    label lessonSixFillThirtyeight:
        scene lesson_6_38 
        Tech "What will the browser display if the 2 audio files are not supported?"

        label begin_question_tet:
        menu:
            "A YouTube video":
                jump if_lsx38_wrong

            "Audio not supported":
                Tech "You are correct"
                jump lessonSixFillThirtynine

            "404 code error":
                jump if_lsx38_wrong
 
        label if_lsx38_wrong:
            Tech "incorrect"
            jump begin_question_tet


    label lessonSixFillThirtynine:
        scene lesson_6_39 
        Tech "What will the browser display if at least one of the audio files is supported?"

        label begin_question_tnn:
        menu:
            "The audio element without any controls":
                jump if_lsx39_wrong

            "The audio element with play/pause and volume controls":
                Tech "You are correct"
                jump lessonSixFillForty

            "The video file with controls":
                jump if_lsx39_wrong
 
        label if_lsx39_wrong:
            Tech "incorrect"
            jump begin_question_tnn


    label lessonSixFillForty:
        scene lesson_6_40  
        Tech "Because...?"

        label begin_question_ft:
        menu:
            "Attributes can`t be applied to multimedia elements":
                jump if_lsx40_wrong

            "It has a default value if no other is specified":
                Tech "You are correct"
                jump lessonSixFillFortyone

 
        label if_lsx40_wrong:
            Tech "incorrect"
            jump begin_question_ft


    label lessonSixFillFortyone:
        scene lesson_6_41  
        Tech "What will the browser display if the 2 audio files are supported?"

        label begin_question_fto:
        menu:
            "The audio element in ogg format":
                jump if_lsx41_wrong

            "Audio not supported":
                jump if_lsx41_wrong

            "The audio element in mp3 format":
                Tech "You are correct"
                jump lessonSixFillFortytwo

 
        label if_lsx41_wrong:
            Tech "incorrect"
            jump begin_question_fto


    label lessonSixFillFortytwo:
        $ ans_fsx_fttw1_was_dropped = False
        $ ans_fsx_fttw2_was_dropped = False
        $ ans_fsx_fttw3_was_dropped = False
        $ ans_fsx_fttw4_was_dropped = False
        scene l6f42
        Tech "You can use {b}autoplay{/b}, {b}muted{/b} and {b}loop{/b} attributes to control the behavior of the multimedia element. Just like {b}controls{/b}, these attributes have their default values omitted."

        e "Anyone wants to answer this problem?"
        menu:
            "Raise Hand":
                pass

            "Ignore":
                jump lessonSixFillFortythree

        call screen lesson_six_ls42_fill

        label call_sx42:
            $ ans_fsx_fttw1_was_dropped = False
            $ ans_fsx_fttw2_was_dropped = False
            $ ans_fsx_fttw3_was_dropped = False
            $ ans_fsx_fttw4_was_dropped = False
            call screen lesson_six_ls42_fill
        
        label if_lsx42_wrong:
            scene l6f42
            Tech "Try again"
            call screen lesson_six_ls42_fill   


    label lessonSixFillFortythree:
        scene lesson_6_43  
        Tech "What will happen as soon as the page is loaded by the browser?"

        label begin_question_fttr:
        menu:
            "The audio will be muted":
                jump if_lsx43_wrong

            "The audio will start playing":
                Tech "You are correct"
                jump lessonSixFillFortyfour

            "The audio will be paused":
                jump if_lsx43_wrong

 
        label if_lsx43_wrong:
            Tech "incorrect"
            jump begin_question_fttr


    label lessonSixFillFortyfour:
        scene lesson_6_44 
        Tech "How will this video behave in the browser?"

        label begin_question_ftfr:
        menu:
            "The audio will play without video":
                jump if_lsx44_wrong

            "The play and volume controls will be displayed":
                jump if_lsx44_wrong

            "The video will start playing automatically without sound":
                Tech "You are correct"
                jump lessonSixFillFortyfive

 
        label if_lsx44_wrong:
            Tech "incorrect"
            jump begin_question_ftfr


    label lessonSixFillFortyfive:
        scene lesson_6_45  
        Tech "How will this multimedia element behave in the browser?"

        label begin_question_ftfv:
        menu:
            "The video will start again every time it finishes":
                jump if_lsx45_wrong

            "The audio will start playing automatically":
                jump if_lsx45_wrong

            "The audio will start again every time it finishes":
                Tech "You are correct"
                jump lessonSixFillFortysix

 
        label if_lsx45_wrong:
            Tech "incorrect"
            jump begin_question_ftfv


    label lessonSixFillFortysix:
        scene lesson_6_46  
        Tech "Can be used with what?"

        label begin_question_ftsx:
        menu:
            "video elements only":
                jump if_lsx46_wrong

            "audio elements only":
                jump if_lsx46_wrong

            "both video and audio elements":
                Tech "You are correct"
                jump lessonSixFillFortyseven

 
        label if_lsx46_wrong:
            Tech "incorrect"
            jump begin_question_ftsx


    label lessonSixFillFortyseven:
        scene lesson_6_47  
        Tech "What`s wrong with this code?"

        label begin_question_ftsv:
        menu:
            "OGG is not a valid audio format":
                jump if_lsx47_wrong

            "The type attribute is missing for the MP3 source":
                Tech "You are correct"
                jump lessoAudioTakeaways

            "There is text in the code that should be surrounded by tags":
                jump if_lsx47_wrong

 
        label if_lsx47_wrong:
            Tech "incorrect"
            jump begin_question_ftsv


    label lessoAudioTakeaways:
        scene lesson_audio_takeaways
        Tech "In the next lesson you`ll learn page layout to improve your web designs."

    stop music fadeout 1.0
    
    play music "audio/quiz.mp3" volume 0.5

    $ persistent.ast2_participation += 25
    label skipped_l6:

    e "Let's Start the Quiz for lesson 6"
    jump start_quiz_05

    label pagtapos_ng_quiz_5:



    $ persistent.lesson_6_quiz6 = persistent_quiz_05_q_counter_correct_answer
    
    Tech "Great job on the quiz, class! You all did fantastic."

    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting project related to what you've just learned."
    jump l6_act6
    label pagtapos_ng_act_6:

    Tech "I hope you're all doing well. Today, I have an important announcement to make."

    Tech "We've covered a lot of material in lessons 4 to 6, and I've been impressed with your engagement and dedication."

    Tech "As a way to assess your understanding and progress, we'll be having an exam next"

    Tech "Ok! Let's start the examination"

    jump Second_one
    label tapos_exam2:





    stop music fadeout 1.0

    play music "audio/sa_tech.mp3" volume 0.5

    scene bg_classroom

    show teacher_crossarm_smile
    e "I want to acknowledge your hard work and dedication in preparing for this exam. It's a crucial part of our learning journey."
    e"Well done young coders. Let's end our class here."
    hide tea
    show teacher_closed_happy
    e"Good bye class"
    e"You can now veiw your lesson 4 to 6 assessment"
    hide teacher_closed_happy

    stop music fadeout 1.0



    
    scene bg_6
    blank "End of chapter 6"
    
    $ lesson_six_finish = True
    jump assessment_two
    call screen lesson_ui




    return
