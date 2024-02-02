


    #$ blank = Character('',window_top_padding=50, window_left_padding=150, window_right_padding=150 )

#██▓▒░ IMAGEMAP MAIN MENU ░▒▓█████████████████████████████████████ 
#This block is responsible for the Imagemap based main menu
screen main_menu:
    tag menu
    imagemap:
        ground 'assets_gui/gui_main_menu.jpg'
        hover 'assets_gui/gui_main_menu.jpg'
        
        hotspot (1486, 166, 282, 92) action Start() 
        hotspot (1486, 284, 282, 92) action ShowMenu('load') 
        hotspot (1486, 403, 282, 92) action ShowMenu('preferences') 
        hotspot (1486, 516, 191, 67) action Start('tawag_mga_leson') #insert lesson label here
        hotspot (1486, 632, 191, 67) action Start('quiz_menu_screen_debug') #insert progress label here
        hotspot (1486, 760, 191, 67) action ShowMenu('about_credits') #insert about label here
        hotspot (1486, 877, 282, 92) action Quit(confirm=False) 

label main_menu_call_from_progress:
    $ renpy.full_restart()





#██▓▒░ IMAGEMAP PREFERENCES ░▒▓███████████████████████████████████ 
#This block is responsible for the Imagemap based main menu

screen preferences:
    tag menu
    
    imagemap:
        ground 'assets_gui/imagemap_config_ground.jpg'
        idle 'assets_gui/imagemap_config_idle.png'
        hover 'assets_gui/imagemap_config_hover.png'
        selected_idle 'assets_gui/imagemap_config_selected_idle.png'
        selected_hover 'assets_gui/imagemap_config_selected_hover.png'

        hotbar (98, 245, 1698, 111) value Preference('music volume') 
        hotbar (98, 543, 1698, 111) value Preference('sound volume') 

        hotspot (465, 934, 199, 95) action ShowMenu('save')
        hotspot (688, 934, 199, 95) action ShowMenu('load')
        hotspot (919, 934, 283, 95) action Return()
        hotspot (1230, 934, 390, 95) action MainMenu() 
        hotspot (1649, 934, 186, 95) action Quit(confirm=False)  














#██▓▒░ IMAGEMAP SAVE / LOAD SCREEN ░▒▓███████████████████████████████████ 
#This block is responsible for the Imagemap based main menu
# This represents a load/save slot. You should customize this to ensure
# that the placement of the thumbnail and the slot text are as desired.
# All positions are relative to the hotspot the slot is inside.

# This represents a load/save slot. You should customize this to ensure
# that the placement of the thumbnail and the slot text are as desired.
# All positions are relative to the hotspot the slot is inside.

screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    add FileScreenshot(number) xpos 80 ypos 80
    text file_text xpos 80 ypos 20 size 30
 
screen load:
    
    tag menu
    
    imagemap:
        ground 'assets_gui/imagemap_load_ground.jpg'
        idle 'assets_gui/imagemap_load_idle.png'
        hover 'assets_gui/imagemap_load_hover.png'
        selected_idle 'assets_gui/imagemap_load_selected_idle.png'
        selected_hover 'assets_gui/imagemap_load_selected_hover.png'

        #hotspot (-1, -1, -1, -1) action FilePage('auto')
        #hotspot (46, 104, 127, 115) action FilePage(1) hover_sound "sfx/click.wav"
        #hotspot (46, 228, 127, 115) action FilePage(2) hover_sound "sfx/click.wav"
        #hotspot (46, 353, 127, 115) action FilePage(3) hover_sound "sfx/click.wav"

        hotspot (98, 280, 750, 485) action FileAction(0): 
            use load_save_slot(number=0) 
        #hotspot (195, 228, 498, 115) action FileAction(1):
            #use load_save_slot(number=1)
        #hotspot (195, 353, 498, 115) action FileAction(2):
            #use load_save_slot(number=2)
        hotspot (465, 934, 199, 95) action ShowMenu('save')
        hotspot (688, 934, 199, 95) action ShowMenu('load')
        hotspot (919, 934, 283, 95) action Return()
        hotspot (1230, 934, 390, 95) action MainMenu() 
        hotspot (1649, 934, 186, 95) action Quit(confirm=False)  
        
