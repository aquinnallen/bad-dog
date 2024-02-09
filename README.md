# bad-dog
Purpose: analyzing sentiment from speech using combined analysis of speech-to-text -> sentiment analysis and recording -> emotion analysis

Tools we will use:
speechbrain model https://huggingface.co/speechbrain/emotion-recognition-wav2vec2-IEMOCAP   
oracle text-to-speech   
oracle sentiment analysis API   
LLM to give final digest of combined analysis of file    

MVP:
User uploads an audio file to our website, our backend accumulates all the info on the file and assembles a response.
Maybe add a sweet graph?
