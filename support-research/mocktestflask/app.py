from flask import Flask,render_template,request
import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
import cv2
import assemblyai as aai
import random
# def transcribe(filepath):
#     aai.settings.api_key = "7da4e41ef2064e469ac7a17185928eef"
#     transcriber = aai.Transcriber()

#     # transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
#     transcript = transcriber.transcribe(filepath)
#     return transcript
import google.generativeai as genai
import json
import base64
import pathlib
import pprint
import requests
import mimetypes
from IPython.display import Markdown

roadmap = {
    "Foundations of Data Science": [
        "Statistics Fundamentals",
        "Probability Theory",
        "Linear Algebra",
        "Calculus",
        "Data Visualization Techniques"
    ],
    "Programming Languages": [
        "Python Basics",
        "Data Manipulation with Pandas",
        "Data Visualization with Matplotlib and Seaborn",
        "Introduction to SQL",
        "Version Control with Git"
    ],
    "Machine Learning Fundamentals": [
        "Introduction to Machine Learning",
        "Supervised Learning Algorithms (Regression, Classification)",
        "Unsupervised Learning Algorithms (Clustering, Dimensionality Reduction)",
        "Model Evaluation and Validation Techniques",
        "Hyperparameter Tuning and Model Optimization"
    ],
    "Deep Learning": [
        "Neural Networks Basics",
        "Deep Learning Frameworks (TensorFlow, Keras, PyTorch)",
        "Convolutional Neural Networks (CNNs) for Image Classification",
        "Recurrent Neural Networks (RNNs) for Sequence Modeling",
        "Transfer Learning and Fine-Tuning Pre-trained Models"
    ],
    "Data Preprocessing and Feature Engineering": [
        "Data Cleaning Techniques",
        "Feature Scaling and Normalization",
        "Handling Missing Data",
        "Feature Engineering Methods",
        "Dimensionality Reduction Techniques"
    ],
    "Big Data Technologies": [
        "Introduction to Big Data and Hadoop Ecosystem",
        "Working with Distributed Data Processing (MapReduce)",
        "Apache Spark Fundamentals",
        "Spark SQL and DataFrame Operations",
        "Stream Processing with Apache Kafka"
    ],
    "Natural Language Processing (NLP)": [
        "Introduction to NLP and Text Processing",
        "Tokenization and Text Normalization",
        "Sentiment Analysis",
        "Named Entity Recognition (NER)",
        "Sequence-to-Sequence Models for Machine Translation"
    ],
    "Time Series Analysis": [
        "Time Series Data Visualization",
        "Time Series Decomposition",
        "Forecasting Methods (ARIMA, SARIMA)",
        "Seasonality and Trend Analysis",
        "Anomaly Detection in Time Series Data"
    ],
    "Model Deployment and Productionization": [
        "Introduction to Model Deployment",
        "Containerization with Docker",
        "Building RESTful APIs with Flask or FastAPI",
        "Model Deployment on Cloud Platforms (AWS, Azure, Google Cloud)",
        "Continuous Integration and Continuous Deployment (CI/CD) Pipelines"
    ],
    "Data Ethics and Privacy": [
        "Introduction to Data Ethics and Privacy",
        "Ethical Considerations in Data Collection and Usage",
        "Bias and Fairness in Machine Learning Models",
        "GDPR and Regulatory Compliance",
        "Privacy-Preserving Techniques (Differential Privacy, Federated Learning)"
    ],
    "Advanced Topics in Data Science": [
        "Reinforcement Learning",
        "Bayesian Methods",
        "Causal Inference",
        "Graph Analytics",
        "Ensemble Learning Techniques"
    ],
    "Soft Skills and Career Development": [
        "Effective Communication and Data Storytelling",
        "Problem-Solving and Critical Thinking",
        "Building a Data Science Portfolio",
        "Interview Preparation and Resume Writing",
        "Networking and Continuous Learning Strategies"
    ]
}


API_KEY="AIzaSyD9ZF_AshNR1jYQSxdSaEED7gboME_X9_M"
genai.configure(api_key=API_KEY)
model = 'gemini-1.0-pro' # @param {isTemplate: true}
contents_b64 = 'W10='
generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC45LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119'
safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d'
questions=[
    "What is Middleware",
    "What are the four pillars of OOPs",
    "What is blockchain"
]
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

    response = chat.send_message(
        user_input,
        stream=stream)
    reply=response.text.replace("*","")
    reply=reply.replace("\n","")
    return reply[:250]

