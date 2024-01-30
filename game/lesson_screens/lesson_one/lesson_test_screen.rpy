screen drag_drop:
    # image "images/places/bg_garage_zoom.webp" blur 10.0

    frame:
        xpadding 40
        ypadding 20
        xpos 100
        ypos 100
        textbutton "Run":
            if p_tag_was_dropped == True and html_tag_was_dropped == True:
                action Jump("thanks")  # Replace "some_label" with the label you want to jump to.
            else:
                action Jump("first_quiz")

    draggroup:
        drag:
            xpos 880
            ypos 680
            
            drag_raise True
            drag_name "pTag"
            dragged dragged_func
            default wasDropped = False
            text "<p>" size 25 color "#103d70" # Solid("#ff9b94") xysize(250, 250)
            
        
        drag:
            xpos 1020
            ypos 680
            
            drag_raise True
            drag_name "htmlTag"
            dragged dragged_func
            default wasDropped = False
            image  "images/chp_one/html_tag.png" xysize(58, 22)

        # Drop Place
        drag:
            xpos 1230
            ypos 680
            drag_raise True
            drag_name "hTagPlace"
            draggable False
            dragged dragged_func
            image  "images/chp_one/p_tag_place.png" xysize(48, 25)

        drag:
            xpos 829
            ypos 515
            drag_raise True
            drag_name "pTagPlace"
            draggable False
            dragged dragged_func
            image  "images/chp_one/p_tag_place.png" xysize(48, 25)

        drag:
            xpos 787
            ypos 322
            drag_raise True
            drag_name "htmlTagPlace"
            draggable False
            dragged dragged_func
            image  "images/chp_one/html_tag_place.png" xysize(58, 22)