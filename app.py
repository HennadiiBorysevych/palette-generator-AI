from flask import Flask, render_template, request, redirect, url_for, session
import openai
from dotenv import dotenv_values
import json
config = dotenv_values(".env")

openai.api_key = config['OPENAI_API_KEY']

app = Flask(__name__,
    template_folder="templates"
)


@app.route('/')
def index():
    response = openai.chat.completions.create(
        messages=[{"role": "user", "content": ''}],
        model="gpt-3.5-turbo",
        max_tokens=200,
    )
    day = response.choices[0].message.content
    print(day)
    return render_template('index.html', day=day)


@app.route('/palette', methods=['POST'])
def palette():
    session['palette'] = request.form['palette']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
