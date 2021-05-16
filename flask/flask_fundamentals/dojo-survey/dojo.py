from flask import Flask , render_template,request
app= Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route("/result", methods=['post'])
def result():
    print(request.form)
    firstname=request.form['firstname']
    lastname= request.form['lastname']
    dojolocation= request.form['dojolocation']
    favlanguage = request.form['favlanguage']
    comment=request.form['comment']
    return render_template('form.html',firstname=firstname,lastname=lastname, dojolocation=dojolocation,favlanguage=favlanguage, comment=comment)


if __name__== '__main__':
    app.run(debug=True)

    
