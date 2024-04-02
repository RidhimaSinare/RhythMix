from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os


mongo_string = "mongodb+srv://sinareridhima:mongodb17@rhythmix.9xdbw8c.mongodb.net/"

webapp_root = "webapp"

static_dir = os.path.join(webapp_root,"static")
template_dir = os.path.join(webapp_root,"templates")

app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)

# Connect to MongoDB Atlas
client = MongoClient(mongo_string)
db = client['users']
users_collection = db['users']

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def register():
    # if request.method == 'POST':
        username = "rid"
        password = "ridhima17"
        confirm = "ridhima17"

        # Check if username or email already exists
        if users_collection.find_one({'username': username}):
            return 'Username or email already exists!'

        # Insert the new user into the database
        if password==confirm:
            users_collection.insert_one({'username': username, 'password': password})
            print("")

            return redirect(url_for('login'))

        return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
