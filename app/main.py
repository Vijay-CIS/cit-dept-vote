
from flask import Flask, render_template, request
import pickle

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def entry():
    return render_template('index.html')


@app.route("/vote", methods=['POST'])
def vote():
    with open('app/data/storage.pkl', 'rb') as input:
        try:
            votes = pickle.load(input)
        except EOFError:
            votes = []
    obj = {
        "name": request.form['name'],
        "email": request.form['email'],
        "school": request.form['school']
    }
    votes.append(obj)
    with open('app/data/storage.pkl', 'wb') as output:
        pickle.dump(votes, output, pickle.HIGHEST_PROTOCOL)
    return render_template('pages/vote.html')


@app.route("/voterlist", methods=['POST', 'GET'])
def voter_list():
    with open('app/data/storage.pkl', 'rb') as input:
        dump = pickle.load(input)
        votes = dump
    return render_template('pages/admin.html', votes=votes)
