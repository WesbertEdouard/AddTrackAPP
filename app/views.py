from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from twilio.twiml.messaging_response import MessagingResponse
import requests

# Create your views here.
# id ="https://open.spotify.com/track/0u7oxreo1pM0JXa2upQVfl"
# post_data = {'track_id': id}
# response = requests.post('http://example.com', data=post_data)
# content = response.content


def index(request):
    if request.method=='POST':
        playlist_values = "6DvAviOnHfUPE5L7qqDdH5"
        song = request.POST.get('song_id')
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="125fcfc2832b46eab16d304808ba603b",
        client_secret="062770b8d48148289b1788b769ea89e0", redirect_uri="https://limitless-wave-3421.herokuapp.com/callback/",
        scope="playlist-modify-public"))
        link = song.split("/")
        value = link[4]
        link = value.split("?")
        track_id = link[0]
        results = spotify.playlist_add_items(playlist_values, items=[track_id])
        print(results, track_id)
        return render(request,'base.html',{"results":results})
    elif request.method=='GET':
        print("HELLOW WORLD")
        return render('GET REQUEST')
    else:
      return render(request,'base.html',)
