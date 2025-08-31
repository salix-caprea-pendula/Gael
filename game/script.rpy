# Main Script

# Characters
define gael = Character("Gael")

define dandy = Character("Dandy")

define colette = Character("Colette")

define old_woman = Character("Old Woman")

# Persistents

default persistent.shown_warning = False

# Content Warning

label before_main_menu:

    scene black with Pause(1)

    show text "A story by Salix Caprea" at truecenter with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    $ persistent.shown_warning = False # For testing purposes

    if not persistent.shown_warning:
        show text "Content warning: miscarriage, child loss, gore, mutilation, ableism, character death, grooming and sexual assault, and animal abuse." at truecenter with dissolve
        with Pause(2)

        hide text with dissolve
        with Pause(1)

        show text "Gael is an adult game that covers adult topics and themes. Use discretion when playing and always remember that you can exit at any time." at truecenter with dissolve
        with Pause(2)

        hide text with dissolve
        with Pause(1)

    return

label start:
    # Scene 1: Collete has a miscarriage
    play music "giselle.mp3"
    
    scene bg bedroom

    "The blood would not stop coming."

    "It poured from the girl's insides, sometimes stiff with tissue and clots, other times loose and messy."
    
    "Pain bombarded her in waves, and she could not restrain herself from crying out at it. It was her punishment, she supposed, for engaging in such licentious behavior."

    colette "Is that it? Is that the baby?" 

    "The question spilled from her lips despite herself. She wanted to see it — the baby. More than anything she wanted to see the baby."
    
    "It had been made to suffer enough, growing inside of her body that was not yet one of a full woman, and hearing the vitriol her mother and father had hissed her way."
    
    "She wanted to at least bury it nicely and kiss its little head before she sent it off."

    old_woman "Silly child, its not big enough for you to see, just like you weren't big enough to show, and thank Cesmae for that blessing." 

    "An old woman, nose long and drooping, jowls swinging as she spoke, let the girl crush her bony hand as she squatted over a basin." 
    
    "She sat straight-backed on a wooden stool, not even grimacing at her frail extremity enduring such abuse."

    colette "Curse Cesmae! Curse her for stealing my baby from me!"

    old_woman "Stupid, stupid girl!"

    "When all of the material had been expelled from her womb the girl sobbed and gripped the basin; the old woman had to rip it from her hands."

    # Scene 2: Dandy and Gael in snowstorm
    scene bg snowforest

    "Gelid wind blew in the forests of the north."
    
    "To make matters worse, at least for the hunched figure attempting to traverse this inhospitable landscape, a snowfall had begun several hours ago." 

    "The wind was so fierce, and the snow upon the ground and in the branches so light, that half of the particles in the air were not freshly fallen, they were merely on a pilgrimage from one part of the earth to another, 
    joining with their younger brethren in a dance aided by the icy gale."

    "Gael. That was the figure's name as well as the wind's, and trust that the irony of the situation was not lost on her."

    show gael default

    "Indeed, little was ever lost to Gael's mind, especially not thoughts of acidic or melancholy nature. 
    Such thoughts were racing through her head right at that moment, cursing her own hubris."
    
    "Traveling alone through the forests of the north in the winter was a feckless choice, and she should know better by her age — nearly into her fourth dozen of years."

    "Still, the alternative had been taking Corbin or Alix with her. Maybe it was better to freeze through."

    "Her bones were not as young as they once were, and they stiffened and ached at the cold.  The lump nestled close to her base layer on her chest squirmed and yowled."

    gael "I'm well aware, Dandy. I can't exactly make the wind cease blowing."

    "Dandy considered this an inadequate answer, and dug his claws into Gael's chest in reply."

    gael "Damn beast!"

    return
