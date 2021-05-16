from flask import Flask , render_template,request, session, redirect
app= Flask(__name__)
app.secret_key='mahmood'
@app.route('/')
def mainPage():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html",count=session['count'])

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')




if __name__== '__main__':
    app.run(debug=True)
