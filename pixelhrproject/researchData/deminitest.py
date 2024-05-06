# !pip install -U -q google-generativeai

# from flask import Flask, render_template, request
import google.generativeai as genai
import json
import base64
import pathlib
import pprint
import requests
import mimetypes
from IPython.display import Markdown

API_KEY="AIzaSyD9ZF_AshNR1jYQSxdSaEED7gboME_X9_M"
genai.configure(api_key=API_KEY)
model = 'gemini-1.0-pro' # @param {isTemplate: true}
contents_b64 = 'W10='
generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC45LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119'
safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d'


def PromptTemplating(year_of_study, role, course, skill, company):

    roletext = ""
    coursetext = ""
    skillstext = ""
    companytext = ""

    for item in role:
        roletext = roletext + item + ", "

    for item in course:
        coursetext = coursetext + item + ", "

    for item in skill:
        skillstext = skillstext + item + ", "

    for item in company:
        companytext = companytext + item + ", "

    part1 = f"""
    I are a engineering student in your {year_of_study}. 
    I have undertaken a few courses like {coursetext} until now. 
    My technical skills are {skillstext} and 
    my preferred job role is {roletext}. 
    My desired companies are {companytext}. 
    Design a roadmap/list of topics for one year in order to improve your interview preparation.

    """
    # give me 6 maintopics and for each maintopic, give 4 subtopics just after the maintopic 

    part2 = """
    give the roadmap/list for one year in a python list only in format
    strictly follow the format
    dont give any other text rather than python code
    example : 

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


}

    """

    myprompt = part1 + part2

    # censoredText = "Act as a task planner for carrer planning where you give the tasks accrdingly to the user profile"
    censoredText = "generate the roadmap for a person wanting to pursue a career in datascience. Take into account the basics ,eg programming languages,theory, courses  etc and divide it into 12 main topics and each of them would have 5 subtopics"

    query = censoredText + myprompt
    print("censoredText : ", censoredText)
    print("myprompt : ", myprompt)

    # post_response = make_post_request(censoredText, myprompt)
    geminiResponse = chatbot(query)

    # print(geminiResponse)
    return geminiResponse



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
    return reply


# role = "Software Enginner"
year_of_study = "Second"

# role    = ["Data Scientist", "Data Analysis"]
role    = ["Data Scientist"]
course  = ["Python", "DBMS", "Algorithms"]
skill   = ["JAVA", "Mongo DB", "Statistics"]
company = ["JP Morgan", "Media.net", "Google", "Microsoft"]

# geminiResponseFinal = PromptTemplating(year_of_study, role, course, skill, company)
# print(geminiResponseFinal)


print(chatbot("hello gimini bot"))

# query = "What is your name?"
# geminiResponse = chatbot(query)
# print("geminiResponse : ", geminiResponse)
# replies=[]
# queries=[]

# @app.route('/chat',methods=['GET','POST'])
# def chat():
#     if request.method=="POST":
#         print(request.form)
#         data=request.form['queryy']
#         queries.append(data)
#         print(data)
        
#         replies.append(chatbot(data))
#         return render_template('chatt.html',combined=zip(replies,queries))
#     return render_template('chatt.html',combined=zip(replies,queries))

# @app.route('/leaderboard')
# def leaderboard():
#     return render_template('tables.html')

# if _name=="main_":
#     app.run(host="0.0.0.0",debug=True)