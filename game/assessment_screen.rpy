







screen radarChart_transforms:
    text "{b}Lesson 0{/b}" size 32 color "#ffffff" xpos 79 ypos 111
    text "Takes: 10" size 24 xpos 79 ypos 150
    frame:
        background None
        xysize (200, 200)
        xpadding 0
        ypadding 0
        xpos 740
        ypos 350
        add animated_spider_web.chart_base at spinner_base
        add animated_spider_web.chart_data at spinner_data
        add animated_spider_web.chart_lines at spinner_base
        add animated_spider_web.chart_labels at spinner_labels



screen ls_one_asses:
    text "{b}Lesson 1{/b}" size 32 color "#ffffff" xpos 79 ypos 111
    text "Takes: [l1_takes]" size 24 xpos 79 ypos 150
    frame:
        background None
        xysize (200, 200)
        xpadding 0
        ypadding 0
        xpos 740
        ypos 350
        add ls_one_rad.chart_base at spinner_base
        add ls_one_rad.chart_data at spinner_data
        add ls_one_rad.chart_lines at spinner_base
        add ls_one_rad.chart_labels at spinner_labels



screen ls_two_asses:
    text "{b}Lesson 2{/b}" size 32 color "#ffffff" xpos 79 ypos 111
    text "Takes: [l2_takes]" size 24 xpos 79 ypos 150
    frame:
        background None
        xysize (200, 200)
        xpadding 0
        ypadding 0
        xpos 740
        ypos 350
        add ls_two_rad.chart_base at spinner_base
        add ls_two_rad.chart_data at spinner_data
        add ls_two_rad.chart_lines at spinner_base
        add ls_two_rad.chart_labels at spinner_labels



screen ls_three_asses:
    text "{b}Lesson 3{/b}" size 32 color "#ffffff" xpos 79 ypos 111
    text "Takes: [l3_takes]" size 24 xpos 79 ypos 150
    frame:
        background None
        xysize (200, 200)
        xpadding 0
        ypadding 0
        xpos 740
        ypos 350
        add ls_three_rad.chart_base at spinner_base
        add ls_three_rad.chart_data at spinner_data
        add ls_three_rad.chart_lines at spinner_base
        add ls_three_rad.chart_labels at spinner_labels



screen ls_four_asses:
    text "{b}Lesson 4{/b}" size 32 color "#ffffff" xpos 79 ypos 111
    text "Takes: [l4_takes]" size 24 xpos 79 ypos 150
    frame:
        background None
        xysize (200, 200)
        xpadding 0
        ypadding 0
        xpos 740
        ypos 350
        add ls_four_rad.chart_base at spinner_base
        add ls_four_rad.chart_data at spinner_data
        add ls_four_rad.chart_lines at spinner_base
        add ls_four_rad.chart_labels at spinner_labels



screen ls_five_asses:
    text "{b}Lesson 5{/b}" size 32 color "#ffffff" xpos 79 ypos 111
    text "Takes: [l5_takes]" size 24 xpos 79 ypos 150
    frame:
        background None
        xysize (200, 200)
        xpadding 0
        ypadding 0
        xpos 740
        ypos 350
        add ls_five_rad.chart_base at spinner_base
        add ls_five_rad.chart_data at spinner_data
        add ls_five_rad.chart_lines at spinner_base
        add ls_five_rad.chart_labels at spinner_labels






screen q1_assesment():

    image "images/qtrly_assessment_bg.png"
    # Written Works
    image Solid("#006eff") xsize(persistent.written_works * 7) ysize(45) xpos 80 ypos 162
    text "{b}Written Works [persistent.written_works] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(162)

    # Performance Task
    image Solid("#006eff") xsize(persistent.performance_task * 7) ysize(45) xpos 80 ypos 257
    text "{b}Performance Task [persistent.performance_task] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(257)

    # Exam
    image Solid("#006eff") xsize(persistent.exam * 70) ysize(45) xpos 80 ypos 352
    text "{b}Exam [persistent.exam] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(352)

    # Overall Grade
    image Solid("#006eff") xsize(persistent.overall_grade * 10) ysize(45) xpos 841 ypos 212
    text "{b}Grade [persistent.overall_grade] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(841) ypos(212)

    # Previous Grade 
    image Solid("#006eff") xsize(persistent.previous_overall_grade * 10) ysize(45) xpos 841 ypos 326
    text "{b}Grade [persistent.previous_overall_grade] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(841) ypos(326)

    # Feedbacks
    text "{b}[persistent.POV]{/b}  (1st Quarter)" size 24 color "#ffffff" xpos(851) ypos(492)
    vbox:
        xpos 851
        ypos 561
        # Feedbacks
        
        text "[quarter_result_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(561)

        text "[written_works_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(649)
        text "[performance_task_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(693)
        text "[exam_feedback]" size 32 color "#ffffff" #xpos(851) ypos(737)



    #Behavior Assessment
    text "{b}([persistent.ast1_recitation]){/b}" size 24 color "#ffffff" xpos(249) ypos(561)
    text "{b}([persistent.ast1_participation]){/b}" size 24 color "#ffffff" xpos(280) ypos(615)
    text "{b}([persistent.ast1_accuracy]){/b}" size 24 color "#ffffff" xpos(241) ypos(669)
    text "{b}([persistent.ast1_kindness]){/b}" size 24 color "#ffffff" xpos(240) ypos(723)
    text "{b}([persistent.ast1_rudeness]){/b}" size 24 color "#ffffff" xpos(246) ypos(766)

    text "[behavior_fb_result]" size 20 color "#ffffff" xpos(90) ypos(875)

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        action ShowMenu("lesson_ui")

    frame:
        background None
        xysize (300, 300)
        xpadding 0
        ypadding 0
        xpos 398
        ypos 564
        add qtrly_ast_one.chart_base at spinner_base
        add qtrly_ast_one.chart_data at spinner_data
        add qtrly_ast_one.chart_lines at spinner_base
        add qtrly_ast_one.chart_labels at spinner_labels


