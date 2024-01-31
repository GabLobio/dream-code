image target:
    "hunt/target.png"
    zoom 0.5

image target_hit:
    "hunt/target_hit.png"
    zoom 0.5

transform moving_target: 
    ypos 540
    linear 3.0 xpos 1800
    xpos -300 
    repeat

default position = At(ImageReference("target"), moving_target)

label begin_hunt:
    
    $ shots_fired = 0
    $ targets_hit = 0      
    $ hits = 0
    call hunting from _call_hunting
    return
    
label hunting:
    $ cursor("metl")   
    scene bg_classroom_ 
    
    show expression position

    if targets_hit == 0:
        show target at moving_target
        $ position = At(ImageReference("target"), moving_target)
        show expression position
    else:
        show target_hit at moving_target
        $ position = At(ImageReference("target_hit"), moving_target)
        show expression position

    $ ui.imagebutton("hunt/crosshair.png", "hunt/crosshair_focused.png", clicked = ui.returns("fired"), xpos= 898, ypos = 787) 
    $ fired_gun = ui.interact()
    
    show expression position 
    if position.xpos > 820: 
        if position.xpos < 920: 
            play sound ("click.mp3") 
            with vpunch
            blank "Hit"
            $ shots_fired += 1
            $ targets_hit += 1
            if shots_fired >= 3:
                return()
            else:
                $ shots_fired += 1
                call hunting from _call_hunting_1
        else:
            with vpunch
            blank "You missed"
            $ shots_fired += 1
            if shots_fired >= 3:
                return()
    else:
        with vpunch
        blank "You missed, teacher Rodriguez looks at you disapprovingly."
        $ shots_fired += 1
        if shots_fired >= 3:
            return()
    
    call hunting from _call_hunting_2
    
    return


label begin_hunt2:
    
    $ shots_fired = 0
    $ targets_hit = 0      
    $ hits = 0
    call hunting2 from _call_hunting2
    return
    
label hunting2:
    $ cursor("metl")   
    scene bg_classroom_ 
    
    show expression position

    if targets_hit == 0:
        show target at moving_target
        $ position = At(ImageReference("target"), moving_target)
        show expression position
    else:
        show target_hit at moving_target
        $ position = At(ImageReference("target_hit"), moving_target)
        show expression position

    $ ui.imagebutton("hunt/crosshair.png", "hunt/crosshair_focused.png", clicked = ui.returns("fired"), xpos= 898, ypos = 787) 
    $ fired_gun = ui.interact()
    
    show expression position 
    if position.xpos > 820: 
        if position.xpos < 920: 
            play sound ("click.mp3") 
            with vpunch
            blank "Hit"
            $ shots_fired += 1
            $ targets_hit += 1
            if shots_fired >= 3:
                return()
            else:
                $ shots_fired += 1
                call hunting2 from _call_hunting_12
        else:
            with vpunch
            blank "You missed"
            $ shots_fired += 1
            if shots_fired >= 3:
                return()
    else:
        with vpunch
        blank "You missed, teacher Rodriguez looks at you disapprovingly."
        $ shots_fired += 1
        if shots_fired >= 3:
            return()
    
    call hunting2 from _call_hunting_22
    
    return


label begin_hunt3:
    
    $ shots_fired = 0
    $ targets_hit = 0      
    $ hits = 0
    call hunting3 from _call_hunting3
    return

label hunting3:
    $ cursor("metl")   
    scene bg_classroom_ 
    
    show expression position

    if targets_hit == 0:
        show target at moving_target
        $ position = At(ImageReference("target"), moving_target)
        show expression position
    else:
        show target_hit at moving_target
        $ position = At(ImageReference("target_hit"), moving_target)
        show expression position

    $ ui.imagebutton("hunt/crosshair.png", "hunt/crosshair_focused.png", clicked = ui.returns("fired"), xpos= 898, ypos = 787) 
    $ fired_gun = ui.interact()
    
    show expression position 
    if position.xpos > 820: 
        if position.xpos < 920: 
            play sound ("click.mp3") 
            with vpunch
            blank "Hit"
            $ shots_fired += 1
            $ targets_hit += 1
            if shots_fired >= 3:
                return()
            else:
                $ shots_fired += 1
                call hunting3 from _call_hunting_13
        else:
            with vpunch
            blank "You missed"
            $ shots_fired += 1
            if shots_fired >= 3:
                return()
    else:
        with vpunch
        blank "You missed, teacher Rodriguez looks at you disapprovingly."
        $ shots_fired += 1
        if shots_fired >= 3:
            return()
    
    call hunting3 from _call_hunting_23
    
    return