







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
    image Solid("#006eff") xsize(persistent.written_works * 70) ysize(45) xpos 80 ypos 162
    text "{b}Written Works [persistent.written_works]0 % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(162)

    # Performance Task
    image Solid("#006eff") xsize(persistent.performance_task * 70) ysize(45) xpos 80 ypos 257
    text "{b}Performance Task [persistent.performance_task]0 % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(257)

    # Exam
    image Solid("#006eff") xsize(persistent.exam * 70) ysize(45) xpos 80 ypos 352
    text "{b}Exam [persistent.exam]0 % {/b}" size 24 color "#ffffff" xoffset 6 yoffset 6 xpos(80) ypos(352)


    frame:
        background None
        xysize (300, 300)
        xpadding 0
        ypadding 0
        xpos 382
        ypos 573
        add qtrly_ast_one.chart_base at spinner_base
        add qtrly_ast_one.chart_data at spinner_data
        add qtrly_ast_one.chart_lines at spinner_base
        add qtrly_ast_one.chart_labels at spinner_labels