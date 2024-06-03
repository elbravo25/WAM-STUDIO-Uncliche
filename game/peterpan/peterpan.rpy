# The script of the game goes in this file.
# The game starts here.

label peterpanBook:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg nurseryRoomOn
    with fade

    "I entered the story in a daze, finding myself in an odd position inside a…drawer?"

    show john angry 
    pause(0.2)

    show john angry at left
    with ease

    j "I’ll teach you to cut off me hand!"
    "Once I snapped back to reality, a boy wearing glasses and a bandanna stood in front of me, his right arm stretched while holding a hanger."
    show wendy neutral at right 
    with moveinright
    w "Oh no, John. It was the left hand."
    show john happy at left with dissolve
    j "Oh yes. Thank you, Wendy."
    "My eyes shifted towards the person who spoke. A young lady wearing a night blue nightgown entered the room: Wendy and this boy in front of me must be John, two of the Darlings’ children."
    show john angry at left with dissolve
    j "Well Peter Pan, give up?"

    "It took a moment to register that John was talking to me. The realization settles in—I am now possessing Michael, the youngest sibling." 
    "And here we are, in the midst of a swordfight, playing out the roles of Peter Pan and Captain Hook."

    menu:

        "Give up":

            jump giveUp

        "Fight":

            jump fight

    label giveUp:

        scene bg nurseryRoomOn
        show michael worried at left
        pause(0.2)

        show michael worried at left
        with ease

        m "I surrender."

        show john angry at right

        j "What are you doing Michael? Peter Pan never gives up!"
        "John looks at me with a disappointed look. I dropped the sword and feign exhaustion, trying to make it as convincing as I can."
        "While it's crucial to maintain the act to avoid suspicion, I should also observe my surroundings."
        "After all, I've just arrived, and it's been a while since I read the story."
        
        hide michael worried
        show wendy worried at left

        w "Now, now John. You've two have been playing for some time. Peter Pan also needs some rest."
        "This may be a chance. Wendy should know all the stories about Peter Pan. Should I ask her?"

        menu:
            "Ask Her":

                jump ask
            
            "No Need":

                jump noNeed
        
        label ask:

            scene bg nurseryRoomOn
            show michael happy at right

            m "Wendy. could you tell the story of Peter Pan again?"
            
            show wendy happy at left
            w "Oh why of course, Michael."

            show wendy neutral at left with dissolve
            show michael neutral at right with dissolve
            w "Peter Pan is boy who lives on the island of Neverland. He has fairy called Tinker Bell."
            w "He is no ordinary boy, because he never grows up and he can fly. Peter is also the leader of the Lost Boys and fights the evil Captain Hook."
            "Before Wendy could continue further, a man with a neatly groomed hair and a neatly trimmed mustache came in the room." 
            "He wore a tailored suit, complete with waistcoat and polished shoes. This must be George Darling."

            jump meet

        label noNeed:

            scene bg nurseryRoomOn
            
            "Peter Pan. Neverland. Lost Boys. Captain Hook. Tinkerbell."
            "I think I still remember some parts of the story. No need to hear it again."
            "As soon as I finished my train of thoughts, a man with a neatly groomed hair and a neatly trimmed mustache came in the room." 
            "He wore a tailored suit, complete with waistcoat and polished shoes. This must be George Darling."

            jump meet
    
    label fight:

        scene bg nurseryRoomOn
        show michael angry at left
        show john angry at right
        m "Never! I'll fight till the end Hook!"
        show john angry at left with easeinleft
        show michael angry at right with easeinright
        "John lunges forward with his sword, I dodged skillfully countering with a swift strike of my own."
        j "Impressive Peter Pan, but I won't go down so easilty!"
        "The nursery room became our battleground, the beds became our makeshift island as we leap, and the sounds of the wooden swords clash around the nursery." 
        hide john angry
        hide michael angry       
        un "Boys, boys less noise please."
        "A man with a neatly groomed hair and a neatly trimmed mustache came in the room." 
        "He wore a tailored suit, complete with waistcoat and polished shoes. This must be George Darling."

        jump meet

