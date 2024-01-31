

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

    
    
    # Lesson 1 
    #$ lesson_1_quiz1 = 5  # Written Works 20%
    #$ lesson_1_act1 = 6  # Performance Task 20%

    # Lesson 2 
    #$ lesson_2_quiz2 = 8  # Written Works 10%
    #$ lesson_2_act2 = 4  # Performance Task 10%

    # Lesson 3 
    #$ lesson_3_quiz3 = 10  # Written Works 10%
    #$ lesson_3_act3 = 7  # Performance Task 10%

    $ exam_score = 10 # Exam 20%



    # Calculate weighted scores for each lesson #############################################################################

    $ lesson_1_weighted_score = (persistent.lesson_1_quiz1/10 * 0.2) + (persistent.lesson_1_act1/10 * 0.2)
    $ lesson_2_weighted_score = (persistent.lesson_2_quiz2/10 * 0.1) + (persistent.lesson_2_act2/10 * 0.1)
    $ lesson_3_weighted_score = (persistent.lesson_3_quiz3/10 * 0.1) + (persistent.lesson_3_act3/10 * 0.1)

    $ lesson_1_weighted_score = lesson_1_weighted_score * 100
    $ lesson_2_weighted_score = lesson_2_weighted_score * 100
    $ lesson_3_weighted_score = lesson_3_weighted_score * 100

    $ exam_weighted_score = (exam_score/10 * 0.2)
    $ exam_weighted_score = exam_weighted_score * 100

    # Calculate weighted scores for each lesson ###############################################################################





    # Calculate overall grade #################################################################################################

    $ persistent.overall_grade = int(lesson_1_weighted_score + lesson_2_weighted_score + lesson_3_weighted_score + exam_weighted_score)

    $ quarter_result_feedback = ""
    # Quarter Assessment Result
    if persistent.overall_grade >= 70 and persistent.overall_grade > persistent.previous_overall_grade:
        $ quarter_result_feedback = "Congratulations on improving your overall result from the previous quarter!"

    elif persistent.overall_grade > 70 and persistent.overall_grade < persistent.previous_overall_grade:
        $ quarter_result_feedback = "While your overall grade is still good, it has decreased from the previous quarter. \nReflect on what might have caused this decline and consider adjustments for the \nnext quarter."

    else:
        $ quarter_result_feedback = "While your current result is commendable, strive for continuous improvement \nin the next quarter."


    # Calculate overall grade ###################################################################################################





    # For the bar graph #########################################################################################################

    $ persistent.written_works = (persistent.lesson_1_quiz1 + persistent.lesson_2_quiz2 + persistent.lesson_3_quiz3)/30
    $ persistent.written_works = int(persistent.written_works * 4.0)

    $ persistent.performance_task = (persistent.lesson_1_act1 + persistent.lesson_2_act2 + persistent.lesson_3_act3)/30
    $ persistent.performance_task = int(persistent.performance_task * 4.0)

    #$ persistent.exam = int(exam_score * 7.0)
    $ persistent.exam = exam_score

    # For the bar graph #########################################################################################################




    $ written_works_feedback = ""
    if persistent.written_works >= 6:
        $ written_works_feedback = "Excellent effort in Written Works, keep it up!"
    else:
        $ written_works_feedback = "Great job in Written Works. Your dedication is commendable!"

    $ performance_task_feedback = ""
    if persistent.performance_task >= 6:
        $ performance_task_feedback = "Outstanding performance in the Performance Task! Your skills are truly impressive."
    else:
        $ performance_task_feedback = "Great job on the Performance Task. Your efforts are making a positive impact!"

    $ exam_feedback = ""
    if persistent.exam >= 6:
        $ exam_feedback = "Congratulations on acing the exam! Your dedication to studying is evident."
    else:
        $ exam_feedback = "Great job on the exam! Your hard work is paying off."








    # Calculate behavior score
    $ behavior_score = persistent.ast1_recitation + persistent.ast1_participation + persistent.ast1_accuracy + persistent.ast1_kindness - persistent.ast1_rudeness

    $ behavior_fb_result = ""

    # Initialize additional grade
    $ additional_grade = 0

    # Determine if the player gets an additional grade based on Rudeness and Kindness
    if persistent.ast1_kindness > persistent.ast1_rudeness:
        $ additional_grade = 2
        $ behavior_fb_result = "Your kindness surpasses your rudeness, you receive an \nadditional 2 points!"
    elif persistent.ast1_rudeness > persistent.ast1_kindness:
        $ behavior_fb_result = "Work on improving your kindness. Unfortunately, you \ndon't receive an additional points"
        $ additional_grade = 0
    elif persistent.ast1_recitation > persistent.ast1_rudeness and persistent.ast1_participation > persistent.ast1_rudeness:
        $ behavior_fb_result = "You participated really well. You got an additional 5 points" 
    else:
        $ behavior_fb_result = "No Additional grade"

    # Calculate overall grade with additional behavior score
    #$ overall_2_grade -= additional_grade
    $ persistent.overall_grade += additional_grade

    call screen q1_assesment
    
    hide screen q1_assesment
    return


