from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('HomeLayout.html', title='home')


@app.route('/dogs')
def dogs():
    return render_template('DogsLayout.html', title='dogs')


@app.route('/coding')
def coding():
    return render_template('CodingLayout.html', title='coding')


@app.route('/resume')
def resume():
    return render_template('ResumeLayout.html', title='resume')


@app.route('/about')
def about():
    return render_template('AboutLayout.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)
