print('''
      Once upon a time, amidst the vast expanse of the ocean, there existed a mysterious island cloaked in mist and legend. 
      Whispers spoke of untold riches hidden within its dense jungles and treacherous terrain. 
      You, a daring adventurer, set sail in pursuit of these fabled treasures, heedless of the dangers that lay ahead.
      ''')

print('Chapter 1: The Landing')
print("As your ship approaches the mysterious island, you face a critical decision:")
print("1. Anchor offshore and silently row to shore under cover of darkness.\n2. Dock at the nearest port and announce your arrival boldly.")

choice1 = int(input("Choose wisely "))
if choice1 == 1:
    print('''
          You choose to anchor offshore and silently row to shore, avoiding detection by any potential inhabitants of the island. 
          As you cautiously step onto the sandy beach, you feel a sense of relief at your stealthy approach. 
          You proceed deeper into the island, ready to face whatever challenges lie ahead.
          ''')
    print("Chapter 2: The Jungle Path")
    print("Entering the dense jungle, you encounter another decision point:")
    print("1. Follow the overgrown path deeper into the jungle, guided by instinct.")
    print("2. Hack your way through the dense foliage, forging your own path.")
    choice2 = int(input("Choose wisely "))
    if choice2 == 1:
        print('''
              You choose to follow the overgrown path deeper into the jungle, trusting your instincts to lead you in the right direction. 
              The path, though challenging, proves navigable, and you make steady progress through the dense vegetation. 
              Along the way, you uncover clues hinting at the location of the island's treasures, fueling your determination to press onward.
              ''')
        print("Chapter 3: The Cave of Whispers")
        print('''
              After navigating through the jungle, you stumble upon a dark cave hidden beneath the vines. 
              Within its depths, faint whispers beckon. Now, you must decide:
              ''')
        print("1. Bypass the cave entirely and press forward through the jungle.")
        print("2. Enter the cave cautiously, following the source of the whispers.")
        choice3 = int(input("Choose wisely "))
        if choice3 == 2:
            print('''
                  You enter the cave cautiously, following the whispers deeper into its dark recesses. 
                  As your eyes adjust to the dim light, you discover ancient markings on the walls, leading you to a 
                  hidden chamber where a valuable artifact lies waiting to be claimed.
                  ''')
            
            print("Chapter 4: The Guardian's Challenge")
            print('''
                  Emerging from the cave, you confront a towering statue with a riddle:
                    "To claim the treasure, you must prove your worth. Answer me this:
                  What is always old and sometimes new, never sad, sometimes blue, never empty, but sometimes full, never pushes, always pulls?"
                  Now, you must decide:
                  ''')
            print("1. Attempt to solve the riddle and prove yourself worthy.")
            print("2. Ignore the statue and press onward, undeterred by its challenge.")
            choice4 = int(input("Choose wisely "))
            if choice4 == 1:
                print('''
                      You ponder the riddle carefully, considering each word. After a moment of contemplation, the answer dawns on you: 
                      "The Moon." You speak the answer aloud, and the statue's stone eyes glow with approval. With a rumble, 
                      the ground beneath you opens to reveal a hidden passage leading deeper into the island.
                      ''')
                print("Chapter 5: The Puzzle Chamber")
                print('''
                As you venture deeper into the island, you come upon a chamber adorned with intricate carvings and mysterious symbols. 
                In the center of the chamber lies a pedestal with a curious artifact resting atop it. 
                Surrounding the pedestal are four pedestals, each with a slot for a gemstone.
                ''')
                print("1. Attempt to bypass the puzzle by brute force or ignoring it altogether.")
                print("2. Examine the carvings and symbols to decipher the puzzle's solution.")
                choice5 = int(input("Choose wisely "))
                if choice5 == 2:
                    print('''
                          You carefully examine the carvings and symbols, deciphering their meaning and piecing together the clues they provide. 
                          Through keen observation and logical deduction, you determine the correct arrangement of the 
                          gemstones and place them in their respective slots. With a satisfying click, the artifact on 
                          the central pedestal unlocks, revealing a hidden passage leading to the treasure chambers.
                          ''')
                    
                elif choice5 == 1:
                    print('''
                          Opting to bypass or ignore the puzzle, you attempt to force your way past it or simply leave it 
                          behind in your eagerness to reach the treasure chambers. However, your impatience proves 
                          costly as the chamber's defenses activate, trapping you within and sealing off any chance of escape. 
                          You find yourself ensnared in a web of intricate mechanisms, unable to proceed 
                          further and facing an uncertain fate within the puzzle chamber.
                          ''')
                    quit()
                else:
                    print("Invalid choice. Game Over")
                    quit()                
                
            elif choice4 == 2:
                print('''
                      Opting to ignore the statue, you press onward, dismissing the riddle as an irrelevant distraction. 
                      However, as you continue your journey, you encounter a series of obstacles that seem 
                      insurmountable without the knowledge gained from solving the riddle. Frustrated and disheartened, 
                      you find yourself unable to progress further, and your adventure on the island comes to an abrupt halt.
                      ''')
                quit()
            else:
                print("Invalid choice. Game Over")
                quit()
            
        elif choice3 == 1:
            print('''
                  Opting to bypass the cave, you continue forward through the jungle, eager to press onward in search of the island's treasures. 
                  However, unbeknownst to you, the cave held vital clues to navigating the treacherous terrain ahead. 
                  Without this knowledge, you find yourself hopelessly lost in the dense jungle, unable to find your way out. 
                  Your adventure on the island ends in frustration as you wander aimlessly, forever trapped within its tangled depths.
                  ''')
        else:
            print("Invalid choice. Game Over") 
            quit()        
        
    elif choice2 == 2:
        print('''
              Opting to blaze your own trail, you begin hacking your way through the dense foliage with a machete. 
              However, your reckless actions attract the attention of a colony of aggressive jungle creatures. 
              Before you can react, you find yourself surrounded by a swarm of venomous snakes, their bites proving fatal. 
              Your journey on the island ends in tragedy as you succumb to the venom coursing through your veins.
              ''')
        quit()
    else:
        print("Invalid choice. Game Over") 
        quit()       
        
elif choice1 == 2:
    print('''
          Opting for a bold approach, you decide to dock at the nearest port and announce your arrival loudly. 
          As you step onto the dock, a group of hostile natives emerges from the jungle, armed with spears and hostility. 
          Before you can react, they attack, overwhelming you and your crew. Your adventure ends abruptly as you meet your 
          demise at the hands of the island's inhabitants.
          ''')
    print("Game Over")
    quit()
else:
    print("Invalid choice. Game Over") 
    quit()
    

