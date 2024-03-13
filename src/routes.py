# from application import app
from flask import Flask, render_template, request
from features import *
from model import *

# app = Flask(__name__)

songDF = pd.read_csv("./data/processed/allsong_data.csv")
complete_feature_set = pd.read_csv("./data/processed/complete_feature.csv")

# @app.route("/")
def home():
   #render the home page
   return render_template('home.html')

# @app.route("/about")
def about():
   #render the about page
   return render_template('about.html')

# @app.route('/recommend', methods=['POST'])
def recommend():
   #requesting the URL form the HTML form
   URL = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
   #using the extract function to get a features dataframe
   df = extract(URL)
   #retrieve the results and get as many recommendations as the user requested
   edm_top40 = recommend_from_playlist(songDF, complete_feature_set, df)
   number_of_recs = 5
   my_songs = []
   for i in range(number_of_recs):
      my_songs.append([str(edm_top40.iloc[i,1]) + ' - '+ '"'+str(edm_top40.iloc[i,4])+'"', "https://open.spotify.com/track/"+ str(edm_top40.iloc[i,-6]).split("/")[-1]])
   print(my_songs)
if __name__=="__main__":
   
   recommend()