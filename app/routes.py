from flask import render_template
from app import app, db
from app.forms import PromptForm
from flask import request

from app.models import Prompt, Tag, PromptTag


@app.route('/')
@app.route('/index')
def index():
    prompt = {'prompt_text' : 'this is a test prompt',
              'tag_text': 'intermediate'}
    return render_template('index.html', title='Prompts', prompt=prompt)

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.form:
        prompt = Prompt(prompt_text=request.form.get("prompt"))
        tag = Tag(tag_text=request.form.get("tag"))
        db.session.add(prompt)
        db.session.add(tag)
        db.session.commit()
        prompttag = PromptTag(prompt_id=prompt.prompt_id, tag_id=tag.tag_id)
        db.session.add(prompttag)
        db.session.commit()

    form = PromptForm()
    return render_template('form.html', title='Submit a Prompt', form=form)

