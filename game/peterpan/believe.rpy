label believe:

    scene bg jollyRogerShipDeckDay

    "It’s crazy, believing a villain the story I’ve read. But I’ve heard the sincerity in his voice."
    "The way he told me, it was like it he was relieving his memory again. Being captured, experiencing those horrors."
    "Hook may be right about Peter."
    show michael angry at right with dissolve
    m "Don’t get me wrong though. I don’t completely trust everything you said."
    show hook neutral at left with dissolve
    h "Don’t you now? Well, that’s a surprise."
    h "Didn’t you just say you trust me just a bit ago? Or were you just lying to me?"
    m "Heroes are always seen as the good guys; people always follow them believing everything they do without thinking that they may have a hidden agenda."
    m "Not everyone is completely good."
    m "What you said may be true or not, but whatever the case..."
    m "I’ll find the truth out for myself."
    show hook grin at left with dissolve
    h "That’s fine with me."
    h "For a child, you’ve got a good head on your shoulder. Perhaps you’re not like the rest of those blind followers."
    h "Since you still have doubts about me, I’ll show you something for you. Wait here."
    hide hook with easeoutleft
    "He went inside a cabin and came back a little while later."
    show hook grin at left with easeinleft
    "He was holding a lamp, but instead of light inside, it was Tinkerbell."
    h "You see, during the fiasco a while ago we managed to capture someone useful: Tinkerbell."
    h "I’ve giving her to you for safekeeping."
    h "If I can trust you to hold onto Tinkerbell for me, then you can trust me on my word."
    show michael surprised with dissolve
    m "Tinkerbell…I’ll take care of her."
    show hook angry at left with dissolve
    h "See that you do. Keep her hidden and keep a close eye on her."
    h "We don’t want any more trouble than we already have."

    scene bg jollyRogerShipDeckNight
    with fade

    "That night I couldn’t sleep. I’ve been thinking about what Hook said and it feels like I should go do something."
    "I decided to explore the ship."
    "Where should I go?"

menu:
    "Look inside the cabin":
        jump lookInsideCabin

    "Look outside the cabin":
        jump outside

label outside:
    
    scene bg jollyRogerShipDeckNight

    "Maybe I should check around the area, find anything that might be useful."
    "I crept silently through the ship, with the Tinkerbell and her glow as my only source of light."
    "As I navigated the passages, I stumbled upon a small boat tucked away in a hidden corner. "
    "A boat huh…Maybe I should escape, go ask Peter Pan the truth."
    "Just then it hit me. Wendy and John. They’re with Peter Pan."
    "If what Hook said was true, then they might be in danger!"
    "Should I use this boat to escape and save my siblings alone?"
    "Or should I stay here and ask for Hook to help me?"
    "What should I do?"

    menu:
        "Take the ship and rescue my Siblings alone":
            jump rescue

        "Stay in the ship and aid Hook":
            jump stay

    label rescue:
    
    scene bg jollyRogerShipDeckNight

    "I remembered what Hook said to me."
    show michael worried with dissolve
    m "They may become blind followers of Peter Pan, but they’re still my siblings."
    m "I must go and rescue them."
    "I managed to lower the boat into the sea without anyone waking up. Without hesitation, I climbed into the boat and began rowing, the sound of the oars cutting through the calm waters masking my departure."
    "The island loomed in the distance, a beacon of hope amidst the darkness of the night."

    scene bg neverlandBeach
    with fade

    "Finally, after hours of relentless rowing, I reached the shore as the sun began to rise across the horizon. Stepping unto the sandy beach, I felt the cool breeze tousled my hair, a welcome relief after the strain of rowing."
    "My arms ached from the exertion, but there was no time to dwell on the fatigue. I must find my siblings."

    scene bg neverlandforest
    with fade

    "As I ventured deeper into the island, I scanned my surroundings, hoping to catch a glimpse of familiar faces or at least find something to eat."
    "Just then, I heard a chorus of voices in the distance. I moved towards the voices but stopped to hide and observed."
    "Those voices belong to a group of ragtag young boys—6 in total. They were all wearing different animal costume: Fox, Rabbit, Two Raccoons, Bear, and Skunk. They were engrossed in their conversation."
    "And they were talking about Peter Pan."

    show lb1 neutral with dissolve
    lb1 "Remember Peter’s orders! Find the boy, sibling of the mother! As the Lost Boys, we must not disappoint our leader!"
    "Lost Boys 2-6" "Aye, aye sir!"
    hide lb1 neutral
    "I knew it. They are the Lost Boys. If Hook’s words held any truth, these were the kidnapped children."
    "It seems like they are looking for me, which meant Wendy and John must be with them. And so was Peter Pan."
    "I took a deep breath and stepped out of my hiding spot."
    show michael neutral at left with easeinleft
    m "Pardo—"
    show lb3 angry at center with easeinright
    show lb4 angry at right with easeinright
    lb3 "An enemy! Prepare for battle!"
    lb4 "Prepare for battle!"
    "Without a moment to spare, they all jumped into action, their makeshift weapons all pointed toward me."
    show michael worried at left with dissolve
    m "Wait! I am not an enemy!"
    hide lb3 angry with easeoutright
    hide lb4 angry with easeoutright
    show lb1 angry at right with easeinright
    lb1 "Who are you? We demand you state your name!"
    m "Michael! I’m looking for my siblings, Wendy and John. Peter must’ve taken them with him."
    show lb6 neutral at center with easeinright
    lb6 "You’re Michael? They’ve been looking everywhere for you."
    hide lb1 angry with easeoutright
    hide lb6 neutral at right with easeoutright
    show michael neutral at center with move
    "I nodded, relieved to know that they knew who I am."
    "I explained the situation to them—how I have been captured by Hook but was let go."
    show michael neutral at left with move
    show lb6 angry at right with easeinright
    lb6 "That’s impossible. Hook would never let you go."
    show michael worried at left with dissolve
    m "The thing is Hook said something about Peter, he may not be who you think he is."
    "I told them everything he said to me: about Peter Pan, the kidnapping, about their escape."
    m "I have to know the truth. You have to take me to Peter Pan."
    show lb5 angry at center with easeinright
    lb5 "Why would we believe anything you said?" 
    hide lb6 angry with easeoutright
    show lb2 angry at right with easeinright
    lb2 "You can be on Hook's side!"
    hide lb5 angry with easeoutright
    hide lb2 angry with easeoutright
    show lb3 angry at center with easeinright
    show lb4 angry at right with easeinright
    lb3 "Yeah you might be an enemy!"
    lb4 "Be an enemy!"
    hide lb3 angry with easeoutright
    hide lb4 angry with easeoutright
    show lb1 angry at right with easeinright
    lb1 "How can we trust you?"
    hide lb1 angry with easeoutright
    show michael worried at center with move
    "They all backed away, eyeing me suspiciously."
    "I wasn’t surprised. Hook is Peter’s longtime enemy, making him their enemy. Suddenly accusing Peter would naturally make them suspicious of me."
    "I wouldn’t be able to get to Peter Pan this way. I had do something to gain their trust."
    "Then it hit me. Tinkerbell!"
    "If I show them Tinkerbell and release her, they might trust me enough to take me to Peter."
    "However, Hook put his trust to me to keep her. Releasing her would mean breaking that trust."
    "What should I do?"

    menu:
        "Let Tinkerbell go":
            jump letGo

        "Keep Tinkerbell":
            jump keep

    label letGo:
        














    label stay:



return