label meet:
    scene bg nurseryRoomOn
    show george at left

    g "Wendy have you been telling the tales of Peter Pan again? You should know better than to stuff the boys' heads with those silly stories."
    
    show wendy neutral at right

    w "Oh, but they are real."
    g "Wendy, you are growing up. It's high time you have a room of your own."
    
    show wendy surprised at right with dissolve
    w "Father!"
    g "I mean it. Young lady. this is your last night in the nursery. And that's my last word on that matter."

    scene bg nurseryRoomOff
    with fade

    "After that conversation, a subtle shift in the nursery’s atmosphere could be felt. The tension lingered, casting a shadow over the room."
    "If it weren’t for Mary Darling, who came to tuck us in, the uneasy atmosphere might have stayed."
    "Apparently, they are going to a party and Nana—our nursemaid and dog—was sent out to teach us to grow by ourselves."
    "As I was about to fall asleep, realization dawns on me. Tonight is the night Peter Pan will visit. It feels like I have to do something. What should I do?"

    menu:

        "Check the window lock":
            jump check_window

        "Check the drawer":
            jump check_drawer

        "Let the story flow":
            jump let_story_flow

    label check_window:

        scene bg nurseryRoomOff

        "Did Mother lock the window? I remember Wendy’s request a while ago, but it can’t hurt to check it though."
        "Careful not to wake up my siblings, I crept to the window as quickly as I can, sliding through the room’s darkness until I neared the window."
        "Just then, a figure appeared. It took a second to take in his appearance."
        "The boy seems relatively normal with his fair skin and short red hair. His ears are somewhat pointy, almost elf-like. His outfit matches his ears, with his attire resembling an elf’s, along with a green bycoket."
        "The only things that make him stand out is a fairy flying all around him, her very presence illuminated the darkness with her celestial glow."
        "Also, he was able to enter through the second-floor window, has no shadow, and he can fly. The characters that I could only imagine from reading the books are flying in front of me: Peter Pan and Tinkerbell."

        show peter worried at left with easeinright
        show tink angry at right with easeinleft
        p "Over there Tink, in its den."
        "I watched as Tinkerbell flew through Nana’s doghouse with Peter Pan following close behind her. It seems like they did not notice me."
        "Is it there?"
        t "{i}shakes head{/i}"
        p "Must be here somewhere."
        "He scanned the room as if searching for something, then he finally noticed me. His face looked at me in surprise, like he was processing something."
        show peter surprised at left
        pause(2.0)
        p "Let’s go Tink!"
        hide tink angry with moveoutright
        show peter angry at right with ease
        "With a swift movement, he darted towards the window to make his escape. But I managed to capture his arm before he could vanish into the night."
        show michael surprised at left with moveinleft
        m "Wait! I know where your shadow is!"
        "Caught off guard by my sudden interruption, Peter’s movements ceased abruptly." 
        show peter surprised at right
        "This completely stopped him from flying outside. It was a lucky break; with my body the chances of stopping him would be futile, leaving me to cling to his arms as he flies."
        p "You know where my shadow is?"
        show michael angry at left with dissolve
        m "Yes, I do. But I need you to trust me, not to fly away so suddenly."
        show peter angry at right with dissolve
        p "I don’t trust you…but I need my shadow back. Show me where it is and I won’t escape."
        "That sealed the deal. Instead of answering, I dragged him to the sewing drawer to ensure he stayed true to his word."
        hide peter angry with moveoutright
        show michael angry at center with move
        pause (2.0)
        show michael surprised at right with move
        "As I opened it, the drawer jerked suddenly, pushing me to the floor. Peter Pan flew, catching his shadow just before it could get away."
        show peter excited at left with easeinleft
        p "Aha! Now do you have any idea how to attach this?"
        show michael neutral at right with dissolve
        m "I don’t. But Wendy might. I’ll wake her."
        hide michael neutral with easeoutright
        hide peter excited with easeoutright

        jump wendy_wakes_up


    label check_drawer:

        scene bg nurseryRoomOff

        show michael angry at right
        "From what I recalled; Wendy hid the shadow in the sewing drawer. I should check if it is still there."
        "Careful not to wake my siblings, I crept towards the drawer."
        show michael surprised at left with ease
        "As I opened it, the drawer jerked suddenly, pushing me to the floor."
        "The shadow flew away, circling the room. I tried to catch it but to no avail. I jumped to my bed to grab it but only managed to grasp the air. It’s impossible to catch it with this body."
        "I jumped from my bed and quickly hid behind the shadow of a couch. I saw the shadow move around the close where I am."
        show michael angry at left with dissolve
        "Just a little more… Closer…"
        m "Aha!"
        show michael happy at right with ease
        "I managed to get catch its feet and stopped it from flying around."
        show tink excited at left with easeinleft
        show peter happy at center with easeinleft
        p "Great catch!"
        show michael surprised at right with dissolve
        "The voice startled me that I almost let go of the shadow. I just noticed the window wide was open and a figure stood in front of me."
        "It took a second to take in his appearance. The boy seems relatively normal with his fair skin and short red hair. His ears are somewhat pointy, almost elf-like. His outfit matches his ears, with his attire resembling an elf’s, along with a green bycoket."
        "The only things that make him stand out is a fairy flying all around him, her very presence illuminated the darkness with her celestial glow."
        "Also, he was able to enter through the second-floor window, has no shadow, and he can fly. The characters that I could only imagine from reading the books are flying in front of me: Peter Pan and Tinkerbell."
        "Peter reached his hand out like he was demanding something."
        show peter angry at center with dissolve
        p "Now hand me my shadow back."
        "Oh right, his shadow."
        "I gave it to him and watched him stick it to his shoes without any luck."
        show peter worried at center with dissolve
        p "Do you have any idea how to attach this?"
        show michael angry at right with dissolve
        m "I don’t. But Wendy might. I’ll wake her."
        hide michael angry with easeoutright
        hide peter worried with easeoutright
        hide tink excited with easeoutright

        jump wendy_wakes_up

    label let_story_flow:

        scene bg nurseryRoomOff

        "I laid back in bed and pretended to sleep. Just then I heard the windows open and a boy appeared accompanied by a small, flying light."
        "It took a second to take in his appearance. The boy seems relatively normal with his fair skin and short red hair. His ears are somewhat pointy, almost elf-like. His outfit matches his ears, with his attire resembling an elf’s, along with a green bycoket."
        "The only things that make him stand out is a fairy flying all around him, her very presence illuminated the darkness with her celestial glow."
        "Also, he was able to enter through the second-floor window, has no shadow, and he can fly. The characters that I could only imagine from reading the books are flying in front of me: Peter Pan and Tinkerbell."
        show peter worried at left with easeinright
        show tink neutral at right with easeinleft
        "I watched the scene unfold as the storybook I read unfold before my eyes. Peter Pan was searching the room looking for his shadow while Tinkerbell was flying around, seemingly intrigued by the unfamiliar items."
        "After some rummaging, Peter Pan found the sewing drawer."
        show peter surprised at left with dissolve
        "As he slowly opened it, it jerked suddenly, and the shadow flew all around the room. Peter Pan leapt into action, attempting to catch it."
        hide tink neutral with easeoutright
        show peter furious at right with ease
        "The chase ended when Peter wrestled with his shadow, knocking down the table and vase in the process."

        jump wendy_wakes_up

