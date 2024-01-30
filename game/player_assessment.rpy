

label behavior_one:

    python:
        global numhc
        global numc
        global numic
        animated_spider_web = RadarChart(
            size=500,
            values=[numhc, numc, numic],
            max_value=100,
            labels = [
                Text("Hints Used", size=24, color="#ffffff"),
                Text("Correctness", size=24, color="#ffffff"),
                Text("Incorrectness", size=24, color="#ffffff")
            ],
            data_colour=("#ff9900"),
            line_colour=("#000000"),
            background_colour=("3F3C39"),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )


    scene BAimage

    show screen radarChart_transforms

    if numhc > numc and numc > numic:
        blank "It seems like you've been exploring the hints quite a bit! That's great for learning. Make sure to apply the hints to your advantage. Keep up the good work!"
    elif numic > numc and numic > numhc:
        blank "It looks like you've been taking some risks with your answers! Remember, understanding the content is key. Take your time reading through the dialogues, and don't hesitate to use hints for a better grasp of the material."
    elif numc > numhc and numc > numic:
        blank "You're doing fantastic! Your correct answers show a good understanding of the material. If you ever need clarification, feel free to revisit the hints. Keep it up, and you'll master HTML in no time!" 
    else:
        # Default message or behavior if none of the conditions are met
        blank "You skipped the whole lesson!"

    hide screen radarChart_transforms


label behavior:

    python:
        global ls1_numhc
        global ls1_numc
        global ls1_numic

        ls_one_rad = RadarChart(
            size=500,
            values=[ls1_numhc, ls1_numc, ls1_numic],
            max_value=50,
            labels = [
                Text("Hints Used", size=24, color="#ffffff"),
                Text("Correctness", size=24, color="#ffffff"),
                Text("Incorrectness", size=24, color="#ffffff")
            ],
            data_colour=("#ff9900"),
            line_colour=("#000000"),
            background_colour=("3F3C39"),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )
            
    scene BAimage

    show screen ls_one_asses
    if ls1_numhc > ls1_numc and ls1_numc > ls1_numic:
        blank "It seems like you've been exploring the hints quite a bit! That's great for learning. Make sure to apply the hints to your advantage. Keep up the good work!"
    elif ls1_numic > ls1_numc and ls1_numic > ls1_numhc:
        blank "It looks like you've been taking some risks with your answers! Remember, understanding the content is key. Take your time reading through the dialogues, and don't hesitate to use hints for a better grasp of the material."
    elif ls1_numc > ls1_numhc and ls1_numc > ls1_numic:
        blank "You're doing fantastic! Your correct answers show a good understanding of the material. If you ever need clarification, feel free to revisit the hints. Keep it up, and you'll master HTML in no time!" 
    else:
        # Default message or behavior if none of the conditions are met
        blank "You skipped the whole lesson!"
    
    hide screen ls_one_asses
    jump l1_ending

label behavior_two:
        
    python:
        global ls2_numhc
        global ls2_numc
        global ls2_numic

        ls_two_rad = RadarChart(
            size=500,
            values=[ls2_numhc, ls2_numc, ls2_numic],
            max_value=100,
            labels = [
                Text("Hints Used", size=24, color="#ffffff"),
                Text("Correctness", size=24, color="#ffffff"),
                Text("Incorrectness", size=24, color="#ffffff")
            ],
            data_colour=("#ff9900"),
            line_colour=("#000000"),
            background_colour=("3F3C39"),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )
            
    scene BAimage

    show screen ls_two_asses
    if ls2_numhc > ls2_numc and ls2_numc > ls2_numic:
        blank "It seems like you've been exploring the hints quite a bit! That's great for learning. Make sure to apply the hints to your advantage. Keep up the good work!"
    elif ls2_numic > ls2_numc and ls2_numic > ls2_numhc:
        blank "It looks like you've been taking some risks with your answers! Remember, understanding the content is key. Take your time reading through the dialogues, and don't hesitate to use hints for a better grasp of the material."
    elif ls2_numc > ls2_numhc and ls2_numc > ls2_numic:
        blank "You're doing fantastic! Your correct answers show a good understanding of the material. If you ever need clarification, feel free to revisit the hints. Keep it up, and you'll master HTML in no time!" 
    else:
        # Default message or behavior if none of the conditions are met
        blank "You skipped the whole lesson!"
    
    hide screen ls_two_asses
    jump chp_two_ending


