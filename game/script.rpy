# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image umbre="images/umbreon.png"

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show umbre at right

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    "Once you add a story, pictures, and music, you can release it to the world!"
    
    $ name=renpy.input("what is your name",default="name")
    $ name=name.strip()
    if not name:
        $ name="anon"
    "Welcome [name]"
    
    menu:
        "this is option 1":
            jump option1
        "this is option 2":
            jump option2
    label option1:
        e "you have chosen option 1"
        jump endoption
    label option2:
        e "you have chosen option 2"
    label endoption:
        
    $ index = 0
    label startloop:
        if index >=10:
            jump endloop
        e "this is iteration [index]"
        $ index = index+1
        jump startloop
    label endloop:
        
        

    return
