from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    prompt = {'prompt_text' : 'this is a test prompt',
              'tag_text': 'intermediate'}
    return render_template('index.html', title='Prompts', prompt=prompt)