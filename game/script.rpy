##  ╔═════════════════════════════════════════════════════════════════════════════╗
##  ║ ███  DIALOGUE FRAME                                                     ███ ║
##  ║ ███  This is the section responsible for the dialogue frame             ███ ║
##  ╚═════════════════════════════════════════════════════════════════════════════╝
init -1 python hide:
    style.window.background = Frame("assets_gui/gui_frame.png", 0, 0)
    style.window.left_padding = 0
    style.window.right_padding = 0
    style.window.top_padding = 0
    style.window.xminimum = 1920
    style.window.yminimum = 343
    style.window.xpos = 0
    style.window.ypos = 736
  
    style.default.size = 40
    style.say_dialogue.size = 40
    style.say_dialogue.xpos = 0
    style.say_dialogue.ypos = 0
    style.say_thought.size = 40
    style.say_thought.xpos = 40

#screen input:
    #window:
        #background None # otherwise, the ordinary textbox image will be used
        #yfill True # to stretch the textbox vertically
        #has vbox xalign 0.5 yalign 0.5 # centers the text onscreen

        #text prompt xalign 0.5 # forces this text to stay at center of line
        #input id "input"   


##  ╔═════════════════════════════════════════════════════════════════════════════╗
##  ║ ███  CHARACTER DECLARATION                                              ███ ║
##  ║ ███  This is the section responsible for declaring characters           ███ ║
##  ╚═════════════════════════════════════════════════════════════════════════════╝
init:
    # Use this one for blank / no name / narration
    $ blank = Character('',window_top_padding=50, window_left_padding=150, window_right_padding=150) 
    #$ POV = Character("{b}[povname]{/b}",window_top_padding=50, window_left_padding=150, window_right_padding=150)
    $ Dad = Character('{b}Dad{/b}',window_top_padding=50, window_left_padding=150, window_right_padding=150)
    $ Mom = Character('{b}Mom{/b}',window_top_padding=50, window_left_padding=150, window_right_padding=150)
    $ Tech = Character('{b}Mrs. Rodriguez{/b}',window_top_padding=50, window_left_padding=150, window_right_padding=150)
    $ Someone = Character('{b}Someone{/b}',window_top_padding=50, window_left_padding=150, window_right_padding=150)
    default POVclass = Character("{b}[persistent.POV] and Class {/b}",window_top_padding=50, window_left_padding=150, window_right_padding=150)
    $ Classmate = Character("{b}Classmate {/b}",window_top_padding=50, window_left_padding=150, window_right_padding=150)
    $ Maria = Character("{b}Maria{/b}",window_top_padding=50, window_left_padding=150, window_right_padding=150)
    $ MomAndDad = Character("{b}Mom and Dad{/b}",window_top_padding=50, window_left_padding=150, window_right_padding=150)
    $ e = Character("{b} Mrs. Rodriguez {/b}",window_top_padding=50, window_left_padding=150, window_right_padding=150)

    #$ persistent.final_test_undertaken = False




init python:
    import datetime

    persistent.date_today = datetime.date.today()
    

    if not persistent.runtime:
        persistent.runtime = 0

    persistent.ots_runtime = 0

    def calc_total_run():
        persistent.runtime += renpy.get_game_runtime()
        renpy.clear_game_runtime()

    def reset_timer():
        persistent.runtime = 0
        renpy.clear_game_runtime()

    def save_total_run():
        persistent.ots_runtime += persistent.runtime
        renpy.clear_game_runtime()

    renpy.restart_interaction()


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define POV = Character("[povname]")
#define POVclass = Character("[povname] and Class")
#define Dad = Character("DAD")
#define Mom = Character("MOM")
#define Tech = Character("Mrs. Rodriguez")
#define Someone = Character ("Someone")
#define Classmate =Character ("Classmate")
#define Maria = Character ("Maria")
#define MomAndDad = "Mom And Dad"
#define e = Character("Mrs. Rodriguez")
default POV = Character("{b}[persistent.POV]{/b}",window_top_padding=50, window_left_padding=150, window_right_padding=150)


# The game starts here.
default lesson_one_finish = False
default lesson_two_finish = False
default lesson_three_finish = False
default lesson_four_finish = False
default lesson_five_finish = False
default lesson_six_finish = False
default lesson_seven_finish = False
default lesson_eight_finish = False
default lesson_nine_finish = False
default lesson_ten_finish = False

default numhc = 0
default numc = 50
default numic = 0

