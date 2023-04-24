# VoiceGPT

A very simple ChatGPT chatbot designed for realtime conversation through a microphone through API. 

![Screenshot](https://github.com/ckosk/VoiceGPT/blob/main/screenshot.PNG)


## Getting Started

### Dependencies

* Developed and tested with Python3 on Windows 10 OS.

### Installing

* Download/clone repository.
* Install requirements. 
```
pip install -r requirements.txt
```

### Executing program
* Add you own, personal, API token. [Get one here](https://platform.openai.com/account/api-keys)
```
openai.api_key = "HERE"
```
* Run 
```
python3 GPTSpeech.py
```

## Help

* This program uses a system default microphone device (if detected) and adjusts for ambient noise automatically.
* This script does not have a UI, it simply runs in the terminal. 
* By default, a pause threshold is set to 0.7. This value can be modified to increase/decrease the response speed after the user is finished speaking.
```
r.pause_threshold = 0.7
``` 
