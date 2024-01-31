


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
 

    blank "You will be back to the class for the activities"

    jump opsl1_1

    blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."

    menu:
        "Talk to him":
            "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
        "Refuse and explain that you can teach him later; choose to focus on the current lesson":
            $ kindness += 1
            $ Participation += 1
            "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
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


label recitation:

    menu:
        "Raise Hand":
            "Bakit ang kulit ni sir Jes?"
            menu: 
                "True":
                    $ Participation += 1
                    return or jump 
                "False":
                    $ Participation += 1
                    return or jump

        "Talk to your rude classmate":
            "Mapapalabas ka ng teacher then comeback sa activities na"
            return or jump

        "Play with your gamer classmate":
            "Jump several part ng lesson"
            return or jump

