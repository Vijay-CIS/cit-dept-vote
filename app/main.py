
from flask import Flask, render_template, request
import pickle

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def entry():
    return render_template('index.html')


@app.route("/vote", methods=['POST'])
def vote():
    obj = {
        "name": request.form['name'],
        "email": request.form['email'],
        "school": request.form['school']
    }
    return render_template('pages/vote.html', user=obj)

@app.route("/submit-vote/<dept>", methods=['GET'])
def submit_vote(dept):
    with open('app/data/storage.pkl', 'rb') as input:
        try:
            votes = pickle.load(input)
        except EOFError:
            votes = []
    obj = {
        "name": request.args['name'],
        "email": request.args['email'],
        "school": request.args['school'],
        "dept": dept
    }
    votes.append(obj)
    with open('app/data/storage.pkl', 'wb') as output:
        pickle.dump(votes, output, pickle.HIGHEST_PROTOCOL)
    return render_template('pages/thanks.html')
    

@app.route("/voterlist", methods=['POST', 'GET'])
def voter_list():
    with open('app/data/storage.pkl', 'rb') as input:
        dump = pickle.load(input)
        votes = dump

    depts = {
        "CSE": 0,
        "IT": 0,
        # ... REPEAT FOR ALL DEPTS
    }

    for item in votes:
        if (item["dept"] == "CSE"):
            depts["CSE"] = depts["CSE"] + 1
        if (item["dept"] == "IT"):
            depts["IT"] = depts["IT"] + 1
        # if (item["dept"] == "IT"):
        #     depts["IT"] = depts["IT"] + 1    Repeat for all Depts

    
    return render_template('pages/admin.html', votes=votes, depts=depts)
