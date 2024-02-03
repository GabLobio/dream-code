





label l11_act1:

    scene activity1
    
    $ persistent.lesson_1_act1 = 0


    $ l1p1 = renpy.input("1.)                            ", length=32,)
    

    if l1p1 == "h1":
        play sound ("correct.mp3") 
        $ persistent.lesson_1_act1 += 2
        blank "Correct"
    else:
        play sound ("wrong.mp3") 
        blank "Incorrect"
        pass


    $ l1p2 = renpy.input("2.)                            ", length=32,)
    

    if l1p2 == "h2":
        play sound ("correct.mp3") 
        $ persistent.lesson_1_act1 += 2
        blank "Correct"
    else:
        play sound ("wrong.mp3") 
        blank "Incorrect"
        pass


    $ l1p3 = renpy.input("3.)                            ", length=32,)
    

    if l1p3 == "/h3":
        play sound ("correct.mp3") 
        $ persistent.lesson_1_act1 += 2
        blank "Correct"
    else:
        play sound ("wrong.mp3") 
        blank "Incorrect"
        pass


    $ l1p4 = renpy.input("4.)                            ", length=32,)
    

    if l1p4 == "h4":
        play sound ("correct.mp3") 
        $ persistent.lesson_1_act1 += 2
        blank "Correct"
    else:
        play sound ("wrong.mp3") 
        blank "Incorrect"
        pass


    $ l1p5 = renpy.input("5.)                            ", length=32,)
    

    if l1p5 == "<h5>":
        play sound ("correct.mp3") 
        $ persistent.lesson_1_act1 += 2
        blank "Correct"
    else:
        play sound ("wrong.mp3") 
        blank "Incorrect"
        pass


    blank "Your lesson 1 activity score is [persistent.lesson_1_act1]"
    return




label l1_act1:
    $ persistent.lesson_1_act1 = 0

    call screen l1act1

    label l1_act1_f:

        blank "Your Lesson 1 activity score is [persistent.lesson_1_act1]"

    return


label l2_act2:
    $ persistent.lesson_2_act2 = 0

    call screen l2act2

    label l2_act2_f:

        blank "Your Lesson 2 activity score is [persistent.lesson_2_act2]"

    return


label l3_act3:
    $ persistent.lesson_3_act3 = 0

    call screen l3act3

    label l3_act3_f:

        blank "Your Lesson 3 activity score is [persistent.lesson_3_act3]"

    return


label l4_act4:
    $ persistent.lesson_4_act4 = 0

    call screen l4act4

    label l4_act4_f:

        blank "Your Lesson 4 activity score is [persistent.lesson_4_act4]"

    return



label l5_act5:
    $ persistent.lesson_5_act5 = 0

    call screen l5act5

    label l5_act5_f:

        blank "Your Lesson 5 activity score is [persistent.lesson_5_act5]"

    return



label l6_act6:
    $ persistent.lesson_6_act6 = 0

    call screen l6act6

    label l6_act6_f:

        blank "Your Lesson 6 activity score is [persistent.lesson_6_act6]"

    return


label l7_act7:
    $ persistent.lesson_7_act7 = 0

    call screen l7act7

    label l7_act7_f:

        blank "Your Lesson 7 activity score is [persistent.lesson_7_act7]"

    return



label l8_act8:
    $ persistent.lesson_8_act8 = 0

    call screen l8act8

    label l8_act8_f:

        blank "Your Lesson 8 activity score is [persistent.lesson_8_act8]"

    return

label l9_act9:
    $ persistent.lesson_9_act9 = 0

    call screen l9act9

    label l9_act9_f:

        blank "Your Lesson 9 activity score is [persistent.lesson_9_act9]"

    return


label l10_act10:
    $ persistent.lesson_10_act10 = 0

    call screen l10act10

    label l10_act10_f:

        blank "Your Lesson 10 activity score is [persistent.lesson_10_act10]"

    return