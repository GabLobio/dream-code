image bg_quiz = "assets_quiz/quiz_window_blank.jpg"
image top_text21 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text22 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text23 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text24 = ParameterizedText(ypos=250, xpos=1030 ,size =40)
image top_text25 = ParameterizedText(ypos=250, xpos=1030 ,size =40)
image top_text26 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text27 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text28 = ParameterizedText(ypos=250, xpos=1030 ,size =35)
image top_text29 = ParameterizedText(ypos=250, xpos=1030 ,size =40)
image top_text30 = ParameterizedText(ypos=250, xpos=1030 ,size =50)

default correct2 = 0




label Second_one:
    $ persistent.q2_exam_score = 0
    scene bg_quiz

    
  

    show top_text21 "What's the HTML tag for the paragraph text element?"

    menu:


        "program robots":
            jump Second_two

        "Analyze data ":
            jump Second_two     

        "Build and structure web pages":
            $ correct2 += 1
            jump Second_two

        "None of the above":
            jump Second_two     

label Second_two:

    scene bg_quiz


    show top_text22 "What's the HTML tag for the image element?"

    menu:


        "<picture>":
            jump Second_three


        "<p> ":
            jump Second_three
   

        " <img>":
            $ correct2 += 1
            jump Second_three


        "<pic>":
            jump Second_three


label Second_three:

    scene bg_quiz


    show top_text23 "Complete the code to add an ACCEPT button to the page: \n _______ Accept  <button>"

    menu:


        " <button>":
            $ correct2 += 1
            jump Second_four


        " Accept ":
            jump Second_four
   

        " </button> ":
            $ correct2 += 1
            jump Second_four


        "<button ":
            jump Second_four



label Second_four:

    scene bg_quiz


    show top_text24 "How many different heading levels can you use in your HTML code?"

    menu:


        "3":
            jump Second_five


        "6 ":
            $ correct2 += 1
            jump Second_five
   

        "12":
            jump Second_five


        "9":
            jump Second_five


label Second_five:

    scene bg_quiz


    show top_text25 "Complete the code to add an ACCEPT button to the page: \n <button> ________ </button>"

    menu:


        "<button>":
            jump Second_six


        "Accept ":
            $ correct2 += 1
            jump Second_six
   

        "</button>":
            jump Second_six


        "<button ":
            jump Second_six


label Second_six:

    scene bg_quiz


    show top_text26 "Button, paragraph and heading elements require …?"

    menu:


        "closing tag only":
            jump Second_seven


        "an opening tag only":
            jump Second_seven
   

        "both opening and closing tags":
            $ correct2 += 1
            jump Second_seven


        "none":
            jump Second_seven
        
    

label Second_seven:

    scene bg_quiz


    show top_text27 "Which of the following are true about web browsers?"

    menu:


        "They read JAVA code to display the resulting page":
            jump Second_eight


        "They require users to understand JAVA code to surf the web":
            jump Second_eight
   

        "They act as CSS code translators for humans":
            jump Second_eight


        "They provide a graphical user Interface":
            $ correct2 += 1
            jump Second_eight
        


label Second_eight:

    scene bg_quiz


    show top_text28 "Many HTML elements require both opening and closing tags to contain elements. \n These tags are also called?"

    menu:


        "Empty tags":
            jump Second_nine


        "Wid tag ":
            jump Second_nine
   

        "Container tags ":
            $ correct2 += 1
            jump Second_nine
            


        "button tags":
            jump Second_nine
    


label Second_nine:

    scene bg_quiz


    show top_text29 "There is a vast amount of information on the Web. \n Where does all this information live?"

    menu:


        "In servers that are listening for requests of information ":
            $ correct2 += 1
            jump Second_ten


        "In the user's device accessing the web":
            jump Second_ten
   

        "It comes from many sources.":
            jump Second_ten


        "None of the above.
        ":
            jump Second_ten





label Second_ten:

    scene bg_quiz


    show top_text30 "What's the HTML tag for the image element?"

    menu:


        " <p> ":
            hide top_text30 
            jump Finish_exam2
          


        " <h1> ":
            hide top_text30 
            jump Finish_exam2
          
   

        " <img> ":
            hide top_text30 
            $ correct2 += 1
            jump Finish_exam2
 


        " </p> ":
            hide top_text30 
            jump Finish_exam2
            




label Finish_exam2:
    $ persistent.q2_exam_score = correct2
    e "Tapos na ang exam"
    e "Your score for this exam is [correct2] "

    jump tapos_exam2










