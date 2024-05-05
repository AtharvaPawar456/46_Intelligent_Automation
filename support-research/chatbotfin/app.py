from flask import Flask,render_template
from flask import Flask, render_template,request
import google.generativeai as genai
import json
import base64
from IPython.display import Markdown
import time
import requests
import re
API_KEY="AIzaSyD9ZF_AshNR1jYQSxdSaEED7gboME_X9_M"
genai.configure(api_key=API_KEY)
model = 'gemini-1.0-pro' # @param {isTemplate: true}
contents_b64 = 'W10='
generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC45LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119'
safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d'

template="Hello act as a HR chatbot your name is Pixel Hr Chat Bot you manage software engineers and other support teams and you assign daily tasks to them for example daily meeting at 11, team addressal at 2, Analyzing pending tasks at 4 so whenever I ask you a question give me all the questions related to my daily task in a professinal manner which is generalized also uyou have the following data 40 employees are present and for more data you can request, you can and ask whether u want to know who they are or resources in a maximum of 40 words the query is below : "


# Define the URLs
# def getdata():
urls = [
    'https://d4d4-103-123-226-98.ngrok-free.app/oneemploy/',
    'https://d4d4-103-123-226-98.ngrok-free.app/oneLeave/',
    'https://d4d4-103-123-226-98.ngrok-free.app/oneReimbusement/'
]

# Define the user_name
# user_name = 'shaun'

# Make GET requests to each URL
# final=""
# for url in urls:
#     response = requests.get(url, params={'user_name': user_name})
#     # print(response.text)
#     final+=response.text
#     if response.status_code == 200:
#         # print("Data for {} from {}: {}".format(user_name, url, response.json()))
#         pass
#     else:
#         # print("Failed to fetch data from {}: {}".format(url, response.status_code))
#         pass
    # return final
def makereq(dept,name,typee,days,reason):
    url = "http://localhost:8000/leave_create/"
    params = {
        'department': dept,
        'user_name': name,
        'leave_type': typee,
        'days': days,
        'reason': reason,
        'status': 'Pending'
    }

    response = requests.get(url, params=params)
# http://127.0.0.1:8000/create_reimbursement/?department=Finance&user_name=shaun&date=2024-04-07&expense_type=Travel&amount=200&shortdesc=Travel%20expense&pdfpath=/path/to/pdf&status=Pending&paymenttype=check&days=2

Travel = [
        'Flight tickets',
        'Taxi fare',
        'Car rental',
        'Parking fees',
        'Train tickets',
        'Gasoline',
        'Toll fees',
        'Visa fees',
        'Baggage fees',
        'Public transportation fares',
        'Hotel stay',
        'Resort booking',
        'Airbnb rental',
        'Hostel accommodation',
        'Cabin rental',
        'Motel stay',
        'Bed and breakfast',
        'Luxury hotel suite',
        'Dormitory booking',
        'Vacation rental',
        'Dinner meeting',
        'Lunch with partner',
        'Coffee meeting',
        'Breakfast during event',
        'Team lunch',
        'Client entertainment',
        'Happy hour drinks',
        'Business dinner',
        'Conference lunch',
        'Breakfast meeting',
        'Office supplies purchase',
        'Printing and photocopying charges',
        'Software subscription renewal',
        'Membership fee',
        'Business card printing',
        'Internet and phone bill',
        'Conference registration fee',
        'Transportation expenses',
        'Gift for client or colleague',
        'Charitable donation'
    ]
from random import choice

def makereq2(dept,name,rtypee,amount):
    url = "http://127.0.0.1:8000/create_reimbursement/"
    params = {
        'user_name': name,
        'department': dept,
        'date':"2024-04-07",
        'leave_type': rtypee,
        'amount': amount,
        'shortdesc ':choice(Travel),
        'pdfpath' :"-",
        'status': 'Pending',
        'paymenttype':"Deposit" 
    }

    response = requests.get(url, params=params)

final=""
def chatbot(text_to_encode,flag=0):
    # text_to_encode = 'what is ai in real world' # @param {isTemplate: true}
    datat=""
    if flag==0:
        datat=f"Hello Consider the following json data {final} Now first understand the data nicely extract all the important fields and now based on this answer the question is put to you "
        print(datat)
    encoded_text_b64 = base64.b64encode(f"{datat}{text_to_encode}".encode()).decode()
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
    # user_input=user_input
    response = chat.send_message(
        user_input,
        stream=stream)
    reply=response.text.replace("*","")
    reply=reply.replace("\n","")
    return reply

