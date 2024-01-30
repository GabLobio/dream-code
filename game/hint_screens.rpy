




######################################################################################################################
init python:
    def IncrementHintCounts():
        global ls2_numhc
        ls2_numhc += 2

    def IncrementHintCounts3():
        global ls3_numhc
        ls3_numhc += 2

    def IncrementHintCounts4():
        global ls4_numhc
        ls4_numhc += 2

    def IncrementHintCounts5():
        global ls5_numhc
        ls5_numhc += 2

screen head_hint():
    image "images/empty_board.png"
    
    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts(), Return()]
    
    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Headings:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. “<h1>”- Heading 1{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use for the main heading or title of your content.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h1>Welcome to My Game</h1>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}2. “<h2>” - Heading 2{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Subheadings or sections within the main content.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h2>Chapter 1: The Beginning</h2>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}3. “<h3>” - Heading 3{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Further subdivisions of <h2> sections.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h3>Scene 1: Exploring the Forest</h3>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}4. “<h4>” - Heading 4{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use for subsections within <h3>.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h4>Discovering a Hidden Path</h4>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}5. “<h5>” - Heading 5{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Subsections of <h4> or smaller details within your content.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h5>Collecting Clues</h5>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}6. “<h6>” - Heading 6{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Rarely used. Smallest level of heading, often for minor details.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h6>Note: Important Reminder</h6>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen img_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts(), Return()]

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Images:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}“<img>” - Image Tag{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use the <img> tag to embed images in your webpage.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n    {b}Attributes{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • {b}src{/b}: Specifies the source (URL or file path) of the image.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • {b}alt{/b}: Provides alternative text for accessibility.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • {b}width{/b}: Sets the width of the image.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      • {b}height{/b}: Sets the height of the image.' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <img src="image.jpg" alt="A beautiful landscape" width="500" height="300">' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n    {b}Explanation:{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • The {b}src{/b} attribute specifies the image file.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • The {b}alt{/b} attribute describes the image for users with screen readers or if ' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '        the image fails to load.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • {b}width{/b} and {b}height{/b} attributes control the size of the displayed image.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n'
                    text '\n'
                    text '\n'
                    text '\n'


######################################################################################################################


screen comment_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts3(), Return()]

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Comments:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}“ <!-- --> ” - Comment{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use <!-- --> to add comments in your HTML code. Comments are not displayed' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '         on the webpage but can provide helpful notes for developers.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n    {b}Example:{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n     <!-- This is a comment. It won`t appear on the webpage. -->' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen standards_best_practices_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts3(), Return()]

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Standards & Best Practices:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}Indentation in HTML{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '\n    • Maintain consistent indentation to enhance code readability. Use spaces or ' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '       tabs consistently throughout your HTML document.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n    • Choose either spaces or tabs and stick to the same indentation style.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n    • Use indentation to represent the hierarchy of HTML elements.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n    {b}Example:{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n     <html>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <head>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <title>My Webpage</title>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        </head>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n        <body>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <h1>Welcome to My Webpage</h1>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <p>This is a sample paragraph.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <!-- Additional elements go here -->' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        </body>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n     <html>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '\n     Use an indentation size of 2 or 4 spaces for readability.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '     Also Consistent indentation helps you spot errors and maintain a clean code structure.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen text_formatting_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts4(), Return()]

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Text Formatting:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Bold Text - <strong> and <b>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use <strong> for strong importance and <b> for bold text. <strong> is semantically preferred.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <p>This is <strong>important</strong> information.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <p>This is <b>bold</b> text.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6




                    text '\n\n{b}2. Italic Text - <em> and <i>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      Use <em> for emphasized text and <i> for italic text. <em> is semantically preferred.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <p>This is <em>emphasized</em> text.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <p>This is <i>italic</i> text.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}3. Underline Text - <u>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use <u> for underlined text. However, underlining is not always recommended for readability.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <p>This text is <u>underlined</u>.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n\nThese tags help convey meaning and structure to your text.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\nAlways consider the semantics of your content when choosing between semantic and presentational tags.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen links_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts4(), Return()]

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Links:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Basic Link - <a>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use the <a> (anchor) tag to create hyperlinks.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      {b}Attributes{/b}:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '      • {b}href{/b}: Specifies the URL of the linked page or resource.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <a href="https://www.example.com">Visit Example.com</a>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}2. Linking to Another Page in the Same Site{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • For links within the same website, use relative URLs.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <a href="/about">About Us</a>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}3. Adding Link Text - <a>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Include descriptive text within the <a> tags to provide context.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <p>Visit <a href="https://www.example.com">Example.com</a> for more informa</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen list_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts4(), Return()]

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}List:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Unordered List - <ul>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Use <ul> to create a list without a specific order.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <ul>>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Item 1</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Item 2</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Item 3</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            </ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n\n{b}2. Ordered List - <ol>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Use <ol> to create a numbered list.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <ol>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>First Step</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Second Step</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Third Step</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            </ol>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n\n{b}3. List Items - <li>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Use <li> inside <ul> or <ol> to represent each item in the list.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Red</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Green</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Blue</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            </ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n\n{b}4. Nested Lists{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • You can put lists inside other lists to create a hierarchy.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Fruits' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                        <li>Apple</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                        <li>Banana</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                </li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n                <li>Vegetables' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                        <li>Carrot</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                        <li>Spinach</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                </li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n            </ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen attribute_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts5(), Return()]

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Attribute:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. What Are Attributes?{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      Attributes give extra information about HTML elements.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n\n            • {b}id{/b}: Gives a unique identifier to an element.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <div {b}id{/b}="header">Page Header</div>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n\n            • {b}src{/b}: Specifies the source (URL or file path) for elements like images.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <img {b}src{/b}="image.jpg" alt="A beautiful landscape">' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n\n            • {b}href{/b}: Provides the link destination for <a> (anchor) elements.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <a {b}href{/b}="https://www.example.com">Visit Example.com</a>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



######################################################################################################################


screen menus_nav_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts5(), Return()]

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Menus & Navigation:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Creating a Navigation Bar{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Use the {b}<nav>{/b} element to define a navigation bar.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            {b}<nav>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <li><a href="#home">Home</a></li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <li><a href="#about">About</a></li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <li><a href="#contact">Contact</a></li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                </ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            {b}</nav>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n\n{b}2. List-Based Menu{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Create a horizontal menu using an unordered list (<ul>) and list items (<li>).' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li><a href="#products">Products</a></li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li><a href="#services">Services</a></li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li><a href="#support">Support</a></li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            </ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen form_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action [lambda: IncrementHintCounts5(), Return()]

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Forms and Submitting Forms:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Creating a Form{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Use the <form> element to create a form.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <form action="/submit">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <!-- Form elements go here -->' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </form>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n\n{b}2. Adding Form Elements{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Use various form elements like <input> and <select>.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <form action="/submit">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <label for="username">Username:</label>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <input type="text" id="username" name="username">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <label for="password">Password:</label>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <input type="password" id="password" name="password">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <input type="submit" value="Submit">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </form>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n\n{b}3. Submitting Data{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Add a submit button (<input type="submit">) to let users send the form data.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <form action="/submit">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <!-- Form elements go here -->' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <input type="submit" value="Submit">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </form>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen drop_down_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Drop-Down Menu:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Creating a Drop-Down {/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the <form> element to create a form.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <label for="cars">Choose a car:</label>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      <select id="cars" name="cars">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <option value="volvo">Volvo</option>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <option value="saab">Saab</option>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <option value="mercedes">Mercedes</option>' size 24 color "#dfdfdf" xoffset 6 yoffset 6 
                    text '\n        <option value="audi">Audi</option>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </select>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen video_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Videos:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Embedding Videos with <video>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the <video> element to embed videos.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <video width="400" height="300" controls>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <source src="example.mp4" type="video/mp4">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        Your browser does not support the video tag.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </video>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      The controls attribute adds play, pause, and volume controls.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen audio_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Audios:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Adding Audio with <audio>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the <audio> element to embed audio files.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <audio controls>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <source src="audio.mp3" type="audio/mp3">' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        Your browser does not support the audio tag.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </audio>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      The controls attribute adds play, pause, and volume controls.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen layout_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Audios:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    text '\nPage Layout in HTML (with Header, Main, Footer)' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n{b}1. Header Section{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the <header> element for the top section of your page.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <header>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <h1>My Website</h1>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <p>Welcome to my awesome website!</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </header>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n\n{b}2. Main Content Section{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the <main> element for the main content of your page.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <main>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <h2>Featured Content</h2>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <p>This is the main content of the page.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </main>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n\n{b}3. Footer Section{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the <footer> element for the bottom section of your page.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <footer>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <p>This is the footer content of the page.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </footer>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the <header>, <main>, and <footer> elements for a clear page structure.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\nCreating a layout with these elements helps maintain a structured and organized webpage.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen style_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}The Style Attribute:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n{b}1. Basic Styling{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the style attribute to apply basic styles like color, font size, and background.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <p style="color: blue; font-size: 16px; background-color: #eee;">Styled Paragraph</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n\n{b}2. Multiple Styles{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Combine multiple styles within the style attribute.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <span style="font-weight: bold; text-decoration: underline;">Bold and Underlined Text</span>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • The style attribute is applied directly to the HTML element within its opening tag.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      • Separate styles with a semicolon (;) and use colons (:) to define property-value pairs.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\nUsing the style attribute allows you to add quick and specific'  size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text 'specific styling directly to individual HTML elements.'  size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen inline_block_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}The Style Attribute:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n{b}1. Block Elements{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Block-level elements start on a new line and take up the full width available.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <div>This is a block-level element.</div>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      <p>This is also a block-level element.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      <h1>This is a heading (block-level).</h1>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n\n{b}2. Inline Elements{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Inline elements don`t start on a new line and only take up as much width as necessary.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <span>This is an inline element.</span>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      <strong>This is also an inline element.</strong>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      <a href="#">This is a link (inline).</a>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n\n{b}3. Mixing Inline and Block{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • You can have both inline and block elements within each other.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <div>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <p>This is a block-level element with <span>inline</span> content.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </div>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen div_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Divide:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n{b}1. Using <div> for Division{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the <div> element to create a division or container for grouping content.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <div>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <h2>Section 1</h2>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <p>This is the content of Section 1.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </div>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n\n      <div>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <h2>Section 2</h2>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <p>This is the content of Section 2.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </div>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n\n The <div> element is versatile and commonly used to structure and separate content.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen table_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Tables:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n{b}1. Creating a Basic Table{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use the <table> element to create a table.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      • Use <tr> for table rows, <th> for table headers, and <td> for table data.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <table>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <th>Name</th>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <th>Age</th>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <th>City</th>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        </tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n        <tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <td>John</td>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <td>25</td>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <td>New York</td>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        </tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
            
                    text '\n        <tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <td>Jane</td>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <td>30</td>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <td>London</td>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        </tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n      </table>' size 20 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n{b}2. Spanning Rows or Columns{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • Use {b}colspan{/b} or {b}rowspan{/b} to span multiple columns or rows.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      <table>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <th>Name</th>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <th {b}colspan{/b}="2">Details</th>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        </tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n        <tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <td>John</td>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <td>Age: 25</td>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <td>City: New York</td>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        </tr>' size 20 color "#dfdfdf" xoffset 6 yoffset 6
                
                    text '\n      </table>' size 20 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n\nUse the <thead>, <tbody>, and <tfoot> elements for better organization in larger tables.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6