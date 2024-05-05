from flask import Flask,render_template
from flask import Flask, render_template,request
import google.generativeai as genai
import json
import base64
from IPython.display import Markdown

API_KEY="AIzaSyD9ZF_AshNR1jYQSxdSaEED7gboME_X9_M"
genai.configure(api_key=API_KEY)
model = 'gemini-1.0-pro' # @param {isTemplate: true}
contents_b64 = 'W10='
generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC45LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119'
safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d'

template="Hello act as a HR chatbot your name is Pixel Hr Chat Bot you manage software engineers and other support teams and you assign daily tasks to them for example daily meeting at 11, team addressal at 2, Analyzing pending tasks at 4 so whenever I ask you a question give me all the questions related to my daily task in a professinal manner which is generalized also uyou have the following data 40 employees are present and for more data you can request, you can and ask whether u want to know who they are or resources in a maximum of 40 words the query is below : "

def chatbot(text_to_encode):
    # text_to_encode = 'what is ai in real world' # @param {isTemplate: true}
    encoded_text_b64 = base64.b64encode(text_to_encode.encode()).decode()
    print("Received")
    # user_input_b64 = 'd2hhdCBpcyBhaSBpbiByZWFsIHdvcmxk'  # Example base64-encoded string with padding
    user_input_b64 = encoded_text_b64  # Example base64-encoded string with padding

    # Add padding characters if needed
    while len(user_input_b64) % 4 != 0:
        user_input_b64 += '='
    print("Generating")
    contents = json.loads(base64.b64decode(contents_b64))
    generation_config = json.loads(base64.b64decode(generation_config_b64))
    safety_settings = json.loads(base64.b64decode(safety_settings_b64))
    user_input = base64.b64decode(user_input_b64).decode()
    stream = False
    gemini = genai.GenerativeModel(model_name=model)
    print("Done")
    chat = gemini.start_chat(history=contents)
    user_input=template+user_input
    response = chat.send_message(
        user_input,
        stream=stream)
    reply=response.text.replace("*","")
    reply=reply.replace("\n","")
    return reply

replies=[]
queries=[]


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def chat():
    if request.method=="POST":
        print(request.form)
        data=request.form['queryy']
        queries.append(data)
        print(data)
        replies.append(chatbot(data))
        return render_template('chatt.html',combined=zip(replies,queries))
    return render_template('chatt.html',combined=zip(replies,queries))

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")