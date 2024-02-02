








label lesson_ten:
    #$ persistent.q3_previous_overall_grade = q3_overall_grade
    $ persistent.rude_lesson = "ten"
    scene bg_classroom

    #if lesson_nine_finish:
    #    jump lessonTableIntro
    #else:
    #    e"Please finish lesson 9"
    #    call screen lesson_ui

    $ persistent.ast4_kindness = 10
    $ persistent.ast4_rudeness = 10
    $ persistent.ast4_recitation = 5
    $ persistent.ast4_participation = 5
    $ persistent.ast4_accuracy = 5

    $ persistent.lesson_10_quiz10 = 0
    $ persistent.lesson_10_act10 = 0

    label lessonTableIntro:
        $ show_quick_menu = False
        play music "audio/sa_tech.mp3" volume 0.5

        scene lesson_table_intro
        e"In this lesson, you’ll learn to add tables to your web page."
        jump lessonTenFillOne


    label lessonTenFillOne:
        $ ans_ften_o1_was_dropped = False
        $ ans_ften_o2_was_dropped = False
        scene l10f1
        e"You can add a table to your web page with the {b}<table>{/b} container tag"
        call screen lesson_ten_ls1_fill

        label call_ten1:
            $ ans_ften_o1_was_dropped = False
            $ ans_ften_o2_was_dropped = False
            call screen lesson_ten_ls1_fill
        
        label if_lten1_wrong:
            scene l10f1
            e"Try again"
            call screen lesson_ten_ls1_fill


    label lessonTenFillTwo:
        scene lesson_8_22 
        show teacher_crossarm_smile
        e"A table of data is made of what...?"

        label choices_tn2:
        menu:
            "rows and columns":
                show teacher_crossarm_happy
                e"You are correct"
                jump lessonTenFillThree
            "wood and nails":
                jump if_ltn2_wrong
 
        label if_ltn2_wrong:
            show teacher_crossarm_sad
            e"incorrect"
            jump lessonTenFillTwo


    label lessonTenFillThree:
        $ ans_ften_thr1_was_dropped = False
        $ ans_ften_thr2_was_dropped = False
        $ ans_ften_thr3_was_dropped = False
        scene l10f3
        e"You can add rows to a table with the {b}<tr>{/b} (table row) container tag. Rows are nested inside the <table> tag."

        label l10Int10:
            menu:
                "Talk to classmate":
                    jump start_hitting_teach3
                    label opsl10_1:
                        $ persistent.ast4_rudeness += 100
                        jump skipped_l10
                "Play with your classmate":
                    jump begin_ho_mg10
                    label opsl10_2:
                        $ persistent.ast4_rudeness += 100
                        jump skipped_l10
                "Raise Hand":
                    pass
                "Ignore":
                    jump lessonTenFillFour

        call screen lesson_ten_ls3_fill

        label call_ten3:
            $ ans_ften_thr1_was_dropped = False
            $ ans_ften_thr2_was_dropped = False
            $ ans_ften_thr3_was_dropped = False
            call screen lesson_ten_ls3_fill
        
        label if_lten3_wrong:
            scene l10f3
            e"Try again"
            call screen lesson_ten_ls3_fill


    label lessonTenFillFour:
        $ ans_ften_fr1_was_dropped = False
        $ ans_ften_fr2_was_dropped = False
        $ ans_ften_fr3_was_dropped = False
        $ ans_ften_fr4_was_dropped = False
        scene l10f4
        e"You can add cells with the {b}<td>{/b} (table data) container tag. They are nested inside rows."
        call screen lesson_ten_ls4_fill

        label call_ten4:
            $ ans_ften_fr1_was_dropped = False
            $ ans_ften_fr2_was_dropped = False
            $ ans_ften_fr3_was_dropped = False
            $ ans_ften_fr4_was_dropped = False
            call screen lesson_ten_ls4_fill
        
        label if_lten4_wrong:
            scene l10f4
            e"Try again"
            call screen lesson_ten_ls4_fill


    label lessonTenFillFive:
        scene l10f5
        e"Run the code to display the table"
        call screen lesson_ten_ls5_fill

        label when_run_ten_five:
            scene lesson_10_5_run 
            e"In later example you wil be able to see the whole table when you applied style to it"
            jump lessonTenFillSix


    label lessonTenFillSix:
        scene l10f6
        e"Borders can be added to tables, rows and cells with the style attribute."
        e"Run the code to display the table"
        call screen lesson_ten_ls6_fill

        label when_run_ten_six:
            scene lesson_10_6_run 
            e"As you can see it added border for both table and table data"
            jump lessonTenFillSeven


    label lessonTenFillSeven:
        scene lesson_10_7
        e"What will the code display?"

        label choices_t7:
        menu:
            "A table with 4 rows and 1 column":
                jump if_lten7_wrong
            "A table with 2 rows and 2 columns":
                e"You are correct"
                jump lessonTenFillEight
            "A table with 1 row and 4 columns":
                jump if_lten7_wrong
 
        label if_lten7_wrong:
            e"incorrect"
            jump lessonTenFillSeven


    label lessonTenFillEight:
        $ ans_ften_et1_was_dropped = False
        $ ans_ften_et2_was_dropped = False
        scene l10f8
        e"How many rows and columns does this table have?"
        call screen lesson_ten_ls8_fill

        label call_ten8:
            $ ans_ften_et1_was_dropped = False
            $ ans_ften_et2_was_dropped = False
            call screen lesson_ten_ls8_fill
        
        label if_lten8_wrong:
            scene l10f8
            e"Try again"
            call screen lesson_ten_ls8_fill


    label lessonTenFillNine:
        scene lesson_10_9
        e"<td> elements within the same row are displayed on the same line, one after the other."

        label choices_t9:
        menu:
            "hybrid elements":
                jump if_lten9_wrong
            "block-level elements":
                jump if_lten9_wrong
            "inline elements":
                e"You are correct"
                jump lessonTenFillTen
 
        label if_lten9_wrong:
            e"incorrect"
            jump lessonTenFillNine


    label lessonTenFillTen:
        $ ans_ften_t1_was_dropped = False
        $ ans_ften_t2_was_dropped = False
        scene l10f10
        e"Remember that white space and line breaks in HTML are ignored by the browser."
        e"How many rows and columns does this table have?"
        call screen lesson_ten_ls10_fill

        label call_ten10:
            $ ans_ften_t1_was_dropped = False
            $ ans_ften_t2_was_dropped = False
            call screen lesson_ten_ls10_fill
        
        label if_lten10_wrong:
            scene l10f10
            e"Try again"
            call screen lesson_ten_ls10_fill


    label lessonTenFillEleven:
        $ ans_ften_el1_was_dropped = False
        $ ans_ften_el2_was_dropped = False
        scene l10f11
        e"Tables usually include headers. A header is a special row at the top of the table used to label each column."
        call screen lesson_ten_ls11_fill

        label call_ten11:
            $ ans_ften_el1_was_dropped = False
            $ ans_ften_el2_was_dropped = False
            call screen lesson_ten_ls11_fill
        
        label if_lten11_wrong:
            scene l10f11
            e"Try again"
            call screen lesson_ten_ls11_fill


    label lessonTenFillTweleve:
        scene l10f12
        e"Run the code to display the table with the header"
        call screen lesson_ten_ls12_fill

        label when_run_ten_tweleve:
            scene lesson_10_12_run 
            e"Also, you can include several headers in HTML tables."
            jump lessonTenFillThirteen


    label lessonTenFillThirteen:
        $ ans_ften_thtt1_was_dropped = False
        $ ans_ften_thtt2_was_dropped = False
        call screen lesson_ten_ls13_fill

        label call_ten13:
            $ ans_ften_thtt1_was_dropped = False
            $ ans_ften_thtt2_was_dropped = False
            call screen lesson_ten_ls13_fill
        
        label if_lten13_wrong:
            scene l10f13
            e"Try again"
            call screen lesson_ten_ls13_fill


    label lessonTenFillFourteen:
        scene lesson_8_22
        show teacher_crossarm_smile
        e"<tr> elements are nested inside... of what?"

        label choices_t14:
        menu:
            "<img>":
                jump if_lten14_wrong
            "<td>":
                jump if_lten14_wrong
            "<table>":
                show teacher_crossarm_happy
                e"You are correct"
                jump lessonTenFillFifteen
            "<th>":
                jump if_lten14_wrong
 
        label if_lten14_wrong:
            show teacher_crossarm_sad
            e"incorrect"
            jump lessonTenFillFourteen


    label lessonTenFillFifteen:
        scene lesson_8_22
        show teacher_crossarm_smile
        e"<td> elements are nested inside... of what?"

        label choices_t15:
        menu:
            "<th>":
                jump if_lten15_wrong
            "<button>":
                jump if_lten15_wrong
            "<tr>":
                show teacher_crossarm_happy
                e"You are correct"
                jump lessonTenFillSixteen
 
        label if_lten15_wrong:
            show teacher_crossarm_sad
            e"incorrect"
            jump lessonTenFillFifteen


    label lessonTenFillSixteen:
        scene lesson_8_22
        show teacher_crossarm_smile
        e"<th> elements are nested inside... of what?"

        label choices_t16:
        menu:
            "<th>":
                jump if_lten16_wrong
            "<tr>":
                show teacher_crossarm_happy
                e"You are correct"
                jump lessonTenFillSeventeen
            "<button>":
                jump if_lten16_wrong
 
        label if_lten16_wrong:
            show teacher_crossarm_sad
            e"incorrect"
            jump lessonTenFillSixteen


    label lessonTenFillSeventeen:
        scene l10f17
        e"You can make cells that take up multiple rows and/or columns, using the attributes {b}colspan{/b} and {b}rowspan{/b}. This is called merging cells."
        call screen lesson_ten_ls17_fill

        label when_run_ten_seventeen:
            scene lesson_10_17_run 
            e"colspan is for the number of columns a cell should span."
            jump lessonTenFillEighteen


    label lessonTenFillEighteen:
        scene l10f18
        e"The {b}rowspan{/b} attribute specifies the number of rows a cell should span. You can use rowspan to merge cells vertically."
        call screen lesson_ten_ls18_fill

        label when_run_ten_eighteen:
            scene lesson_10_18_run 
            e"Great! remember the difference of {b}colspan{/b} and {b}rowspan{/b}."
            jump lessonNineFillNineteen



    label lessonNineFillNineteen:
        scene l10f19
        show teacher_crossarm_smile
        e"Complete this code for a table with 2 columns, 2 rows of data and a header row."
        hide teacher_crossarm_smile
        call screen lesson_nine_ls19_fill

        label if_ln19_correct:
            scene lesson_8_22
            show teacher_closed_happy
            e"Great job"
            jump lessonTableTakeaways


    label lessonTableTakeaways:
        scene lesson_table_takeaways
        e"Well done young coders"
        e"Now lets have quiz"

    stop music fadeout 1.0
    
    play music "audio/quiz.mp3" volume 0.5

    $ persistent.ast4_participation += 100
    label skipped_l10:

    jump start_quiz_09

    label pagtapos_ng_quiz_9:

    $ persistent.lesson_10_quiz10 = persistent_quiz_09_q_counter_correct_answer
    $ persistent.lesson_10_act10 = 6

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

        
    scene bg_10
    blank "End of chapter 10"



    $ lesson_ten_finish = True
    jump assessment_four
    call screen lesson_ui



    return 