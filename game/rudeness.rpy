


init python:
    def cursor(name = None):
        if name:
            config.mouse = {'default' : [('images/cursor_' + name + '.png', 0, 0)]}
        else:
            config.mouse = None
    Cursor = renpy.curry(cursor)

label start_hitting_teach:

    scene bg_classroom_
    show teach_smile

    # Ito inaaya nya yung player 
    blank "Wanna throw these 3 crumpled paper to our teacher?"
    menu:
        "Let's go!":
            pass
        "Refuse":
            jump l1Int1

    call begin_hunt from _call_begin_hunt
    
    
    if targets_hit == 0: 
        $ cursor() 
        scene bg_classroom_ with dissolve
        show teach_smile
        blank "Let's do it again some time"
        scene bg_classroom_ with dissolve
        show teach_smile
        
    if targets_hit > 0: 
        $ cursor() 
        blank "[targets_hit]/3 hit"
        scene bg_classroom_ with dissolve
        show teacher_crossarm_sad

        # T
        blank "Ouch! You hit the teacher! You have to leave the class for a while."   
 

    blank "You will be back to the class for the quiz"

    jump opsl1_1

    
    return



label start_hitting_teach2:

    scene bg_classroom_
    show teach_smile
    # Ito inaaya nya yung player 
    blank "Wanna throw these 3 crumpled paper to out teacher?"
    menu:
        "Let's go!":
            pass
        "Refuse":
            jump l2Int2

    call begin_hunt2 from _call_begin_hunt2
    
    
    if targets_hit == 0: 
        $ cursor() 
        scene bg_classroom_ with dissolve
        show teach_smile
        blank "Let's do it some time"
        scene bg_classroom_ with dissolve
        show teach_smile
        
    if targets_hit > 0: 
        $ cursor() 
        blank "[targets_hit]/3 hit"
        scene bg_classroom_ with dissolve
        show teacher_crossarm_sad
        blank "Ouch! You hit the teacher! You have to leave the class for a while."   
 

    blank "You will be back to the class for the quiz"

    jump opsl2_1

    
    return


label start_hitting_teach3:

    scene bg_classroom_
    show teach_smile
    # Ito inaaya nya yung player 
    blank "Wanna throw these 3 crumpled paper to out teacher?"
    menu:
        "Let's go!":
            pass
        "Refuse":
            if persistent.rude_lesson == "three":
                jump l3Int3
            elif persistent.rude_lesson == "four":
                jump l4Int4
            elif persistent.rude_lesson == "five":
                jump l5Int5
            elif persistent.rude_lesson == "six":
                jump l6Int6
            elif persistent.rude_lesson == "seven":
                jump l7Int7
            elif persistent.rude_lesson == "eight":
                jump l8Int8
            elif persistent.rude_lesson == "nine":
                jump l9Int9
            elif persistent.rude_lesson == "ten":
                jump l10Int10
            else:
                pass

    call begin_hunt3 from _call_begin_hunt3
    
    
    if targets_hit == 0: 
        $ cursor() 
        scene bg_classroom_ with dissolve
        show teach_smile
        blank "Let's do it some time"
        scene bg_classroom_ with dissolve
        show teach_smile
        
    if targets_hit > 0: 
        $ cursor() 
        blank "[targets_hit]/3 hit"
        scene bg_classroom_ with dissolve
        show teacher_crossarm_sad
        blank "Ouch! You hit the teacher! You have to leave the class for a while."   
 

    blank "You will be back to the class for the quiz"

    if persistent.rude_lesson == "three":
        jump opsl3_1
    elif persistent.rude_lesson == "four":
        jump opsl4_1
    elif persistent.rude_lesson == "five":
        jump opsl5_1
    elif persistent.rude_lesson == "six":
        jump opsl6_1
    elif persistent.rude_lesson == "seven":
        jump opsl7_1
    elif persistent.rude_lesson == "eight":
        jump opsl8_1
    elif persistent.rude_lesson == "nine":
        jump opsl9_1
    elif persistent.rude_lesson == "ten":
        jump opsl10_1
    else:
        pass
    
    return















label classmate_interaction:
    blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."
    # Dialogue to nung kaklaseng nyang boy
    "Hey, mind lending a hand? I'm a bit lost with some of the words the teacher just used. Could you help me catch up on what I missed? I'd appreciate it, and maybe we can quickly go through it together so we don't fall too behind."

    menu:
        "Talk to him":
            blank "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
            $ persistent.ast1_kindness = 50
            jump aftermath
        "Refuse and explain that you can teach him later; choose to focus on the current lesson":
            blank "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
            $ persistent.ast1_kindness = 50
            jump aftermath






