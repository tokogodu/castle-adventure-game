import pyttsx3
engine = pyttsx3.init()

engine.say("hello!, we are going to go on a advanture!  ")
engine.runAndWait()
engine.say("which way do you want to go? to the castle, or to the forest?  ")
engine.runAndWait()
def wheretogo():
    location = input("where do you want to go?:")
    if "castle" == location:
        engine.say("ok, lets go to the castle  ")
        engine.runAndWait()
    else:
        engine.say("oh, thats not a location, lets try again")
        engine.runAndWait()
        wheretogo()
wheretogo()
engine.say("oh no, there are zombies after us!")
engine.runAndWait()
engine.say("ok, we have to fight them, choose your weapon ")
engine.runAndWait()
def whichweapon():
    weapon = input("gun axe or a toothbrush:")
    if "gun" == weapon:
        engine.say("ok, thats a good choise, lets shoot those nasty zombies! ")
        engine.runAndWait()
    elif "axe" == weapon:
        engine.say("ok, thats a good choise, lets chop up those zombies!!  ")
        engine.runAndWait()
    elif "toothbrush" == weapon:
        engine.say("thats a very very bad decision, what are we going to do with that little plastic toothbrush, clean their teeth?, thats it your dead!")
        engine.runAndWait()
        engine.say("ok, we have to start again ")
        engine.runAndWait()
        whichweapon()
    else:
        engine.say("oh, thats not a weapon, lets try again")
        engine.runAndWait()
        whichweapon()
whichweapon()
engine.say("thats good we killed those zombies")
engine.runAndWait()
engine.say("ok, now thats over, lets continue our journey")
engine.runAndWait()
engine.say("oh no, there is a giant zombie!")
engine.runAndWait()
engine.say("ok, these kind of zombies have a big tree log, and they always attack on the enemys left, so remember that")
engine.runAndWait()
engine.say("ok get ready we have to destroy that giant zombie")
engine.runAndWait()
engine.say("and, remember you have a special abilty called dash you can dash forward, back ,left,  and,  right!")
engine.runAndWait()
engine.say("get ready, hes attacking you!")
engine.runAndWait()
def whichdash():
    dash = input("which way do you want to dash? right or left?:")
    if "right" == dash:
        engine.say("oh, good job,!! you remembered that the giant zombie attacked on your left, and you dashed right, im proud of you!")
        engine.runAndWait()
    elif "left" == dash:
        engine.say("come on, didnt i say that the giant zombie attacked on your left?, and you dashed to the left,thats it, giant zombie bonked your head, and now your dead")
        engine.runAndWait()
        whichdash()
    else:
        engine.say("thats not a place you can dash to, lets try again")
        whichdash()
        
whichdash()
engine.say("ok, now that you dodged his attack, we can fight back, and also remember this!,, the giant zombie holds his giant tree log on the ground and pushes it around, so attacking him in the legs would be a bad choice")
engine.runAndWait()
engine.say("and you will be fighting with your axe because the gun will do nothing because of his hard skin")
engine.runAndWait()
engine.say("ok, get ready to attack")
engine.runAndWait()
def wheretohit():
    hitplace = input("where do you want to hit the giant zombie? to the legs? or to the arms?:")
    if "arms" == hitplace:
        engine.say("thats good you rememberd that attacking him on his legs would be a bad choise so you attacked on his arms, hes a little damaged so thats good for us,")
        engine.runAndWait()
    elif "legs" == hitplace:
        engine.say("come on didnt i tell you thats attacking him in the legs would be a bad choise? thats it he killed you we have to start again")
        engine.runAndWait()
        wheretohit()
    else:
        engine.say("thats not a place you can attack, lets try again!")
        engine.runAndWait()
        wheretohit()
