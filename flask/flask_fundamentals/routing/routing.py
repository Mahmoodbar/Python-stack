from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_flask():
    return"Hello World!"
@app.route("/dojo")
def dojo_Flask():
    return "Dojo!" 
@app.route("/say/<name>")
def say_name(name):
    return f"Hi {name}"
@app.route("/repeat/<int:num>/<word>")
def name_no(word,num):
    html = ""
    for i in range(int(num)):
        html += "<p>" + word + "</p>"
    return html 


if __name__=='__main__':
    app.run(debug=True)
