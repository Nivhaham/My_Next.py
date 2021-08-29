from file2 import *
from gtts import gTTS
import pyttsx3
def main():
    Niv1 = GreenCard()
    Niv2 = BirthdayCard()
    print(Niv1.greeting_msg())
    print(Niv2.greeting_msg())

    mytext ='first time i\'m using a package in next.py course '
    myobj = gTTS(text=mytext, slow=False)
    print(myobj)

    engine = pyttsx3.init()
    engine.say("first time i\'m using a package in next.py course")
    engine.runAndWait()

if __name__ == '__main__':
    main()