def mix_audio_to_video(pathVideoInput, pathVideoNonAudio, pathVideoOutput):
  videoclip = mp.VideoFileClip(pathVideoInput)
  audioclip = videoclip.audio
  new_audioclip = mp.CompositeAudioClip([audioclip])
  videoclipNew = mp.VideoFileClip(pathVideoNonAudio)
  videoclipNew.audio = new_audioclip
  videoclipNew.write_videofile(pathVideoOutput)

def getaudiotext(filename):
    cap = cv2.VideoCapture("testt.mp4")
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(f'Checking Video  Frames {frames} fps: {fps}')
    if frames == 0:
        print(f'No frames data in video file, trying to convert this video..')
        writer = cv2.VideoWriter("fixVideo.avi", cv2.VideoWriter_fourcc(*'DIVX'), int(cap.get(cv2.CAP_PROP_FPS)),(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))                  
        while True:
            ret, frame = cap.read()
            if ret is True:
                writer.write(frame)
            else:
                cap.release()
                print("Stopping video writer")
                writer.release()
                writer = None
                break
    mix_audio_to_video("testt.mp4", "fixVideo.avi", "fixVideo.mp4")
    clip = mp.VideoFileClip(r"C:\Users\Shaun\Desktop\Hackathons\Aeravat 24\fixVideo.mp4")
    clip.audio.write_audiofile(r"testt.wav")

    # Split the audio file into smaller chunks to avoid memory issues
    audio_file = AudioSegment.from_file(r"testt.wav", format="wav")
    chunk_size = 10 * 1000  # 10 seconds
    chunks = []
    for i in range(0, len(audio_file), chunk_size):
        chunks.append(audio_file[i:i + chunk_size])

    # Initialize variables for result text and summarized text
    result_text = ""

    # Create a Recognizer instance and transcribe each chunk
    r = sr.Recognizer()
    for chunk in chunks:
        try:
            with sr.AudioFile(chunk.export(format="wav")) as audio:
                audio_data = r.record(audio)
                text = r.recognize_google(audio_data)
                print(text)
                result_text += text + " "
        except sr.UnknownValueError:
            # Handle the case when no speech is recognized in the chunk
            print("No speech detected in a chunk.")
            continue
    print(result_text)

def transcribe():
    aai.settings.api_key = "7da4e41ef2064e469ac7a17185928eef"
    transcriber = aai.Transcriber()

    # transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
    transcript = transcriber.transcribe("testt.mp4")

    print(transcript.text)
    return transcript.text
app=Flask(__name__)
answer=""
@app.route('/',methods=['GET','POST'])
def home():
    ques=questions[random.randint(0,3)]
    if request.method=="POST":
        answer=""
        answer=transcribe()
        print("It is here")
        print(answer)
        query="What is Middleware"
        prompt=f"For the following question {ques} rate the following answer {answer} on a scale of 1 to 10 with supporting reason for the same"
        feedback=chatbot(prompt)
        return render_template('index.html',answer=answer,feedback=feedback,ques=ques)
    return render_template('index.html',ques=ques)

@app.route('/save-video', methods=['POST'])
def save_video():
    if 'video' not in request.files:
        return 'No video file found', 400
    
    video_file = request.files['video']
    
    if video_file.filename == '':
        return 'Invalid file name', 400
    
    video_file.save('testt.mp4')  # Change path as needed
    # getaudiotext("A")
    
    
    return "hELLO wORLD"
    # return Response(answer, mimetype='text/plain')
def getpops(n):
    t2=[]
    for i in range(1,n+1):
        t2.append(i)
    return t2

@app.route('/test')
def test():
    st=[]
    mt=list(roadmap.keys())
    for i in mt:
        temp=[]
        print(mt)
        for j in roadmap[i]:
            temp.append(j)
        st.append(temp)
    print(st)
    print(mt)
    print(len(mt),len(st))
    return render_template('test22.html',combined=zip(mt,st))
def genpops(n):
    t=[]
    for i in range(1,n+1):
        t.append(f"popup{i}")
    return t
@app.route('/testt')
def testt():
    st=[]
    mt=list(roadmap.keys())
    for i in mt:
        temp=[]
        print(mt)
        for j in roadmap[i]:
            temp.append(j)
        st.append(temp)
    print(st)
    print(mt)
    print(len(mt),len(st))
    return render_template('test33.html',combined=zip(mt,st,genpops(len(st)),getpops(len(st))))


if __name__=="__main__":
    app.run(debug=True)