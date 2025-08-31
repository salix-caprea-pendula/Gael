# Main Script

# Characters
define gael = Character("Gael")

define dandy = Character("Dandy")

define collete = Character("Colette")

# Persistents

default persistent.shown_warning = False

# The game starts here.

label start:
    # Content Warning
    label before_main_menu:

    scene black with Pause(1)

    show text "A story by Salix Caprea" at truecenter with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    $ persistent.shown_warning = False # For testing purposes

    if not persistent.shown_warning:
        "Content warning: miscarriage, child loss, gore, mutilation, ableism, character death, grooming and sexual assault, animal abuse."

    # Scene 1: Collete has a miscarriage

    # Scene 2: Dandy and Gael in snowstorm
    scene bg snowforest

    "Gelid wind blew in the forests of the north."
    
    "To make matters worse, at least for the hunched figure attempting to traverse this inhospitable landscape, a snowfall had begun several hours ago. 
    The wind was so fierce, and the snow upon the ground and in the branches so light, that half of the particles in the air were not freshly fallen, they were merely on a pilgrimage from one part of the earth to another, 
    joining with their younger brethren in a dance aided by the icy gale."

    "Gael. That was the figure's name as well as the wind's, and trust that the irony of the situation was not lost on her."

    show gael default

    "Indeed, little was ever lost to Gael's mind, especially not thoughts of acidic or melancholy nature. 
    Such thoughts were racing through her head right at that moment, cursing her own hubris. Traveling alone through the forests of the north in the winter was a feckless choice, and she should know better by her age — nearly into her fourth dozen of years."

    "Still, the alternative had been taking Corbin or Alix with her. Maybe it was better to freeze through."

    "Her bones were not as young as they once were, and they stiffened and ached at the cold.  The lump nestled close to her base layer on her chest squirmed and yowled."

    gael "I'm well aware, Dandy. I can't exactly make the wind cease blowing."

    "Dandy considered this an inadequate answer, and dug his claws into Gael's chest in reply."

    gael "Damn beast!"

    return
