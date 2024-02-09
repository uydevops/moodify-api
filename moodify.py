from flask import Flask, request, jsonify
from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

app = Flask(__name__)
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read"))

@app.route('/moodify', methods=['POST'])
def moodify():
    data = request.get_json()
    text = data.get('text')
    mood = get_user_mood(text)
    recommended_tracks = get_spotify_tracks(mood)
    return jsonify({"mood": mood, "tracks": recommended_tracks})

def get_user_mood(text):
    blob = TextBlob(text)
    mood = blob.sentiment.polarity
    return "happy" if mood > 0 else "sad"

def get_spotify_tracks(mood):
    mood_dict = {
        "happy": ["happy", "party", "upbeat", "energetic"],
        "sad": ["sad", "calm", "relaxing", "mellow"]
    }
    mood_genre = random.choice(mood_dict[mood])
    results = spotify.search(q=mood_genre, limit=10)
    tracks = [track['name'] for track in results['tracks']['items']]
    return tracks

if __name__ == '__main__':
    app.run(debug=True)
