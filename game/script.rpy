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
    $ boy = Character("{b} Boy {/b}",window_top_padding=50, window_left_padding=150, window_right_padding=150)
    $ girl = Character("{b} Girly {/b}",window_top_padding=50, window_left_padding=150, window_right_padding=150)

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

default persistent.rude_lesson = ""


default persistent.ast1_kindness = 0
default persistent.ast1_rudeness = 0 
default persistent.ast1_recitation = 0
default persistent.ast1_participation = 0
default persistent.ast1_accuracy = 0


default persistent.written_works = 0 
default persistent.performance_task = 0 #10 Screen 10 Problem
default persistent.exam = 0

# lesson 1
default persistent.lesson_1_quiz1 = 0
default persistent.lesson_1_act1 = 0

# Lesson 2 
default persistent.lesson_2_quiz2 = 0  # Written Works 10%
default persistent.lesson_2_act2 = 0  # Performance Task 10%

# Lesson 3 
default persistent.lesson_3_quiz3 = 0  # Written Works 10%
default persistent.lesson_3_act3 = 0  # Performance Task 10%

default persistent.exam_score = 0 # Exam 20%

#default persistent.lesson_1_weighted_score = 0
#default persistent.lesson_2_weighted_score = 0
#default persistent.lesson_3_weighted_score = 0

default persistent.overall_grade = 0
default persistent.previous_overall_grade = 0



# 2nd Quarter ######################################

default persistent.ast2_kindness = 5
default persistent.ast2_rudeness = 5 
default persistent.ast2_recitation = 0
default persistent.ast2_participation = 0
default persistent.ast2_accuracy = 0


default persistent.q2_written_works = 0 
default persistent.q2_performance_task = 0 #10 Screen 10 Problem
default persistent.q2_exam = 0

# lesson 4
default persistent.lesson_4_quiz4 = 0
default persistent.lesson_4_act4 = 0

# Lesson 5 
default persistent.lesson_5_quiz5 = 0  # Written Works 10%
default persistent.lesson_5_act5 = 0  # Performance Task 10%

# Lesson 6 
default persistent.lesson_6_quiz6 = 0  # Written Works 10%
default persistent.lesson_6_act6 = 0  # Performance Task 10%

default persistent.q2_exam_score = 0 # Exam 20%

#default persistent.lesson_4_weighted_score = 0
#default persistent.lesson_5_weighted_score = 0
#default persistent.lesson_6_weighted_score = 0

default persistent.q2_overall_grade = 0
default persistent.q2_previous_overall_grade = 0



# 3rd Quarter ######################################

default persistent.ast3_kindness = 0
default persistent.ast3_rudeness = 0 
default persistent.ast3_recitation = 0
default persistent.ast3_participation = 0
default persistent.ast3_accuracy = 0


default persistent.q3_written_works = 0 
default persistent.q3_performance_task = 0 #10 Screen 10 Problem
default persistent.q3_exam = 0

# lesson 7
default persistent.lesson_7_quiz7 = 0
default persistent.lesson_7_act7 = 0

# Lesson 8 
default persistent.lesson_8_quiz8 = 0  # Written Works 10%
default persistent.lesson_8_act8 = 0  # Performance Task 10%

# Lesson 9 
default persistent.lesson_9_quiz9 = 0  # Written Works 10%
default persistent.lesson_9_act9 = 0  # Performance Task 10%

default persistent.q3_exam_score = 0 # Exam 20%

#default persistent.lesson_4_weighted_score = 0
#default persistent.lesson_5_weighted_score = 0
#default persistent.lesson_6_weighted_score = 0

default persistent.q3_overall_grade = 0
default persistent.q3_previous_overall_grade = 0 



# 4th Quarter ######################################

default persistent.ast4_kindness = 0
default persistent.ast4_rudeness = 0 
default persistent.ast4_recitation = 0
default persistent.ast4_participation = 0
default persistent.ast4_accuracy = 0


default persistent.q4_written_works = 0 
default persistent.q4_performance_task = 0 #10 Screen 10 Problem
default persistent.q4_exam = 0

# lesson 7
default persistent.lesson_10_quiz10 = 0
default persistent.lesson_10_act10 = 0

default persistent.q4_exam_score = 0 # Exam 20%

default persistent.q4_overall_grade = 0
default persistent.q4_previous_overall_grade = 0 


########## ENDING GENERAL WEIGHTED AVERAGE #####

default persistent.all_lesson_done = False
default persistent.gwa = 0

default persistent.total_kind = 0
default persistent.total_rude = 0

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
    #show screen totaltimeplayedbutton
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