default ls1_numhc = 0
default ls1_numc = 0
default ls1_numic = 0
default l1_takes = 0

default ls2_numhc = 0
default ls2_numc = 0
default ls2_numic = 0
default l2_takes = 0

default ls3_numhc = 0
default ls3_numc = 0
default ls3_numic = 0
default l3_takes = 0

default ls4_numhc = 0
default ls4_numc = 0
default ls4_numic = 0
default l4_takes = 0

default ls5_numhc = 0
default ls5_numc = 0
default ls5_numic = 0
default l5_takes = 0

default persistent.f_numhc = 0
default persistent.f_numc = 0
default persistent.f_numic = 0
default persistent.f_ttime = ""

default persistent.hours = 0
default persistent.minutes = 0
default persistent.seconds = 0




###################################### New Computation ######################################



default persistent.ast1_kindness = 0
default persistent.ast1_rudeness = 0 
default persistent.ast1_recitation = 0
default persistent.ast1_participation = 0
default persistent.ast1_accuracy = 0


default persistent.written_works = 0 
default persistent.performance_task = 0 #10 Screen 10 Problem
default persistent.exam = 0

###################################### New Computation ######################################





screen totaltimeplayedbutton():
    $ calc_total_run()
    $ minute, second = divmod(int(persistent.ots_runtime), 60)
    $ hour, minute = divmod(minute, 60)
    $ persistent.f_ttime = "{:02}:{:02}:{:02}".format(hour, minute, second)

    vbox:
        xpos 0
        ypos 0
        text "[persistent.f_ttime]" size 10


label start:
    show screen totaltimeplayedbutton
    $ persistent.f_numhc = 5
    $ persistent.f_numc = 0
    $ persistent.f_numic = 5

    
    
    transform moving_points:
        zoom 0.0
        align (0.5, 0.5)
        alpha 0.0
        parallel:
            linear 0.5 zoom 1.0
            linear 0.5 zoom 0.9
            repeat
        parallel:
            linear 1.0 alpha 1.0
        
    transform spinner_base:
        zoom 0.0
        align (0.5, 0.5)
        rotate 0.0
        alpha 0.0
        parallel:
            linear 1.0 rotate 360
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 alpha 1.0
    
    transform spinner_data:
        zoom 0.0
        align (0.5, 0.5)
        rotate 0.0
        alpha 0.0
        parallel:
            linear 1.0 rotate 360
        parallel:
            pause 1.0
            linear 0.5 zoom 1.0
        parallel:
            linear 2.0 alpha 1.0
                
    transform spinner_labels:
        zoom 0.0
        align (0.5, 0.5)
        alpha 0.0
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 alpha 1.0

    #call screen chp_one_assessment
    #jump lessonNineFillFive
    $ persistent.gameplay_started = True
    scene bg p
    
    $ show_quick_menu = False
    $ persistent.POV = renpy.input("What is your full name?", length=32 )

    $ show_quick_menu = True
    POV "Your name is [persistent.POV]"

    ## ╔════════════════════════╗
    ## ║ temporary please erase ║
    ## ╚════════════════════════╝ 

    $ persistent.ast1_kindness = 10
    $ persistent.ast1_rudeness = 0
    $ persistent.ast1_recitation = 0
    $ persistent.ast1_participation = 0
    $ persistent.ast1_accuracy = 0

    $ persistent.written_works = 7 
    $ persistent.performance_task = 4 #10 Screen 10 Problem
    $ persistent.exam = 8

    #jump assessment_one 
    #jump lesson_two






    # Lesson 1 
    $ lesson_1_quiz1 = 5  # Written Works 20%
    $ lesson_1_act1 = 6  # Performance Task 20%

    # Lesson 2 
    $ lesson_2_quiz2 = 8  # Written Works 10%
    $ lesson_2_act2 = 4  # Performance Task 10%

    # Lesson 3 
    $ lesson_3_quiz3 = 10  # Written Works 10%
    $ lesson_3_act3 = 7  # Performance Task 10%

    $ exam_score = 10 # Exam 20%

    # Calculate weighted scores for each lesson
    $ lesson_1_weighted_score = (lesson_1_quiz1/10 * 0.2) + (lesson_1_act1/10 * 0.2)
    $ lesson_2_weighted_score = (lesson_2_quiz2/10 * 0.1) + (lesson_2_act2/10 * 0.1)
    $ lesson_3_weighted_score = (lesson_3_quiz3/10 * 0.1) + (lesson_3_act3/10 * 0.1)

    $ lesson_1_weighted_score = lesson_1_weighted_score * 100
    $ lesson_2_weighted_score = lesson_2_weighted_score * 100
    $ lesson_3_weighted_score = lesson_3_weighted_score * 100

    $ exam_weighted_score = (exam_score/10 * 0.2)
    $ exam_weighted_score = exam_weighted_score * 100

    # Calculate overall grade
    $ overall_grade = int(lesson_1_weighted_score + lesson_2_weighted_score + lesson_3_weighted_score + exam_weighted_score)
    

    # Display the results
    blank "Lesson 1 Weighted Score: [lesson_1_weighted_score]"
    blank "Lesson 2 Weighted Score: [lesson_2_weighted_score]"
    blank "Lesson 3 Weighted Score: [lesson_3_weighted_score]"
    blank "Exam Weighted Score: [exam_weighted_score]"
    blank "Overall Grade: [overall_grade]"


        # Lesson 1 
    $ lesson_4_quiz4 = 8  # Written Works 20%
    $ lesson_4_act4 = 8  # Performance Task 20%

    # Lesson 2 
    $ lesson_5_quiz5 = 8  # Written Works 10%
    $ lesson_5_act5 = 8  # Performance Task 10%

    # Lesson 3 
    $ lesson_6_quiz6 = 8  # Written Works 10%
    $ lesson_6_act6 = 8  # Performance Task 10%

    $ exam_2_score = 8 # Exam 20%

    # Calculate weighted scores for each lesson
    $ lesson_4_weighted_score = (lesson_4_quiz4/10 * 0.2) + (lesson_4_act4/10 * 0.2)
    $ lesson_5_weighted_score = (lesson_5_quiz5/10 * 0.1) + (lesson_5_act5/10 * 0.1)
    $ lesson_6_weighted_score = (lesson_6_quiz6/10 * 0.1) + (lesson_6_act6/10 * 0.1)

    $ lesson_4_weighted_score = lesson_4_weighted_score * 100
    $ lesson_5_weighted_score = lesson_5_weighted_score * 100
    $ lesson_6_weighted_score = lesson_6_weighted_score * 100

    $ exam_2_weighted_score = (exam_2_score/10 * 0.2)
    $ exam_2_weighted_score = exam_2_weighted_score * 100

    # Calculate overall grade
    $ overall_2_grade = int(lesson_4_weighted_score + lesson_5_weighted_score + lesson_6_weighted_score + exam_2_weighted_score)
    

    # Display the results
    blank "Lesson 1 Weighted Score: [lesson_4_weighted_score]"
    blank "Lesson 2 Weighted Score: [lesson_5_weighted_score]"
    blank "Lesson 3 Weighted Score: [lesson_6_weighted_score]"
    blank "Exam Weighted Score: [exam_2_weighted_score]"
    blank "Overall Grade: [overall_2_grade]"


    jump chapter_1_01