label behavior_three:
        
    python:
        global ls3_numhc
        global ls3_numc
        global ls3_numic

        ls_three_rad = RadarChart(
            size=500,
            values=[ls3_numhc, ls3_numc, ls3_numic],
            max_value=100,
            labels = [
                Text("Hints Used", size=24, color="#ffffff"),
                Text("Correctness", size=24, color="#ffffff"),
                Text("Incorrectness", size=24, color="#ffffff")
            ],
            data_colour=("#ff9900"),
            line_colour=("#000000"),
            background_colour=("3F3C39"),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )
            
    scene BAimage

    show screen ls_three_asses
    if ls3_numhc > ls3_numc and ls3_numc > ls3_numic:
        blank "It seems like you've been exploring the hints quite a bit! That's great for learning. Make sure to apply the hints to your advantage. Keep up the good work!"
    elif ls3_numic > ls3_numc and ls3_numic > ls3_numhc:
        blank "It looks like you've been taking some risks with your answers! Remember, understanding the content is key. Take your time reading through the dialogues, and don't hesitate to use hints for a better grasp of the material."
    elif ls3_numc > ls3_numhc and ls3_numc > ls3_numic:
        blank "You're doing fantastic! Your correct answers show a good understanding of the material. If you ever need clarification, feel free to revisit the hints. Keep it up, and you'll master HTML in no time!"
    elif ls3_numhc > ls3_numc and ls3_numhc > ls3_numic:
        blank "It seems that the teacher failed to educate you. You can always try and take the lesson again anytime you want."
    else:
        # Default message or behavior if none of the conditions are met
        blank "You skipped the whole lesson!"
    
    hide screen ls_three_asses
    jump chp_three_ending



label behavior_four:
        
    python:
        global ls4_numhc
        global ls4_numc
        global ls4_numic

        ls_four_rad = RadarChart(
            size=500,
            values=[ls4_numhc, ls4_numc, ls4_numic],
            max_value=100,
            labels = [
                Text("Hints Used", size=24, color="#ffffff"),
                Text("Correctness", size=24, color="#ffffff"),
                Text("Incorrectness", size=24, color="#ffffff")
            ],
            data_colour=("#ff9900"),
            line_colour=("#000000"),
            background_colour=("3F3C39"),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )
            
    scene BAimage

    show screen ls_four_asses
    if ls4_numhc > ls4_numc and ls4_numc > ls4_numic:
        blank "It seems like you've been exploring the hints quite a bit! That's great for learning. Make sure to apply the hints to your advantage. Keep up the good work!"
    elif ls4_numic > ls4_numc and ls4_numic > ls4_numhc:
        blank "It looks like you've been taking some risks with your answers! Remember, understanding the content is key. Take your time reading through the dialogues, and don't hesitate to use hints for a better grasp of the material."
    elif ls4_numc > ls4_numhc and ls4_numc > ls4_numic:
        blank "You're doing fantastic! Your correct answers show a good understanding of the material. If you ever need clarification, feel free to revisit the hints. Keep it up, and you'll master HTML in no time!" 
    else:
        # Default message or behavior if none of the conditions are met
        blank "You skipped the whole lesson!"
    
    hide screen ls_four_asses
    jump chp_four_ending


label behavior_five:
        
    python:
        global ls5_numhc
        global ls5_numc
        global ls5_numic

        ls_five_rad = RadarChart(
            size=500,
            values=[ls5_numhc, ls5_numc, ls5_numic],
            max_value=100,
            labels = [
                Text("Hints Used", size=24, color="#ffffff"),
                Text("Correctness", size=24, color="#ffffff"),
                Text("Incorrectness", size=24, color="#ffffff")
            ],
            data_colour=("#ff9900"),
            line_colour=("#000000"),
            background_colour=("3F3C39"),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )
            
    scene BAimage

    show screen ls_five_asses
    if ls5_numhc > ls5_numc and ls5_numc > ls5_numic:
        blank "It seems like you've been exploring the hints quite a bit! That's great for learning. Make sure to apply the hints to your advantage. Keep up the good work!"
    elif ls5_numic > ls5_numc and ls5_numic > ls5_numhc:
        blank "It looks like you've been taking some risks with your answers! Remember, understanding the content is key. Take your time reading through the dialogues, and don't hesitate to use hints for a better grasp of the material."
    elif ls5_numc > ls5_numhc and ls5_numc > ls5_numic:
        blank "You're doing fantastic! Your correct answers show a good understanding of the material. If you ever need clarification, feel free to revisit the hints. Keep it up, and you'll master HTML in no time!" 
    else:
        # Default message or behavior if none of the conditions are met
        blank "You skipped the whole lesson!"
    
    hide screen ls_five_asses
    jump chp_five_ending



label assessment_one:

    python:
        
        qtrly_ast_one = RadarChart(
            size=300,
            values=[persistent.ast1_recitation, persistent.ast1_participation, persistent.ast1_accuracy, persistent.ast1_kindness, persistent.ast1_rudeness],
            max_value=100,
            labels = [
                Text("*", size=24, color="#007bf7"),
                Text("*", size=24, color="#2ecc71"),
                Text("*", size=24, color="#bdc3c7"),
                Text("*", size=24, color="#ffd700"),
                Text("*", size=24, color="#e74c3c")
            ],
            data_colour=("#006eff"),
            line_colour=("#000000"),
            background_colour=("#D9D9D9"),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )
            

    call screen q1_assesment

    "wow"
    
    hide screen q1_assesment
    return


