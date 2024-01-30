# hf - HiddenFolks (hidden objects)
# used in conjunction with the 7dots.rpy module

# usage example:
init 1:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ hf_init("bg_garage", 5,
        ("battery", 1013, 705, _("Battery")),
        ("fleeb", 111, 560, _("Fleeb")),
        ("sbattery", 700, 615, _("Super Battery")),
        ("rserum", 1813, 161, _("Red Serum")),
        ("gserum", 355, 240, _("Green Serum")),
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
        w=200,
        h=200
    )




# then the game will be called:
    # $hf_start()
    
    # the number of uncollected items will be in hf_return

    # transform to move the tooltip
    transform hf_hint_at():
        anchor(.5, 1.25)
        function hf_hint_at_f

    # style for tooltip
    style hint_style is frame:
        # yellow background is stretched to fit the text
        background Frame("#fe9", 0, 0)
        # padding from edges to text
        xpadding 20
        ypadding 15

    # style for tooltip text
    style hint_style_text is text:
        color "#014"
        outlines []

init python:
    # automatic declaration of sprites (including webp)
    images_auto()

    # mouse coordinates
    def hf_hint_at_f(trans, st, at):
        trans.pos = renpy.get_mouse_pos()
        return 0

# SETTINGS
    # whether it is necessary to change the cursor when hovering
    hf_mouse = True

    # whether to display a tooltip
    hf_hint = False

    # True - found items are added to inventory
    # False - found items disappear from inventory
    # None - inventory is not displayed
    hf_inventory = None

    # transform for highlighting on hover
    # could be, for example, brightness(.05)
    hf_hover = None

    # name of the folder with game sprites in the images directory plus a space
    hf_dir = "game"

    # sizes of items in inventory
    hf_w, hf_h = 300, 300

    # timebar sizes
    hf_t_w, hf_t_h = 1040, 32

    # indentation of items from inventory edges
    hf_xpadding = 20
    hf_ypadding = 40

    # position of inventory window
    hf_xalign = .5
    hf_yalign = .05

    # timebar position
    hf_t_xalign = .5
    hf_t_yalign = .01

# INTERNAL VARIABLES
    # time in which to collect items
    hf_time = 5

    # time to reset for animation
    hf_bar = 100

    # game mode (False - background mode)
    hf_game_mode = False

    # items to find
    hf_needed = []

    # items that have already been found
    hf_picked = []

    # game background
    hf_back = "black"

    # whether the timebar needs to be repainted (a quarter of the time remains)
    hf_warning = False

    # number of uncollected items
    hf_return = 0

    # initial number of items
    hf_max_count = 0

    # game initialization
    def hf_init(bg, time, *args, **kwargs):
        global hf_needed, hf_picked, hf_back, hf_time, hf_bar, hf_max_count
        # reset lists and variables
        hf_needed = []
        hf_picked = []
        hf_back = bg
        hf_time = time
        hf_bar = 100
        # add items to be found to the list
        for item, x, y, h in args:
            hf_needed.append((item, x, y, h))
        hf_max_count = len(hf_needed)
        # use optional game parameters
        # essentially changing the values of similar variables,
        # but only they must start with hf_
        for k, v in kwargs.items():
            kk = "hf_" + k
            if kk in globals().keys():
                globals()[kk] = kwargs.get(k)

    # show the game as a background on the master layer
    def hf_bg():
        store.hf_game_mode = False
        show_s("HiddenFolks")

    # hide background game
    # but first show if the game screen is hidden
    def hf_hide():
        hf_bg()
        renpy.with_statement(None)
        hide_s("HiddenFolks")

    # start the game
    # if some effect is specified, then show the game with it first
    def hf_start(effect=None):
        store.hf_game_mode = False
        store.hf_warning = False
        hf_bg()
        renpy.with_statement(effect)
        store.hf_game_mode = True
        store.hf_return = len(hf_needed)
        renpy.call_screen("HiddenFolks")
        hf_bg()

    # click on an item (move it to inventory or remove it from there)
    def hf_click(item, x, y, h):
        store.hf_picked.append(store.hf_needed.pop(hf_needed.index((item, x, y, h))))
        splay("click")
        renpy.restart_interaction()
        # осталось собрать
        store.hf_return = len(hf_needed)
    HFClick = renpy.curry(hf_click)

    # change the timer color
    # or run the time decreasing animation
    def hf_go(warning=False):
        if warning:
            # change color
            store.hf_warning = True
        else:
            # start animation
            store.hf_bar = 0
        renpy.restart_interaction()
    HFGo = renpy.curry(hf_go)

    # get inventory sprite
    def hf_isprite(item):
        # if there is the required item in the inventory folder,
        # then we take it, otherwise we take what is on the screen
        i = hf_dir + " inventory " + item
        if has_image(i):
            item = i
        # get the sprite size of the item
        w, h = get_size(item)
        # zoom factors
        zoom = 1
        # if the object is larger than the cell, calculate a new zoom
        if w > hf_w or h > hf_h:
            # on the larger side
            if w > h:
                zoom = hf_w / w
            else:
                zoom = hf_h / h
        # return a sprite that fits the dimensions of the inventory cell
        return Transform(item, zoom=zoom)

    # hint text
    hf_hint_text = ""

    # change the tooltip text
    def hf_set_hint(t=""):
        if hf_hint and hf_hint_text != t:
            store.hf_hint_text = t
            renpy.restart_interaction()
    SetHint = renpy.curry(hf_set_hint)

