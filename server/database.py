from mongoengine import *
import json 

#connect to the database running in the background
connect('MediaCenter', host='localhost', port=27017)

#update the spotify
class Song(EmbeddedDocument):
	song_title = StringField(required=True)
	artists = ListField(StringField(required=True),required=True)
	album = StringField(required=True)
	spotifyURI = StringField(required=True,primary_key=True)

class Playlist(Document):
	playlist_title =  StringField(max_length=200, required=True)
	userName = StringField(max_length=200, required=True)
	spotifyURI = StringField(max_length=300, required=True,primary_key=True)
	songs = ListField(EmbeddedDocumentField(Song)) 
	meta ={'db-alias':'playlist-db'}

def insertPlaylist(playlist):
#	playlist = json.loads(playlist_json)
	track_objects = (playlist["tracks"])["items"]
	print(type(track_objects))
	songDoc = []
	for track_object in track_objects:
		song = track_object["track"]
		artList = [] 
		for artist in song["artists"]:
			artList.append(artist["name"])	
		songDoc.append(Song(song_title = song["name"], artists=artList,album=song["album"]["name"], spotifyURI=song["uri"]))
	playListDoc = Playlist(playlist_title = playlist["name"], userName = playlist["owner"]["display_name"],  spotifyURI = playlist["uri"], songs = songDoc)
	playListDoc.save()

def getPlaylist(URI):
	playlist = Playlist.objects(spotifyURI = URI)[0]
	print(playlist.playlist_title)
	print("success")
		
