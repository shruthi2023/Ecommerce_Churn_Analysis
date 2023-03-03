from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return("This is Shruthi!!")

@app.route("/admin")
def hello_admin():
    return("Admin is here")


app.run()