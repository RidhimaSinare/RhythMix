# from application import app
from flask import Flask, render_template, request, redirect, url_for
from src.features import *
from src.model import *
import os
from pymongo import MongoClient


mongo_string = "mongodb+srv://sinareridhima:mongodb17@rhythmix.9xdbw8c.mongodb.net/"
params_path = "params.yaml"
webapp_root = "webapp"

# Connect to MongoDB Atlas
client = MongoClient(mongo_string)
db = client['users']
users_collection = db['users']

static_dir = os.path.join(webapp_root,"static")
template_dir = os.path.join(webapp_root,"templates")

app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)


@app.route('/',methods=['GET','POST'])
def register():

   if request.method == 'POST':
      username = request.form["username"]
      password = request.form['password']
      confirm = request.form['cpassword']

        # Check if username or email already exists
      if users_collection.find_one({'username': username}):
            return 'Username or email already exists!'

        # Insert the new user into the database
      if password==confirm:
            users_collection.insert_one({'username': username, 'password': password})
            print("Registration Successful")

            return redirect(url_for('login'))

   return render_template('register.html')

@app.route("/login")
def login():
   #render the home page
   return render_template('login.html')

# @app.route('/recommend', methods=['POST'])
def recommend():
   #requesting the URL form the HTML form
   URL = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
   #using the extract function to get a features dataframe
   df = extract(URL)
   #retrieve the results and get as many recommendations as the user requested
   edm_top40 = recommend_from_playlist(params_path)
   number_of_recs = 5
   my_songs = []
   for i in range(number_of_recs):
      my_songs.append([str(edm_top40.iloc[i,1]) + ' - '+ '"'+str(edm_top40.iloc[i,4])+'"', "https://open.spotify.com/track/"+ str(edm_top40.iloc[i,-6]).split("/")[-1]])
   print(my_songs)

if __name__=="__main__":
   
   recommend()
   # app.run(debug=True, host='127.0.0.1',port=5000)