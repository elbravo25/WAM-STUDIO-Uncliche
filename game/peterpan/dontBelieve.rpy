label dontBelieve:

    scene bg jollyRogerShipDeckNight
    with fade

    "Definitely not. Those are just lies, nothing more than an attempt to manipulate me into helping him. With my decision final, I decide to explore the ship."
    "Everyone was asleep, worn out from the day."
    "I need to find a way out. It’s now or never. But where should I search?"

menu:
        "Look inside the cabin":
            jump lookInsideCabin

        "Look outside the cabin":
            jump lookOutsideCabin

label lookOutsideCabin:

    scene bg jollyRogerShipDeckNight

    "Maybe I should check around the area, find anything that might be useful."
    "I crept silently through the ship, with the moonlight as my only source of light. As I navigated the passages, I stumbled upon a small boat tucked away in a hidden corner."
    "It was a stroke of luck—a chance to escape from this ship."
    "I managed to lower the boat into the sea without anyone waking up. Without hesitation, I climbed into the boat and began rowing, the sound of the oars cutting through the calm waters masking my departure."
    "The island loomed in the distance, a beacon of hope amidst the darkness of the night."

    scene bg neverlandBeach
    with fade

    "Finally, after hours of relentless rowing, I reached the shore as the sun began to rise across the horizon. Stepping unto the sandy beach, I felt the cool breeze tousled my hair, a welcome relief after the strain of rowing."
    "My arms ached from the exertion, but there was no time to dwell on the fatigue. I must find my siblings."
    "But first, I have to search for food to restore my energy."

    scene bg neverlandforest
    with fade

    "As I ventured deeper into the island, I scanned my surroundings, hoping to catch a glimpse of familiar faces or at least find something to eat."
    "Just then, I heard a chorus of voices in the distance. I moved towards the voices but stopped to hide and observed."
    "Lesson learned from my recent captivity."
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
    "I explained the situation to them—how I have been captured by Hook but managed to escape."
    "However, I omitted the details of Hook’s claim about Peter Pan, not wanting to sow discord among the group."
    "The Boys listened intently, amazed by what happened."
    show michael neutral at center with easeinright
    show lb2 neutral at right with easeinright
    lb2 "Wow! You escaped Hook by yourself!"
    show lb5 neutral at left with easeinleft
    lb5 "He must be worthy of being a Lost Boy."
    hide lb5 neutral with easeoutleft
    show lb1 neutral at left with easeinleft
    lb1 "Easy now. Our priority is to bring him back to Peter and accomplish the mission."
    m "I really want to see my siblings. And to be honest, I could use something to eat. I’m starving."
    lb2 "Don’t worry. We’ll get you something to eat once we reach our hideout."
    show michael happy at center with dissolve
    m "Thank you. I appreciate it."

    scene bg peterPanHideout
    with fade

    show wendy worried at right with easeinleft
    show john worried at left with easeinright
    w "Oh Michael! We were so worried!"
    j "Where have you been? You were just behind me, then the next thing we know—bam. You’re gone."
    "Finally, after what felt like eternity, I was reunited with them. I recounted the events that led to my disappearance while I devoured the food given to me."
    "So much had happened, but in the moment, I was grateful to be here. Finally getting the much-needed food and rest as well."
    hide wendy worried
    hide john worried
    show peter happy with dissolve
    p "Well, that was something! You really have what it takes to be a Lost Boy. But we really do have to do something about Hook. We must take him down!"
    "We all cheered, buoyed by Peter’s words. I felt a swell of pride, especially at being praised by Peter himself. He truly is a remarkable leader."
    "After resting, my energy was restored, and I was back into action."
    p "You know, since you’re the only one stuck with Hook, you haven’t had a chance to explore Neverland."
    show peter excited with dissolve
    p "Boys, gather round!"
    p "I’m giving you this important mission, if you wish to take it. Show Michael around Neverland. I’ll go ahead and scout the island, Wendy and John, stay here."
    hide peter excited with easeoutleft
    "With that, Peter flew off into the distance, leaving me with the other Lost Boys. He was right—I hadn’t had the chance to explore Neverland, and now seemed like a perfect opportunity to do so."
    
    
    scene bg neverlandForest
    with fade

    "As we finished exploring Neverland, a sense of camaraderie had blossomed between me and the Lost Boys. We had traversed through the Mermaid Lagoon, Skull Rock, Indian Camp, Dead Man’s Peak and other locations."
    "Everything was just as I imagined from the stories I heard and read."
    "Just when we were about to head back to camp, Peter descended from the sky, his face filled with urgency."

    show peter furious with easeinright
    p "Boys, listen up! I’ve received word of Hook’s whereabouts. He’s planning something big, and we need to stop him once and for all."
    "The Lost Boys erupted into cheers and shouts, ready for the challenge that lays ahead. Then Peter’s gaze turned towards me."
    show peter angry with dissolve
    p "Michael. You’ve proven to be brave and resourceful. Have what it takes to be part of us."
    p "So what will it be? Will you join our battle with Hook and officially become a member of the Lost Boys?"
    "What will I do?"

    menu:
        "Go back to my Siblings":
            jump siblings
        "Fight together with the lost boys":
            jump fight_together

    label siblings:

    scene bg neverlandForest

    show michael worried at right with dissolve    
    m "As much as I would like to join the fight, I can’t accept it."
    m "My siblings need me, and I can’t leave them worrying about my safety."
    show peter worried at left with dissolve
    p "That’s too bad. You would’ve been a valuable ally."
    p "You can find your way back to the hideout alone, can’t you?"
    show michael neutral at right with dissolve
    m "Yes, I’ll manage."
    show peter furious at left with dissolve
    p "Alright boys let’s get planning! This will be the greatest battle ever! And we will win!"
    "The greatest battle, and I won’t have any part of it."
    "I watched for a moment as they eagerly discussed their strategy. A sense of longing tugged at my heart, the idea of the thrill of battle beckoned."
    "But no. I need to go back to my siblings."
    hide michael with easeoutright
    "And with that, I rush back to the Hideout."

    scene bg peterPanHideout
    with fade

    show michael worried at left with easeinleft
    m "Wendy! John!"
    show wendy surprised at center with easeinright
    show john surprised at right with easeinright
    w "Oh my, what is it Michael?"
    j "What’s the rush?"
    show michael angry at left with dissolve
    m "Peter Pan and the Lost Boys are going to fight Captain Hook. We have to get out of here fast."
    show john happy at right with dissolve
    j "Really? Then we should watch! A great war will begin, we can’t miss it."
    show wendy worried at center with dissolve
    w "Michael’s right. As much as I want to stay, we have to leave."
    w "We might get caught in the crossfire."
    show wendy neutral at center with dissolve
    w "And besides, we’ve been gone long enough. Mother and father must be worried."
    show john worried at right with dissolve
    j "Aw shucks, you’re right. But how do we get back by ourselves?"
    "Silence was the only answer. We had no idea. We just followed Peter Pan, and that’s all we know. Even in the stories, it didn’t mention how to get back."
    "That’s it. We’re doomed."
    j "I think we need to go to Peter, ask for his help."
    hide john worried
    hide michael angry
    show tink happy at right with easeinright
    show wendy surprised at left with easeinleft
    "Suddenly, Tinkerbell appeared, darting around us."
    w "Oh what is it, Tink?"
    "Tinkerbell flew towards a jar full of scrolls and stood on top of one."
    "Wendy went towards her and got the scroll; she unrolled it and revealed a map."
    "The map shows Skull Rock, and further than that is another island, Tinkerbell went and pointed towards a location in the map on that island."
    show wendy neutral at left with dissolve
    w "Should we go there? Is that the way home?"
    show tink excited at right with dissolve
    "Tinkerbell nodded excitedly, then she flew all around on top of us."
    "Like she was celebrating something."
    hide tink with easeoutleft
    "Weird. I never thought she would help us. At the very beginning, it seems like she hated us—or Wendy to be exact."
    "I guess she really wants us to leave Neverland."
    show wendy worried at left with dissolve
    w "But how can we get there? Certainly, flying would be difficult."
    show michael neutral at center with easeinright
    m "My boat. I mean Captain Hook’s boat, the one I used to escape his ship. We can use that."
    show john worried at right with easeinright
    j "Do you remember where it is?"
    m "Of course."
    show wendy happy at left with dissolve
    w "That’s great! We should leave now while the sun is still high."
    w "Thank you, Tink!"
    hide wendy happy with easeoutleft
    hide john worried with easeoutleft
    hide michael neutral with easeoutleft
    show tink excited with dissolve
    "We gathered our things quickly. Tink still dancing around, not bothering to hide her happiness at our departure."
    "It’s a good thing Wendy doesn’t think much of it; otherwise, she may be offended."

    scene bg neverlandBeach
    with fade

    "The travel going to this island took hours. But thankfully, it wasn’t as challenging with all three of us taking turns rowing."
    "As we landed, the sun was still high, but its descent signaled that the night was approaching."
    "We have to hurry."
    "With no time to rest, we ventured onwards with only ourselves and a map to rely on."
    "Eventually, we were able to stumble upon the fairies’ cave, hidden deep within the forest."
    show wendy neutral with dissolve
    w "Well then, let’s go in."

    scene bg fairyCave
    with fade

    "As we stepped into the cave, the darkness dissolved, replaced by soft, shimmering light around us."
    "Fairies."
    "They emerged from the depths of the cave, their delicate wings glimmering in the gentle glow."
    "The once silent cave was now filled with the sound of their chatter, surprised at our unexpected presence."
    "Suddenly, a fairy flew in front of us, commanding the attention of the entire cave. The silence returned, with all eyes towards her."
    show queen neutral with dissolve
    q "Welcome to the Fairy Cove. I am the Fairy Queen."
    q "It’s rare for us to have visitors. What brings you here?"
    show queen neutral at right with move
    show wendy neutral at center with easeinleft
    w "Why, hello. I am Wendy, and these are my brothers, John and Michael. We’ve come seeking your help."
    show john neutral at left with easeinleft
    j "A fairy we know, Tinkerbell, led us to this place. Telling us that you can help us return home."
    hide wendy neutral
    show michael worried at center with easeinleft
    m "Is it true? Can you really help us?"
    "Whispers and murmurs from the fairies echoed among the fairies as the Queen pondered on our request."
    "We held our breath, our only hope resting on her decision."
    q "Please wait here."
    hide queen neutral with easeoutright
    "After what felt like an eternity, she returned back accompanied by another fairy."
    hide michael worried
    hide john worried
    show navigator neutral at right with easeinright
    show queen neutral at center with easeinright
    q "We can help you."
    q "This is our navigator, skilled in guiding those who are lost in their way."
    q "She will become your guide home. Follow her and be careful not to lose your way."
    q "And to return home, you must fly."
    show wendy happy at left with easeinleft
    w "Oh, thank you! Thank you so much!"
    hide wendy happy with easeoutleft
    hide navigator neutral with easeoutleft
    "With gratitude in our hearts, we bid farewell to the Queen and the fairies."
    "And just like that, with faith, trust, and a sprinkle of pixie dust, we were soaring through the air once more."

    scene bg neverlandIslandTV
    with fade

    "As we flew above the island, our eyes widened at the breathtaking sight below. Neverland stretched out before us, its beauty amplified by the vast expanse of the surrounding ocean."
    "But as we gazed further, a revelation unfolded—the presence of countless other islands, hidden from view until now."
    show john surprised at right with dissolve
    j "Incredible. I had no idea there were so many islands here."
    hide john surprised
    show navigator neutral at left with dissolve
    n "Indeed. These islands remain veiled to those who traverse Neverland’s skies. The fog and clouds shroud them from sight, rendering them nearly invisible."
    show wendy surprised at right with dissolve
    w "So Neverland isn’t just a small place? It’s part of something bigger?"
    n "Precisely. Neverland is part of an archipelago in Asia. Yet, Neverland remains unknown to the world beyond. They do not appear on the maps commonly used by your people."
    n "At least, that’s what I’ve heard."

    scene bg nurseryRoomOff
    with fade

    "Finally, we returned home. We thanked and bid farewell the navigator fairy."
    "We had been through so much, and now we were back in the familiar comforts of our home."
    show wendy happy at left with easeinleft
    w "I can't believe we're finally back."
    show john happy at right with easeinright
    j "Me neither. It feels like a dream."
    show michael happy at center with easeinleft
    m "A dream that we'll never forget."
    "We shared a moment of quiet reflection, each lost in our own thoughts as we processed the whirlwind of emotions from our journey."
    show wendy neutral at left with dissolve
    w "I wonder if anyone will believe our story."
    show john neutral at right with dissolve
    j "Who knows? Maybe it's better if they don't."
    show michael neutral at center with dissolve
    m "Agreed. It is now our story to keep."
    hide john neutral with dissolve
    hide wendy neutral with dissolve
    "As we settled back into the familiar rhythms of home, the memories of Neverland lingered like a cherished dream—a chapter of our lives that we would always carry with us."
    hide michael neutral with dissolve

    jump end

    label fight_together:

    scene bg neverlandForest

    show michael angry at left with easeinleft
    m "There’s not much to think about. If it means keeping Neverland safe from Hook, I’ll help."
    m "Let me join the battle."
    show peter excited at right with easeinright
    p "Now that is what I’m talking about."
    hide michael with easeoutleft
    show peter angry at center with move
    "Okay boys, time to start the meeting."
    p "I heard that Hook is planning to go after the Indian chief’s daughter, Tiger Lily. Most likely to blackmail them into joining their side and to get information on our hideout."
    show lb1 angry at left with dissolve
    lb1 "That’s low!"
    hide lb1 angry with dissolve
    show peter furious at center with dissolve
    p "The lowest of the low! That’s why we’ll ambush them, just like how they ambushed us."
    p "We must stop him, end it once and for all."
    p "For the sake of Neverland!"
    "Cheers erupted among us. As we gathered around, Peter laid out the plan. We would launch a surprise attack on the Jolly Roger, coming from above and throwing the crew overboard."
    show peter happy at center with dissolve
    p "Instead of always defending, we must attack. Show them what we’re capable off!"
    hide peter happy with dissolve
    "With that, we started preparing for our battle. Waiting for the start of our battle filled us with nervousness and anxiety. Will we be able to pull it off?"
    "During the waiting period I managed to convince Wendy and John to let me join. They were really against it but eventually gave up and accepted it when I wouldn’t budge."
    "Finally, the time of the battle arrived. It starts now."

    scene bg jollyRogerShipDeckDay
    with fade

    "We quickly flew above the ship, hiding amongst the clouds."
    show peter angry with dissolve
    p "This is it, folks. Commence operation in 3…2…1…0."
    hide peter angry    
    "As soon as the countdown reached zero, we dove down towards the Jolly Roger."
    "The plan was simple."
    "Three of the Lost Boys stayed above the clouds, hidden from view, acting as our snipers. The rest of us went in as hand-to-hand combatants, stationed in different areas of the ship to cover each other’s blindspot."
    "Peter would handle Hook, while we took care of the crew, ensuring that the fight between the two captains remained uninterrupted by other pirates."
    "As we descended, we immediately started our attack, throwing them overboard one by one."
    show crew1 neutral with dissolve
    "Crew 1" "AMBUSH! ALERT THE CAPTAIN!"
    hide crew1 neutral
    "It seems like the commotion we made was enough since Hook, immediately showed up as soon as the words left the crew’s mouth."
    "With that, the battle officially began. Swords clashed and water splashed as we threw the pirates overboard. Shouts of struggle and determination filled the noise of the ship."
    "Our small bodies made it easier for us to avoid their attacks and outmaneuver them."
    "Our main goal: Seize the ship."
    show peter furious at left with dissolve
    show hook angry at right with dissolve
    "From my peripheral vision, I could see Peter and Hook fighting on the deck above. There was a huge difference between their weapons—Peter’s dagger against Hook’s longsword."
    "But Peter held his own, his flying skills compensating for the disadvantage in weaponry."
    hide peter furious with dissolve
    hide hook angry with dissolve
    show michael angry at left  
    show crew2 neutral at right
    "I returned my focus to the crew member I was fighting. It was the same pirate who had captured me before."
    "Time for revenge."
    show crew2 neutral at left with easeinleft
    show michael angry at right with easeinright
    "With swift movements, I dodged his attacks, using my smaller size to my advantage."
    "I swung my weapon, aiming for his legs to destabilize him. The pirate stumbled, and with a final push, I managed to knock him overboard."
    hide crew2 neutral with fade
    show lb6 angry
    lb6 "Michael, watch out!"
    hide lb6 angry
    show crew1 neutral at right with easeinleft
    show michael angry at left with easeinright
    "I turned just in time to see another pirate lunging at me. With quick reflexes, I parried his attack and countered, sending him tumbling off the side of the ship."
    hide crew1 neutral with fade    
    m "Thanks!"
    hide michael angry
    "The battle raged on. Our plan was working; we were gaining the upper hand. The rest of the Lost Boys were also holding their ground, throwing pirates overboard."
    show smee neutral
    "Just then, out of the corner of my eye, I saw a pirate in the corner of the ship, hiding. No one was marking him. He then saw me look at him and raised his gun."
    "He was aiming for me."
    hide smee neutral
    
    scene bg black with pixellate

    with hpunch
    "{b}{i}{size=+10}BANG!{/b}{/i}{/size}"
    "The sound was deafening I braced myself for the pain, but I never felt it."
    lb5 "Peter!"

    scene bg jollyRogerShipDeckDay with pixellate

    show smee neutral with dissolve
    "Opening my eyes, it became clear that pirate shoot towards Peter. His aim towards me was a diversion. His true goal was Peter."
    hide smee  neutral
    show peter surprised at right with dissolve
    show hook excited at left with dissolve
    "Peter lay on the ground, his dagger far away from him, and Hook is stepping on his foot, preventing him from flying. His longsword was pointed directly at Peter’s chest."
    "He wasn’t shot, but the gunshot had distracted him, giving Hook the upper hand."
    hide peter surprised
    hide hook excited
    show michael surprised at left
    show smee neutral at right
    "My attention snapped back to reality when I heard a shout nearby. A pirate lunged, trying to capture me."
    show michael angry at right with easeinleft
    show smee neutral at left with easeinright
    "I reacted instantly, outmaneuvering him. Using the momentum he had from running, I easily pushed him overboard."
    hide smee with fade
    hide michael
    show lb3 angry at right with dissolve
    show lb4 angry at left with dissolve
    lb3 "Let me go!"
    lb4 "Me go!"
    hide lb3 angry
    hide lb4 angry
    "I watched as the pirates took advantage of the distraction to capture the Lost Boys, including the three snipers who had descended to help. Chaos was breaking out all around us."
    "Everyone was captured, everyone except me."
    "Panic surged in my veins, but there was no time to waste. I had to act quickly to save them."
    "Flying towards the upper deck, I hid from the pirates who were too busy celebrating by capturing the Boys."
    "My focus is on Hook, who was fixated on Peter, relishing his victory."
    show peter angry at left with easeinright
    show hook excited at center with easeinright
    h "Just as I thought, Pan. Without flying, you’re just a boy."
    h "A boy who fears growing up."
    "I inspected my surroundings and spotted a loose rope. Perfect."
    "I grabbed it, tying it into a makeshift lasso, and quietly ascended the rigging above the deck, positioning myself directly above Peter and Hook."
    "Not yet."
    show hook grin at center with dissolve
    h "And here you are. Thinking that you can defeat a grown up like me. You and your little bands of misfits are finished."
    "Just a bit more."
    show hook neutral at center with dissolve
    h "Any last words Pan?"
    show peter furious at left with dissolve
    p "You haven’t won, Hook. We’ll always prevail."
    show hook grin at center with dissolve
    h "Such adorable last words."
    h "Goodbye, Peter Pan."
    "{b}{i}{size=+10}NOW!{/b}{/i}{/size}"
    "Just as he was about to stab Peter, I swung the lasso, looping it around the sword and flinging it into the sea."  with hpunch
    show michael angry at center with easeinleft
    show hook angry at right with easeinleft
    show peter surprised at left with dissolve
    h "WHAT THE—"
    "The surprise made him lose his footing and before he could regain it. I flew towards him, putting all my weight into a push."
    "And he fell."
    hide hook angry with fade
    "{b}{i}{size=+10}SPLASH!{/b}{/i}{/size}"
    hide peter surprised
    hide michael angry at right
    "He fell into the sea."
    "Pirate Crew" "CAPTAIN!"    
    "The crew immediately went to the side of the boat, eagerly watching for their captain to rise."
    "His head popped out of the water, his fury evident even from the deck."
    h "Michael! I’ll get you! Even if it’s the last th—"
    "Before he could finish his sentence, he was pulled back underwater, as if something had grabbed him from below."
    "We watched, bewildered, as he scrambled back up, panicking."
    h "Help me! Help me please!"
    "He flailed wildly, like he was drowning."
    "We were all confused until the clear water slowly turned red."
    "None of us could react as he submerged, the last thing we saw was his golden hook."
    "Too stunned to speak, we watched as a crocodile emerged from where Hook had been."
    "It hit me. Crocodile Creek was the place in Neverland where crocodiles mainly stay there. One crocodile in particular had a grudge against Hook for reasons I couldn’t recall."
    "It seems like that crocodile has finally enacted its revenge."
    show michael surprised at right with dissolve
    m "Hook is dead."
    show peter surprised at left with dissolve
    p "That’s right Hook is dead, we won."
    hide michael surprised
    show peter furious at center with move
    p "ATTENTION!"
    p "The battle is over. Your captain has fallen. We won."
    p "If you don’t want to end up like your captain, release the Lost Boys at once, and abandon ship."
    "With that, the pirate crew quickly untied the Lost Boys their faces pale with fear. They scramble to unto their small boat, eager to sail away from the Jolly Roger. The sight of their captain’s demise had shattered their resolve."
    show peter happy at left with easeinright
    show michael neutral at right with easeinright
    p "Michael, you really saved me there. We won this battle because of you."
    show michael happy at right with dissolve
    m "Thanks, Peter but it’s not just me. I couldn’t have done it without all of you."
    show peter excited at left with dissolve
    p "Let’s go back home and celebrate!"
    "Lost Boys" "Aye, aye, Captain!"
    hide peter excited with dissolve
    hide michael happy with dissolve
    "We flew back to the hideout, the adrenaline of victory still pumping through our veins. The Lost Boys were buzzing with excitement, reliving moments of the battle with animated gestures and loud laughter."

    scene bg peterPanHideout
    with fade

    show wendy worried at right with easeinleft
    show john worried at left with easeinleft
    "When we arrived, Wendy and John greeted us with concern in their eyes. Questions bombarded us about what happened, why we were gone for so long, where we were, and the like."
    "We told them everything: the battle, Hook’s demise, our victory."
    w "Oh Michael. That was quite an adventure. You’ve been very brave, but it’s about time we head home now. Mother and Father must be worried."
    hide john with easeinleft
    show peter worried at left with easeinleft
    p "Michael, you’ve proven yourself worthy today. How about you stay with us in Neverland? You could be a Lost Boy, help us recruit more kids, just like I did with you."
    hide wendy worried
    hide peter worried
    "What they both said tore me. While I missed home, I wouldn’t be able to get the adrenaline I had there."
    "The idea of staying in Neverland, of living this adventurous life indefinitely, was tempting. The thought of endless days of fun, of never growing up."
    "The adventures that I’ve only heard from Wendy—they’re all going to be real. They’re going to be my life. That’s when I made the decision."
    show michael neutral at left with easeinleft
    show john worried at center with easeinleft
    show wendy worried at right with easeinleft
    m "I’d love to go home, Wendy."
    m "But I’m a Lost Boy now, and I want to help Peter and the others in finding more children like me."
    m "I do miss Mom and Dad, and I’ll miss both of you but I’ll be staying in Neverland. This is where I belong."
    show wendy neutral at right with dissolve
    w "Oh Michael, I understand. We won’t force you."
    show john neutral at center with dissolve
    j "Just don’t forget to visit us, okay?"
    show michael happy at left with dissolve
    m "Of course, John, I wouldn’t miss it."

    scene bg black
    "We then went back to London for Wendy and John to return, using the Jolly Roger ship with Tinkerbell’s dust. We bid a tearful farewell before heading back to Neverland."
    
    scene bg peterPanHideout
    with fade

    show peter excited with dissolve
    p "We have a recruit! The seventh Lost Boy and our Vice-Captain! Let’s all celebrate!"
    hide peter excited
    show michael worried with dissolve
    "As we celebrated our victory, the reality of my decision sank in."
    "I would be staying in Neverland, living the life of a Lost Boy, recruiting new kids to join our adventures."
    show michael neutral with dissolve
    "It was a new chapter, one filled with endless possibilities and adventures. The memory of my family tugged at my heart, but I knew they would understand. This is my new home, my new family."
    show michael happy with dissolve
    "I’ve become a boy who never grows up."

    jump end