label wendy_wakes_up:

    scene bg nurseryRoomOff

    "Wendy woke up in a daze with the noise. She looked around the room, then saw the boy from her stories."
    show wendy surprised at center
    w "Peter Pan! Oh, Peter!"
    hide wendy surprised with easeoutright
    show peter surprised at right with easeinleft
    show wendy happy at center with easeinleft

    "Wendy approached Peter Pan with excitement in her voice, causing him to back away as if he were a cornered animal."
    "Wendy began to ramble, her words tumbling out as she noticed the shadow and started sewing it back in place."
    "As she spoke, John woke up equally surprised as Wendy to see Peter Pan in person."
    show john surprised at left with easeinleft
    j "Peter Pan? The Peter Pan?"
    "Remembering that no introductions were made, Wendy introduced us to Peter."
    "She then recounted the events of the night: how it was her last night in the nursery room, and there will be no more stories to listen to."
    hide john surprised at left
    show wendy worried at left with move
    show peter worried at right with dissolve
    p "If you grow up, that means no more stories…"
    show peter furious at right with dissolve
    p "No! Come on! We’re going to Neverland!"
    show wendy surprised at left with dissolve
    w "How do we get to Neverland?"
    show peter happy at right with dissolve
    p "Fly of course!"
    w "Fly?"
    p "It’s easy! All it takes is faith, trust, and pixie dust!"
    show peter excited at right with dissolve
    "Peter grabbed Tinkerbell and some dust fell unto us. The next thing we knew, our feet were no longer touching the floor."
    "We were flying freely."
    p "Come on everybody! Off to Neverland!"
    hide wendy happy with easeoutright
    hide peter excited with easeoutright
    "With that, we are out of our windows, flying over London on the way to Neverland, second star to the right and straight on till morning."
    "After flying for some time, we finally arrived in Neverland."
 

    # This ends the game.

    jump neverland
