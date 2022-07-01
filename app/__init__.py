from email.policy import default
import os, datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
from flask import Response

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                        user=os.getenv("MYSQL_USER"),
                        password=os.getenv("MYSQL_PASSWORD"),
                        host=os.getenv("MYSQL_HOST"),
                        port=3306)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/aboutMe')
def aboutMe():
    return render_template('about_me.html', title="MLH Fellow")

@app.route('/experience')
def experience():
    return render_template('experience.html', title="MLH Fellow")

@app.route('/travel')
def travel():
    return render_template('travel.html', title="MLH Fellow")

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="MLH Fellow")

@app.route('/education')
def education():
    return render_template('education.html', title="MLH Fellow")

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    if 'name' not in request.form or not request.form["name"]:
        return Response(
        "Invalid name",
        status=400,
        )
    if 'email' not in request.form or not request.form["email"]:
        return Response(
        "Invalid email",
        status=400,
        )
    if 'content' not in request.form or not request.form["content"]:
        return Response(
        "Invalid content",
        status=400,
        )
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name = name, email = email, content = content)
    
    
        
    
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
    }
