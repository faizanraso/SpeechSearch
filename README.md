# SpeechSearch

SpeechSearch was designed using Python. The program takes a audio recording of a single English word, and returns it's definition. The audio can either be prerecorded and placed in the file directory, or can be recorded using your laptops built in microphone. 

This program uses the SpeechRecognition library which is equipped with Google's Web Speech API. The input recognized from this API is then searched within the PyDictionary Module. If the input is valid, and the word is found in the dictionary, then it's definition is returned, else an error is thrown.


![alt text](https://github.com/faizanraso/SpeechSearch/blob/main/screenshot_1.png?raw=true)
