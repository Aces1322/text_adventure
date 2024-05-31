# Christian Reyes
# P:2 Text Adventure Game
print(r"""
          
    MMMM          MMMMMMMMMM
  MM-----0000MM000----------000MMMM   
MM------MM-----------------------000MM
MM---000-----------MM----MM----------000MM
MM000000-----------MM----MM---------------MM
MM000--------------MM----MM---------------MM
MM----------0000--------------0000--------00MM
MM000-----------------MM--------------000---MM
    MM----------------MM--------------000---MM
    MM000------------------------------MMMMMM
    MM000-------------------------MM000000000MM
       MM000-------------------MM000000000000MM
       MMMM000----------------MM000000000000MM
    MM000000MMMM00000000000MM000000000000MM
  MM0000000000000MMMMMMMMMM000000000MM
  MMMMMMMMMMMM              MMMMMMM



      """)

item = "blank"
print("Welcome to Dreamland! This is Kirby, the pink puffball.")
print("\nKing Dedede has stolen all the food for himself! The residents are starving!")
print("\nKirby is going on an adventure through Dreamland to stop him.")
print("\nHelp Kirby decide where to go first.")
score = 0
while True:
    world_1 = input("\nWill you go to the Green Grounds (1) or the Butter Building (2)?: ")
    if world_1 ==  "1":
        print(f"\nKirby visits the apple tree named Whispy Woods.")
        print(f"\nHe helps remove the spiky gordos stuck in it's leaves.")
        print(f"\nScore: 25/100")
        score = 25
        break
    elif world_1 == "2":    
        print("\nKirby climbs to the top of the Butter Building and finds Mr Shine.")
        print("\nKirby takes a short breather before continuing the journey.")
        print(f"\nScore: 7/100")
        score = 7
        break
    else:
        False
        print("\nKirby doesn't seem to understand what you said")    
while True:
    world_2 = input("\nWill you go to the Olive Ocean(1) or the Abandoned Aisles(2)?: ")
    if world_2 == "1":
        print(f"\nKirby visits the apple tree named Whispy Woods.")
        print(f"\nHe helps remove the spiky gordos stuck in it's leaves.")
        print(f"\nScore: {score + 25}/100")
        score = score + 25
        break
    elif world_2 == "2":    
        print("\nKirby encounters Meta Knight, the lone swordsman.")
        print("\nMeta Knight gifts a maxim tomato, one of the few foods Dedede couldn't steal.")
        print("\nKirby put the maxim tomato in his inventory")
        print(f"\nScore: {score + 7}/100")
        score = score + 7
        item = 1
        break
    else:
        False
        print("\nKirby doesn't seem to understand what you said")
while True:    
    world_3 = input("\nWill you travel to Dedede Castle(1) or side track to Dangerous Dinner(2)?: ")
    if world_3 == "1":
        print("\nKirby is nearing the end of his journey as he travels to his rival's castle")
        print("\nKing Dedede seems to be acting strange…")
        print("\nKirby defeats King Dedede in a battle, however the sky grows dark...")
        print("\nEnding 1, score: {score + 0}/100")
        score = score + 0
        break
        
    elif world_3 == "2":
        print("\nBefore Kirby completes his journey, he travels to Dangerous Dinner.")
        print("\nKirby helps resolve an argument between the wizard Magolor and the dragon Landia")
        print(f"\nScore: {score + 50}/100")
        score = score + 50
        print("\nKirby has reached the end of his journey and finds King Dedede devouring food on his throne.")
        print("\nSomething seems off about the King…")
        break
    else:
        False
        print("\nKirby didn't understand what you said.")
while True:
    if item == 1:
            print("\nMaybe the maxim tomato will bring him back to his senses!")
            choice = input("\nWill you attempt to feed King Dedede the maxim tomato? Yes(1) No(2)")
            if choice == "1":
                import random 
                a = random.randint(1,3)
                if a == 2:
                    print("\nDedede was freed from a horrible curse placed on him by a dark entity.")
                    print("\nThe sky is a brilliant blue.")
                    print("\nEnding 3, Score: 200/100")
                    break
                else:
                    False
                    print("\nThe King resists.")
            elif choice == "2":
                print("\nKirby leaves the King alone and the people are eventually starved")
                print("\nEnding 2, Score: 0/100")
            else:
                False
                print("\nKirby doesn't seem to understand what you said")   
    else:
        print("\nKirby defeats King Dedede in a battle, however the sky grows dark...")
        print(f"\nEnding 1, score: {score} /100")
        break