image bg_quiz = "assets_quiz/quiz_window_blank.jpg"
image top_text31 = ParameterizedText(ypos=250, xpos=1030 ,size =35)
image top_text32 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text33 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text34 = ParameterizedText(ypos=295, xpos=1030 ,size =32)
image top_text35 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text36 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text37 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text38 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text39 = ParameterizedText(ypos=290, xpos=1030 ,size =40)
image top_text40 = ParameterizedText(ypos=280, xpos=1030 ,size =32)

default correct3 = 0




label Third_one:
    $ persistent.q3_exam_score = 0
    scene bg_quiz

    
  

    show top_text31 "Content elements like buttons, paragraphs, and images need to be nested inside …?"

    menu:


        "the tail container":
            jump Third_two

        "the head container":
            jump Third_two     

        "the body container":
            $ correct3 += 1
            jump Third_two

        "the end container":
            jump Third_two     

label Third_two:

    scene bg_quiz


    show top_text32 "Complete the code to disable the button \n ____ <button>OK</button> ____"

    menu:


        "<!--  -->":
            $ correct3 += 1
            jump Third_three


        "<!--":
            jump Third_three
   

        " -->":
            jump Third_three


        " None of the above ":
            jump Third_three


label Third_three:

    scene bg_quiz


    show top_text33 "Specific and technical information like title, description,\n  author and keywords are nested inside … "

    menu:


        "the tail container":
            jump Third_four


        "the head container":
            $ correct3 += 1
            jump Third_four
   

        "the body container":
            jump Third_four


        "the end container":
            jump Third_four



label Third_four:

    scene bg_quiz


    show top_text34 "What's wrong with this code? \n <h1>Welcome to my website!</h1> \n <p>This is the home page.</p> \n <h1>About me</h1>"

    menu:


        "It uses multiple <p> tags":
            jump Third_five


        "It uses multiple </p> tags ":
            $ correct3 += 1
            jump Third_five
   

        "It uses multiple <h1> tags":
            jump Third_five


        "<p> tags shouldn't be nested inside the body.":
            jump Third_five


label Third_five:

    scene bg_quiz


    show top_text35 "Complete the code to make a comment \n < !-- Explanation - - ____"

    menu:


        "<":
            jump Third_six


        ">":
            $ correct3 += 1
            jump Third_six
   

        " = ":
            
            jump Third_six


        "*":
            jump Third_six


label Third_six:

    scene bg_quiz


    show top_text36 "Complete the code to make a comment \n ____ !-- Explanation - - >"

    menu:


        "<":
            $ correct3 += 1
            jump Third_seven


        "> ":
            jump Third_seven
   

        "=":
            jump Third_seven


        "*":
            jump Third_seven
        
    

label Third_seven:

    scene bg_quiz


    show top_text37 "Match the terms with their definitions \n Display the web page: _____"

    menu:


        "web server":
            jump Third_eight


        "web browser ":
            $ correct3 += 1
            jump Third_eight
   

        " web site ":
            jump Third_eight


        "None of the above":
            jump Third_eight
        


label Third_eight:

    scene bg_quiz


    show top_text38 "Match the terms with their definitions \n Stores and provides information: _____"

    menu:


        "web server":
            $ correct3 += 1
            jump Third_nine


        "web browser":
            jump Third_nine
   

        " web site":
            jump Third_nine


        "None of the above":
            jump Third_nine
    


label Third_nine:

    scene bg_quiz


    show top_text39 "How many lines will the browser display \n <p>Welcome! \n Enter your name</p>"

    menu:


        "1 line ":
            $ correct3 += 1
            jump Third_ten


        "2 lines ":
            jump Third_ten
   

        "3 lines ":
            jump Third_ten


        "4 lines ":
            jump Third_ten





label Third_ten:

    scene bg_quiz


    show top_text40 "How many lines will the browser display \n <h1> Welcome! </h1> \n <p> Enter your name</p>"

    menu:


        "1 line ":
            hide top_text40
            jump Finish_exam3
            


        "2 lines ":
            $ correct3 += 1
            hide top_text40
            jump Finish_exam3
        
   

        "3 lines ":
            hide top_text40
            jump Finish_exam3
            


        "4 lines ":
            hide top_text40
            jump Finish_exam3
            
    
    hide bg_quiz



label Finish_exam3:
    $ persistent.q3_exam_score = correct3
    e "Tapos na ang exam"
    e "Your score for this exam is [correct3] "

    jump tapos_exam3

    











