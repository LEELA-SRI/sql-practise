import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tasks.db')

db = SQLAlchemy(app)

class tasks(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task_title = db.Column(db.String(50),nullable = False)
    task_desc = db.Column(db.String(50),nullable = True)
    task_date = db.Column(db.DateTime,default = datetime.utcnow)
    task_importance = db.Column(db.Boolean,default = False,nullable = False)

    def __repr__(self):
        return f"Task Title : {self.task_title}, Desc : {self.task_desc} , Date : {self.task_date}, Important : {self.task_importance}"

    

@app.route('/')
def home():
    return "lilo"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


