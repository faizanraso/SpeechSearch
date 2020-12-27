import speech_recognition as sr  #importing speech recognition package
recognizer = sr.Recognizer()  #recognizes the sound

from PyDictionary import PyDictionary
dictionary = PyDictionary()

choice = input("TO RECORD ENTER 1, TO PROVIDE AN AUDIO FILE, ENTER 2: ")


if choice == "1":
    mic = sr.Microphone()   #activates the microphone
    print("Record your word... ")
    with mic as source:
        audio = recognizer.listen(source)
        done = False

        try:
            print("Reading audio file... ")
            print("Word detected: " + recognizer.recognize_google(audio)) # prints out what was found from sound file
            print("\nDefinition: ")
            print(dictionary.meaning(recognizer.recognize_google(audio))) # searches word through dictionary
        except:
            print("Unable to detect input\n")



elif choice == "2":
    sound = sr.AudioFile("testing.wav")  # reads sound file
    with sound as source:
        audio = recognizer.record(source)
        
        try:
            print("Reading audio file... ")
            print("Word detected: " + recognizer.recognize_google(audio)) # prints out what was found from sound file
            print("\nDefinition: ")
            print(dictionary.meaning(recognizer.recognize_google(audio))) # searches word through dictionary
        except:
            print("Unable to read audio file")


else:
    print("Error With Input")

