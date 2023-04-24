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
        print("Speak:")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        prompt = r.recognize_google(audio, language="en-EN", show_all=False)
        print(colored(prompt, 'green') + "\n")
        resp = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=300
        )

        #response
        GPT_resp = str(resp['choices'][0]['text']).strip('\n\n')
        print(GPT_resp + "\n")
        engine.say(GPT_resp)
        engine.runAndWait()

    #if spoken recognition fails
    except:
        GPT_resp = ("I could not understand your request, please try again shortly.")
        print(GPT_resp)
        engine.say(GPT_resp)
        engine.runAndWait()
