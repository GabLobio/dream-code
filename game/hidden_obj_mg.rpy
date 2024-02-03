define gui.text_outlines = [(4, "0124", 0, 0), (3, "0124", 0, 0), (1, "0124", 0, 0), (1, "0124", 0, 0)]



# Game starts here:
label begin_ho_mg:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg

        "Enough":
            pass

    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"

    $ hf_hide()
    with dissolve
    jump opsl1_2
    return()


label begin_ho_mg2:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg2

        "Enough":
            pass
    
    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"
    $ hf_hide()
    with dissolve
    jump opsl2_2

    return()


label begin_ho_mg3:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg3

        "Enough":
            pass

    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"
    $ hf_hide()
    with dissolve
    jump opsl3_2

    return()


label begin_ho_mg4:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg4

        "Enough":
            pass

    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"
    $ hf_hide()
    with dissolve
    jump opsl4_2

    return()



label begin_ho_mg5:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg5

        "Enough":
            pass
    
    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"
    $ hf_hide()
    with dissolve
    jump opsl5_2

    return()





label begin_ho_mg6:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg6

        "Enough":
            pass

    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"
    $ hf_hide()
    with dissolve
    jump opsl6_2

    return()




label begin_ho_mg7:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg7

        "Enough":
            pass

    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"
    $ hf_hide()
    with dissolve
    jump opsl7_2

    return()


label begin_ho_mg8:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg8

        "Enough":
            pass
    
    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"
    $ hf_hide()
    with dissolve
    jump opsl8_2

    return()




label begin_ho_mg9:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg9

        "Enough":
            pass
    
    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"
    $ hf_hide()
    with dissolve
    jump opsl9_2

    return()




label begin_ho_mg10:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ random_x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_y = renpy.random.randint(0, 1080)

    $ random_2x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_2y = renpy.random.randint(0, 1080)

    $ random_3x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_3y = renpy.random.randint(0, 1080)

    $ random_4x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_4y = renpy.random.randint(0, 1080)

    $ random_5x = renpy.random.randint(0, 1920)  # Adjust the range as needed
    $ random_5y = renpy.random.randint(0, 1080)

    $ hf_init("bg_garage", 10,
        ("battery", random_x, random_y, _("Battery")),
        ("fleeb", random_2x, random_2y, _("Fleeb")),
        ("sbattery", random_3x, random_3y, _("Super Battery")),
        ("rserum", random_4x, random_4y, _("Red Serum")),
        ("gserum", random_5x, random_5y, _("Green Serum")),
        # OPTIONAL PARAMETERS:
        # enable cursor change on hover
        mouse=True,
        # turn on the inventory and remove found items from it
        inventory=False,
        # disable tooltips
        hint=False,
        # enable item highlighting when hovering
        hover=brightness(.05),
        # reducing the size of inventory slots so that they don’t interfere with collecting items
        w=100,
        h=100
    )

    # we will show the figures on it along with the background
    $ hf_bg()
    with dissolve

    centered "{size=+24}{color=#ffa600}You need to collect all the items in 10 seconds.\nLet's start!" 

    # let's start the game
    $ hf_start()

    # hard pause so that the player stops clicking and does not miss the results
    $ renpy.pause(1, hard=True)

    # results
    if hf_return == 0:
        centered "{size=+24}{color=#ffa600}Hooray! All items have been collected!"
    else:
        centered "{size=+24}{color=#ffa600}GAME OVER\nNumber of items you missed : [hf_return]."

    menu:
        "Again":
            jump begin_ho_mg10

        "Enough":
            pass

    blank "Teacher Rodriguez caught you playing with your classmate. You will be back for the Quiz"
    $ hf_hide()
    with dissolve
    jump opsl10_2

    return()