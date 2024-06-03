label neverland:

    scene bg neverlandIslandTV
    with fade

    show peter happy at right with easeinleft
    show tink excited at left with easeinright
    p "There it is folks. Neverland."
    "Neverland was a vast island filled with mountains and forests."
    "In the distance, there lies a skull-shaped cave surrounded by jagged rock and steep cliff. and in another area in the sea, mermaids can be seen lounged on top of large boulders."
    "We were admiring the beauty of the island where I saw from the middle of the ocean, a pirate ship."
    "Just then…"
    hide peter happy
    hide tink excited
    with vpunch
    "{b}{i}{size=+10}BANG!{/b}{/i}{/size}"
    "A cannonball suddenly came flying towards us!"
    show michael surprised
    m "Look out!"
    hide michael surprised
    "We managed to veer away from the cannonball's trajectory, when we realize they were preparing to fire another round."
    show tink angry at left
    show peter furious at right
    p "Quick Tink! Take Wendy and the boys to the island. I’ll stay here and draw Hook’s fire."
    hide peter furious with easeoutleft 
    t ". . ."
    hide tink angry with easeoutright
    "Tinkerbell suddenly flew off after given instructions."
    "What should I do?"

    menu:

        "Follow Tinkerbell":
            jump follow_tinkerbell

        "Go and hide elsewhere":
            jump hide_elsewhere

    label follow_tinkerbell:

        scene bg neverlandIslandTV

        "We flew after her, each of us struggling to keep up, but Tinkerbell was flying too fast."
        "I didn’t notice a cloud in front of me, making my vision blurry for a moment."
        "Next thing I know, I couldn’t see Tink nor my siblings. Peter had flown off as well, leaving me alone in the sky."
        "I descended towards the waters, hoping to reach the shore when I spotted a boat in the distance."
        "Desperate for help, I flew closer to the boat."
        show michael worried at center with dissolve
        m "Pardon me…"
        show crew1 neutral at right
        "Crew 1" "Oh, what’s this? A flying boy? He must be one of the Lost Boys!"
        show crew2 neutral at left
        "Before I could react, another crew member grabbed me from behind, making escape impossible."
        "Crew 2" "When Captain sees him, he’s going to be ecstatic! Let’s get him back to the ship."
        "I messed up. They are part of the Captain Hook’s crew. And now I’m their prisoner."

        jump captured_by_hook

    label hide_elsewhere:

        scene bg neverlandIslandTV

        "They’re too fast. I won’t be able to keep up. Maybe I should head in a different direction."
        "I decided to veer off, trying to avoid Jolly Roger and stay close to the waters as much as possible."
        "Suddenly a thick fog rolls in, obscuring my vision. Just then I saw a shadow despite the fog."
        show michael worried at center with dissolve
        m "That must be the island."
        "Just as I manage to approach…"
        show crew1 neutral at right
        "Crew 1" "Well, well, what do we have here?"
        show crew2 neutral at left
        "Before I could react, another crew member grabbed me from behind, making escape impossible."
        "Crew 1" "Welcome aboard the Jolly Roger, lad."
        show michael angry at center with dissolve
        m "Let me go!"
        "Crew 2" "Not a chance. Captain’s going to be thrilled to see you."
        "I messed up. Looks like trying to avoid them has led me straight into their hands."
        "And now I’m their prisoner."

        jump captured_by_hook

label captured_by_hook:

    scene bg jollyRogerShipDeckDay
    with fade

    "Being caught by Captain Hook as soon as I got to Neverland. This is definitely the {i}best{/i} thing to happen."
    "The column at my back felt cool, seeping through my clothes, the rope tied tightly around my body to prevent any chance of escape. Various crew members surround me, their eyes fixated on me, ready to react if I made any move."
    "Not that I could, especially with this situation."
    "They were talking amongst themselves when the sudden opening of the door immediately silenced them."
    "A thin man with curly red hair, a large hooked nose, and a large chin wearing a black coat with gold lining and red cuffs walks in. Matching the top is a gray pants with black shoes."
    "Not only that, he also wore a large black hat with a huge orange feathers and an orange sash over his shoulder, likely where he kept his sword. This man is definitely eye-catching, even for a pirate."
    "Especially with his gold hook replacing his left hand. He is, without a doubt, the antagonist of the story: Captain Hook."

    show hook neutral at center with dissolve
    h "Welcome, my boy. I apologize for the lack of hospitality. You see, we are wary you are under the control of Peter Pan, one of the Lost Boys."
    h "But given your strange attire and confusion, it seems like you’re another one of his new recruits."

    show hook neutral at right with move
    show michael surprised at left with easeinleft
    m "Under control? Recruit? What are you talking about?"
    h "Ah you’re new to Neverland. I’ll let you have the privilege of hearing the real Peter Pan from me."
    show hook grin at right with dissolve
    h "Peter Pan, a boy who never grows up, who despises adults, the very idea of children growing up. So what does he do?"
    show hook angry at right with dissolve
    h "He kidnaps children! Takes them away from their homes and families! Filling their heads with the notion that they should never grow up."
    "He brings them to Neverland, turning them into Lost Boys."
    show michael angry at left with dissolve
    m "That’s not true! Peter Pan’s a hero!"
    h "A hero? That’s blasphemy! He is nothing more than a kidnapper, worse: a murderer. Show any signs of wanting to leave or grow up?"
    h "It’s the plank for them, if you catch my drift."
    "The crew erupts in cries of anger, denouncing Peter Pan. It doesn’t make any sense. All of that information is not written in the story. What’s going on?"
    show hook grin at right with dissolve
    h "Oh? Having a hard time believing me are you? Well, I am the villain after all."
    h "But have you ever considered the darkness of your so-called hero? His true image? Because we know."
    h "We were all Lost Boys once."
    "A heavy silence falls. I immediately looked up at Hook, his eyes full of sadness."
    show hook sad at right with dissolve
    h "He killed so many children—those we know, spent time with. We had to escape him."
    h "We lost many in the process, but we were managed to escape his clutches… to grow up."
    h "Now we are pirates, fighting to kill Peter Pan and rescue the children he kidnapped. To save the Lost Boys."
    m "Are you saying you'll let me go?"
    show hook neutral at right with dissolve
    h "Depends on whose side you’re on, boy. Help us stop Pan and free other children."
    h "Pay attention to what you see and hear. You’ll realize the truth soon enough."
    "I fell silent, mulling over my options."
    "Disagreeing might seal my fate. I must pretend."
    show michael neutral at left with dissolve    
    m "I believe you. I’ll do whatever it takes to help you stop him."
    show hook happy at right with dissolve
    h "Excellent decision, my boy. Now, what are you waiting for? Untie him!"
    "Or so I say. But what should I do? Do I really believe everything he said?"

    menu:

        "Believe Captain Hook":
            jump believe

        "Don't believe Captain Hook":
            jump dontBelieve

return