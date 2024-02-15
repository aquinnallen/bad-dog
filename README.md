<h1>BAD DOG!(they said sweetly)</h1>
This project is a collaboration between four students from The Evergreen State College for the purpose of entering into the Major Leauge Hacking Global Hack Week AI/ML Challenge from 2/9/24-2/15/24.

We are:
Dominic Severe - https://github.com/abyssalremark
Torsten Spieler - https://github.com/EvergreenTor
Devin Eason - https://github.com/de02E
Quinn Allen - https://github.com/aquinnallen

We began work on this project at the beginning of the week-long hack.

None of us had previous experience using trained AI/ML models in our software projects, so we certainly learned a lot!

## Inspiration
You know the way you can confuse a dog by saying "bad dog" in a sweet voice? That's the inspiration. The computer needs to learn how not to be fooled in this way.

## What it does
Takes user upload of an audio file, limited to a recording of a single speaker and performing best on short clips 1-2 minutes at most.

## How we built it
We duct-taped together some existing models with python and built a rudimentary front end website. Models we used include a pre-trained voice-emotion analysis model (https://huggingface.co/speechbrain/emotion-recognition-wav2vec2-IEMOCAP) based on speechbrain (https://huggingface.co/speechbrain), a text sentiment analysis model trained by SamLowe (https://huggingface.co/SamLowe/roberta-base-go_emotions) based on roberta-base (https://huggingface.co/roberta-base). We also used a python speech recognition package for speech-to-text step in our pipeline (https://pypi.org/project/SpeechRecognition/). We used GPT4 to combine/summarize the sentiment analysis data from and also provide an alternative sentiment analysis from the resulting transcript.

We hosted our project in the oracle cloud using apache2 as a webserver for static content. We wrote our API server in Python using Flask.

## Challenges we ran into
We originally intended to use the OCI (Oracle Cloud Infrastructure) AI tools to carry out speech-to-text and sentiment analysis on transcript text, this proved more complicated than we were able to work out in the limited time frame of a week.
We are not experts on the subject, just dipping our toes, so we were not able to successfully train our own models or make anything incredibly sophisticated from scratch.

## Accomplishments that we're proud of
You can upload a .wav file to our website and get an analysis output.
None of us had worked with trained models or high-level AI/ML interfaces previous to this project, so getting anything done was a good outcome from our view!

## What we learned
That we have a lot more to learn!

## What's next for <3Bad Dog:)
Add TLS certs and proxy our API route for security
Maybe clean up that front-end a bit to more clearly communicate with the user.
Experiment with training the speechbrains model from scratch, and creating a custom label set, to articulate more depth if voice-emotion analysis 
