


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
    blank "Wanna throw these 3 crumpled paper to out teacher?"
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

    jump opsl1_1

    
    return



label start_hitting_teach2:

    scene bg_classroom_
    show teach_smile
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




label start_hitting_teach4:

    scene bg_classroom_
    show teach_smile
    blank "Wanna throw these 3 crumpled paper to out teacher?"
    menu:
        "Let's go!":
            pass
        "Refuse":
            if persistent.rude_lesson == "four":
                jump l4Int4
            

    call begin_hunt4 from _call_begin_hunt4
    
    
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

    if persistent.rude_lesson == "four":
        jump opsl4_1
    else:
        pass

    
    return












label classmate_interaction:
    blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."

    menu:
        "Talk to him":
            "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
            jump aftermath
        "Refuse and explain that you can teach him later; choose to focus on the current lesson":
            $ kindness += 1
            $ Participation += 1
            "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
            jump aftermath

    label aftermath:
    # Additional code for the aftermath or consequences of the player's choice can go here.
    # This label can be used to handle any specific outcomes or events resulting from the player's decision.

    return




