image bg_quiz = "assets_quiz/quiz_window_blank.jpg"
image top_text1 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text2 = ParameterizedText(ypos=260, xpos=1000 ,size =45)
image top_text3 = ParameterizedText(ypos=280, xpos=1020 ,size =45)
image top_text4 = ParameterizedText(ypos=280, xpos=1000 ,size =45)
image top_text5 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text6 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text7 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text8 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text9 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text10 = ParameterizedText(ypos=250, xpos=1030 ,size =50)

default correct1 = 0



label First_one:
    $ persistent.exam_score = 0
    scene bg_quiz



    show top_text1 "HTML code is used to?"


    menu:

        "program robots":
            hide top_text1 
            jump First_two

        "Analyze data ":
            hide top_text1 
            jump First_two     

        "Build and structure web pages":
            hide top_text1 
            $ correct1 += 1
            jump First_two

        "None of the above":
            hide top_text1 
            jump First_two   

    

label First_two:

    show top_text2 "Complete the button element tag :\n ____ button >"

    menu:


        "*":
            jump First_three


        "Greater than symbol ":
            jump First_three
   

        " Less than symbol":
            $ correct1 += 1
            jump First_three


        "#":
            jump First_three

    hide top_text2


label First_three:

    scene bg_quiz


    show top_text3 "Complete the button element tag : \n < button _____"

    menu:


        "*":
            jump First_four


        "Greater than symbol  \" > \"":
            $ correct1 += 1
            jump First_four
   

        " Less than symbol \" < \"":
            jump First_four


        "#":
            jump First_four

    hide top_text3



label First_four:

    scene bg_quiz


    show top_text4 "Complete the image tag :\n < img ___"

    menu:


        "Hashtag \" # \"":
            jump First_five


        "Greater than symbol \" > \" ":
            $ correct1 += 1
            jump First_five
   

        "Less than symbol \" < \"":
            jump First_five


        "Asterisk \" * \"":
            jump First_five

    hide top_text4


label First_five:

    scene bg_quiz


    show top_text5 "For HTML tag is <img> ?"

    menu:


        "Button":
            jump First_six


        "Image ":
            $ correct1 += 1
            jump First_six
   

        "Text paragraph":
            jump First_six


        "Table":
            jump First_six


    hide top_text5


label First_six:

    scene bg_quiz


    show top_text6 "For HTML tag is <p> ?"

    menu:


        "Button" :
            jump First_seven


        "Image ":
            jump First_seven
   

        "Text paragraph ":
            $ correct1 += 1
            jump First_seven


        "Table":
            jump First_seven

    hide top_text6
        
    

label First_seven:

    scene bg_quiz


    show top_text7 "Fill the black: \n The _______ controls the structure of a web page "

    menu:


        "CSS":
            jump First_eight


        "HTML":
            $ correct1 += 1
            jump First_eight
   

        "JavaScript":
            jump First_eight


        "Python":
            jump First_eight

    hide top_text7
        


label First_eight:

    scene bg_quiz


    show top_text8 "Fill the black: \n The _________ controls the presentation of a web. "

    menu:


        "CSS":
            $ correct1 += 1
            jump First_nine


        "HTML":
            jump First_nine
   

        "JavaScript":
            jump First_nine


        "Python":
            jump First_nine

    hide top_text8
    


label First_nine:

    scene bg_quiz


    show top_text9 "Fill thae black: \n The _________ controls the behavior of a web page"

    menu:


        "CSS":
            jump First_ten


        "HTML":
            jump First_ten
   

        "JavaScript":
            $ correct1 += 1
            jump First_ten


        "Python":
            jump First_ten

    hide top_text9 





label First_ten:

    scene bg_quiz


    show top_text10 "Who is the founder of HTML?"

    menu:


        "Tim Berners-Lee ":
            hide top_text10 
            $ correct1 += 1
            jump Finish_exam1


        "Wium Lie":
            hide top_text10 
            jump Finish_exam1
   

        "James Gosling":
            hide top_text10 
            jump Finish_exam1


        "Guido van Rossum":
            hide top_text10 
            jump Finish_exam1
    
    hide bg_quiz




label Finish_exam1:
    $ persistent.exam_score = correct1
    e "Tapos na ang exam"
    e "Ang score mo ay [correct1] "

    jump tapos_exam1

    











