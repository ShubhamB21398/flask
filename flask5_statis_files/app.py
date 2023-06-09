from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return render_template('index.html',name=name)

@app.route('/')
def redirect():
    return 'Enter / folllowed by a name in URL to redirect'

if __name__=="__main__":
    app.run(debug=True)