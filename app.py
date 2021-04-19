from flask import Flask, render_template, request, flash, make_response
import sqlite3
import db
from utils.challenge_2_form import LoginForm

app = Flask(__name__)
db.init_app(app)
app.secret_key = 'secret'

# todo abstract database into another file
################
#   Database   #
################
DATABASE = './helper_files/challenge_2.sql'
# def get_db():
    # db = getattr(g, '_database', None)
    # if not db:
        # db = g._database = sqlite3.connect(DATABASE)
    # return db
    
# @app.teardown_appcontext
# def close_connection(exception):
    # db = get_attr(g, '_database', None)
    # if not db:
        # db.close()

# NOTE Create function to reset database to original in event of database deletion
# TODO Store flags in separate file for easy access. Must ensure it is not reachable by users.
FLAG_2 = 'IHackedAWebsite'
###############
#    Routes   #
###############
@app.route('/')
def homepage():
    return render_template('hpg.html')
    


@app.route('/challenge/')
@app.route('/challenge/<int:challenge_num>',methods=['GET'])

def challenge(challenge_num):
    challenge_num = int(challenge_num)
    if challenge_num == 4:
        resp = make_response(render_template('challenge_4.html'))
        resp.set_cookie("session","VGhpcyBpcyB5b3VyIGZsYWcgZm9yIGNoYWxsZW5nZSA1OiBDb29raWVzX2FyZV9pbnNlY3VyZSE=")
        return resp
    if challenge_num < 6 and challenge_num > 0:
        return render_template('challenge_{}.html'.format(challenge_num))
    else:
        return render_template('challenge_0.html')
        
@app.route('/login', methods=['POST'])
def login():
    username = request.form['Username']
    password = request.form['Password']
    query = "SELECT * FROM credentials WHERE username IS \'{}\' and password IS \'{}\';".format(username, password)
    challenge_2_db = db.get_db()
    result = challenge_2_db.execute(query)
    success = len([i for i in result])
    if success:
        flash('Congrats! Flag 2 is {}'.format(FLAG_2), category = 'msg-success')
    else:
        flash('Username or Password is incorrect.', category = 'msg-error')
    
    return render_template('challenge_2.html')

@app.route('/feedback/')
@app.route('/feedback/<rating>')
def feedback(rating):
    print(rating)
    rating = int(rating)
    if rating <= 5 and rating > 0:
        flash('Thank you for your feedback... but we want a higher score!', category = 'msg-error')
    elif rating >= 6:
        flash('Thank you :) Here is your flag: CTFisFUN', category = 'msg-success')
    return render_template('challenge_3.html')
    
#10.219.39.132       
if __name__ == "__main__":
    app.run(debug=True,threaded=True, host='10.219.39.132', port='8001')  

  
