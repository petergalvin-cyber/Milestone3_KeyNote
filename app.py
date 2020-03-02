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
    
    speakers = mongo.db.speakers.find({"category": {'$in': request.form.getlist('category')}})    
    print_list = ' and '.join(request.form.getlist('category'))
    print_list = print_list+"."
    
    return render_template("speaker_list.html", speakers=speakers, category=print_list)


@app.route('/speakerbio/<speaker_id>')
def speakerbio(speaker_id):
    speaker_info = mongo.db.speakers.find({'_id': ObjectId(speaker_id)}) 
    return render_template("speaker_bio.html", speaker_info=speaker_info)


@app.route('/new_speaker')
def new_speaker():
    topics = mongo.db.categories.find()
    return render_template('newspeaker.html',categories=topics)


@app.route('/new_category')
def new_category():
    topics = mongo.db.categories.find()
    return render_template('newcategory.html',categories=topics)


@app.route('/addcategory', methods=['POST'])
def addcategory():
    mongo.db.categories.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


@app.route('/delcategory', methods=['POST'])
def delcategory():
    job = request.form.getlist('category')
    print(job)
    mongo.db.categories.remove({'category': {'$in' :request.form.getlist('category')}})
    return redirect(url_for('index'))


@app.route('/add_speaker', methods=['POST'])
def add_speaker():
    mongo.db.speakers.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


@app.route('/remove_category', methods=['POST','GET'])
def remove_category():
    topics = mongo.db.categories.find()
    return render_template('deletecategory.html',categories=topics)


@app.route('/deletespeaker/<speaker_id>')
def deletespeaker(speaker_id):
    mongo.db.speakers.remove({'_id': ObjectId(speaker_id)})
    return redirect(url_for('index'))


@app.route('/editspeaker/<speaker_id>')
def editspeaker(speaker_id):
    speaker_info = mongo.db.speakers.find_one({'_id': ObjectId(speaker_id)})
    topics = mongo.db.categories.find() 
    return render_template('editspeaker.html', speaker=speaker_info, categories=topics)


@app.route('/updatespeaker/<speaker_id>')
def updatespeaker(speaker_id):
    mongo.db.speakers.update({'_id': ObjectId(speaker_id)},
    {
        'name': request.form.get('name'),
        'category': request.form.getlist('category'),
        'bio': request.form.get('bio'),
        'banner': request.form.get('banner'),
        'photo': request.form.get('photo')
    })
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)