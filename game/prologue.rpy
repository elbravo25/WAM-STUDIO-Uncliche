# Left side of screen
transform tarinasurprised:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinagrateful:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinaconfident:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinabigsmile:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinaannoyed:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinasigh:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinahurt:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinaamazed:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinaneutral:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinascream:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinathinkingleft:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinadetermined:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinasad:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinaexcited:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinaconfused:
    zoom 3
    xalign 0.0
    yalign 1.0

transform tarinaembarassed:
    zoom 3
    xalign 0.0
    yalign 1.0

# Right side of screen
transform ozproud:
    zoom 3
    xalign 1.0
    yalign 1.0

transform ozamused:
    zoom 3
    xalign 1.0
    yalign 1.0

transform ozmischief:
    zoom 3
    xalign 1.0
    yalign 1.0

transform ozsmile:
    zoom 3
    xalign 1.0
    yalign 1.0

transform ozdisappointed:
    zoom 3
    xalign 1.0
    yalign 1.0

transform friendaright:
    zoom 3
    xalign 1.0
    yalign 1.0

# Center of screen
transform ozmischiefcenter:
    zoom 3
    xalign 0.5
    yalign 1.0

transform tarinathinking:
    zoom 3
    xalign 0.5
    yalign 1.0

transform tarinaneutralcenter:
    zoom 3
    xalign 0.5
    yalign 1.0

transform friendacenter:
    zoom 3
    xalign 0.5
    yalign 1.0

transform ozsilhouette:
    zoom 3
    xalign 0.5
    yalign 1.0

