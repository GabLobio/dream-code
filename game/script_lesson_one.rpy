image lof1 = "images/lesson_one/Lesson 1.1.png"
image lof2 = "images/lesson_one/Lesson 1.2.png"
image lof3 = "images/lesson_one/Lesson 1.3.png"
image lof4 = "images/lesson_one/Lesson 1.4.png"
image lof5 = "images/lesson_one/Lesson 1.5.png"
image lof6 = "images/lesson_one/Lesson 1.6.png"
image lof7 = "images/lesson_one/Lesson 1.7.png"
image lof8 = "images/lesson_one/Lesson 1.8.png"
image lof9 = "images/lesson_one/Lesson 1.9.png"
image lof10 = "images/lesson_one/Lesson 1.10.png"
image lof12 = "images/lesson_one/Lesson 1.12.png"

"""
init python:
    import datetime

    persistent.date_today = datetime.date.today()
    

    if not persistent.runtime:
        persistent.runtime = 0

    def calc_total_run():
        persistent.runtime += renpy.get_game_runtime()
        renpy.clear_game_runtime()

    def reset_timer():
        persistent.runtime = 0
        renpy.clear_game_runtime()

    renpy.restart_interaction()
"""


default current_playtime = 0
default total_playtime = 0

default persistent.chp_one_time = ""
default persistent.chp_prev_one_time = ""
default persistent.formatted_time = ""  # Define as a persistent variable

default persistent.chp_prev_date = 0
default persistent.chp_date_taken = 0

default persistent.chp_prev_score = 0


screen timeplayedbutton():
    $ calc_total_run()

    $ minutes, seconds = divmod(int(persistent.runtime), 60)
    $ hours, minutes = divmod(minutes, 60)
    $ persistent.formatted_time = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

    vbox:
        xpos 0
        ypos 1041
        text "[persistent.f_ttime]" size 10
        text "[persistent.formatted_time]" size 10


screen chp_one_assessment():
    image "images/chp_asses.png"

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/next_button.png"
        hover "images/interactive_button/next_button_hover.png"
        
        action Jump("chp_one_ending")

    
    text '{b}[persistent.chp_prev_one_time]{/b}' size 20 color "#87431E" xpos(539) ypos(243)
    text '{b}[persistent.chp_prev_date]{/b}' size 20 color "#87431E" xpos(358) ypos(387)
    image Solid("#FF5A00") xsize(persistent_quiz_00_q_counter_correct_previous_answer * 80) ysize(45) xpos 435 ypos 301

    #text "{b}[persistent.chp_prev_score]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 301# 
    text "{b}[persistent_quiz_00_q_counter_correct_previous_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 301 

    text '{b}[persistent.chp_one_time]{/b}' size 20 color "#171716" xpos(539) ypos(541)
    text '{b}[persistent.chp_date_taken]{/b}' size 20 color "#171716" xpos(358) ypos(679)
    image Solid("#FF5A00") xsize(persistent_quiz_00_q_counter_correct_answer * 80) ysize(45) xpos 435 ypos 599
    text "{b}[persistent_quiz_00_q_counter_correct_answer]0 % {/b}" size 24 color "#87431E" xoffset 6 yoffset 6 xpos 435 ypos 599
    



