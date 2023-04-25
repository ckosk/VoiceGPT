import openai
import speech_recognition as sr
import pyttsx3
from termcolor import colored
from colorama import init
init()

openai.api_key = "OPENAI_API_TOKEN_HERE"
engine = pyttsx3.init()

#listen for input
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7 #value can be changed for how quickly user speaks. Higher value if user speaks with longer pauses in sentences. 
        r.adjust_for_ambient_noise(source) #automatically adjust for ambient noise
        print("Speak:")
        audio = r.listen(source) #starts listening

    try:
        prompt = r.recognize_google(audio, language="en-EN", show_all=False)
        print(colored(prompt, 'green') + "\n")
        resp = openai.Completion.create(
            engine="text-davinci-003", #engine, 003 is higher quality content generation than 002 engine
            prompt=prompt,
            temperature=0.7, #how much randomness is in the output. Between 0 and 1. Lower value = more simple/repetitive responses. 
            max_tokens=150 #value can be changed to fit user needs/usage limits
        )

        #response
        GPT_resp = str(resp['choices'][0]['text']).strip('\n\n')
        print(GPT_resp + "\n")
        engine.say(GPT_resp)
        engine.runAndWait()

    #if spoken recognition fails
    except:
        GPT_resp = ("Your request was not understood, please try again shortly.")
        print(GPT_resp)
        engine.say(GPT_resp)
        engine.runAndWait()
