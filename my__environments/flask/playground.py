from flask import Flask, render_template
app = Flask(__name__) 
@app.route('/play')
def level1():
    return render_template('index.html',many=3, color="orange")

@app.route('/play/<int:many>')
def level2(many):
    return render_template('index.html', many=many, color="orange")

@app.route('/play/<int:many>/<color>')
def level3(many,color):
    return render_template('index.html', many=many,color=color)


if __name__=='__main__':
    app.run(debug=True)