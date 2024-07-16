from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABSE_URI']='sqllite:///test.db'
db=SQLAlchemy(app)

class TODO(db.model):
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(200), nullable=False)
    date=db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