##  ╔══════════════════════════════════════════════════════╗
##  ║ ███  Chapter 1                                  ███  ║
##  ╚══════════════════════════════════════════════════════╝ 

label chapter_1_01:



    play music "audio/sa_town.mp3" volume 0.5

    scene bg town with fade

    blank "In the town of Webville "
    scene bg office with fade

    blank "[persistent.POV] loved watching his dad, who made cool websites ."
    scene mouth_shot with fade
    POV "I want to make websites too, Dad!" 
    blank "[persistent.POV] said one day"
    scene bg_school with fade

    blank "[persistent.POV]'s school started a class about making websites."
    #blank "They started with HTML, the basic stuff that makes websites work."
    
    stop music fadeout 1.0

    


    play music "audio/sa_tech.mp3" volume 0.5

label lesson_choices:

    menu:
        "Start Lesson":
            call screen lesson_ui
    






    #Game End


label ending:
    if persistent_quiz_total_points_counter_correct_answer >= 75:
        e"sorry you didn't pass this course better luck next time"
        $ persistent.final_test_undertaken = True
        e "graduate ka na!!!"  
        $ renpy.full_restart()
    elif persistent_quiz_total_points_counter_correct_answer == 75:
        e"You pass this course" 
        $ persistent.final_test_undertaken = True
        e "graduate ka na!!!" 
        $ renpy.full_restart()
    else:
        e"Bagsak ka"
        $ persistent.final_test_undertaken = True
        e "DIIIIIII KA graduate ka na!!!" 
        $ renpy.full_restart()







    return
