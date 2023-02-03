""" AI Assistant robot with Arduino and Python Version 1.0.1 

"""


import speech_recognition as sr   # voice recognition library
import random                     # to choose random words from list
import pyttsx3                    # offline Text to Speech
import datetime                   # to get date and time
import webbrowser                 # to open and perform web tasks
import serial                     # for serial communication
import pywhatkit                  # for more web automation

# Declare robot name (Wake-Up word)
robot_name = 'john'

# random words list
hi_words = ['hi', 'hello', 'yo baby', 'salam']
bye_words = [ 'tata', 'hasta la vista']
r_u_there = ['you there']

# initilize things
engine = pyttsx3.init()                    # init text to speech engine

"""For female voice"""
# voices = engine.getProperty('voices')      #check for voices
# engine.setProperty('voice', voices[1].id)  # female voice

listener = sr.Recognizer()                 # initialize speech recognition API



# connect with NiNi motor driver board over serial communication
try:
    port = serial.Serial("COM9", 9600)
    print("Phycial body, connected.")
except:
    print("Unable to connect to my physical body")


def listen():
    """ listen to what user says"""
    try:
        with sr.Microphone() as source:                         # get input from mic
            print("Talk>>")
            # listen from microphone
            voice = listener.listen(source)
            command = listener.recognize_google(
                voice).lower()  # use google API
            # all words lowercase- so that we can process easily
            #command = command.lower()
            print(command)

            # look for wake up word in the beginning
            if (command.split(' ')[0] == robot_name):
                # if wake up word found....
                print("[wake-up word found]")
                # call process funtion to take action
                process(command)
    except:
        pass


def process(words):
    """ process what user says and take actions """
    print(words)  # check if it received any command

    # break words in
    # split by space and ignore the wake-up word
    word_list = words.split(' ')[1:]

    if (len(word_list) == 1):
        if (word_list[0] == robot_name):
            talk("How Can I help you?")
            # port.write(b'l')
        return



    if word_list[0] == 'play':
        """if command for playing things, play from youtube"""
        talk("Okay boss, playing")
        # search without the command word
        extension = ' '.join(word_list[1:])
        port.write(b'u')
        pywhatkit.playonyt(extension)
        port.write(b'l')
        return



    elif word_list[0] == 'search':
        """if command for google search"""
        port.write(b'u')
        talk("Okay boss, searching")
        port.write(b'l')
        extension = ' '.join(word_list[1:])
        pywhatkit.search(extension)
        return



    if (word_list[0] == 'get') and (word_list[1] == 'info'):
        """if command for getting info"""
        port.write(b'u')
        talk("Okay, I am right on it")
        port.write(b'u')
        # search without the command words
        extension = ' '.join(word_list[2:])
        inf = pywhatkit.info(extension)
        # read from result
        talk(inf)
        return



    elif word_list[0] == 'open':
        """if command for opening URLs"""
        port.write(b'l')
        talk("Okay, I am on it ,Opening, Boss")
        url = f"http://{''.join(word_list[1:])}"   # make the URL
        webbrowser.open(url)
        return



    elif word_list[0] == 'say':
        """if command for opening URLs"""
        talk("Scanning panalists, 3 faces detected. the panalists are, DR. prabha niranjan, Dr shivakumar b r, ashwini")
        port.write(b'h')
        port.write(b'l')
        # url = f"http://{''.join(word_list[1:])}"   # make the URL
        # webbrowser.open(url)
        return




    elif word_list[0] == 'who':
        """if command for opening URLs"""
        talk("I am A I powered robot operating in 5 volts 0.5 amps with arduino nano microcontroller with 3 servo motors , 7 0 8 5 Ic and bunch of wires.  ")
        port.write(b'u')
        # url = f"http://{''.join(word_list[1:])}"   # make the URL
        # webbrowser.open(url)
        return


        
    elif word_list[0] == 'what':
        """if command for opening URLs"""
        talk("Hi, I am your personal assistant.There's a lot I can help with. Try saying play music, search anything, turn on light.")
        port.write(b'u')
        # url = f"http://{''.join(word_list[1:])}"   # make the URL
        # webbrowser.open(url)
        return



    
    elif word_list[0] == 'make':
        """if command for opening URLs"""
        talk("eee sala cup rcb gay")
        port.write(b'u')
        port.write(b'l')
        # url = f"http://{''.join(word_list[1:])}"   # make the URL
        # webbrowser.open(url)
        return

        



    elif word_list[0] == 'my':
        """if command for opening URLs"""
        talk("the menter is sudharshan , and team members are karthik, kiran, mokshith, kishan, gowtham")
        port.write(b'u')
        # url = f"http://{''.join(word_list[1:])}"   # make the URL
        # webbrowser.open(url)
        return




    elif word_list[0] == 'are':
        """if command for opening URLs"""
        talk("I am always there ,to you help you, Waiting for your commands, Boss")
        port.write(b'p')
        # url = f"http://{''.join(word_list[1:])}"   # make the URL
        # webbrowser.open(url)
        return


    elif word_list[0] == 'power':
        """if command for opening URLs"""
        talk("Shutting down system.")
        port.write(b'h')
        port.write(b'u')
        port.write(b'l')
        # url = f"http://{''.join(word_list[1:])}"   # make the URL
        # webbrowser.open(url)
        return



    elif word_list[0] == 'self':
        """if command for opening URLs"""
        talk("system check in processes. Reclibrating components.")
        port.write(b'h')
        port.write(b'u')
        port.write(b'l')
        port.write(b'p')
        talk("Self test is completed with no fault")
        # url = f"http://{''.join(word_list[1:])}"   # make the URL
        # webbrowser.open(url)
        return


    elif word_list[0] == 'uppercut':
        port.write(b'u')

    elif word_list[0] == 'smash':
        port.write(b's')

    elif word_list[0] == 'punch':
        port.write(b'p')

    # now check for matches
    for word in word_list:
        if word in hi_words:
            """ if user says hi/hello greet him accordingly"""
            port.write(b'l')               # send command to wave hand
            talk(random.choice(hi_words))

        elif word in bye_words:
            """ if user says bye etc"""
            talk(random.choice(bye_words))


def talk(sentence):
    """ talk / respond to the user """
    engine.say(sentence)
    engine.runAndWait()


# run the app
while True:
    listen()  # runs listen one time
