

























screen final_behavior_assessment:
    text "{b}Assessment{/b}" size 32 color "#ffffff" xpos 79 ypos 111
    text "Hints Used: [persistent.f_numhc]" size 24 xpos 79 ypos 175
    text "Correctness: [persistent.f_numc]" size 24 xpos 79 ypos 229
    text "Incorrectness: [persistent.f_numic]" size 24 xpos 79 ypos 283
    text "Overall Time spent: [persistent.f_ttime]" size 24 xpos 79 ypos 337

    frame:
        background None
        xysize (200, 200)
        xpadding 0
        ypadding 0
        xpos 740
        ypos 350
        add ovr_ls_chart.chart_base at spinner_base
        add ovr_ls_chart.chart_data at spinner_data
        add ovr_ls_chart.chart_lines at spinner_base
        add ovr_ls_chart.chart_labels at spinner_labels


label FBA:
        
    python:

        ovr_ls_chart = RadarChart(
            size=500,
            values=[persistent.f_numhc, persistent.f_numc, persistent.f_numic],
            max_value=100,
            labels = [
                Text("HU", size=24, color="#ffffff"),
                Text("CN", size=24, color="#ffffff"),
                Text("ICN", size=24, color="#ffffff")
            ],
            data_colour=("#ff9900"),
            line_colour=("#000000"),
            background_colour=("3F3C39"),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )
            
    scene BAimage

    show screen final_behavior_assessment

    #if ls5_numhc > ls5_numc and ls5_numc > ls5_numic:
    #    blank "It seems like you've been exploring the hints quite a bit! That's great for learning. Make sure to apply the hints to your advantage. Keep up the good work!"
    #elif ls5_numic > ls5_numc and ls5_numic > ls5_numhc:
    #    blank "It looks like you've been taking some risks with your answers! Remember, understanding the content is key. Take your time reading through the dialogues, and don't hesitate to use hints for a better grasp of the material."
    #elif ls5_numc > ls5_numhc and ls5_numc > ls5_numic:
    #    blank "You're doing fantastic! Your correct answers show a good understanding of the material. If you ever need clarification, feel free to revisit the hints. Keep it up, and you'll master HTML in no time!" 
    #else:
        # Default message or behavior if none of the conditions are met
    #    blank "You skipped the whole lesson!"

    if persistent.f_numhc > persistent.f_numc and persistent.f_numc > persistent.f_numic:
        blank "It seems like you've been exploring the hints quite a bit! That's great for learning. Make sure to apply the hints to your advantage. Keep up the good work!"

    elif persistent.f_numic > persistent.f_numc and persistent.f_numic > persistent.f_numhc:
        blank "It looks like you've been taking some risks with your answers! Remember, understanding the content is key. Take your time reading through the dialogues, and don't hesitate to use hints for a better grasp of the material."

    elif persistent.f_numc > persistent.f_numhc and persistent.f_numc > persistent.f_numic:
        blank "You're doing fantastic! Your correct answers show a good understanding of the material. If you ever need clarification, feel free to revisit the hints. Keep it up, and you'll master it in no time!"

    elif persistent.f_numhc > persistent.f_numc and persistent.f_numhc > persistent.f_numic:
        blank "There might be some error"
    
    elif persistent.f_numc < persistent.f_numhc and persistent.f_numc < persistent.f_numic:
        blank "It appears you may be facing challenges in answering correctly. Don't worry—everyone encounters difficulties while learning. Consider revisiting the hints for a better understanding, and take your time to grasp the concepts. Learning is a process, and each step brings you closer to mastery."

    else:
        # Default message or behavior if none of the conditions are met
        blank "It seems like you've had a balanced approach to the lesson. Remember, using hints strategically and understanding correct answers both contribute to effective learning. Keep up the good work!"

    # Additional feedback based on overall time spent
    if persistent.ots_runtime > 10800:  # 10800 seconds = 3 Hours
        blank "Additionally, it looks like you spent a considerable amount of time on this lesson. Remember to pace yourself, and feel free to move on when you feel confident in your understanding."
    else:
        blank "It appears you completed the lesson efficiently! While quick progress is commendable, make sure you thoroughly understand the material. Consider reviewing hints or exploring related content to reinforce your learning."
    
    hide screen final_behavior_assessment