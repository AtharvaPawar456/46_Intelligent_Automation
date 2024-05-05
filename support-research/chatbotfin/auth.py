from flask import Flask

app=Flask(__name__)

@app.route('/')
def authenticate():
    print("User Request Received")
    return "OK"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=6000)