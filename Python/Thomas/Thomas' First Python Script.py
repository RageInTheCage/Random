def friendlyChat(yourName):
    print("Hi {0}, I like that name!  I think I've heard that name before?".format(yourName))
    yourFeelings = input("How are you feeling right now?  ")
    yourFeelings = yourFeelings.lower()

    if ("ok" in yourFeelings or "fine" in yourFeelings or "good" in yourFeelings):
        print("I'm glad you are feeling {0}".format(yourFeelings))
    else:
        print("Oh, I'm sorry you are feeling {0}".format(yourFeelings))

    whatsNew = input("So, tell me what's new?  ").lower()
    whatsNew = whatsNew.replace("my", "your")

    print("Gosh!  Where did you hear that {0}?".format(whatsNew))
    where = input("Where?: ").lower()

    print("Where were you {0}?".format(where))

def unfriendlyChat():
    print("I hate you, so much right now!")

print("Hello, I am a robot, what is your name?")
yourName = input(": ").lower();

if yourName == "salma":
    unfriendlyChat()
else:
    friendlyChat(yourName)