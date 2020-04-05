from app import db

class Prompts(db.Model):
    prompt_id = db.Column(db.Integer, primary_key=True)
    prompt_text = db.Column(db.VARCHAR(2500))
    tag_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Prompt {}>'.format(self.prompt_id)

class Tags(db.Model):
    tag_id = db.Column(db.Integer, primary_key=True)
    tag_text = db.Column(db.VARCHAR(100))

    def __repr__(self):
        return '<Tag {}>'.format(self.tag_text)

class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(56))
    password = db.Column(db.VARCHAR56))

    def __repr__(self):
        return '<Admin {}>'.format(self.username)