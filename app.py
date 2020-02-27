import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'SpeakerHub'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
def index():
    topics = mongo.db.categories.find()
    #print(topics.count())
    return render_template("index.html", categories=topics)


@app.route('/findspeaker', methods=['POST', 'GET'])
def findspeaker():
    speakers = mongo.db.speakers.find({"category": request.form.get('category')})    
    print(speakers.count())
    return render_template("speaker_list.html", speakers=speakers)


@app.route('/speakerbio/<speaker_id>')
def speakerbio(speaker_id):
    speaker_info = mongo.db.speakers.find({'_id': ObjectId(speaker_id)}) 
    return render_template("speaker_bio.html", speaker_info=speaker_info)


@app.route('/new_speaker')
def new_speaker():
    topics = mongo.db.categories.find()
    return render_template('newspeaker.html',categories=topics)


@app.route('/add_speaker', methods=['POST'])
def add_speaker():
    mongo.db.speakers.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)