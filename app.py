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
    return render_template("index.html", category_list=topics)


@app.route('/findspeaker', methods=['POST'])
def findspeaker():
    speakers = mongo.db.speakers.find({"category": request.form.get('category')})    
    return render_template("dud.html", speakers=speakers)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)