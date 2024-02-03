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

    Tech "Good day, class! Ready to learn somr HTML lesson?"
    
    POVclass "Yes, Mrs. Rodriguez! "
    show teacher smile
    Tech "Ready to dive into the world of drag-and-drop? Let's start with a few friendly tutorials to get the hang of it!"

    label button_tutorial:
        scene lesson_tutorial_next
        Tech "When you're all set, hit the next button to move on to the next exciting challenge. Enjoy the journey!"
        scene lesson_tutorial_reset
        Tech "If you ever feel stuck, just hit the reset button to give it another shot."

    label tutorial:
        scene dnd_tutorial
        Tech "Before we start the lesson, let's discuss what drag-and-drop is."
        Tech 'Your task is to drag HTML elements from the choices below and drop them onto the corresponding blanks space'
        scene dnd_tutorial_two
        Tech '"Simply click, hold, and drag the element you think fits, then release it over the blank space. If correct, it`ll snap into place. If not, try again!"'
        scene dnd_tutorial_three
        Tech 'Let`s get started! Match the choices to the correct blanks below by dragging and dropping. Have fun learning HTML through this hands-on experience!'

    #The Core Web Technology


    label coreWebTechnology:
        scene the_core_web_technology
        e"HTML is like a magic language that helps make websites."
        e"It uses special codes to tell the computer where to put words, pictures, and buttons on a webpage."
        Tech"Every website you’ve ever visited is built with {b}HTML code{/b}."
        Tech"With this lesson you’ll be able to {b}build your own web page{/b}."  

    label HTML:  
        scene one 
        e"{b}HTML{/b}, which stands for {b}HyperText Markup Language{/b}"
        scene two
        e"HTML was created by a person named {b} Tim Berners-Lee {/b} in the early {b}1990s{/b}. "
        e" He wanted a way to share and link documents on computers."
        scene one 
        e" Think of HTML like the building blocks of the internet "
        e" it helps put words, pictures, and links together to make websites "

    label Feature:
        scene three
        e "Simplicity"
        e "HTML is Easy to Learn and Use"
        e "Imagine HTML as the language that tells computers how to create awesome webpages."
        e " And guess what? It's super easy to learn!"
        e "Support"
        e "It is Supported by All Browsers "
        e "HTML is like a rockstar that all browsers love! Whether you're using Chrome, Firefox, or Safari."
        e " HTML makes sure your webpage looks fantastic everywhere"
        e "Speed"
        e " It is Lightweight and Fast"
        e "HTML is like a speedy cheetah! It helps your webpages load quickly'"
        e "So you don't have to wait forever to see your favorite cat videos."
        e "In Tracking Websites. It's Easy to Be Found by Search Engines"
        e "HTML is like a treasure map for search engines. "
        e "It makes your website easy to find so that people can discover your amazing creations."
        e "In Integration. It's Easy to Integrate with Other Programming Languages"
        e " HTML is like a team player. "
        e " It loves to work with other programming languages, making your website even more awesome"
        e "Error Handling. If Code Mistakes it Won't Crash the Site"
        e "HTML is like a forgiving friend. If you make a mistake in your code"
        e "Don't worry! Your website won't crash; it will just keep going with default settings."

    label drawbacks:
        scene four
        e "Now, let's talk about some challenges HTML faces. Every superhero has its weaknesses, right?"
        e "Static"
        e" HTML Can Only Make Static Webpages"
        e "HTML is like a picture it can't change on its own."
        e "Lack of Security"
        e "HTML is like a castle with a simple lock. "
        e "To make it super secure, we need to team up with PHP and JavaScript. Safety first!"
        e "Complex"
        e " Code Gets Tricky with Lots of Content"
        e "HTML is like a puzzle. As your website grows, the code can get a bit tricky to read. "
        e "But don't worry; with practice, you'll become a coding superhero!"
        e "Not a Programming Language"
        e " Can't Do All the Cool Stuff Alone"
        e "HTML is like a superhero sidekick. It can't do everything on its own, but when combined with other languages."
        e " it becomes part of an unstoppable team!"
        e "Styling, Needs a Friend Named CSS for a Stylish Look"
        e " HTML is like a canvas, and CSS is the paint."
        e "To make your website look fantastic, we need to invite CSS to the party."

    label ide:
        scene five
        e "Now that we know about HTML, it's time to talk about the tools we use to create our webmasterpieces!"
        e"IDE stands for Integrated Development Environment"
        e"is like a magical toolbox for coding. It has everything we need a code editor, compiler, and a debugger all in one place!"
        e "Choosing a Good IDE is Important"
        e " It's like picking the perfect wand for a wizard!"
        e" A good IDE saves time, helps us write better code, and makes finding and fixing mistakes easier"
        e" Brackets, Notepad++ and Visual Studio Code are some of example of IDE."
        e "These are like superhero suits for our coding adventures! Choose the one that feels just right for you."
        e"And there you have it, kids! You're now armed with the knowledge to start your web development journey"



    label lessonOneFillOne:
        $ rudeness1 = True
        $ ans_button_lt_dropped = False
                    
        scene lof1 
        e "HTML code is based on tags like <button> tag[ls1_numhc]"
        e "Tags use angle brackets (<>)"

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
            e "Try again"
            $ ls1_numic += 1
            call screen lesson_one_fill


    label lessonOneFillTwo:
        $ ls1_numc  += 1
        $ ans_button_was_dropped = False
        $ ans_gt_was_dropped = False
        scene lof2 
        e "The angle brackets <> surround the name of the element you want to add to the page"
        e "Elements like buttons, text and images are added to web pages with different tags."

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
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_two_fill


    label lessonOneFillThree:
        $ ls1_numc  += 1
        $ ans_fl2_was_dropped = False
        scene lof3
        e "You can use {b}image tag (<img>){/b} to add images to a web page"

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
        e "You need HTML tags to add different elements to a page."
        e "Anyone want to answer the next problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneIntro
        call screen lesson_four_fill

        label call_o4:
            $ ans_btn_was_dropped = False
            $ ans_img_was_dropped = False
            $ ans_tp_was_dropped = False
            $ ans_tbl_was_dropped = False
            call screen lesson_four_fill

        label if_wrong_l4:
            scene lof4
            Tech"Try again"
            $ ls1_numic += 1
            call screen lesson_four_fill

    label lessonOneIntro:
        show lesson_one_intro
        Tech"Take note..."
        jump lessonBeforeFillFive

    label lessonBeforeFillFive:
        scene lesson_before_f5
        Tech"The structure of a web page is built in HTML"
        Tech"You can then style the page with CSS"
        Tech"JavaScript is used to make pages Interactive"

    label lessonOneFillFive:
        $ ls1_numc  += 1
        $ ans_html_was_dropped = False
        $ ans_js_was_dropped = False
        $ ans_css_was_dropped = False
        scene lof5
        e "Anyone wants to answer this problem?"
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
            Tech"Try again"
            $ ls1_numic += 1
            call screen lesson_five_fill

    label lessonHtmlTakeaways:
        show lesson_html_takeaways
        Tech"Before we move on to the next one, try to remember this lesson takeaways"
        jump introToHTML

    label introToHTML:
        scene lesson_0_1
        Tech"You’ll start writing, running and testing real {b}HTML code{/b} in this lesson to build the structure of a web page."
        Tech"But, first let's discuss the element tag"
        jump openingTag

    label openingTag:
        scene opening_tag
        Tech"An opening tag is the first part of an HTML element and is enclosed in angle brackets ({b}<{/b} and {b}>{/b})."
        Tech"It signifies the beginning of an HTML element."
        jump closingTag

    label closingTag:
        scene closing_tag
        Tech"A {b}closing tag{/b} is the second part of an HTML element and is also enclosed in angle brackets ({b}<{/b} and {b}>{/b}), but it includes a forward slash {b}(/){/b} before the tag name."
        Tech"It signifies the end of an HTML element."
        jump tagContent

    label tagContent:
        scene tag_content
        Tech"The {b}content{/b} of an HTML element is the information between the {b}opening{/b} and {b}closing tags{/b}."
        Tech"It represents the data or text that will be displayed on the web page."
        jump elementTag

    label elementTag:
        scene elelment_tag
        Tech"An {b}HTML element{/b} consists of the {b}opening tag{/b}, {b}content{/b}, and {b}closing tag{/b}."
        Tech"It represents a specific piece of content or structure on a {b}web page{/b}."
        Tech"In later lesson we wil discussing and use different elements"
        Tech"This element called heading tag it has 6 different kind"
        Tech"moving on"
        jump tagAttribute

    label tagAttribute:
        scene tag_attribute
        Tech"This example {b}<a> tag{/b} can be called {b}HyperText, Hyperlink, or link tag{/b}. Let`s use this to exaplain {b}attributes{/b}"
        Tech"An {b}attribute{/b} provides additional information about an HTML element and is always included in the {b}opening tag{/b}."
        Tech"It is made up of a {b}name{/b} and a {b}value{/b}."
        Tech'"Example: In {b}<a href="https://www.example.com">{/b}, {b}href{/b} is the attribute {b}name{/b},"'
        Tech'and "{b}https://www.example.com{/b}" is the attribute {b}value{/b}.'
        jump tagAttributeName

    label tagAttributeName:
        scene tag_attribute_name
        Tech"The {b}name{/b} of an attribute specifies the type of information it is providing" 
        Tech"It comes {b}before{/b} the equal sign {b}(=){/b} in the attribute."
        Tech'Example: In <a href="https://www.example.com">, {b}href{/b} is an {b}attribute name{/b}.'
        jump tagAttributeValue

    label tagAttributeValue:
        scene tag_attribute_value
        Tech "The {b}value{/b} of an attribute provides the specific information associated with that attribute."
        Tech "It comes {b}after{/b} the equal sign {b}(=){/b} in the attribute, enclosed in quotes."
        Tech 'Example: In <a href="https://www.example.com">, {b}"https://www.example.com"{/b} is an {b}attribute values{/b}.'
        jump tagSummary

    label tagSummary:
        scene tag_summary
        Tech"In summary, {b}HTML{/b} uses a combination of {b}opening{/b} and {b}closing tags{/b}, {b}content{/b}, and {b}attributes{/b} to structure and present {b}information{/b} on a web page."
        Tech"{b}Elements{/b} represent different parts of the content, and attributes provide additional details about those elements."
        Tech'Also, there are elements that don`t require a closing tag. These are called "void" or "empty" element tags. '
        Tech'These elements consist only of an opening tag, and they don`t have content or a closing tag.'
        Tech'Instead, they may include attributes in the opening tag to provide additional information.'
        jump basicTag

    label basicTag:
        scene lesson_0_2
        Tech "Many HTML elements require both opening and closing tags."
        
        jump lessonOneFillSix

    label lessonOneFillSix:
        $ ls1_numc += 1
        $ ans_btntg_was_dropped = False
        $ ans_like_was_dropped = False
        
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
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_six_fill

            

    label lessonOneFillSeven:
        $ ls1_numc += 1
        $ ans_tgbtn_was_dropped = False
        scene lof7
        e "Closing tags are very similar to the opening tags. "
        e "The only difference is that they contain a forward slash."
        
        e "Anyone wants to answer this problem?"
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
            Tech"Try again"
            $ ls1_numic += 1
            call screen lesson_seven_fill




    label lessonOneFillEighth:
        $ ls1_numc += 1
        $ ans_comment_was_dropped = False
        scene lof8
        e "You can customize the text for the button. The content of the button is placed between the tags"

        e "Anyone wants to answer this problem?"
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
            Tech"Try again"
            $ ls1_numic += 1
            call screen lesson_eighth_fill



    
    label lessonOneFillNine:
        $ ls1_numc += 1
        $ ans_ptag_was_dropped = False
        $ ans_ptag2_was_dropped = False
        scene lof9
        e "Many elements require both opening and closing tags, also known as container tags. The paragraphtext is another example"

        e "Anyone wants to answer this problem?"
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
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_nine_fill


        
    label lessonOneFillTen:
        $ ls1_numc += 1
        $ ans_ft1_was_dropped = False
        $ ans_ft2_was_dropped = False
        $ ans_ft3_was_dropped = False
        scene lof10

        e "Anyone wants to answer this problem?"
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
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_ten_fill


    label lessonOneBeforeEleven:
        $ ls1_numc += 1
        scene lesson_one_11
        Tech"Ready to write, run and test real HTML code? The {b}Code Playground{/b} allows you to do that"
        Tech "hit the 'Run' textbutton below to see what the web browser will display"

        e "Anyone wants to answer this problem?"
        menu:
                "Raise Hand":
                    pass

                "Ignore":
                    jump lessonOneFillEleven

        call screen lesson_before_eleven_fill

        label lesson_one_11_run:
            show lesson_one_11_run 
            Tech "The code you write in 'index.html' will be read by the browser and display it"
            Tech "And you coded p tag and button tag now the content will be displayed like so"
            jump lessonOneFillEleven


    label lessonOneFillEleven:
        scene lesson_1_11 
        Tech "You can combine multiple elements in your code."
        Tech "If you were to run this, what would be the content of the web page?"

        menu:
            'An image and a button':
                $ ls1_numic += 1
                jump if_wrong_l11
            'A paragraph text and a button':
                Tech "you are correct"
                $ ls1_numc += 1
                jump lessonOneFillTwelve
            

        
        label if_wrong_l11:
            Tech "incorrect"
            $ ls1_numic += 1
            jump lessonOneFillEleven 
    

    label lessonOneFillTwelve:
        $ ls1_numc += 1
        $ ans_t1_was_dropped = False
        $ ans_t2_was_dropped = False
        scene lof12
        e "Tags use angle brackets <>"

        e "Anyone wants to answer this problem?"
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
            Tech "Try again"
            $ ls1_numic += 1
            call screen lesson_twelve_fill


    label webBrowser:
        $ ls1_numc += 1
        scene lesson_after_of12
        Tech "Your {b}web browser{/b} (e.g. Chrome, Safari, etc.) can read HTML code and translate it into what you see when you surf the web."
        jump aWebBrowser

    label aWebBrowser:
        scene lesson_8_22 
        show teacher_crossarm_happy
        Tech "A web browser…"
        hide teacher_crossarm_happy
        show teacher_crossarm_smile
        Tech "Is what?"

        menu:
            'requires the user to understand HTML code':
                $ ls1_numic += 1
                jump if_wrong_l13
            'translates HTML code into web pages':
                show teacher_crossarm_happy
                e "you are correct"
                $ ls1_numc += 1
                jump lessonOneTakeaways
            

        
        label if_wrong_l13:
            show teacher_crossarm_sad
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

    Tech "Now that we finish the lesson lets start the quiz 1"

    
    $ show_quick_menu = False
    
    stop music fadeout 1.0

    play music "audio/quiz.mp3" volume 0.5

    jump start_quiz_00

    label pagtapos_ng_quiz_0:


    # Lesson 1
    $ persistent.lesson_1_quiz1 = persistent_quiz_00_q_counter_correct_answer  # Written Works 20%


    Tech "Great job on the quiz, class! You all did fantastic."

    Tech "Now, let's move on to our next activity. Today, we'll be diving into an exciting project related to what you've just learned."
    
    jump l1_act1

    label pagtapos_ng_act_1:
    

    hide teacher smile

    stop music fadeout 1.0

    play music "audio/sa_tech.mp3" volume 0.5

    scene bg_classroom
    
    show teacher_crossarm_smile
    e"Well done young coders. Let's end our class here."
    hide teacher_crossarm_smile
    show teacher_closed_happy
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