screen save:
    
    tag menu
    
    imagemap:
        ground 'assets_gui/imagemap_save_ground.jpg'
        idle 'assets_gui/imagemap_save_idle.png'
        hover 'assets_gui/imagemap_save_hover.png'
        selected_idle 'assets_gui/imagemap_save_selected_idle.png'
        selected_hover 'assets_gui/imagemap_save_selected_hover.png'
 
        #hotspot (-1, -1, -1, -1) action FilePage('auto')
        #hotspot (46, 104, 127, 115) action FilePage(1) hover_sound "sfx/click.wav"
        #hotspot (46, 228, 127, 115) action FilePage(2) hover_sound "sfx/click.wav"
        #hotspot (46, 353, 127, 115) action FilePage(3) hover_sound "sfx/click.wav"

        
        hotspot (98, 280, 750, 485) action FileAction(0): 
            use load_save_slot(number=0) 
        #hotspot (195, 228, 498, 115) action FileAction(1):
            #use load_save_slot(number=1)
        #hotspot (195, 353, 498, 115) action FileAction(2):
            #use load_save_slot(number=2)
        hotspot (465, 934, 199, 95) action ShowMenu('save')
        hotspot (688, 934, 199, 95) action ShowMenu('load')
        hotspot (919, 934, 283, 95) action Return()
        hotspot (1230, 934, 390, 95) action MainMenu() 
        hotspot (1649, 934, 186, 95) action Quit(confirm=False)  


#██▓▒░ IMAGEMAP PREFERENCES ░▒▓███████████████████████████████████ 
#This block is responsible for the Imagemap based main menu

screen about_credits:
    tag menu
    
    imagemap:
        ground 'assets_gui/imagemap_about_ground.jpg'
        idle 'assets_gui/imagemap_about_idle.png'
        hover 'assets_gui/imagemap_about_hover.png'
        selected_idle 'assets_gui/imagemap_about_selected_idle.png'
        selected_hover 'assets_gui/imagemap_about_selected_hover.png'

        hotbar (98, 245, 1698, 111) value Preference('music volume') 
        hotbar (98, 543, 1698, 111) value Preference('sound volume') 

        hotspot (465, 934, 199, 95) action ShowMenu('save')
        hotspot (688, 934, 199, 95) action ShowMenu('load')
        hotspot (919, 934, 283, 95) action Return()
        hotspot (1230, 934, 390, 95) action MainMenu() 
        hotspot (1649, 934, 186, 95) action Quit(confirm=False) 



    text _p("""
        {color=#ca4700}{b}Arajane Dimaunahan{/b}{/color}{p}
        {color=#ca4700}Project Manager │ Programmer │ Writer{/color}{p}{p}
        {color=#ca4700}{b}Gab Emmanuel Lobio{/b}{/color}{p}
        {color=#ca4700}Project Manager │ Programmer{/color}{p}{p}
        {color=#ca4700}{b}Jeanne Mesa{/b}{/color}{p}
        {color=#ca4700}Writer{/color}{p}{p}
        {color=#ca4700}{b}Maricar Murcia{/b}{/color}{p}
        {color=#ca4700}Writer{/color}{p}{p}

        """) xpos 450 ypos 224 size 50 color "#000000" text_align 0.5

    text _p("""
        {color=#ffffff}{b}Arajane Dimaunahan{/b}{/color}{p}
        {color=#ffffff}Project Manager │ Programmer │ Writer{/color}{p}{p}
        {color=#ffffff}{b}Gab Emmanuel Lobio{/b}{/color}{p}
        {color=#ffffff}Project Manager │ Programmer{/color}{p}{p}
        {color=#ffffff}{b}Jeanne Mesa{/b}{/color}{p}
        {color=#ffffff}Writer{/color}{p}{p}
        {color=#ffffff}{b}Maricar Murcia{/b}{/color}{p}
        {color=#ffffff}Writer{/color}{p}{p}

        """) xpos 450 ypos 220 size 50 color "#000000" text_align 0.5
        




style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False


#init offset = -1
screen input(prompt):
    #style prefix "input"

    frame:
        background Frame("assets_gui/quiz_mini_window.png", Borders (25,25,25,25))
        xalign 0.5
        ypos 0.5
        xpadding 30
        ypadding 30
        vbox:
            spacing 10
            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
    color '#ffffff'
style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    color '#ffffff'



screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 604
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")




label tawag_mga_leson:   
    call screen lesson_ui

    return 



##### VIEWPORT #####

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"



## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if show_quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.92
            yalign 0.93


            #textbutton _("Back") action Rollback()
            #textbutton _("History") action ShowMenu('history')
            #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            imagebutton auto "menuUI/save_%s.png" action ShowMenu('save')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            imagebutton auto "menuUI/option_%s.png" action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default show_quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    

style quick_button_text:
    properties gui.button_text_properties("quick_button")



































################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675
    #xpos 0

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
#screen quick_menu():
    #variant "touch"

   # zorder 100

    #if quick_menu:

        #hbox:
            #style_prefix "quick"

            xalign 0.90
            yalign 0.93

            #textbutton _("Back") action Rollback()
            #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


#style window:
    #variant "small"
    #background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900