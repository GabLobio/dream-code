init: 
    # This is where the standard animated background imagemap used for all quizes is declared
    image quiz_animated_countdown_timer = Animation("assets_quiz/quiz_window_idle_29.jpg", 1.00,"assets_quiz/quiz_window_idle_28.jpg", 1.00,"assets_quiz/quiz_window_idle_27.jpg", 1.00,"assets_quiz/quiz_window_idle_26.jpg", 1.00,"assets_quiz/quiz_window_idle_25.jpg", 1.00,"assets_quiz/quiz_window_idle_24.jpg", 1.00,"assets_quiz/quiz_window_idle_23.jpg", 1.00,"assets_quiz/quiz_window_idle_22.jpg", 1.00,"assets_quiz/quiz_window_idle_21.jpg", 1.00,"assets_quiz/quiz_window_idle_20.jpg", 1.00,"assets_quiz/quiz_window_idle_19.jpg", 1.00,"assets_quiz/quiz_window_idle_18.jpg", 1.00,"assets_quiz/quiz_window_idle_17.jpg", 1.00,"assets_quiz/quiz_window_idle_16.jpg", 1.00,"assets_quiz/quiz_window_idle_15.jpg", 1.00,"assets_quiz/quiz_window_idle_14.jpg", 1.00,"assets_quiz/quiz_window_idle_13.jpg", 1.00,"assets_quiz/quiz_window_idle_12.jpg", 1.00,"assets_quiz/quiz_window_idle_11.jpg", 1.00,"assets_quiz/quiz_window_idle_10.jpg", 1.00,"assets_quiz/quiz_window_idle_09.jpg", 1.00,"assets_quiz/quiz_window_idle_08.jpg", 1.00,"assets_quiz/quiz_window_idle_07.jpg", 1.00,"assets_quiz/quiz_window_idle_06.jpg", 1.00,"assets_quiz/quiz_window_idle_05.jpg", 1.00,"assets_quiz/quiz_window_idle_04.jpg", 1.00,"assets_quiz/quiz_window_idle_03.jpg", 1.00,"assets_quiz/quiz_window_idle_02.jpg", 1.00,"assets_quiz/quiz_window_idle_01.jpg", 1.00,"assets_quiz/quiz_window_idle_00.jpg", 10000000000000000.0,) 
    # This counts all the correct answer from all the quizes
    $ persistent_quiz_total_points_counter_correct_answer = 0
    #$ final_test_undertaken = False

    image quiz_window_blank = "assets_quiz/quiz_window_blank.jpg"
    image quiz_next_question = "assets_quiz/next_question.png"
    image quiz_start = "assets_quiz/quiz_start.png"
    image blank_question_windows = "assets_quiz/blank_question_windows.png"
    image times_up = "assets_quiz/times_up.png"

    image pie_10 = "assets_quiz/pie_quiz_10.jpg"
    image pie_09 = "assets_quiz/pie_quiz_09.jpg"
    image pie_08 = "assets_quiz/pie_quiz_08.jpg"
    image pie_07 = "assets_quiz/pie_quiz_07.jpg"
    image pie_06 = "assets_quiz/pie_quiz_06.jpg"
    image pie_05 = "assets_quiz/pie_quiz_05.jpg"
    image pie_04 = "assets_quiz/pie_quiz_04.jpg"
    image pie_03 = "assets_quiz/pie_quiz_03.jpg"
    image pie_02 = "assets_quiz/pie_quiz_02.jpg"
    image pie_01 = "assets_quiz/pie_quiz_01.jpg"
    image pie_00 = "assets_quiz/pie_quiz_00.jpg"

    image bawal_background = "assets_quiz/background_quiz_01.jpg"

init:
    $ whole_quiz_00_seen = False
    $ whole_quiz_01_seen = False
    $ whole_quiz_02_seen = False
    $ whole_quiz_03_seen = False
    $ whole_quiz_04_seen = False
    $ whole_quiz_05_seen = False
    $ whole_quiz_06_seen = False
    $ whole_quiz_07_seen = False
    $ whole_quiz_08_seen = False
    $ whole_quiz_09_seen = False