label lesson_one:


    $ persistent.ast1_kindness = 10
    $ persistent.ast1_rudeness = 10
    $ persistent.ast1_recitation = 5
    $ persistent.ast1_participation = 5
    $ persistent.ast1_accuracy = 5

    $ persistent.lesson_1_quiz1 = 0
    $ persistent.lesson_1_act1 = 0
    
    $ show_quick_menu = False
    play music "audio/sa_tech.mp3" volume 0.5

    scene bg_classroom

    # Start ng Time ###############
    $ save_total_run()
    $ reset_timer()
    show screen timeplayedbutton
    # Start ng Time ###############

    blank "After a week, the school had just started"
    
    show teacher smile 

    blank "Mrs. Rodriguez Introduced herself as their programming teacher"

    blank "She welcomed her students warmly."

    hide teacher smile 

    show teacher_closed_smile

    play sound "T_audio/les1/1.1.mp3" volume 0.8

    Tech "Good day, class! Ready to learn some HTML lesson?"
    
    POVclass "Yes, Mrs. Rodriguez! "
    hide teacher_closed_smile
    show teacher smile
    play sound "T_audio/les1/1.2.mp3" volume 0.8
    Tech "Ready to dive into the world of drag-and-drop? Let's start with a few friendly tutorials to get the hang of it!"

    label button_tutorial:
        scene lesson_tutorial_next
        play sound "T_audio/les1/1.3.mp3" volume 0.8
        Tech "When you're all set, hit the next button to move on to the next exciting challenge. Enjoy the journey!"
        scene lesson_tutorial_reset
        play sound "T_audio/les1/1.4.mp3" volume 0.8
        Tech "If you ever feel stuck, just hit the reset button to give it another shot."

    label tutorial:
        scene dnd_tutorial
        play sound "T_audio/les1/1.5.mp3" volume 0.8
        Tech "Before we start the lesson, let's discuss what drag-and-drop is."
        play sound "T_audio/les1/1.6.mp3" volume 0.8
        Tech 'Your task is to drag HTML elements from the choices below and drop them onto the corresponding blanks space'
        scene dnd_tutorial_two
        play sound "T_audio/0.1.mp3" volume 0.8
        Tech '"Simply click, hold, and drag the element you think fits, then release it over the blank space. If correct, it`ll snap into place. If not, try again!"'
        scene dnd_tutorial_three
        play sound "T_audio/les1/1.8.mp3" volume 0.8
        Tech 'Let`s get started! Match the choices to the correct blanks below by dragging and dropping. Have fun learning HTML through this hands-on experience!'

    #The Core Web Technology


    label coreWebTechnology:
        scene the_core_web_technology
        play sound "T_audio/les1/1.9.mp3" volume 0.8
        e"HTML is like a magic language that helps make websites."
        play sound "T_audio/les1/1.10.mp3" volume 0.8
        e"It uses special codes to tell the computer where to put words, pictures, and buttons on a webpage."
        play sound "T_audio/les1/1.11.mp3" volume 0.8
        Tech"Every website you’ve ever visited is built with {b}HTML code{/b}."
        play sound "T_audio/les1/1.12.mp3" volume 0.8
        Tech"With this lesson you’ll be able to {b}build your own web page{/b}."  
        Tech "Read the Lesson Plan for Lesson 1-3"
        call screen lesson_plan_q1

    label HTML:  
        scene one 
        play sound "T_audio/les1/1.13.mp3" volume 0.8
        e"{b}HTML{/b}, which stands for {b}HyperText Markup Language{/b}"
        scene two
        play sound "T_audio/les1/1.14.mp3" volume 0.8
        e"HTML was created by a person named {b} Tim Berners-Lee {/b} in the early {b}1990s{/b}. "
        play sound "T_audio/les1/1.15.mp3" volume 0.8
        e" He wanted a way to share and link documents on computers."
        scene one 
        play sound "T_audio/les1/1.16.mp3" volume 0.8
        e" Think of HTML like the building blocks of the internet "
        play sound "T_audio/les1/1.17.mp3" volume 0.8
        e" it helps put words, pictures, and links together to make websites "

    label Feature:
        scene three
        play sound "T_audio/les1/1.18.mp3" volume 0.8
        e "Simplicity"
        play sound "T_audio/les1/1.19.mp3" volume 0.8
        e "HTML is Easy to Learn and Use"
        play sound "T_audio/les1/1.20.mp3" volume 0.8
        e "Imagine HTML as the language that tells computers how to create awesome webpages."
        play sound "T_audio/les1/1.21.mp3" volume 0.8
        e " And guess what? It's super easy to learn!"
        play sound "T_audio/les1/1.22.mp3" volume 0.8
        e "Support"
        play sound "T_audio/les1/1.23.mp3" volume 0.8 
        e "It is Supported by All Browsers "
        play sound "T_audio/les1/1.24.mp3" volume 0.8 
        e "HTML is like a rockstar that all browsers love! Whether you're using Chrome, Firefox, or Safari."
        play sound "T_audio/les1/1.25.mp3" volume 0.8 
        e " HTML makes sure your webpage looks fantastic everywhere"
        play sound "T_audio/les1/1.26.mp3" volume 0.8 
        e "Speed"
        play sound "T_audio/les1/1.27.mp3" volume 0.8 
        e " It is Lightweight and Fast"
        play sound "T_audio/les1/1.28.mp3" volume 0.8 
        e "HTML is like a speedy cheetah! It helps your webpages load quickly'"
        play sound "T_audio/les1/1.29.mp3" volume 0.8 
        e "So you don't have to wait forever to see your favorite cat videos."
        play sound "T_audio/les1/1.30.mp3" volume 0.8 
        e "In Tracking Websites. It's Easy to Be Found by Search Engines"
        play sound "T_audio/0.2.mp3" volume 0.8 
        e "HTML is like a treasure map for search engines. "
        play sound "T_audio/les1/1.32.mp3" volume 0.8 
        e "It makes your website easy to find so that people can discover your amazing creations."
        play sound "T_audio/les1/1.33.mp3" volume 0.8 
        e "In Integration. It's Easy to Integrate with Other Programming Languages"
        play sound "T_audio/les1/1.34.mp3" volume 0.8 
        e " HTML is like a team player. "
        play sound "T_audio/les1/1.35.mp3" volume 0.8 
        e " It loves to work with other programming languages, making your website even more awesome"
        play sound "T_audio/les1/1.36.mp3" volume 0.8 
        e "Error Handling. If Code Mistakes it Won't Crash the Site"
        play sound "T_audio/les1/1.37.mp3" volume 0.8 
        e "HTML is like a forgiving friend. If you make a mistake in your code"
        play sound "T_audio/les1/1.38.mp3" volume 0.8 
        e "Don't worry! Your website won't crash; it will just keep going with default settings."

    label drawbacks:
        scene four
        play sound "T_audio/les1/1.39.mp3" volume 0.8 
        e "Now, let's talk about some challenges HTML faces. Every superhero has its weaknesses, right?"
        play sound "T_audio/les1/1.40.mp3" volume 0.8 
        e "Static"
        play sound "T_audio/les1/1.41.mp3" volume 0.8 
        e" HTML Can Only Make Static Webpages"
        play sound "T_audio/les1/1.42.mp3" volume 0.8 
        e "HTML is like a picture it can't change on its own."
        play sound "T_audio/les1/1.43.mp3" volume 0.8 
        e "Lack of Security"
        play sound "T_audio/les1/1.44.mp3" volume 0.8 
        e "HTML is like a castle with a simple lock. "
        play sound "T_audio/les1/1.45.mp3" volume 0.8 
        e "To make it super secure, we need to team up with PHP and JavaScript. Safety first!"
        play sound "T_audio/les1/1.46.mp3" volume 0.8 
        e "Complex"
        play sound "T_audio/les1/1.47.mp3" volume 0.8 
        e " Code Gets Tricky with Lots of Content"
        play sound "T_audio/les1/1.48.mp3" volume 0.8 
        e "HTML is like a puzzle. As your website grows, the code can get a bit tricky to read. "
        play sound "T_audio/les1/1.49.mp3" volume 0.8 
        e "But don't worry; with practice, you'll become a coding superhero!"
        play sound "T_audio/les1/1.50.mp3" volume 0.8 
        e "Not a Programming Language"
        play sound "T_audio/les1/1.51.mp3" volume 0.8 
        e " Can't Do All the Cool Stuff Alone"
        play sound "T_audio/les1/1.52.mp3" volume 0.8 
        e "HTML is like a superhero sidekick. It can't do everything on its own, but when combined with other languages."
        play sound "T_audio/les1/1.53.mp3" volume 0.8 
        e " it becomes part of an unstoppable team!"
        play sound "T_audio/les1/1.54.mp3" volume 0.8 
        e "Styling, Needs a Friend Named CSS for a Stylish Look"
        play sound "T_audio/les1/1.55.mp3" volume 0.8 
        e " HTML is like a canvas, and CSS is the paint."
        play sound "T_audio/les1/1.56.mp3" volume 0.8 
        e "To make your website look fantastic, we need to invite CSS to the party."
        
    label ide:
        scene five
        play sound "T_audio/les1/1.57.mp3" volume 0.8 
        e "Now that we know about HTML, it's time to talk about the tools we use to create our webmasterpieces!"
        play sound "T_audio/les1/1.58.mp3" volume 0.8 
        e"IDE stands for Integrated Development Environment"
        play sound "T_audio/les1/1.59.mp3" volume 0.8 
        e"is like a magical toolbox for coding. It has everything we need a code editor, compiler, and a debugger all in one place!"
        play sound "T_audio/les1/1.60.mp3" volume 0.8 
        e "Choosing a Good IDE is Important"
        play sound "T_audio/les1/1.61.mp3" volume 0.8 
        e " It's like picking the perfect wand for a wizard!"
        play sound "T_audio/les1/1.62.mp3" volume 0.8 
        e" A good IDE saves time, helps us write better code, and makes finding and fixing mistakes easier"
        play sound "T_audio/les1/1.63.mp3" volume 0.8 
        e" Brackets, Notepad++ and Visual Studio Code are some of example of IDE."
        play sound "T_audio/les1/1.64.mp3" volume 0.8 
        e "These are like superhero suits for our coding adventures! Choose the one that feels just right for you."
        play sound "T_audio/les1/1.65.mp3" volume 0.8 
        e"And there you have it, kids! You're now armed with the knowledge to start your web development journey"



    label lessonOneFillOne:
        $ rudeness1 = True
        $ ans_button_lt_dropped = False
                    
        scene lof1 
        play sound "T_audio/les1/1.66.mp3" volume 0.8 
        e "HTML code is based on tags like <button> tag [ls1_numhc]"
        play sound "T_audio/les1/1.67.mp3" volume 0.8 
        e "Tags use angle brackets (<>)"

        play sound "T_audio/les1/1.68can.mp3" volume 0.8 
        e "Can someone answer the first problem today?"
        label l1Int1:
            menu:
                "Talk to classmate":
                    jump start_hitting_teach
                    label opsl1_1:
                        $ persistent.ast1_rudeness += 50
                        jump skipped_l1
                "Play with your classmate":
                    jump begin_ho_mg
                    label opsl1_2:
                        $ persistent.ast1_rudeness += 50
                        jump skipped_l1
                "Raise Hand":
                    pass
                "Ignore":
                    jump lessonOneFillTwo

        call screen lesson_one_fill

        label call_o1:
            $ ans_button_lt_dropped = False
            call screen lesson_one_fill

        label if_wrong:
            scene lof1
            play sound "T_audio/Try_again.mp3" volume 0.8 
            e "Try again"
            $ ls1_numic += 1
            call screen lesson_one_fill


    label lessonOneFillTwo:
        $ ls1_numc  += 1
        $ ans_button_was_dropped = False
        $ ans_gt_was_dropped = False
        scene lof2 
        play sound "T_audio/les1/1.69.mp3" volume 0.8 
        e "The angle brackets <> surround the name of the element you want to add to the page"
        play sound "T_audio/les1/1.70.mp3" volume 0.8 
        e "Elements like buttons, text and images are added to web pages with different tags."
        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone want to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneFillThree

        call screen lesson_two_fill

        label call_o2:
            $ ans_button_was_dropped = False
            $ ans_gt_was_dropped = False
            call screen lesson_two_fill

        label if_wrong_l2:
            scene lof2
            play sound "T_audio/Try_again.mp3" volume 0.8 
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_two_fill


    label lessonOneFillThree:
        $ ls1_numc  += 1
        $ ans_fl2_was_dropped = False
        scene lof3
        play sound "T_audio/les1/1.72.mp3" volume 0.8 
        e "You can use {b}image tag (<img>){/b} to add images to a web page"
        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone want to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneFillFour

        call screen lesson_three_fill

        label call_o3:
            $ ans_fl2_was_dropped = False
            call screen lesson_three_fill

        label if_wrong_l3:
            scene lof3
            play sound "T_audio/Try_again.mp3" volume 0.8 
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_three_fill



    label lessonOneFillFour:
        $ ls1_numc  += 1
        $ ans_btn_was_dropped = False
        $ ans_img_was_dropped = False
        $ ans_tp_was_dropped = False
        $ ans_tbl_was_dropped = False
        scene lof4
        play sound "T_audio/les1/1.73.mp3" volume 0.8 
        e "You need HTML tags to add different elements to a page."
        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone want to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneIntro

        # Classmate Confused Interaction
        blank "As you're concentrating on the current lesson, a classmate approaches you, looking a bit confused."
        # Dialogue to nung kaklaseng nyang boy
        show boy2
        boy "Hey, mind lending a hand? I'm a bit lost with some of the words the teacher just used. Could you help me catch up on what I missed? I'd appreciate it, and maybe we can quickly go through it together so we don't fall too behind."
        hide boy2
        menu:
            "Talk to him":
                blank "You missed several parts of the lesson as you help your classmate catch up. While you feel good about helping, you realize you've sacrificed your own understanding."
                $ persistent.ast1_kindness = 50
                jump lessonHtmlTakeaways
            "Refuse and explain that you can teach him later; choose to focus on the current lesson":
                blank "You politely refuse, explaining that you're trying to focus on the current lesson. You offer to help your classmate after class, emphasizing the importance of catching up together."
                $ persistent.ast1_kindness = 50
                pass
                
        call screen lesson_four_fill

        label call_o4:
            $ ans_btn_was_dropped = False
            $ ans_img_was_dropped = False
            $ ans_tp_was_dropped = False
            $ ans_tbl_was_dropped = False
            call screen lesson_four_fill

        label if_wrong_l4:
            scene lof4
            play sound "T_audio/Try_again.mp3" volume 0.8 
            Tech"Try again"
            $ ls1_numic += 1
            call screen lesson_four_fill

    label lessonOneIntro:
        show lesson_one_intro
        play sound "T_audio/Take_note.mp3" volume 0.8 
        Tech"Take note..."
        jump lessonBeforeFillFive

    label lessonBeforeFillFive:
        scene lesson_before_f5
        play sound "T_audio/les1/1.74.mp3" volume 0.8 
        Tech"The structure of a web page is built in HTML"
        play sound "T_audio/les1/1.75.mp3" volume 0.8 
        Tech"You can then style the page with CSS"
        play sound "T_audio/les1/1.76.mp3" volume 0.8 
        Tech"JavaScript is used to make pages Interactive"

    label lessonOneFillFive:
        $ ls1_numc  += 1
        $ ans_html_was_dropped = False
        $ ans_js_was_dropped = False
        $ ans_css_was_dropped = False
        scene lof5
        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone wants to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonHtmlTakeaways

        call screen lesson_five_fill

        label call_o5:
            $ ans_html_was_dropped = False
            $ ans_js_was_dropped = False
            $ ans_css_was_dropped = False
            call screen lesson_five_fill

        label if_wrong_l5:
            scene lof5
            play sound "T_audio/Try_again.mp3" volume 0.8 
            Tech"Try again"
            $ ls1_numic += 1
            call screen lesson_five_fill

    label lessonHtmlTakeaways:
        show lesson_html_takeaways
        play sound "T_audio/les1/1.77.mp3" volume 0.8 
        Tech"Before we move on to the next one, try to remember this lesson takeaways"
        jump introToHTML

    label introToHTML:
        scene lesson_0_1
        play sound "T_audio/les1/1.78.mp3" volume 0.8 
        Tech"You’ll start writing, running and testing real {b}HTML code{/b} in this lesson to build the structure of a web page."
        play sound "T_audio/les1/1.79.mp3" volume 0.8 
        Tech"But, first let's discuss the element tag"
        jump openingTag

    label openingTag:
        scene opening_tag
        play sound "T_audio/les1/1.80.mp3" volume 0.8 
        Tech"An opening tag is the first part of an HTML element and is enclosed in angle brackets ({b}<{/b} and {b}>{/b})."
        play sound "T_audio/les1/1.82.mp3" volume 0.8 
        Tech"It signifies the beginning of an HTML element."
        jump closingTag

    label closingTag:
        scene closing_tag
        play sound "T_audio/les1/1.83.mp3" volume 0.8 
        Tech"A {b}closing tag{/b} is the second part of an HTML element and is also enclosed in angle brackets ({b}<{/b} and {b}>{/b}), but it includes a forward slash {b}(/){/b} before the tag name."
        play sound "T_audio/les1/1.84.mp3" volume 0.8 
        Tech"It signifies the end of an HTML element."
        jump tagContent

    label tagContent:
        scene tag_content
        play sound "T_audio/les1/1.85.mp3" volume 0.8 
        Tech"The {b}content{/b} of an HTML element is the information between the {b}opening{/b} and {b}closing tags{/b}."
        play sound "T_audio/les1/1.86.mp3" volume 0.8 
        Tech"It represents the data or text that will be displayed on the web page."
        jump elementTag

    label elementTag:
        scene elelment_tag
        play sound "T_audio/les1/1.87.mp3" volume 0.8 
        Tech"An {b}HTML element{/b} consists of the {b}opening tag{/b}, {b}content{/b}, and {b}closing tag{/b}."
        play sound "T_audio/les1/1.88.mp3" volume 0.8 
        Tech"It represents a specific piece of content or structure on a {b}web page{/b}."
        play sound "T_audio/les1/1.89.mp3" volume 0.8 
        Tech"In later lesson we wil discussing and use different elements"
        play sound "T_audio/les1/1.90.mp3" volume 0.8 
        Tech"This element called heading tag it has 6 different kind"
        play sound "T_audio/les1/1.91.mp3" volume 0.8 
        Tech"moving on"
        jump tagAttribute

    label tagAttribute:
        scene tag_attribute
        play sound "T_audio/les1/1.92.mp3" volume 0.8 
        Tech"This example {b}<a> tag{/b} can be called {b}HyperText, Hyperlink, or link tag{/b}. Let`s use this to exaplain {b}attributes{/b}"
        play sound "T_audio/les1/1.93.mp3" volume 0.8 
        Tech"An {b}attribute{/b} provides additional information about an HTML element and is always included in the {b}opening tag{/b}."
        play sound "T_audio/les1/1.94.mp3" volume 0.8 
        Tech"It is made up of a {b}name{/b} and a {b}value{/b}."
        play sound "T_audio/les1/1.95.mp3" volume 0.8 
        Tech'"Example: In {b}<a href="https://www.example.com">{/b}, {b}href{/b} is the attribute {b}name{/b},"'
        play sound "T_audio/les1/1.96.mp3" volume 0.8 
        Tech'and "{b}https://www.example.com{/b}" is the attribute {b}value{/b}.'
        jump tagAttributeName

    label tagAttributeName:
        scene tag_attribute_name
        play sound "T_audio/les1/1.97.mp3" volume 0.8 
        Tech"The {b}name{/b} of an attribute specifies the type of information it is providing" 
        play sound "T_audio/les1/1.98.mp3" volume 0.8 
        Tech"It comes {b}before{/b} the equal sign {b}(=){/b} in the attribute."
        play sound "T_audio/les1/1.99.mp3" volume 0.8 
        Tech'Example: In <a href="https://www.example.com">, {b}href{/b} is an {b}attribute name{/b}.'
        jump tagAttributeValue

    label tagAttributeValue:
        scene tag_attribute_value
        play sound "T_audio/les1/1.100.mp3" volume 0.8 
        Tech "The {b}value{/b} of an attribute provides the specific information associated with that attribute."
        play sound "T_audio/les1/1.102.mp3" volume 0.8 
        Tech "It comes {b}after{/b} the equal sign {b}(=){/b} in the attribute, enclosed in quotes."
        play sound "T_audio/les1/1.103.mp3" volume 0.8 
        play sound "T_audio/les1/1.104.mp3" volume 0.8 
        Tech 'Example: In <a href="https://www.example.com">, {b}"https://www.example.com"{/b} is an {b}attribute values{/b}.'
        jump tagSummary

    label tagSummary:
        scene tag_summary
        play sound "T_audio/les1/1.105.mp3" volume 0.8 
        Tech"In summary, {b}HTML{/b} uses a combination of {b}opening{/b} and {b}closing tags{/b}, {b}content{/b}, and {b}attributes{/b} to structure and present {b}information{/b} on a web page."
        play sound "T_audio/les1/1.106.mp3" volume 0.8 
        Tech"{b}Elements{/b} represent different parts of the content, and attributes provide additional details about those elements."
        play sound "T_audio/les1/1.107.mp3" volume 0.8 
        Tech'Also, there are elements that don`t require a closing tag. These are called "void" or "empty" element tags. '
        play sound "T_audio/les1/1.108.mp3" volume 0.8 
        Tech'These elements consist only of an opening tag, and they don`t have content or a closing tag.'
        play sound "T_audio/les1/1.109.mp3" volume 0.8 
        Tech'Instead, they may include attributes in the opening tag to provide additional information.'
        jump basicTag

    label basicTag:
        scene lesson_0_2
        play sound "T_audio/les1/1.110.mp3" volume 0.8 
        Tech "Many HTML elements require both opening and closing tags."
        
        jump lessonOneFillSix

    label lessonOneFillSix:
        $ ls1_numc += 1
        $ ans_btntg_was_dropped = False
        $ ans_like_was_dropped = False
        
        play sound "T_audio/anyone_wants.mp3" volume 0.8 
        e "Anyone wants to answer this problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneFillSeven

        call screen lesson_six_fill

        label call_o6:
            $ ans_btntg_was_dropped = False
            $ ans_like_was_dropped = False
            call screen lesson_six_fill

        label if_wrong_l6:
            show screen lesson_six_fill
            play sound "T_audio/les1/1.74.mp3" volume 0.8 
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_six_fill

            

    label lessonOneFillSeven:
        $ ls1_numc += 1
        $ ans_tgbtn_was_dropped = False
        scene lof7
        play sound "T_audio/les1/1.111.mp3" volume 0.8 
        e "Closing tags are very similar to the opening tags. "
        play sound "T_audio/les1/1.112.mp3" volume 0.8 
        e "The only difference is that they contain a forward slash."
        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone wants to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneFillEighth

        call screen lesson_seven_fill

        label call_o7:
            $ ans_tgbtn_was_dropped = False
            call screen lesson_seven_fill

        label if_wrong_l7:
            scene lof7
            play sound "T_audio/Try_again.mp3" volume 0.8 
            Tech"Try again"
            $ ls1_numic += 1
            call screen lesson_seven_fill




    label lessonOneFillEighth:
        $ ls1_numc += 1
        $ ans_comment_was_dropped = False
        scene lof8
        play sound "T_audio/les1/1.113.mp3" volume 0.8 
        e "You can customize the text for the button. The content of the button is placed between the tags"
        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone wants to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneFillNine

        call screen lesson_eighth_fill

        label call_o8:
            $ ans_comment_was_dropped = False
            call screen lesson_eighth_fill

        label if_wrong_l8:
            scene lof8
            play sound "T_audio/Try_again.mp3" volume 0.8 
            Tech"Try again"
            $ ls1_numic += 1
            call screen lesson_eighth_fill



    
    label lessonOneFillNine:
        $ ls1_numc += 1
        $ ans_ptag_was_dropped = False
        $ ans_ptag2_was_dropped = False
        scene lof9
        play sound "T_audio/les1/1.114.mp3" volume 0.8
        e "Many elements require both opening and closing tags, also known as container tags. The paragraphtext is another example"
        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone wants to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneFillTen

        call screen lesson_nine_fill

        label call_o9:
            $ ans_ptag_was_dropped = False
            $ ans_ptag2_was_dropped = False
            call screen lesson_nine_fill

        label if_wrong_l9:
            scene lof9
            play sound "T_audio/Try_again.mp3" volume 0.8
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_nine_fill


        
    label lessonOneFillTen:
        $ ls1_numc += 1
        $ ans_ft1_was_dropped = False
        $ ans_ft2_was_dropped = False
        $ ans_ft3_was_dropped = False
        scene lof10
        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone wants to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneBeforeEleven

        call screen lesson_ten_fill

        label call_o10:
            $ ans_ft1_was_dropped = False
            $ ans_ft2_was_dropped = False
            $ ans_ft3_was_dropped = False
            call screen lesson_ten_fill

        label if_wrong_l10:
            scene lof10
            play sound "T_audio/Try_again.mp3" volume 0.8
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_ten_fill


    label lessonOneBeforeEleven:
        $ ls1_numc += 1
        scene lesson_one_11
        play sound "T_audio/les1/1.115.mp3" volume 0.8 
        Tech"Ready to write, run and test real HTML code? The {b}Code Playground{/b} allows you to do that"
        play sound "T_audio/les1/1.116.mp3" volume 0.8 
        Tech "hit the 'Run' textbutton below to see what the web browser will display"

        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone wants to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneFillEleven

        call screen lesson_before_eleven_fill

        label lesson_one_11_run:
            show lesson_one_11_run 
            play sound "T_audio/les1/1.117.mp3" volume 0.8 
            Tech "The code you write in 'index.html' will be read by the browser and display it"
            play sound "T_audio/les1/1.118.mp3" volume 0.8 
            Tech "And you coded p tag and button tag now the content will be displayed like so"
            jump lessonOneFillEleven


    label lessonOneFillEleven:
        scene lesson_1_11 
        play sound "T_audio/les1/1.119.mp3" volume 0.8 
        Tech "You can combine multiple elements in your code."
        play sound "T_audio/les1/1.120.mp3" volume 0.8 
        Tech "If you were to run this, what would be the content of the web page?"

        menu:
            'An image and a button':
                $ ls1_numic += 1
                jump if_wrong_l11
            'A paragraph text and a button':
                play sound "T_audio/correct.mp3" volume 0.8 
                Tech "correct"
                $ ls1_numc += 1
                jump lessonOneFillTwelve
            

        
        label if_wrong_l11:
            play sound "T_audio/incorrect.mp3" volume 0.8 
            Tech "incorrect"
            $ ls1_numic += 1
            jump lessonOneFillEleven 
    

    label lessonOneFillTwelve:
        $ ls1_numc += 1
        $ ans_t1_was_dropped = False
        $ ans_t2_was_dropped = False
        scene lof12
        play sound "T_audio/les1/1.121.mp3" volume 0.8 
        e "Tags use angle brackets <>"

        play sound "T_audio/les1/1.71can.mp3" volume 0.8 
        e "Anyone wants to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump webBrowser

        call screen lesson_twelve_fill

        label call_o12:
            $ ans_t1_was_dropped = False
            $ ans_t2_was_dropped = False
            call screen lesson_twelve_fill

        label if_wrong_l12:
            scene lof12
            play sound "T_audio/Try_again.mp3" volume 0.8 
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_twelve_fill


    label webBrowser:
        $ ls1_numc += 1
        scene lesson_after_of12
        play sound "T_audio/les1/1.122.mp3" volume 0.8 
        Tech "Your {b}web browser{/b} (e.g. Chrome, Safari, etc.) can read HTML code and translate it into what you see when you surf the web."
        jump aWebBrowser

    label aWebBrowser:
        scene lesson_8_22 
        show teacher_crossarm_happy
        play sound "T_audio/0.3.mp3" volume 0.8 
        Tech "A web browser…"
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        play sound "T_audio/0.4.mp3" volume 0.8 
        Tech "Is what?"

        menu:
            'requires the user to understand HTML code':
                $ ls1_numic += 1
                jump if_wrong_l13
            'translates HTML code into web pages':
                show teacher_crossarm_happy
                play sound "T_audio/correct.mp3" volume 0.8 
                e " correct"
                $ ls1_numc += 1
                jump lessonOneTakeaways
            

        
        label if_wrong_l13:
            show teacher_crossarm_sad
            play sound "T_audio/incorrect.mp3" volume 0.8 
            Tech "incorrect"
            $ ls1_numic += 1
            jump aWebBrowser 
    
    
    label lessonOneTakeaways:
        show lesson_one_takeaways
        Tech "In the next lesson, you’ll learn about a new HTML element: the heading."

    scene lesson_8_22 

    show teacher smile  



    $ persistent.ast1_participation += 50

    label skipped_l1:
    play sound "T_audio/les1/1.124.mp3" volume 0.8 
    show teacher_crossarm_smile
    Tech "Now that we finish the lesson lets start the quiz 1"
    hide teacher_crossarm_smile

    
    $ show_quick_menu = False
    
    stop music fadeout 1.0

    call start_quiz_00