wheretohit()
engine.say("ok he is a little damaged an he cant hold his giant tree log anymore so thats good,")
engine.runAndWait()
engine.say("ok hes getting ready to attack but he cant attack with his tree log he has to fight with his fists and his fists are not that strong than the tree log")
engine.runAndWait()
engine.say("remember, you have a shield, so its time to block,")
engine.runAndWait()
def blockwhere():
    wheretoblock = input("which way do you want to block left? or to the right?:")
    if "left" == wheretoblock:
        engine.say("good job, you still rememberd that he attacked on your left,you have good brain,")
        engine.runAndWait()
    elif "right" == wheretoblock:
        engine.say("haha you have bad brain, you didnt remember that he attacked on your left haha you are dead ")
        engine.runAndWait()
        blockwhere()
    else:
        engine.say("thats not a location you can block, lets try again")
        engine.runAndWait()
        blockwhere()
blockwhere()
engine.say("good job you blocked his fists, now its time for the final attack,you have to chop his head off if you want him to die,and on his left he has a rocky neck and with that axe you would do nothing,")
engine.runAndWait()
engine.say("if you want to reach his head you have to jump on these big rocks and then jump again to reach his head, theres two big rocks, one on his left and one on his right")     
engine.runAndWait()
def jumptowhere():     
    wheretojump = input("which way do you want to go on his left or to his right?:")
    if  "left" == wheretojump:
        engine.say("come on didnt i say that on his left he had a rocky neck thats it we have to start again")
        engine.runAndWait()
        jumptowhere()
    elif "right" == wheretojump  :
        engine.say("good job you cut his head off now we can finnaly continue our journey in peace")
        engine.runAndWait()
    else:
        engine.say("thats not a place you can jump to lets try again")
        engine.runAndWait()
        jumptowhere()
jumptowhere()
engine.say("lets go, we finnaly arrived at the castle, outside of the castle there was a metal sign, that said stay out of this castle!, im helding the princess hostage, and im a big dragon, so stay out of this land")
engine.runAndWait()
engine.say("we go inside the castle and what we see? a bunch of human skeletons")
engine.runAndWait()
engine.say("now we are in the castle we need to find the princess and set her free")
engine.runAndWait()
engine.say("you hear that?, is that the dragon breathing??, oh no! ok get ready, lets fight the dragon,")
engine.runAndWait()
engine.say("now remeber the dragon is very strong, and he flies everywhere, so ill give you this bow so it can be easier,")
engine.runAndWait()
engine.say("you see that dragon yea? we need to pull his heart out thats the only way we can deafeat him")
engine.runAndWait()
engine.say("okay i think the dragon is sleeping, first we have to make damage to the heart, beacouse thats were all the power is, so if we can make damage to the heart he wont be as strong than he is now")
def attacktowhere():
    wheretoattack = input("ok where do you want to attack to the leg or to the heart?:")
    if "leg" == wheretoattack:
        engine.say("oh no you forgot that the dragons only weakness was his heart and now you awakend the dragon and you are gonna die, good luck next time")
        engine.runAndWait()
        attacktowhere()
    elif "heart" == wheretoattack:
        engine.say("good job you did a lot of damage to the dragon but you awakend him and now is the time that we have to fight seriously")
        engine.runAndWait()
    else:
        engine.say("thats not a place you can attack to, lets try again")
        engine.runAndWait()
        attacktowhere()
attacktowhere()
engine.say("ok now that we did damage we have to fight with the bow, looks like he is flying left so we have to lounch that arrow into hes heart! remember we have to fight with the bow")
engine.runAndWait()
def shoottowhere():
    wheretoshoot = input("what weapon do you want to fight with? with the bow? or with sword?")
    if "bow" == wheretoshoot:
        engine.say("good job you have made real damage to the dragon")
        engine.runAndWait()
    elif "sword" == wheretoshoot:
        engine.say("oh no you didnt remember that you will have to fight with the bow to defeat the dragon that it the dragon killed you, lets try again")
        engine.runAndWait()
        shoottowhere()
    else:
        engine.say("oh thats not a place where you can shoot that bow, lets try again")
        engine.runAndWait()
        shoottowhere()
shoottowhere()

