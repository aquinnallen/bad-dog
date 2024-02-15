from openai import OpenAI

def get_analysis(query, api_key):

  client = OpenAI(api_key=api_key)

  response = client.chat.completions.create(
    model="gpt-4",
    messages=[
      {
        "role": "system",
        "content": "You turn sentiment analysis generated from an audio file into a helpful 3-5 sentence summary. Please do not include percentages from the data. Provide insight to combine the vocal_tone_analysis with the text_analysis."
      },
      {
        "role": "user",
        "content": ("text_analysis{" + str(query["text_analysis"]) + "}\n vocal_tone_analysis: "+ query["vocal_tone_analysis"] + "\n")
      },
    ],
    temperature=.75,
    max_tokens=250,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0.5
  )
  resp = response.choices[0].message.content
  print(resp)
  return resp

def get_sentiment(transcript,api_key):
  
  client = OpenAI(api_key=api_key)

  response = client.chat.completions.create(
    model="gpt-4",
    messages=[
      {
        "role": "system",
        "content": "You are a text sentiment analysis engine, you provide concise analysis of transcripts taken from audio files which are provided by the user."
      },
      {
        "role": "user",
        "content": str(transcript)
      },
    ],
    temperature=.75,
    max_tokens=250,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0.5
  )
  resp = response.choices[0].message.content
  print(resp)
  return resp