screen HiddenFolks():
    # game background
    add hf_back

    # all items on the screen
    for i, x, y, h in hf_needed:

        $ item = hf_dir + " " + i
        # button item
        imagebutton:
            style "empty"
            # sprite the object
            idle item
            # position of the object (coordinates of its center)
            pos(x, y)
            # pixel hover
            focus_mask True
            # all actions are only in game mode
            if hf_game_mode:

                # change the cursor if necessary
                if hf_mouse:
                    mouse "hand"

                # if hover highlighting is enabled
                if not hf_hover is None:
                    # if there is a picture for the selected object, then display it
                    if has_image(item + " hover"):
                        hover item + " hover"
                    # otherwise highlight with the transform specified in the settings
                    else:
                        hover At(item, hf_hover)

                # change the tooltip text on hover
                hovered SetHint(h)
                unhovered SetHint()

                # handle clicks
                action HFClick(i, x, y, h)

    # timer animation
    if hf_game_mode and hf_time > 0:
        # activate timer
        timer .01 action HFGo()

        # bar recolor timer (one third of total time)
        timer hf_time * .6666 action HFGo(True)

        # visualization of the timer as a bar
        bar:
            # timebar position and size
            align(hf_t_xalign, hf_t_yalign)
            xysize(hf_t_w, hf_t_h)
            value AnimatedValue(hf_bar, 100, hf_time)

            # recoloring and flickering of the left bar strip,
            # when less than a third of time remains
            if hf_warning:
                left_bar Frame(At("gui/bar/left.png", paint2("#e02", "#e028", .2)), gui.bar_borders, tile=gui.bar_tile)

        # loss by timer
        timer hf_time repeat True action SetHint(), SPlay("gameover"), Return()

        # we've collected everything, let's leave (Return()() from def no longer works)
        if hf_return < 1:
            timer .01 repeat True action SetHint(), SPlay("gamewin"), Return()

        # inventory
        if not hf_inventory is None:
            # inventory frame
            frame:
                style "empty"
                xysize (hf_max_count * hf_w + hf_xpadding * 2, hf_h + hf_ypadding * 2)
                # inventory position
                align(hf_xalign, hf_yalign)
                background Frame("framei", 48, 48)
                # container for items
                hbox:
                    align(.5, .5)
                    # display collected items
                    if hf_inventory:
                        for item, x, y, h in hf_picked:
                            # xysize(hf_w, hf_h)
                            imagebutton idle hf_isprite(item) align(.5, .5):
                                # pixel hover
                                focus_mask True
                                action NullAction()
                                if hf_game_mode:
                                    # change the cursor if necessary
                                    if hf_mouse:
                                        mouse "hand"
                                    # change the tooltip text on hover
                                    hovered SetHint(h)
                                    unhovered SetHint()
                    # or display the items that remain to be collected
                    else:
                        for item, x, y, h in hf_needed:
                            imagebutton idle hf_isprite(item) align(.5, .5):
                                # pixel hover
                                focus_mask True
                                action NullAction()
                                if hf_game_mode:
                                    # change the cursor if necessary
                                    if hf_mouse:
                                        mouse "hand"
                                    # change the tooltip text on hover
                                    hovered SetHint(h)
                                    unhovered SetHint()

    # if necessary, display a hint
    if hf_hint and hf_hint_text:
        frame:
            style "hint_style"
            text hf_hint_text style "hint_style_text" align(.5, .5)
            at hf_hint_at()
