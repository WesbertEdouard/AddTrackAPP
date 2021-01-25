from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os 
import random

# Create your views here.
# id ="https://open.spotify.com/track/0u7oxreo1pM0JXa2upQVfl"
# post_data = {'track_id': id}
# response = requests.post('http://example.com', data=post_data)
# content = response.content

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
                            
def index(request,):
    state = random.randint(100,150)
    
    if request.method=='POST':
        playlist_id = "6DvAviOnHfUPE5L7qqDdH5"
        song = request.POST.get('song_id')
        
        code = request.POST.get('https://accounts.spotify.com/authorize')
        spotifyGet = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
        reponse_type=code, redirect_uri="https://limitless-wave-3421.herokuapp.com", state=state, scope="playlist-modify-public"))
        
        output = spotifyGet.query(code, state)
        
        spotifyPOST = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET, scope="playlist-modify-public"))
        
        link = song.split("/")
        value = link[4]
        link = value.split("?")
        track_id = link[0]
        
        results = spotifyPOST.playlist_add_items(playlist_id, items=[track_id])
        return render(request,'base.html',  {"output":output}, {"results":results})
    
    # elif request.method=='GET':
    #     code = request.POST.get('https://accounts.spotify.com/authorize')
    #     spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
    #     reponse_type=code, redirect_uri="https://limitless-wave-3421.herokuapp.com", state=state_value, scope="playlist-modify-public"))
    else:
      return render(request,'base.html')