screen q2_assesment():

    image "images/qtrly_assessment_bg.png"
    # Written Works
    image Solid("#006eff") xsize(persistent.q2_written_works * 7) ysize(45) xpos 80 ypos 162
    text "{b}Written Works [persistent.q2_written_works] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(162)

    # Performance Task
    image Solid("#006eff") xsize(persistent.q2_performance_task * 7) ysize(45) xpos 80 ypos 257
    text "{b}Performance Task [persistent.q2_performance_task] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(257)

    # Exam
    image Solid("#006eff") xsize(persistent.q2_exam_score * 70) ysize(45) xpos 80 ypos 352
    text "{b}Exam [persistent.q2_exam_score] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(352)

    # Overall Grade
    image Solid("#006eff") xsize(persistent.q2_overall_grade * 10) ysize(45) xpos 841 ypos 212
    text "{b}Grade [persistent.q2_overall_grade] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(841) ypos(212)

    # Previous Grade 
    image Solid("#006eff") xsize(persistent.q2_previous_overall_grade * 10) ysize(45) xpos 841 ypos 326
    text "{b}Grade [persistent.q2_previous_overall_grade] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(841) ypos(326)

    # Feedbacks
    text "{b}[persistent.POV]{/b}  (2nd Quarter)" size 24 color "#ffffff" xpos(851) ypos(492)
    vbox:
        xpos 851
        ypos 561
        # Feedbacks
        
        text "[quarter_result_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(561)

        text "[written_works_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(649)
        text "[performance_task_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(693)
        text "[exam_feedback]" size 32 color "#ffffff" #xpos(851) ypos(737)



    #Behavior Assessment
    text "{b}([persistent.ast2_recitation]){/b}" size 24 color "#ffffff" xpos(249) ypos(561)
    text "{b}([persistent.ast2_participation]){/b}" size 24 color "#ffffff" xpos(280) ypos(615)
    text "{b}([persistent.ast2_accuracy]){/b}" size 24 color "#ffffff" xpos(241) ypos(669)
    text "{b}([persistent.ast2_kindness]){/b}" size 24 color "#ffffff" xpos(240) ypos(723)
    text "{b}([persistent.ast2_rudeness]){/b}" size 24 color "#ffffff" xpos(246) ypos(766)
    
    text "[behavior_fb_result]" size 20 color "#ffffff" xpos(90) ypos(875)

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        action ShowMenu("lesson_ui")

    frame:
        background None
        xysize (300, 300)
        xpadding 0
        ypadding 0
        xpos 398
        ypos 564
        add qtrly_ast_two.chart_base at spinner_base
        add qtrly_ast_two.chart_data at spinner_data
        add qtrly_ast_two.chart_lines at spinner_base
        add qtrly_ast_two.chart_labels at spinner_labels








