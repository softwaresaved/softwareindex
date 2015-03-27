from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello World!'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index/test/')
@app.route('/index/test/<software>')
def test(software=None):
    return render_template('test.html', software=software)

if __name__ == '__main__':
    app.run(debug=True)
