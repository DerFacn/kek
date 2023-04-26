from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return redirect(url_for('confirmation', name=name))


@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    return f'Thank you for submitting the form, {name}!'


if __name__ == '__main__':
    app.run(debug=True)