screen q3_assesment():

    image "images/qtrly_assessment_bg.png"
    # Written Works
    image Solid("#006eff") xsize(persistent.q3_written_works * 7) ysize(45) xpos 80 ypos 162
    text "{b}Written Works [persistent.q3_written_works] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(162)

    # Performance Task
    image Solid("#006eff") xsize(persistent.q3_performance_task * 7) ysize(45) xpos 80 ypos 257
    text "{b}Performance Task [persistent.q3_performance_task] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(257)

    # Exam
    image Solid("#006eff") xsize(persistent.q3_exam_score * 70) ysize(45) xpos 80 ypos 352
    text "{b}Exam [persistent.q3_exam_score] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(352)

    # Overall Grade
    image Solid("#006eff") xsize(persistent.q3_overall_grade * 10) ysize(45) xpos 841 ypos 212
    text "{b}Grade [persistent.q3_overall_grade] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(841) ypos(212)

    # Previous Grade 
    image Solid("#006eff") xsize(persistent.q3_previous_overall_grade * 10) ysize(45) xpos 841 ypos 326
    text "{b}Grade [persistent.q3_previous_overall_grade] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(841) ypos(326)

    # Feedbacks
    text "{b}[persistent.POV]{/b}  (3rd Quarter)" size 24 color "#ffffff" xpos(851) ypos(492)
    vbox:
        xpos 851
        ypos 561
        # Feedbacks
        
        text "[quarter_result_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(561)

        text "[written_works_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(649)
        text "[performance_task_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(693)
        text "[exam_feedback]" size 32 color "#ffffff" #xpos(851) ypos(737)



    #Behavior Assessment
    text "{b}([persistent.ast3_recitation]){/b}" size 24 color "#ffffff" xpos(249) ypos(561)
    text "{b}([persistent.ast3_participation]){/b}" size 24 color "#ffffff" xpos(280) ypos(615)
    text "{b}([persistent.ast3_accuracy]){/b}" size 24 color "#ffffff" xpos(241) ypos(669)
    text "{b}([persistent.ast3_kindness]){/b}" size 24 color "#ffffff" xpos(240) ypos(723)
    text "{b}([persistent.ast3_rudeness]){/b}" size 24 color "#ffffff" xpos(246) ypos(766)
    
    text "[behavior_fb_result]" size 20 color "#ffffff" xpos(90) ypos(875)

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        action ShowMenu("lesson_ui")
        
    frame:
        background None
        xysize (300, 300)
        xpadding 0
        ypadding 0
        xpos 398
        ypos 564
        add qtrly_ast_three.chart_base at spinner_base
        add qtrly_ast_three.chart_data at spinner_data
        add qtrly_ast_three.chart_lines at spinner_base
        add qtrly_ast_three.chart_labels at spinner_labels





screen q4_assesment():

    image "images/qtrly_assessment_bg.png"
    # Written Works
    image Solid("#006eff") xsize(persistent.q4_written_works * 7) ysize(45) xpos 80 ypos 162
    text "{b}Written Works [persistent.q4_written_works] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(162)

    # Performance Task
    image Solid("#006eff") xsize(persistent.q4_performance_task * 7) ysize(45) xpos 80 ypos 257
    text "{b}Performance Task [persistent.q4_performance_task] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(257)

    # Exam
    image Solid("#006eff") xsize(persistent.q4_exam_score * 70) ysize(45) xpos 80 ypos 352
    text "{b}Exam [persistent.q4_exam_score] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(352)

    # Overall Grade
    image Solid("#006eff") xsize(persistent.q4_overall_grade * 10) ysize(45) xpos 841 ypos 212
    text "{b}Grade [persistent.q4_overall_grade] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(841) ypos(212)

    # Previous Grade 
    image Solid("#006eff") xsize(persistent.q4_previous_overall_grade * 10) ysize(45) xpos 841 ypos 326
    text "{b}Grade [persistent.q4_previous_overall_grade] % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(841) ypos(326)

    text "{b}[persistent.POV]{/b}  (4rth Quarter)" size 32 color "#ffffff" xpos(851) ypos(492)

    vbox:
        xpos 851
        ypos 561
        # Feedbacks
        
        text "[quarter_result_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(561)

        text "[written_works_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(649)
        text "[performance_task_feedback]\n" size 32 color "#ffffff" #xpos(851) ypos(693)
        text "[exam_feedback]" size 32 color "#ffffff" #xpos(851) ypos(737)



    #Behavior Assessment
    text "{b}([persistent.ast4_recitation]){/b}" size 28 color "#ffffff" xpos(249) ypos(561)
    text "{b}([persistent.ast4_participation]){/b}" size 28 color "#ffffff" xpos(280) ypos(615)
    text "{b}([persistent.ast4_accuracy]){/b}" size 28 color "#ffffff" xpos(241) ypos(669)
    text "{b}([persistent.ast4_kindness]){/b}" size 28 color "#ffffff" xpos(240) ypos(723)
    text "{b}([persistent.ast4_rudeness]){/b}" size 28 color "#ffffff" xpos(246) ypos(766)
    
    text "[behavior_fb_result]" size 20 color "#ffffff" xpos(90) ypos(875)

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        action ShowMenu("lesson_ui")

    frame:
        background None
        xysize (300, 300)
        xpadding 0
        ypadding 0
        xpos 398
        ypos 564
        add qtrly_ast_four.chart_base at spinner_base
        add qtrly_ast_four.chart_data at spinner_data
        add qtrly_ast_four.chart_lines at spinner_base
        add qtrly_ast_four.chart_labels at spinner_labels



