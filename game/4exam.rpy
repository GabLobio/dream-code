image bg_quiz = "assets_quiz/quiz_window_blank.jpg"
image top_text41 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text42 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text43 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text44 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text45 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text46 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text47 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text48 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text49 = ParameterizedText(ypos=250, xpos=1030 ,size =50)
image top_text50 = ParameterizedText(ypos=250, xpos=1030 ,size =50)

default correct4 = 0

label Fourth_one:

    scene bg_quiz


    show top_text41 "Add the required tags to display the text in bold. \n _____ Web development</b>"

    menu:


        "</d>":
            jump Fourth_two

        "<b>":
            $ correct4 += 1
            jump Fourth_two     

        "</b>":
            jump Fourth_two

        "<d>":
            jump Fourth_two     

label Fourth_two:

    scene bg_quiz


    show top_text42 "Add the required tags to display the text in bold. \n <b>  Web design _____"

    menu:

        "</d>":
            jump Fourth_three

        "<b>":
            jump Fourth_three     

        "</b>":
            $ correct4 += 1
            jump Fourth_three

        "<d>":
            jump Fourth_three



label Fourth_three:

    scene bg_quiz


    show top_text43 "Add the required tags to display the text in bold. \n _____ Web design _____"

    menu:


        "<d> </d> ":
            jump Fourth_four


        "<b> </b>":
            $ correct4 += 1
            jump Fourth_four
   

        "<p> </p>":
            jump Fourth_four


        "<i> </i>":
            jump Fourth_four



label Fourth_four:

    scene bg_quiz


    show top_text44 "Add the required tags to display the text in italics. \n _____ Digital marketing </i>"

    menu:


        "<i>":
            $ correct4 += 1
            jump Fourth_five


        "</i>":
            jump Fourth_five
   

        " <p>":
            jump Fourth_five


        "</p>":
            jump Fourth_five


label Fourth_five:

    scene bg_quiz


    show top_text45 "Add the required tags to display the text in italics. \n <i> Digital marketing _____"

    menu:



        "<i> ":
            jump Fourth_six


        "</i> ":
            $ correct4 += 1
            jump Fourth_six
   

        "<p> ":
            jump Fourth_six


        "</p>":
            jump Fourth_six



label Fourth_six:

    scene bg_quiz

    show top_text45 "Add the required tags to display the text in italics. \n _____ Digital marketing _____"

    menu:



        "<i> </i>":
            $ correct4 += 1
            jump Fourth_seven


        "<b> </b>":
            jump Fourth_seven
   

        "<p> </p>":
            jump Fourth_seven


        "<d> </d>":
            jump Fourth_seven
        
    

label Fourth_seven:

    scene bg_quiz


    show top_text47 "Add the required tags to underline the text. \n <u> Search Engine _____"

    menu:


        "<u>":
            jump Fourth_eight


        "</u> ":
            $ correct4 += 1
            jump Fourth_eight
   

        " <s>":
            jump Fourth_eight


        "</s>":
            jump Fourth_eight
        


label Fourth_eight:

    scene bg_quiz


    show top_text48 "Add the required tags to underline the text. \n _____ Adobong Manok _____"

    menu:


        "<b> </b>":
            jump Fourth_nine


        "<p> </p>":
            jump Fourth_nine
   

        "<i> </i>":
            jump Fourth_nine


        "<u> </u>":
            $ correct4 += 1
            jump Fourth_nine
    


label Fourth_nine:

    scene bg_quiz


    show top_text49 "Add the missing tags to show importance: \n _____ Warning! </strong>"

    menu:


        "</bold>":
            jump Fourth_ten


        "<italic>":
            jump Fourth_ten
   

        "<strong>":
            $ correct4 += 1
            jump Fourth_ten


        "/underlined" :
            jump Fourth_ten





label Fourth_ten:

    scene bg_quiz


    show top_text50 "Add the missing tags to show importance: \n _____ Warning! _____"

    menu:


        "<bold> </bold>":
            hide top_text50 
            jump Finish_exam4


        "<italic> </italic>":
            hide top_text50 
            jump Finish_exam4
   

        "<strong> </strong>":
            $ correct4 += 1
            hide top_text50 
            jump Finish_exam4


        "<underline> </underlined>":
            hide top_text50 
            jump Finish_exam4

    

label Finish_exam4:
    


    e "Tapos na ang exam"
    e "Ang score mo ay [correct4] "

    jump tapos_exam4










