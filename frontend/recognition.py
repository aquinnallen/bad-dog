from flask import flask, request, render_template, jsonify
from flask_cors import CORS 
from speechbrain.pretrained.interfaces import foreign_class
classifier = foreign_class(source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP",pymodule_file="custom_interface.py",className = "CustomEncoderWav2vec2Classifier")

app = flask(__name__)
@app.route("/",methods= ["GET", "POST"])
def.hello():
    return render_template("index.html")

@app.route("/upload_audio_file", methods=["POST"])
def upload_audio_file():
    audioFile = request.files["audio_file"]
    out_prob, score, index, text_lab = classifier.classify_file(audioFile)

    resp = {"success": True, "response": "file saved!"}
    return text_lab