label prlgue:

    scene bg City

    show tarina thinking at tarinathinking

    u1 "Ta...na...rina... {b}{size=+10}Tarina!{/b}{/size}"
    # This can be either alerted or surprised.
    show tarina surprised at tarinasurprised with dissolve 
    # Just add in a delay here.
    show tarina neutral at tarinaneutral with dissolve and easeinright

    show frienda concerned at friendacenter with dissolve
    # Add another delay here later.
    show frienda concerned at friendaright with dissolve and easeinleft

    u1 "Are you okay?"

    ta "I'm... fine... just... thinking is all."
    
    show frienda concerned with dissolve

    u1 "You know we're friends right? You can talk to me if you're having a hard time trying to look for an internship."

    u1 "I know some people who would let you work for them if I asked them for a favour."

    show tarina grateful at tarinagrateful with dissolve

    ta "I appreciate it, Fey, really... I do."

    ta "I know that we've always had each other's backs since our first year in the Academy."

    ta "But there are times where we need to do things on our own."

    ta "This is one of them."

    show tarina confident at tarinaconfident with dissolve

    ta "Besides, I can't let my bestie owe someone else because of me."

    show tarina bigsmile at tarinabigsmile with dissolve

    ta "Watch, I'll get the best job in there is."

    ta "Else, I won't be called Tarina the Stubborn at the Academy for nothing"

    show frienda sigh with dissolve

    fa "You do realise that it's an insult right?"

    show frienda smile with dissolve

    fa "Anyways this is me. Good luck with your job hunt."

    fa "And remember..."

    show tarina annoyed at tarinaannoyed with dissolve

    ta "If I need help I should call you... Sure Mom!"

    scene bg CityOverview

    "Time passes by"

    ta "I say all of that to Fey and here I am still jobless."

    scene bg SecludedPartoftheCity

    show tarina sigh at tarinasigh with dissolve
    
    ta "Am I really that hopeless?"
    # She hits a pole here.
    "Bonk"

    show tarina hurt at tarinahurt with dissolve
    
    ta "Owwww... I should've been paying attention to where I was walking."

    ta "Another lucky day for our heroine Tarina I guess..."

    "As she finally snaps out of her thoughts Tarina notices something weird."

    show tarina surprised at tarinasurprised with dissolve

    ta "Why is it all quiet all of a sudden?"

    ta "It's not even 3pm, yet I don't hear any sounds that are usually there in this city."

    scene bg Alleyway

    play music "oztheme.mp3"

    "As she falls silent she is suddenly drawn to a nearby alleyway."

    

    menu:
        "Should you follow your instinct and follow where the allyway goes to?"

        "Ignore it and go home":
            "You went home..."
            jump end1

        "Walk through the alleyway":
            "You followed went through the alleyway hoping for it to lead you somewhere."

    scene bg OldBuilding

    "As you walked through the alleyway you eventually come across a really old looking building."

    show tarina neutral at tarinaneutral with dissolve

    ta "{i}Well this looks creepy... What's this creepy old building doing in a city known for innovation?{/i}"

    show oz silhouette at ozsilhouette with dissolve

    ou "The owner of that creepy old building is right here you know."

    show tarina surprised at tarinasurprised with dissolve

    ta "{b}{size=+10}Gyaaaaaaaaah!!!{b}{/size}"

    # Center
    show oz mischief at ozmischiefcenter with dissolve
    
    "A mysterious man shows up"

    show oz mischief at ozmischief with easeinleft

    ou "Hohohoo... what an interesting young lady."

    ou "Not only is she lively but she was easily able to get passed the barriers that I have setup all over the place."

    show tarina sigh at tarinasigh with dissolve

    show tarina neutral at tarinaneutral with dissolve

    ta "{i}That scared me... who's this old man? He said that he owned this building... What even is it?{/i}"

    ou "Oh my, do forgive me for my manners young lady. But you can call me Dr. Oz, a humble old wizard that owns this library."

    ta "{i}Oz? Where have I heard of that name before? Wait a minute... Is he reading my mind?!?{/i}"

    o "Hohohoo! I wonder about that young lady. I shall let you think what you will."

    show tarina scream at tarinascream with dissolve

    ta "{b}{size=+10}So he is reading my mind!!!{/b}{/size}"

    o "Fufuu... Well would you come inside? We can talk more about you needing that internship."

    show tarina guarded with dissolve

    ta "Wait... How did you know that I needed one? I have never"

    o "Never mentioned anything and haven't even thought of it the moment you came close to my library?"

    show tarina surprised at tarinasurprised with dissolve

    o "Let's just say a dusty old crow told me."
    
    o "But let's not focus on that, I've been needing an assistant lately."

    o "And your timely arrival makes this the perfect opportunity for both you and me."

    o "I get an assistant that can liven up the library and you get my signature so that you can graduate"

    show tarina thinking at tarinathinkingleft with dissolve

    ta "{i}He is making a good point. This can be an easy job for me to do so I can finally graduate.{/i}"

    ta "{i}Urghhhh... It's annoying how this is literally something that I can't really ignore.{/i}"

    o "So, your response?"

    ta "Alright alright! I'll at least hear you out."

    o "Splendid! Now follow me inside the library."

    scene bg LibraryInside

    play music "librarytheme.mp3"

    # Tarina at left
    show tarina amazed at tarinaamazed with dissolve

    ta "{i}This place is way too different on how it looks like outside{/i}"

    o "Welcome to my Grand Library. Breathtaking isn't it?"

    ta "This is amazing how many books are even in this library?"

    # Oz at right
    show oz proud at ozproud with dissolve

    o "Well I do believe that I have every book under the sun."

    o "The magic I used alone to expand this library to fit all of them took me copius amounts of time."

    ta "Wait you're Dr. Oz of the Tea Party!!!"

    show oz amused at ozamused with dissolve

    o "Well yes I do believe that is indeed one of the groups that I was part with."

    ta "What are you even doing here? You're one of the greatest space and time wizards of all time!"

    ta "You even created the space expansion magic used in magical bags and rooms used today!"

    o "I do believe I did study that on a whim because I wanted a library like this."

    o "Enough about me though... We should talk about your possible internship as my assistant here."

    show tarina determined at tarinadetermined with dissolve

    ta "I accept!!!"

    show oz mischief at ozmischief with dissolve

    o "Fufuuu, while I do quite enjoy your enthusiasm about the job young lady, I really should explain what you are going into young lady."

    show tarina embarassed at tarinaembarassed with dissolve

    ta "Yes! Sorry... Hehe."

    show oz smile at ozsmile with dissolve
    # Add a loud one clap like you're asking for attention.
    o "Onto the explaination then."

    o "But before that I should ask you this question."

    o "Do you hate cliches?"

    ta "I... don't? While technically it gets boring the more it happens. But I'm fine with them."

    o "Well I hate them, it makes it predictable. Oh how I wish there is more variety in stories. That is where you as my assistant come in."

    o "As my assistant you will be required to not only help me arrange the books inside my library and study about the complexities and magic of the stories in these books."

    show tarina confused at tarinaconfused with dissolve
    
    ta "Magic? Complexities?"

    o "Ah! Did I forget to mention that everything in this library has it's own unique magic?"

    o "Not only do they have their own magic. Each book is literally a new world of it's own."

    show tarina neutral at tarinaneutral with dissolve

    o "And your job is to study them by going inside and changing the stories with your presence."

    o "While I have tested the magic of these before we are technically going through uncharted magical territory here."

    o "This is unique magic that you would only be able to experience here."

    o "So, will you join me in this research of mine?"

    show tarina neutral at tarinaneutral with dissolve

    menu:
        "Will you become Dr. Oz's assistant?"

        "Deny the invitation":
            show tarina sad at tarinasad with dissolve
            t "Sorry Dr. Oz but I don't think I can do it."
            show oz disappointed at ozdisappointed with dissolve
            o "It's fine, good luck with your endeavours"
            jump end1

        "Accept the invitation":
            show tarina excited at tarinaexcited with dissolve
            ta "It sounds interesting, I accept!"
            show oz mischief at ozmischief with dissolve
            o "Let's get started then."

    o "These are stories that I have read recently."

    o "Take your pick."

    menu:
        "Which world will you head in first?"

        "The Snow Queen":
            n "Browsing through an array of books, a certain title piqued Tarina’s eyes -- The Snow Queen. A story of bond between two sisters."
            show tarina neutral at tarinaneutralcenter with dissolve
            ta "This seems like a good choice. A straightforward story should be easy to make more unique, right?"
            jump snowqueenBook

        "Peter Pan":
            jump peterpanBook