replies=[]
queries=[]
leaves=["sick","casual","maternity"]
leave_prompt="Based on the attendance and leave history of employee id {no} wants to take a leave for {leav} days with reason being {reason} suggest whether the leave should be granted rejected or no answer with reason"

def djangosend(i,vals):
    # http://localhost:8000/leavecreate/?department=HR&user_name=John&leave_type=Vacation&days=2&reason=Family%20time&status=Pending
    url = 'http://localhost:8000/leave_create/'
    if i==1:
        params = {
            'department': vals[0],
            'user_name': vals[1],
            'leave_type': vals[2],
            'days': vals[3],
            'reason': vals[4],
            'status': vals[5]
        }
    if i==2:
        params = {
    'department': vals[0],
    'user_name': vals[1],
    'date': "2024-04-06",
    'expense_type': vals[2],
    'amount': vals[3],
    'shortdesc': vals[4],
    'pdfpath': '',
    'status': '',
    'paymenttype': 'deposit',
    'days': '1'
}


    response = requests.get(url, params=params)

    if response.status_code == 200:
        # print("Request successful:", response.text)
        pass
    else:
        print("Request failed:", response.status_code)

app=Flask(__name__)

name=""
pasw=""

@app.route('/login',methods=['GET','POST'])
def login():
    global name
    if request.method=="POST":
        name=request.form['name']
        # department=request.form['dept']
        return render_template('chatt.html')
    return render_template('login.html')

@app.route('/prompt')
def prompt():
    return render_template('chatt.html')

@app.route('/',methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/chat',methods=['GET','POST'])
def chat():
    name="ryan"
    dept="Web Development"
    trep=""
    
    if request.method=="POST":
        # print(request.form)
        data=request.form['queryy']
        # department=request.form['dept']
        # name=request.form['name']

        queries.append(data)
        # print(data)
        # params=data.split(',')
        # params.remove(params[0])
        # params.insert(0,name)
        # params.insert(1,"Software")
        trep=chatbot(data)
        if "leave" in data:
            reason=chatbot(f"Hello please extract the reason the employee asked for this leave from the below query {data}",1)
            pattern = r'\b(\d+)\s+days?\b'
            # Find all matches in the text
            days = re.findall(pattern, data)
            leavetype="Sick"
            leavetypee=["maternity","sick","casual","priviledge","paternity"]
            for i in leavetypee:
                if i in data:
                    leavetype=i
            # date="7-04-2024"
            trep="Your leave application has been submitted and is under review Any other way may in which I can assist you ?"
            makereq(dept,name,leavetype,days,reason)
            # http://localhost:8000/leave_create/?department=HR&user_name=John&leave_type=Vacation&days=2&reason=Family%20time&status=Pending

            # if "request" in data:
            #     d1=chatbot(data+f"Check whether {name} has enough balance leaves and is elegible for a leave based on this reason {params[2]}")
            #     replies.append("Your Leave application has been conveyed")
            #     # d4=chatbot(data+f"Determine whether ")
            #     print("Analyzing")
            #     if "yes" in d1:
            #         pred="Yes"
            #         trep+="Yes you have enough balance leaves and "
            #     if "no" in d1:
            #         pred="No"
            #         trep+="You do not have enough balance leaves "
            #     trep+="Your query has been submitted for review"
            # else:
            #     trep+=chatbot(data+f"For {name}")
        elif "reimbursement" or "money" in data:
            # time.sleep(1000)
            patternn = r'Rs\s*(\d+(?:\.\d+)?)'
    # Find all matches in the text
            rtypee=""
            amount=""
            amount = re.findall(patternn, data)
            expense_typelist = ['Travel', 'Accomodation', 'BusinessMeals', 'Miscellaneous']
            for j in expense_typelist:
                if j in data:
                    rtypee=j
            trep="Your Request for Reimbursement has been received. You will be be notified upon its clearance"
            makereq2(dept,name,rtypee,amount)
        elif "attendance" in data:
            d5=chatbot(data.replace("my",name))
            trep+=d5
        elif "salary":
            d6=chatbot(data+"for {name}")
            trep+=d6
        replies.append(trep)
        return render_template('chatt.html',combined=zip(replies,queries))
    return render_template('chatt.html',combined=zip(replies,queries))

@app.route('/mobileauth')
def authenticate():
    print("User Request Received")
    return "OK"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")