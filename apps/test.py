
# song = "https://open.spotify.com/track/2CDcXWYWilHTXrsOXJza8n?si=iouT1Qd3RXCzSfxZsFGGvw"
song = "https://open.spotify.com/track/2CDcXWYWilHTXrsOXJza8n"
link = song.split("/")
value = link[4]
link = value.split("?")
track_id = link[0]

print(track_id)