label pagtapos_ng_quiz_0:
    
    stop music fadeout 1.0


    # Lesson 1
    $ persistent.lesson_1_quiz1 = persistent_quiz_00_q_counter_correct_answer  # Written Works 20%

    scene bg_classroom

    play sound "T_audio/quiz_class.mp3" volume 0.8
    show teacher_closed_smile
    Tech "Great job on the quiz, class! You all did fantastic."
    hide teacher_closed_smile
    show teacher_crossarm_happy
    play sound "T_audio/0.6.mp3" volume 0.8
    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting project related to what you've just learned."
    hide teacher_crossarm_happy
    play music "audio/office.mp3" volume 0.5
    jump l1_act1


label pagtapos_ng_act_1:
    

    hide teacher smile

    stop music fadeout 1.0
    

    play music "audio/sa_tech.mp3" volume 0.5

    scene bg_classroom
    
    show teacher_crossarm_smile
    play sound "T_audio/well done young coders.mp3" volume 0.8 
    e"Well done young coders. Let's end our class here."
    hide teacher_crossarm_smile
    show teacher_closed_happy
    play sound "T_audio/goodbye class.mp3" volume 0.8 
    e"Good bye class"
    hide teacher_closed_happy

    

    ######### Time save ######################################

   


    #$ persistent.chp_date_taken = persistent.date_today
    #$ persistent.chp_one_time = persistent.formatted_time





    label chp_one_end:
        #$ persistent.f_ttime = persistent.formatted_time
        #jump FBA
        #$ persistent.f_numhc += ls1_numhc
        #$ persistent.f_numc += ls1_numc
        #$ persistent.f_numic += ls1_numic
        $ save_total_run()
        $ reset_timer()
        #call screen chp_one_assessment()
        
        


    ######### Time save ######################################

    stop music fadeout 1.0




    label chp_one_ending:
        
        label l1_ending:
            #$ persistent.chp_prev_one_time = persistent.chp_one_time
            #$ persistent.chp_prev_score = persistent_quiz_00_q_counter_correct_answer
            #$ persistent.chp_prev_date = persistent.date_today
            
            scene bg_lesson_choices
            blank "End of chapter 1"
            


            $ lesson_one_finish = True

            #jump assessment_one
            #jump pagtapos_ng_lesson_one
    
    call screen lesson_ui

    stop music fadeout 1.0
    

    return