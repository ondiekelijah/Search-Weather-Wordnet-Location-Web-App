from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, flash, url_for
from models import *
from forms import *
from app import app
from googlesearch import search 
from geopy.geocoders import Nominatim
import json 
import urllib.request 
import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')

@app.route("/",methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("quiz.html",title="Search | Engine")

@app.route("/location finder",methods=("GET", "POST"), strict_slashes=False)
def location():
    form = Location()
    if request.method == "POST":
        data = form.address.data
    else: 
        data = 'Barrie'
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(data)
    return render_template("location_finder.html",title="Location Finder",form=form,location=location,label="Location Finder")

@app.route("/wordnet",methods=("GET", "POST"), strict_slashes=False)
def wordnet():
    return render_template("wordnet.html",title="Wordnet | Home")
    # --------------------------------------
@app.route("/wordnet/definitions",methods=("GET", "POST"), strict_slashes=False)
def definitions():
    form = Wordnet()
    if request.method == "POST":
        data = form.word.data
    else: 
        data = 'Spider'
    defined_word = wn.synset(data + '.n.01').definition()
    return render_template("wordnet_action.html",form=form,defined_word=defined_word,title="Wordnet | Definitions",label="Find Word Definitions")

@app.route("/wordnet/synonyms & antonyms",methods=("GET", "POST"), strict_slashes=False)
def synonyms_antonyms():
    form = Wordnet()
    if request.method == "POST":
        data = form.word.data
    else: 
        data = 'Soft'
    synonyms = []
    antonyms = []

    for syn in wn.synsets(data):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    return render_template("wordnet_action.html",synonyms=synonyms,antonyms=antonyms,label_wordnet_a="Similar words",label_wordnet_b="Opposite words",form=form,title="Antonyms | Synonyms",label="Find Similar and Opposite words")

    # -----------------------------------------

@app.route("/weather",methods=("GET", "POST"), strict_slashes=False)
def weather():
    form = Weather()
    if request.method == 'POST': 
        city = form.place.data 
    else: 
        city = 'mathura'
  
    api = "9190163a9836abfa2af57df7c275b258"
  # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    url = base_url + "appid=" + api + "&q=" + city
    # source contain json data from api 
    source = urllib.request.urlopen(url).read() 
  
    # converting JSON data to a dictionary 
    list_of_data = json.loads(source) 
  
    # data for variable list_of_data 
    data = { 
        "country_code": str(list_of_data['sys']['country']), 
        "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                    + str(list_of_data['coord']['lat']), 
        "temp": str(list_of_data['main']['temp']) + 'k', 
        "pressure": str(list_of_data['main']['pressure']), 
        "humidity": str(list_of_data['main']['humidity']), 
    } 
    return render_template("weather.html",data=data,form=form,label="Weather Updates", title='Weather Updates')

@app.route("/Ask Quiz/Data Science",methods=("GET", "POST"), strict_slashes=False)
def datasci():
    form = Questions()
    if request.method == "POST":
        data = form.body.data
        category = "Data Science"
        # to search 
        query = data
        for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
            # print(j) 
            answer = Answers(
                question = data,
                answer = j,
                category = category
            )
        db.session.add(answer)
        db.session.commit()
        flash(f"Answer found,Follow the link to read more" "  "+j, "info")
        return redirect(url_for("datasci"))
    elif request.method == "GET":
        recent = Answers.query.order_by(Answers.id.desc()).all()
    return render_template("quiz_action.html",label="Ask a Question on Data Science" ,title="Quiz | Data Science",form = form,recent =recent )



@app.route("/Ask Quiz/Web Development",methods=("GET", "POST"), strict_slashes=False)
def webdev():
    form = Questions()
    if request.method == "POST":
        data = form.body.data
        category = "Web Development"
        # to search 
        query = data
        for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
            # print(j) 
            answer = Answers(
                question = data,
                answer = j,
                category = category
            )
        db.session.add(answer)
        db.session.commit()
        flash(f"Answer found,Follow the link to read more" "  "+j, "info")
        return redirect(url_for("webdev"))
    elif request.method == "GET":
        recent = Answers.query.order_by(Answers.id.desc()).all()
    return render_template("quiz_action.html",label="Ask a Question on Web Development",title="Quiz | Web Development",form = form,recent = recent)



@app.route("/Ask Quiz/Cyber Security",methods=("GET", "POST"), strict_slashes=False)
def cybersec():
    form = Questions()
    if request.method == "POST":
        data = form.body.data
        category = "Cyber Security"
        # to search 
        query = data
        for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
            # print(j) 
            answer = Answers(
                question = data,
                answer = j,
                category = category
            )
        db.session.add(answer)
        db.session.commit()
        flash(f"Answer found,Follow the link to read more" "  "+j, "info")
        return redirect(url_for("cybersec"))
    elif request.method == "GET":
        recent = Answers.query.order_by(Answers.id.desc()).all()
    return render_template("quiz_action.html",label="Ask a Question on Cyber Security" ,title="Quiz | Cyber Security",form = form,recent = recent)

    if __name__ == "__main__":
        app.run(debug=True)