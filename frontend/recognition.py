import os
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS 
from speechbrain.pretrained.interfaces import foreign_class


counter = 0

classifier = foreign_class(source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP", pymodule_file="custom_interface.py", classname="CustomEncoderWav2vec2Classifier")

app = Flask(__name__)
CORS(app)

@app.route("/",methods= ["GET", "POST"])
def hello():
    return render_template("index.html")

@app.route("/upload_audio_file", methods=["POST"])
def upload_audio_file():
    audioFile = request.files["audioFile"]
    path = "tmp"+str(counter)+".wav"
    audioFile.save(path)
    out_prob, score, index, text_lab = classifier.classify_file(path)    
    resp = {"success": True, "response": text_lab[0]}
    return resp




if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000)
