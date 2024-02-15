#Allows acces to .env variables
import os
from dotenv import load_dotenv

#Server handling
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

#speech to text
import speech_recognition as sr

#Modules
from speechbrain.pretrained.interfaces import foreign_class
from transformers import pipeline

#gpt_query
from gpt_call import *

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

counter = 0

#this one is for the audio analysis. change name later for clarity.
classifier = foreign_class(source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP", pymodule_file="custom_interface.py", classname="CustomEncoderWav2vec2Classifier")

#this one for text
classifier_text = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

# Initialize recognizer class (for audio to text)
r = sr.Recognizer()

app = Flask(__name__)
CORS(app)

@app.route("/",methods= ["GET", "POST"])
def hello():
    return render_template("index.html")

@app.route("/upload_audio_file", methods=["POST"])
def upload_audio_file():
    global counter
    audioFile = request.files["audioFile"]
    path = "tmp"+str(counter)+".wav"
    counter = counter +1
    audioFile.save(path)
    text = rip_text(path)
    out_prob, score, index, text_lab = classifier.classify_file(path)
    text_label = ''
    match text_lab[0]:
      case 'neu':
        text_label = 'neutral'
      case 'ang':
        text_label = 'angry'
      case 'hap':
        text_label = 'happy'
      case 'sad':
        text_label = 'sad'

    #print(classifier.hparams.label_encoder)
    text_output = classifier_text(text)
    text_output = text_output[0][0:5]
    print(text_output)

    label = []
    percent = []
    for i in range(0,5):
       # print(type(text_output))
        label.append(text_output[i].get("label"))
        percent.append(str(int(text_output[i].get("score") * 100))+'%')
    query = {"vocal_tone_analysis":text_label,"text_analysis":{label[0]:percent[0],label[1]:percent[1], label[2]:percent[2], label[3]:percent[3], label[4]:percent[4]}}
    print(query)
    gpt_resp = get_analysis(query,OPENAI_API_KEY)
    gpt_sentiment = get_sentiment(text,OPENAI_API_KEY)
    resp = {"Audio Transcript":text,"Chat GPT4 Combined Sentiment":gpt_resp,"Chat GPT4 Sentiment from Text":gpt_sentiment,"Text Sentiment Analysis Result from Go Emotions":query['text_analysis'], "Vocal Tone Analysis Result from SpeechBrain":query['vocal_tone_analysis']}
    return resp

def rip_text(path):
    # audio object
    audio = sr.AudioFile(path)
    #read audio object and transcribe
    with audio as source:
        audio = r.record(source)
        result = r.recognize_google(audio)
    return result

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000)
