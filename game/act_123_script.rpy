





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